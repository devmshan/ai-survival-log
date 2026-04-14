---
title: "수직적 규모 확장 vs 수평적 규모 확장"
created: "2026-04-14"
updated: "2026-04-14"
type: concept
sources: ["[[sources/2026-04-14-system-design-interview-v1]]"]
tags: ["system-design", "scalability", "scale-up", "scale-out", "distributed-systems"]
status: active
published: false
slug: ""
description: ""
---

# 수직적 규모 확장 vs 수평적 규모 확장

시스템이 더 많은 트래픽을 감당해야 할 때 선택해야 하는 두 가지 전략.

## 수직적 규모 확장 (Scale Up)

**정의:** 단일 서버에 더 좋은 자원을 추가하는 방식.

- CPU 업그레이드, RAM 증설, 더 빠른 디스크 교체
- 단순함: 코드 변경 없이 하드웨어만 업그레이드
- 예: AWS EC2 인스턴스 타입 변경 (t2.micro → m5.4xlarge)

**한계:**

- 하드웨어 한계가 존재 — CPU/RAM을 무한정 늘릴 수 없음
- 장애 발생 시 자동 복구(failover) 불가
- 다중화/이중화(redundancy) 없음 → 단일 장애 지점(SPOF) 위험

## 수평적 규모 확장 (Scale Out)

**정의:** 서버를 여러 대 추가해 분산 처리하는 방식.

- 비슷한 스펙의 서버를 풀(pool)에 추가
- 로드밸런서와 함께 사용
- 대규모 서비스에서 필수적인 전략

**장점:**

- 이론적으로 무한 확장 가능
- 한 서버 장애 시 다른 서버가 트래픽 흡수 가능
- 트래픽에 따라 유연하게 서버 수 조절 가능

## 비교

| | 수직적 (Scale Up) | 수평적 (Scale Out) |
|--|--|--|
| 방법 | 서버 스펙 업그레이드 | 서버 수 추가 |
| 한계 | 하드웨어 한계 존재 | 이론적으로 무제한 |
| 장애 복구 | 불가 (SPOF) | 가능 (다중화) |
| 적합 규모 | 소규모 초기 단계 | 대규모 서비스 |
| 비용 | 고성능 서버 단가 높음 | 저사양 서버 여러 대 |

## 언제 무엇을 선택하는가

```
초기/소규모  → Scale Up (단순함)
트래픽 폭발  → Scale Out (유연성)
고가용성 필요 → Scale Out (다중화)
```

대규모 시스템 설계의 기본 전략은 **수평적 확장**. 이를 위해 [[concepts/load-balancer]], [[concepts/stateless-architecture]]가 필요하다.

## 관련 페이지

- [[concepts/load-balancer]] — 수평 확장 시 트래픽 분산
- [[concepts/stateless-architecture]] — 수평 확장을 가능하게 하는 조건
- [[concepts/database-sharding]] — DB 수평 확장 전략
- [[projects/study-system-design-interview]] — 시스템 설계 스터디
