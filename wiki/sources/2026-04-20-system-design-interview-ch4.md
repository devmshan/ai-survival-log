---
title: "가상 면접 사례로 배우는 대규모 시스템 설계 기초 — 4장: 처리율 제한 장치의 설계"
created: "2026-04-20"
updated: "2026-04-20"
type: source
sources: []
tags: ["system-design", "rate-limiter", "token-bucket", "leaky-bucket", "distributed-systems", "backend", "book"]
status: active
published: false
slug: ""
description: ""
---

# 가상 면접 사례로 배우는 대규모 시스템 설계 기초 — 4장: 처리율 제한 장치의 설계

> 원본: `raw/books/스크린샷 2026-04-20 오전 10.17.14~43.png` (13개 이미지)
> 저자: Alex Xu

## 핵심 요약

- 처리율 제한 장치(rate limiter)는 클라이언트/서비스의 트래픽 전송률을 제어하는 컴포넌트
- 배치 위치: 클라이언트 측, 서버 측, 미들웨어(API Gateway) — 대부분 API Gateway 활용
- 5가지 알고리즘: 토큰 버킷, 누출 버킷, 고정 윈도 카운터, 이동 윈도 로그, 이동 윈도 카운터
- 분산 환경에서는 경쟁 조건(race condition)과 동기화(synchronization) 문제가 핵심 과제
- Redis의 INCR, EXPIRE를 활용한 카운터 구현이 일반적

## 주요 포인트

### 처리율 제한 장치가 필요한 이유

- **DoS/DDoS 방지**: 의도적/비의도적 과다 요청으로 인한 서비스 중단 예방
- **비용 절감**: 우선순위 낮은 API 호출 차단으로 서버 자원 절약 (특히 외부 API 비용)
- **서버 과부하 방지**: 봇, 크롤러 등 비정상 트래픽 필터링

### 1단계: 문제 이해 및 설계 범위 확정

면접에서 먼저 확인해야 할 질문들:
- 어느 쪽(클라이언트/서버)에 제한 장치를 둘 것인가?
- 어떤 기준으로 제한? (IP, 사용자 ID, 기타)
- 처리해야 할 트래픽 규모
- 별도 서비스로 구축? 아니면 애플리케이션 코드에 포함?
- 분산 환경 고려 여부

### 2단계: 개략적 설계안

**배치 위치 선택**:
- 클라이언트 측: 위변조 가능, 모든 클라이언트 통제 불가 → 비추
- 서버 측: API 서버에 직접 구현
- 미들웨어(API Gateway): 클라우드 MSA에서 일반적 선택 — 처리율 제한 + SSL termination + 인증 등 통합

**처리율 제한 규칙 예시 (YAML)**:
```yaml
domain: messaging
descriptors:
  - key: message_type
    value: marketing
    rate_limit:
      unit: day
      requests_per_unit: 5
```

### 5가지 알고리즘

| 알고리즘 | 핵심 방식 | 장점 | 단점 |
|---------|-----------|------|------|
| 토큰 버킷 | 버킷에 토큰 채우기, 요청마다 토큰 소비 | 짧은 트래픽 집중 허용, 구현 간단 | 버킷 크기·토큰 공급률 튜닝 어려움 |
| 누출 버킷 | FIFO 큐, 고정 속도로 처리 | 안정적 출력률, 메모리 효율 | 버스트 처리 불가, 큐 가득 차면 최신 요청 소실 |
| 고정 윈도 카운터 | 고정 시간 윈도로 카운터 관리 | 구현 간단, 메모리 효율 | 윈도 경계에서 2배 허용 버그 |
| 이동 윈도 로그 | 요청 타임스탬프를 로그로 저장 | 경계 문제 없음, 정확 | 메모리 비효율 (거부된 요청도 저장) |
| 이동 윈도 카운터 | 이전 윈도 카운터 가중치 적용 | 정확성과 효율성 균형 | 직전 윈도 균등 분포 가정 |

### 3단계: 상세 설계

**Redis 기반 카운터**:
- `INCR`: 카운터 증가
- `EXPIRE`: TTL 설정으로 윈도 자동 만료

**한도 초과 처리**:
- HTTP 429 (Too Many Requests) 반환
- 응답 헤더로 정보 제공:
  - `X-Ratelimit-Remaining`: 남은 요청 수
  - `X-Ratelimit-Limit`: 윈도 내 최대 허용 요청 수
  - `X-Ratelimit-Retry-After`: 재시도 대기 시간 (초)

**분산 환경 문제**:
- **경쟁 조건(Race condition)**: 여러 서버가 동시에 카운터를 읽고 쓸 때 발생 → Lua 스크립트 또는 Redis sorted set으로 해결
- **동기화(Synchronization)**: 다중 rate limiter 서버 간 상태 공유 → Redis를 중앙 데이터 저장소로 사용

**성능 최적화**:
- 최종 일관성 모델(eventual consistency) 채택
- 다중 데이터센터 지원 시 지연 최소화를 위해 가장 가까운 엣지 서버 활용

### 4단계: 마무리 추가 논의

- **경성(hard) vs 연성(soft) 처리율 제한**: hard는 절대 초과 불가, soft는 단기간 초과 허용
- **다양한 계층**: 애플리케이션 레이어(7계층)뿐 아니라 IP 계층(3계층)에서도 제한 가능
- **처리율 제한 회피**: 클라이언트 캐시 활용, 예외 처리, 재시도 로직에 충분한 백오프 적용
- **클라이언트 모범 사례**: 429 예외 처리, 지수 백오프(exponential backoff)

## 인사이트

- Rate Limiter는 독립 컴포넌트로 설계할수록 재사용성이 높아짐
- Envoy, Kong 같은 오픈소스 API Gateway가 이미 rate limiting 내장 — 직접 구현 전에 검토 필수
- 분산 환경에서의 경쟁 조건은 Lua 스크립트 원자적 실행으로 해결하는 것이 간결함
- 이동 윈도 카운터가 정확성·효율성 균형이 가장 좋아 실무에서 가장 많이 쓰임

## 관련 페이지

- [[concepts/rate-limiter]]
- [[topics/system-design-interview-04]]
- [[projects/study-system-design-interview]]
- [[concepts/stateless-architecture]]
- [[concepts/load-balancer]]
