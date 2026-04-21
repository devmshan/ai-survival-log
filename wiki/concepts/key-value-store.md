---
title: "키-값 저장소 (Key-Value Store)"
created: "2026-04-21"
updated: "2026-04-21"
type: concept
sources: ["[[sources/2026-04-21-system-design-interview-ch6]]"]
tags: [system-design, key-value-store, nosql, distributed-systems, cache]
status: active
published: false
slug: ""
description: ""
---

# 키-값 저장소 (Key-Value Store)

키(key)와 값(value) 쌍으로 데이터를 저장하는 비관계형 데이터베이스. 키는 유일 식별자이고 값은 문자열부터 객체까지 무엇이든 될 수 있다.

## 대표 구현체

- **Redis:** 인메모리, 다양한 자료구조(list, set, sorted set, hash), 만료 시간 지원
- **Memcached:** 단순 캐시 특화, 멀티스레드
- **Amazon DynamoDB:** 관리형 서비스, 자동 확장

## 단일 서버 설계

- 메모리에 해시 테이블로 저장 → 빠르지만 용량 제한
- 개선: 자주 쓰는 데이터만 메모리, 나머지는 디스크. 데이터 압축 적용

## 분산 설계 핵심 요소

### 데이터 파티션
[[concepts/consistent-hashing]]으로 서버에 고르게 분산, 노드 추가/삭제 시 재배치 최소화.

### 데이터 다중화(Replication)
해시 링에서 시계 방향으로 N개 서버에 복제. 가용성과 내구성 확보.

### 일관성 — 정족수 합의(Quorum Consensus)
- N: 복제 수 / W: 쓰기 응답 수 / R: 읽기 응답 수
- W+R > N → 강한 일관성
- 느슨한 설정(W=1, R=1) → 빠른 응답, 약한 일관성

### 불일치 해소 — [[concepts/vector-clock]]
버전 충돌을 감지하고 클라이언트 측에서 해소.

### 장애 감지 — [[concepts/gossip-protocol]]
분산 방식으로 노드 장애를 효율적으로 감지.

### 쓰기/읽기 경로

**쓰기:**
```
요청 → 커밋 로그(영속성) → 메모리 캐시 → (캐시 가득 차면) SSTable(디스크)
```

**읽기:**
```
메모리 캐시 확인 → 없으면 블룸 필터로 어떤 SSTable에 있는지 확인 → SSTable 조회
```

## CAP 정리와의 관계

[[concepts/cap-theorem]]에 따라 분산 키-값 저장소는 CP 또는 AP를 선택:
- DynamoDB, Cassandra: AP (가용성 우선, 최종 일관성)
- HBase, Zookeeper: CP (일관성 우선)

## 관련 페이지

- [[concepts/cap-theorem]]
- [[concepts/consistent-hashing]]
- [[concepts/vector-clock]]
- [[concepts/gossip-protocol]]
- [[concepts/db-replication]]
- [[sources/2026-04-21-system-design-interview-ch6]]
- [[topics/system-design-interview-06]]
