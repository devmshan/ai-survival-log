---
title: "가용성 (Availability)"
created: "2026-04-15"
updated: "2026-04-15"
type: concept
sources: ["[[sources/2026-04-15-system-design-interview-ch2]]"]
tags: ["system-design", "availability", "sla", "high-availability", "distributed-systems"]
status: active
published: false
slug: ""
description: ""
---

# 가용성 (Availability)

시스템이 지속적으로 중단 없이 운영될 수 있는 능력. 퍼센트로 표현하며, "나인(nine)"으로 줄여 부른다. 99.9% = "three nines", 99.999% = "five nines".

## 가용성과 장애 시간

| 가용률 | 별칭 | 하루 장애 | 한 달 장애 | 1년 장애 |
|--------|------|-----------|------------|----------|
| 90% | one nine | 2.4시간 | 72시간 | 36.5일 |
| 99% | two nines | 14.4분 | 7.31시간 | 3.65일 |
| 99.9% | three nines | 1.44분 | 43.8분 | 8.77시간 |
| 99.99% | four nines | 8.64초 | 4.38분 | 52.6분 |
| 99.999% | five nines | 864ms | 26.3초 | 5.26분 |

## SLA (Service Level Agreement)

서비스 제공자가 고객에게 공식적으로 약속하는 가용성 수준.

- **Amazon, Google, Microsoft** 등 주요 클라우드: 99.9% 이상 SLA 제공
- SLA를 지키지 못하면 크레딧 환급, 패널티 등 계약상 의무 발생
- "SLA 99.9%"는 1년에 8.77시간까지 장애가 허용된다는 의미

## 설계 관점에서의 가용성

### SPOF(Single Point of Failure) 제거

어느 한 컴포넌트가 죽으면 전체가 죽는 구조를 없애야 한다.

```
잘못된 예: 로드밸런서 1대 → 로드밸런서가 죽으면 서비스 전체 다운
올바른 예: 로드밸런서 Active-Standby 2대 운영
```

### 다중화 (Redundancy)

- **웹 서버:** 여러 대 + 로드밸런서
- **DB:** Master + Replica 구조 → [[concepts/db-replication]]
- **캐시:** Redis 클러스터
- **데이터센터:** 복수 리전 Active-Active 또는 Active-Standby

### 장애 격리 (Fault Isolation)

한 컴포넌트의 장애가 다른 컴포넌트로 전파되지 않도록 경계를 설계한다.
메시지 큐([[concepts/message-queue]])는 생산자와 소비자를 분리하여 장애 격리를 제공한다.

## 가용성 vs 일관성 (CAP 정리)

분산 시스템에서는 가용성(Availability)과 일관성(Consistency)이 트레이드오프 관계다. 파티션 장애(P)가 발생하면 A와 C 중 하나를 선택해야 한다.

- **AP 시스템 (가용성 우선):** 장애 중에도 응답하되 일부 데이터가 오래될 수 있음
- **CP 시스템 (일관성 우선):** 모든 데이터가 최신이지만 장애 시 일부 요청 거부

## 관련 페이지

- [[concepts/back-of-envelope-estimation]]
- [[concepts/db-replication]]
- [[concepts/load-balancer]]
- [[concepts/message-queue]]
- [[concepts/stateless-architecture]]
- [[sources/2026-04-15-system-design-interview-ch2]]
- [[topics/system-design-interview-02]]
