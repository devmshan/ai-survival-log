---
title: "대규모 시스템 설계 기초 5장 — 안정 해시 설계"
created: "2026-04-20"
updated: "2026-04-20"
type: source
sources: ["[[sources/2026-04-14-system-design-interview-v1]]"]
tags: ["system-design", "consistent-hashing", "hash-ring", "virtual-nodes", "distributed-systems", "book"]
status: active
published: false
slug: ""
description: ""
---

# 대규모 시스템 설계 기초 5장 — 안정 해시 설계

> 원본: 가상 면접 사례로 배우는 대규모 시스템 설계 기초 (Alex Xu) 5장
> 캡처: raw/books/스크린샷 2026-04-20 오후 10.56.42~55.png (7개 이미지)

## 핵심 요약

- **문제:** 단순 나머지 연산 해시(`serverIndex = hash(key) % N`)는 서버 수 N이 바뀌면 대부분의 키를 재배치해야 한다 → 대규모 캐시 미스
- **해결:** 안정 해시(Consistent Hashing) — 해시 공간을 링(ring)으로 구성. 서버 추가/제거 시 영향받는 키를 최소화
- **보완:** 가상 노드(Virtual Nodes) — 각 서버를 여러 가상 노드로 분산 배치해 균등 분포 달성
- **활용:** Amazon DynamoDB, Apache Cassandra, Discord, Akamai CDN, Maglev 로드 밸런서

## 주요 내용

### 해시 키 재배치(rehash) 문제

기본 해시 방식: `serverIndex = hash(key) % N`

| 키 | hash(key) | 서버 인덱스 (N=4) |
|----|-----------|-------------------|
| key0 | 18358617 | 1 |
| key1 | 26143584 | 0 |
| key2 | 10130523 | 3 |
| key3 | 5765437 | 1 |

서버가 4개→3개로 변하면 거의 모든 키가 다른 서버로 재배치됨 → 대규모 캐시 미스 발생

### 안정 해시 기본 구조

**해시 링(Hash Ring):**
- SHA-1 기준 해시 공간: `0 ~ 2^160 - 1`
- 양 끝을 연결해 원(ring)으로 구성
- 서버와 키 모두 같은 해시 함수로 링 위 특정 위치에 배치

**서버 배치:** 서버 IP/이름을 해시해 링 위에 배치 (server0, server1, server2, server3)

**키 배치:** 키를 해시해 링 위에 배치 → 시계 방향으로 탐색해 만나는 첫 번째 서버에 저장

**서버 조회:** key0 → 시계 방향 탐색 → server0에 저장

### 서버 추가/제거

**서버 추가:**
- 새 서버(server4) 추가 시 key0만 server4로 이동
- 나머지 키는 영향 없음 → 최소한의 재배치

**서버 제거:**
- server1 제거 시 server1이 담당하던 키들만 시계 방향 다음 서버(server2)로 이동

### 기본 구현의 두 가지 문제

1. **불균등 파티션:** 서버 추가/제거 후 파티션 크기 차이가 매우 커질 수 있음
2. **키 쏠림:** 링 위 서버 배치가 불균등하면 특정 서버에 키가 집중됨

### 가상 노드(Virtual Nodes)

각 서버를 링 위 여러 위치(가상 노드)로 분산 배치:
- server0 → server0_0, server0_1, server0_2, ...
- server1 → server1_0, server1_1, server1_2, ...

**효과:**
- 노드 수가 많아질수록 분포가 균등해짐 (표준편차 감소)
- 100~200개 가상 노드 사용 시 표준편차 약 5~10%
- 트레이드오프: 가상 노드 수 늘리면 균등 분포 ↑, 데이터 저장 공간 ↑

### 활용 사례 (마무리)

- **Amazon DynamoDB:** 데이터 파티셔닝에 안정 해시 사용
- **Apache Cassandra:** 분산 데이터 파티셔닝
- **Discord:** Elixir로 5백만 동시 접속 처리 시 사용
- **Akamai CDN:** 엣지 서버 분산
- **Maglev 로드 밸런서:** 네트워크 로드 밸런싱

## 인사이트

- 안정 해시는 "추가/삭제 시 재배치할 키를 최소화"하는 아이디어가 핵심
- 가상 노드는 일종의 "섀도 서버" 패턴 — 실제 서버 1개가 링 위에서는 N개처럼 보임
- 6장(키-값 저장소) 설계에서 안정 해시가 바로 재활용됨

## 관련 페이지

- [[concepts/consistent-hashing]]
- [[topics/system-design-interview-05]]
- [[sources/2026-04-14-system-design-interview-v1]]
- [[projects/study-system-design-interview]]
