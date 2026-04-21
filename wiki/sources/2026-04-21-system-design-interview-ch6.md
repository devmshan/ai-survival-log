---
title: "대규모 시스템 설계 기초 — 6장: 키-값 저장소 설계"
created: "2026-04-21"
updated: "2026-04-21"
type: source
sources: []
tags: [system-design, key-value-store, cap-theorem, distributed-systems, book]
status: active
published: false
slug: ""
description: ""
---

# 대규모 시스템 설계 기초 — 6장: 키-값 저장소 설계

**원본:** `raw/books/system-design-interview-ch6-01.png` ~ `ch6-13.png`
**페이지:** 71–115

## 핵심 요약

키-값 저장소(key-value store)는 비관계형 데이터베이스로, 키(key)는 유일 식별자이고 값(value)은 무엇이든 될 수 있다. Redis, Memcached, DynamoDB가 대표적 구현체다. 이 장은 단일 서버 구현부터 시작해 분산 환경의 설계 원칙(CAP 정리, 데이터 파티션·다중화·일관성·장애 처리)과 아키텍처 전반을 다룬다.

## 주요 내용

### 단일 서버 키-값 저장소
- 메모리에 해시 테이블로 저장 — 빠르지만 용량 제한
- 압축, 자주 쓰는 데이터만 메모리/나머지는 디스크 분리

### 분산 키-값 저장소

#### CAP 정리
세 가지 속성 중 두 가지만 동시에 만족 가능:
- **일관성(Consistency):** 모든 클라이언트가 항상 동일 데이터 조회
- **가용성(Availability):** 일부 노드 장애 시에도 응답 반환
- **파티션 감내(Partition Tolerance):** 네트워크 단절 상황에서도 동작

실세계 분산 시스템은 P를 포기할 수 없으므로 CP 또는 AP 선택.

#### 데이터 파티션
[[concepts/consistent-hashing]]을 사용해 데이터를 고르게 분산하고 노드 추가/삭제 시 재배치를 최소화한다.

#### 데이터 다중화
해시 링에서 시계 방향으로 N개 서버에 복제 저장. 가용성과 신뢰성 확보.

#### 일관성 — 정족수 합의(Quorum Consensus)
- N: 복제 서버 수 / W: 쓰기 성공 기준 수 / R: 읽기 성공 기준 수
- W+R > N이면 강한 일관성 보장
- W=1, R=1 → 빠른 응답 / W=N, R=N → 강한 일관성

#### 불일치 해소 — 벡터 시계(Vector Clock)
`[서버, 버전]` 쌍의 리스트로 데이터 버전을 추적. 충돌 감지 및 해소에 활용. 단점: 클라이언트 측 충돌 해소 로직 필요, 버전 정보 증가.

#### 장애 감지 — 가십 프로토콜(Gossip Protocol)
멀티캐스팅은 비효율적 → 가십 프로토콜로 분산 장애 감지:
- 각 노드가 멤버십 목록(heartbeat 카운터) 유지
- 주기적으로 무작위 노드에 목록 전파
- 카운터가 오래 갱신 안 된 노드를 장애로 판단

#### 일시적 장애 처리
- **단순 정족수:** 장애 노드는 작업 거부
- **느슨한 정족수(Sloppy Quorum):** 대신 다른 서버가 처리 후 복구 시 전달(hinted handoff)

#### 영구 장애 처리 — 머클 트리(Merkle Tree)
해시 트리로 두 서버 간 데이터 불일치를 효율적으로 감지·동기화.

### 시스템 컴포넌트 요약
- **쓰기 경로:** 쓰기 요청 → 커밋 로그 → 메모리 캐시 → SSTable(디스크)
- **읽기 경로:** 메모리 캐시 확인 → 없으면 SSTable에서 블룸 필터로 탐색
- **블룸 필터(Bloom Filter):** 특정 SSTable에 키 존재 여부를 확률적으로 확인

### 핵심 기술 정리 표

| 기능 | 기술 |
|------|------|
| 데이터 파티션 | 안정 해시 |
| 데이터 다중화 | 안정 해시 |
| 일관성 | 정족수 합의 |
| 불일치 해소 | 벡터 시계 |
| 장애 감지 | 가십 프로토콜 |
| 장애 처리 | 느슨한 정족수 + hinted handoff |
| 영구 장애 복구 | 머클 트리 |
| 데이터 저장 | SSTable + LSM 트리 |

## 인사이트

- CAP 정리는 단순 이론이 아니라 실제 시스템 설계 시 트레이드오프의 언어다.
- 벡터 시계로 충돌을 클라이언트에게 넘기는 방식은 DynamoDB 실제 구현에서 사용한다.
- 블룸 필터 + SSTable 조합은 쓰기 최적화(LSM 트리)의 핵심 패턴이다.

## 관련 페이지

- [[concepts/key-value-store]]
- [[concepts/cap-theorem]]
- [[concepts/vector-clock]]
- [[concepts/gossip-protocol]]
- [[concepts/consistent-hashing]]
- [[concepts/db-replication]]
- [[topics/system-design-interview-06]]
