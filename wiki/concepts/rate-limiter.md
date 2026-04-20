---
title: "처리율 제한 장치 (Rate Limiter)"
created: "2026-04-20"
updated: "2026-04-20"
type: concept
sources: ["[[sources/2026-04-20-system-design-interview-ch4]]"]
tags: ["system-design", "rate-limiter", "token-bucket", "leaky-bucket", "distributed-systems", "api-gateway", "backend"]
status: active
published: false
slug: ""
description: ""
---

# 처리율 제한 장치 (Rate Limiter)

클라이언트 또는 서비스가 보내는 트래픽의 처리율(rate)을 제어하는 컴포넌트. API 남용 방지, 비용 절감, 서버 과부하 예방을 위해 사용된다.

## 왜 필요한가

- **DoS/DDoS 방지**: 대량 요청으로 인한 서비스 중단 예방
- **비용 절감**: 과다 호출로 인한 외부 API 비용, 서버 자원 낭비 방지
- **서버 보호**: 봇, 스크레이퍼 등 비정상 트래픽 차단
- **공정 사용**: 한 사용자가 전체 자원을 독점하지 못하게 제한

## 배치 위치

```
클라이언트 → [Rate Limiter] → API 서버 → DB
```

| 위치 | 장점 | 단점 |
|------|------|------|
| 클라이언트 측 | 서버 부하 없음 | 위변조 가능, 통제 불가 |
| 서버 측 (미들웨어) | 완전한 통제 | 추가 구현 필요 |
| API Gateway | 인증·SSL 등과 통합, 관리 쉬움 | 벤더 종속 가능성 |

**실무 선택**: 클라우드 MSA 환경에서는 API Gateway(Envoy, Kong, AWS API Gateway 등)에 내장된 rate limiting 기능을 활용하는 것이 일반적.

## 5가지 알고리즘

### 1. 토큰 버킷 (Token Bucket)

버킷에 일정 속도로 토큰을 채우고, 요청마다 토큰 1개를 소비한다. 토큰이 없으면 요청을 거부.

```
파라미터:
- 버킷 크기(bucket size): 최대 토큰 수
- 토큰 공급률(refill rate): 초당 추가 토큰 수
```

- **장점**: 짧은 순간의 트래픽 집중(burst) 허용, 구현 단순
- **단점**: 버킷 크기·공급률 튜닝이 까다로움
- **사용처**: Amazon, Stripe 등이 채택

### 2. 누출 버킷 (Leaky Bucket)

FIFO 큐에 요청을 쌓고, 고정된 속도로 처리한다. 큐가 가득 차면 새 요청을 버린다.

```
파라미터:
- 버킷 크기(queue size): 최대 대기 요청 수
- 처리율(outflow rate): 초당 처리할 요청 수
```

- **장점**: 안정적인 출력률, 메모리 효율
- **단점**: 트래픽 집중 시 최신 요청이 먼저 버려짐, 오래된 요청이 큐 점유

### 3. 고정 윈도 카운터 (Fixed Window Counter)

타임라인을 고정 크기의 윈도(예: 1분)로 나누고, 각 윈도마다 카운터를 관리한다.

```
예) 1분 최대 5요청:
- 00:00~01:00: 요청 5개까지 허용
- 01:00~02:00: 카운터 초기화 후 다시 5개
```

- **장점**: 구현 단순, 메모리 효율
- **단점**: **경계 버그** — 윈도 끝과 시작에 집중되면 실제 허용량의 2배 요청이 통과됨

### 4. 이동 윈도 로그 (Sliding Window Log)

요청마다 타임스탬프를 로그(Redis sorted set 등)에 저장하고, 현재 시각 기준 이전 N초 내 요청 수를 카운트한다.

- **장점**: 고정 윈도의 경계 버그 없음, 정확
- **단점**: 메모리 비효율 (거부된 요청도 로그에 저장됨)

### 5. 이동 윈도 카운터 (Sliding Window Counter)

고정 윈도 카운터 + 이동 윈도 로그의 혼합. 이전 윈도의 카운터에 겹치는 비율을 가중치로 적용한다.

```
허용 요청 수 =
  현재 윈도 카운터 + 이전 윈도 카운터 × (윈도 겹치는 비율)
```

- **장점**: 정확성과 효율성의 균형, 메모리 효율
- **단점**: 이전 윈도 요청이 균등하게 분포했다고 가정 (현실과 약간 다를 수 있음)
- **실무 추천**: 세 방식 중 가장 균형 잡힌 선택

## 상세 설계

### Redis 기반 구현

```
INCR {user_id}:{window}    # 카운터 증가
EXPIRE {user_id}:{window} 60  # 윈도 만료 설정
```

두 명령을 원자적으로 실행하려면 **Lua 스크립트** 사용.

### 처리율 초과 응답

- HTTP 상태코드: **429 Too Many Requests**
- 응답 헤더로 상태 정보 제공:

| 헤더 | 의미 |
|------|------|
| `X-Ratelimit-Remaining` | 현재 윈도 내 남은 요청 수 |
| `X-Ratelimit-Limit` | 윈도 내 최대 허용 요청 수 |
| `X-Ratelimit-Retry-After` | 재시도까지 대기 시간 (초) |

### 처리율 제한 규칙 (YAML 예시)

```yaml
domain: messaging
descriptors:
  - key: message_type
    value: marketing
    rate_limit:
      unit: day
      requests_per_unit: 5

domain: auth
descriptors:
  - key: auth_type
    value: login
    rate_limit:
      unit: minute
      requests_per_unit: 5
```

## 분산 환경의 도전 과제

### 경쟁 조건 (Race Condition)

여러 서버가 동시에 Redis 카운터를 읽고 쓰면 카운터가 부정확해짐.

**해결책**:
- Lua 스크립트로 읽기-쓰기를 원자적으로 실행
- Redis sorted set 활용 (이동 윈도 로그 알고리즘)

### 동기화 (Synchronization)

다중 rate limiter 서버가 각자 상태를 가지면 불일치 발생.

**해결책**: Redis를 중앙 집중식 데이터 저장소로 사용해 모든 rate limiter가 공유.

## 추가 고려사항

- **경성(hard) vs 연성(soft) 제한**: hard는 절대 초과 불가, soft는 단기간 허용
- **다계층 제한**: 애플리케이션 레이어(L7)뿐 아니라 IP 레이어(L3)에서도 적용 가능
- **클라이언트 모범 사례**: 429 예외 처리 + 지수 백오프(exponential backoff) + 캐시 활용

## 트레이드오프 정리

| 알고리즘 | 버스트 허용 | 메모리 효율 | 정확성 | 구현 복잡도 |
|---------|------------|------------|--------|------------|
| 토큰 버킷 | ✅ | ✅ | 보통 | 낮음 |
| 누출 버킷 | ❌ | ✅ | 높음 | 낮음 |
| 고정 윈도 카운터 | ✅ | ✅ | 낮음 (경계 버그) | 낮음 |
| 이동 윈도 로그 | ❌ | ❌ | 높음 | 중간 |
| 이동 윈도 카운터 | 보통 | ✅ | 높음 | 중간 |

## 관련 페이지

- [[sources/2026-04-20-system-design-interview-ch4]]
- [[topics/system-design-interview-04]]
- [[concepts/load-balancer]]
- [[concepts/stateless-architecture]]
- [[concepts/database-sharding]]
- [[projects/study-system-design-interview]]
