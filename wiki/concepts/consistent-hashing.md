---
title: "안정 해시 (Consistent Hashing)"
created: "2026-04-20"
updated: "2026-04-20"
type: concept
sources: ["[[sources/2026-04-20-system-design-interview-ch5]]"]
tags: ["system-design", "consistent-hashing", "hash-ring", "virtual-nodes", "distributed-systems", "partitioning"]
status: active
published: false
slug: ""
description: ""
---

# 안정 해시 (Consistent Hashing)

분산 시스템에서 서버 추가/제거 시 재배치되는 키의 수를 최소화하는 해시 기법. 해시 공간을 원(ring)으로 구성해 변경의 영향 범위를 국소화한다.

## 왜 필요한가

### 단순 해시의 한계

```
serverIndex = hash(key) % N
```

서버 수 N이 바뀌면 거의 모든 키의 `hash(key) % N` 결과가 달라진다.

- N=4 → N=3으로 변경 시: 대부분의 키가 다른 서버로 이동
- 결과: **대규모 캐시 미스** — 분산 캐시 시스템에서 치명적

## 핵심 개념

### 해시 링(Hash Ring)

1. 해시 함수(SHA-1 등)의 출력 공간(`0 ~ 2^160 - 1`)을 원으로 구성
2. 서버를 해시 함수로 링 위 특정 위치에 배치
3. 키도 같은 함수로 링 위에 배치
4. **시계 방향으로 탐색해 만나는 첫 번째 서버에 키 저장**

```
링 위: ... server0 ... key0 ... key1 ... server1 ... key2 ... server2 ...
→ key0, key1은 server1에 저장
→ key2는 server2에 저장
```

### 서버 추가/제거의 영향

**서버 추가 (server4 추가):**
- server4 직전(반시계 방향) 서버가 담당하던 키 중 일부만 server4로 이동
- 나머지 키: 변화 없음

**서버 제거 (server1 제거):**
- server1이 담당하던 키들이 시계 방향 다음 서버(server2)로 이동
- 나머지 키: 변화 없음

→ **영향받는 키 = k/n** (k: 전체 키 수, n: 서버 수)

## 기본 구현의 두 가지 문제

### 1. 불균등 파티션

서버 추가/제거 후 링 위 간격이 매우 불균등해질 수 있음:
- 어떤 파티션은 매우 크고, 어떤 파티션은 매우 작은 상황 발생

### 2. 키 쏠림 (Non-uniform Key Distribution)

서버가 적고 배치가 편향되면 특정 서버에 키가 집중:
- server2 구간이 링의 절반을 차지하면 전체 키의 절반이 server2로 쏠림

## 해결: 가상 노드(Virtual Nodes)

각 서버를 링 위 여러 위치(가상 노드)로 분산 배치:

```
server0 → server0_0, server0_1, server0_2, ... (링 위 여러 곳)
server1 → server1_0, server1_1, server1_2, ... (링 위 여러 곳)
```

### 효과

| 가상 노드 수 | 표준편차 |
|-------------|---------|
| 적음 | 크다 (불균등) |
| 100~200개 | 약 5~10% |
| 많음 | 작다 (균등) |

### 트레이드오프

- 가상 노드 수 ↑ → 분포 균등성 ↑, 데이터 저장 공간 ↑
- 시스템 요구사항에 맞게 노드 수 조정 필요

## 알고리즘 요약

```
# 키 저장
1. key를 해시 함수로 링 위 위치 결정
2. 시계 방향으로 탐색
3. 만나는 첫 번째 서버(가상 노드)에 저장

# 서버 추가
1. 새 서버의 가상 노드들을 링에 배치
2. 각 가상 노드의 직전(반시계) 구간 키만 이동

# 서버 제거
1. 해당 서버의 가상 노드들을 링에서 제거
2. 해당 구간의 키들이 시계 방향 다음 서버로 이동
```

## 실제 활용 사례

| 시스템 | 용도 |
|--------|------|
| **Amazon DynamoDB** | 데이터 파티셔닝 |
| **Apache Cassandra** | 분산 데이터 파티셔닝 |
| **Discord** | 5백만 동시 접속 처리 (Elixir 기반) |
| **Akamai CDN** | 엣지 서버 분산 |
| **Maglev** | Google 네트워크 로드 밸런서 |

## 다른 개념과의 연결

- **[[concepts/database-sharding]]**: 안정 해시는 샤딩 전략 중 하나로 사용됨
- **[[concepts/load-balancer]]**: Maglev처럼 로드 밸런서에도 적용
- **6장 키-값 저장소**: CAP 정리와 함께 분산 KV 스토어 파티셔닝에 재활용

## 관련 페이지

- [[sources/2026-04-20-system-design-interview-ch5]]
- [[topics/system-design-interview-05]]
- [[concepts/database-sharding]]
- [[concepts/load-balancer]]
- [[concepts/db-replication]]
- [[projects/study-system-design-interview]]
