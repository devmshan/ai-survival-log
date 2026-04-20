---
title: "처리율 제한 장치 — 5가지 알고리즘으로 API 남용을 막는 법"
created: "2026-04-20"
updated: "2026-04-20"
type: topic
sources: ["[[sources/2026-04-20-system-design-interview-ch4]]"]
tags: ["system-design", "rate-limiter", "token-bucket", "distributed-systems", "study", "backend", "interview"]
status: active
published: true
slug: "system-design-interview-04"
description: "처리율 제한 장치를 5가지 알고리즘으로 설계하는 방법. 토큰 버킷부터 이동 윈도 카운터까지, 분산 환경의 경쟁 조건 해결까지 — 4장 스터디 기록."
seoTitle: "처리율 제한 장치 설계: 5가지 알고리즘 완전 정복"
series: "가상 면접 사례로 배우는 대규모 시스템 설계 기초"
seriesOrder: 4
---

# 처리율 제한 장치 — 5가지 알고리즘으로 API 남용을 막는 법

> 가상 면접 사례로 배우는 대규모 시스템 설계 기초 — 4장 스터디 기록

처리율 제한 장치(rate limiter)는 시스템을 지키는 문지기다. 초당 100개 이상의 요청이 오면 막는다. 봇이 로그인을 1만 번 시도하면 막는다. 그런데 어떻게 막는 게 좋을까? 알고리즘이 5가지나 있고, 분산 환경에서는 또 다른 문제가 생긴다.

## 왜 Rate Limiter가 필요한가

단순해 보이지만 이유가 세 가지다.

**첫째, DoS 방지.** 악의적이든 실수든, 서버에 요청이 폭증하면 서비스가 죽는다. Rate limiter는 그 전에 차단한다.

**둘째, 비용 절감.** 외부 API를 쓸 때 호출당 과금되는 경우가 많다. 내부 서비스라도 서버 자원은 유한하다.

**셋째, 공정 사용.** 한 사용자가 전체 API 할당량을 독점하지 못하게 한다.

## 어디에 둘 것인가

세 가지 선택지가 있다.

```
클라이언트 → [?] → API 서버 → DB
```

**클라이언트 측**은 위변조할 수 있어서 신뢰할 수 없다. **서버 측 미들웨어**는 완전한 통제가 가능하다. **API Gateway**는 인증, SSL termination, 로깅까지 한 곳에서 처리할 수 있어 MSA 환경에서 가장 일반적인 선택이다.

Envoy, Kong, AWS API Gateway 모두 rate limiting을 내장하고 있다. 직접 구현 전에 기존 도구를 먼저 확인하는 게 실용적이다.

## 5가지 알고리즘

### 1. 토큰 버킷 (Token Bucket)

버킷에 토큰을 일정 속도로 채우고, 요청마다 토큰 1개를 소비한다. 토큰이 없으면 거부.

파라미터는 두 가지: **버킷 크기**(한 번에 쌓아둘 수 있는 최대 토큰)와 **공급률**(초당 추가 토큰 수).

특징은 버스트를 허용한다는 것이다. 토큰이 가득 차 있으면 순간적으로 많은 요청을 처리할 수 있다. Amazon과 Stripe가 이 방식을 쓴다.

### 2. 누출 버킷 (Leaky Bucket)

FIFO 큐에 요청을 쌓고, 고정된 속도로 처리한다. 큐가 가득 차면 새 요청을 버린다.

출력률이 일정하다. 서버 입장에서 부하 예측이 쉽다. 대신 트래픽이 갑자기 몰릴 때 최신 요청이 먼저 버려지는 문제가 있다. Shopify가 이 방식을 사용한다.

### 3. 고정 윈도 카운터 (Fixed Window Counter)

타임라인을 고정 크기 윈도(예: 1분)로 나누고, 각 윈도마다 카운터를 관리한다.

구현이 제일 단순하다. 하지만 **경계 버그**가 있다. 1분 최대 5요청 정책이라면, 00:59에 5개, 01:01에 5개 — 2초 안에 10개가 통과된다.

### 4. 이동 윈도 로그 (Sliding Window Log)

요청마다 타임스탬프를 저장하고, 현재 시각 기준 이전 1분 내 요청 수를 정확히 카운트한다.

경계 버그가 없고 정확하다. 단점은 메모리다. 거부된 요청도 로그에 남아야 한다.

### 5. 이동 윈도 카운터 (Sliding Window Counter)

고정 윈도 카운터와 이동 윈도 로그의 중간. 이전 윈도의 카운터에 겹치는 비율을 가중치로 적용한다.

```
허용 = 현재 윈도 카운터 + 이전 윈도 카운터 × 겹치는 비율
```

예를 들어 현재 윈도 3개, 이전 윈도 5개, 겹치는 비율 60%라면:
`3 + 5 × 0.6 = 6`

정확성과 메모리 효율의 균형이 가장 좋다. 실무에서 가장 많이 쓰인다.

## 상세 설계: Redis와 HTTP 429

카운터 저장소로 Redis가 일반적이다.

```
INCR user:123:2026042010    # 카운터 증가
EXPIRE user:123:2026042010 60  # 1분 후 만료
```

한도를 넘은 요청에는 **HTTP 429 (Too Many Requests)** 를 반환하고, 헤더로 상태를 알린다.

```
X-Ratelimit-Remaining: 0
X-Ratelimit-Limit: 100
X-Ratelimit-Retry-After: 30
```

처리율 제한 규칙은 YAML 파일로 관리한다.

```yaml
domain: auth
descriptors:
  - key: auth_type
    value: login
    rate_limit:
      unit: minute
      requests_per_unit: 5
```

## 분산 환경의 함정

단일 서버에서는 단순하다. 하지만 여러 rate limiter 서버가 병렬로 돌면 두 가지 문제가 생긴다.

**경쟁 조건(Race Condition)**: 두 요청이 동시에 카운터를 읽으면 둘 다 "아직 여유 있음"으로 판단할 수 있다. Redis Lua 스크립트로 읽기-쓰기를 원자적으로 묶어 해결한다.

**동기화(Synchronization)**: 서버마다 상태가 다르면 사용자는 서버에 따라 다른 제한을 경험한다. Redis를 중앙 저장소로 써서 모든 서버가 같은 카운터를 공유하게 한다.

## 알고리즘 선택 기준

| 상황 | 추천 알고리즘 |
|------|-------------|
| 트래픽 집중(burst) 허용 필요 | 토큰 버킷 |
| 일정한 처리율 유지가 목표 | 누출 버킷 |
| 구현 단순함 우선 | 고정 윈도 카운터 |
| 정확성이 최우선 | 이동 윈도 로그 |
| 정확성 + 효율성 균형 | 이동 윈도 카운터 |

## 마무리

Rate limiter는 4장에서 처음 등장하는 독립 컴포넌트 설계 문제다. 이후 챕터에서 안정 해시, KV 스토어 등 빌딩 블록이 계속 등장한다. 공통 패턴은 하나다 — **요구사항부터 명확히 하고, 트레이드오프를 비교한 다음, 분산 환경 문제를 마지막에 다룬다.**

## 관련 페이지

- [[concepts/rate-limiter]]
- [[sources/2026-04-20-system-design-interview-ch4]]
- [[topics/system-design-interview-03]]
- [[topics/system-design-interview-01]]
- [[topics/system-design-interview-02]]
- [[projects/study-system-design-interview]]
