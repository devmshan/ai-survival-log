---
title: "분산 유일 ID 생성기 (Distributed Unique ID Generator)"
created: "2026-04-21"
updated: "2026-04-21"
type: concept
sources: ["[[sources/2026-04-21-system-design-interview-ch7]]"]
tags: [system-design, unique-id, snowflake, distributed-systems, uuid]
status: active
published: false
slug: ""
description: ""
---

# 분산 유일 ID 생성기 (Distributed Unique ID Generator)

분산 환경에서 여러 서버가 충돌 없이 유일한 ID를 생성하는 메커니즘. 단일 DB의 auto_increment는 다중 서버 환경에서 유일성을 보장하지 못한다.

## 요구사항

- 숫자로만 구성된 64비트 정수
- 시간순 정렬 가능
- 초당 10,000개 이상 생성
- 서버 간 조율 최소화

## 주요 접근 방법

### 1. UUID (Universally Unique Identifier)
- 128비트 무작위 값, 서버 독립적 생성
- 단점: 숫자가 아님, 시간순 정렬 불가, 64비트 초과

### 2. 티켓 서버 (Ticket Server)
- 중앙 서버에서 auto_increment 발급
- 단점: SPOF, 다중화 시 동기화 문제

### 3. 트위터 스노우플레이크 (Twitter Snowflake) ✓

```
| 1bit   | 41bit      | 5bit         | 5bit      | 12bit   |
| 사인   | 타임스탬프 | 데이터센터ID | 서버ID    | 일련번호|
```

| 구간 | 비트 | 내용 |
|------|------|------|
| 사인 비트 | 1 | 항상 0, 음수 ID 방지 |
| 타임스탬프 | 41 | 기원 시각 이후 밀리초. 약 69년치 |
| 데이터센터 ID | 5 | 최대 32개 데이터센터 |
| 서버 ID | 5 | 데이터센터당 최대 32개 서버 |
| 일련번호 | 12 | 밀리초당 최대 4096개 ID |

타임스탬프가 상위 비트이므로 시간순 정렬 자동 보장.

## 스노우플레이크 설계 고려사항

- **시계 동기화:** NTP 사용 필수. 시계가 역행하면 중복 ID 가능
- **섹션 크기 조정:** 동시성이 낮고 고가용성이 필요하면 일련번호 비트 축소, 타임스탬프 비트 증가
- **고가용성 모니터링**

## 관련 페이지

- [[sources/2026-04-21-system-design-interview-ch7]]
- [[topics/system-design-interview-07]]
