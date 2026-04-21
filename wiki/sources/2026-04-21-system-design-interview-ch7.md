---
title: "대규모 시스템 설계 기초 — 7장: 분산 시스템을 위한 유일 ID 생성기 설계"
created: "2026-04-21"
updated: "2026-04-21"
type: source
sources: []
tags: [system-design, unique-id, snowflake, distributed-systems, book]
status: active
published: false
slug: ""
description: ""
---

# 대규모 시스템 설계 기초 — 7장: 분산 시스템을 위한 유일 ID 생성기 설계

**원본:** `raw/books/system-design-interview-ch7-01.png` ~ `ch7-05.png`
**페이지:** 117–125

## 핵심 요약

분산 환경에서 자동 증가(auto_increment) 방식은 여러 데이터베이스 서버를 쓸 때 유일성을 보장하지 못한다. 이 장은 UUID, 티켓 서버, 트위터 스노우플레이크 세 가지 접근을 비교하고, 스노우플레이크 구조를 중심으로 상세 설계를 다룬다.

## 요구사항

- 유일성 보장
- 숫자로만 구성
- 64비트로 표현 가능
- 시간순 정렬 가능
- 초당 10,000개 이상 생성

## 접근 방법 비교

### 다중 마스터 복제(Multi-master Replication)
- DB auto_increment를 k(서버 수)씩 증가
- 규모 확장이 어렵고 여러 데이터센터에 걸친 ID 정렬 불가

### UUID
- 128비트, 서버 간 조율 없이 독립 생성
- 단점: 숫자가 아님, 시간순 정렬 불가, 64비트 초과

### 티켓 서버(Ticket Server)
- 중앙 서버에서 auto_increment 발급
- 단점: SPOF, 다중화 시 동기화 문제

### 트위터 스노우플레이크(Twitter Snowflake) ✓
64비트 ID를 구간으로 분할:

```
| 1bit   | 41bit      | 5bit         | 5bit      | 12bit  |
| 사인   | 타임스탬프 | 데이터센터ID | 서버ID    | 일련번호|
```

- **타임스탬프(41bit):** 밀리초 단위, 기원 시각(epoch) 이후 경과 시간. 약 69년치 표현 가능
- **데이터센터 ID(5bit):** 최대 32개 데이터센터
- **서버 ID(5bit):** 데이터센터당 최대 32개 서버
- **일련번호(12bit):** 같은 밀리초 내 최대 4096개 ID, 다음 밀리초 시작 시 초기화

타임스탬프가 상위 비트이므로 시간순 정렬 자동 보장.

## 마무리 고려사항

- **시계 동기화:** NTP(Network Time Protocol) 사용 필수
- **일련번호 섹션 조정:** 낮은 동시성 + 높은 고가용성이면 일련번호 비트 축소
- **고가용성:** 임계값이 높은 가용성(mission critical) 컴포넌트로 반드시 모니터링 필요

## 관련 페이지

- [[concepts/unique-id-generator]]
- [[topics/system-design-interview-07]]
