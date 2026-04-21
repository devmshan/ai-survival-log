---
title: "안정 해시 — 서버 추가/삭제해도 키 재배치를 최소화하는 방법"
created: "2026-04-20"
updated: "2026-04-20"
type: topic
sources: ["[[sources/2026-04-20-system-design-interview-ch5]]"]
tags: ["system-design", "consistent-hashing", "hash-ring", "virtual-nodes", "distributed-systems", "study", "backend", "interview"]
status: active
published: true
slug: "system-design-interview-05"
description: "단순 나머지 해시의 한계에서 시작해, 해시 링과 가상 노드로 분산 시스템의 키 재배치를 최소화하는 안정 해시를 5장 스터디 기록으로 정리한다."
---

# 안정 해시 — 서버 추가/삭제해도 키 재배치를 최소화하는 방법

분산 캐시에 서버를 하나 더 붙였더니 캐시 히트율이 폭락했다. 이유는 간단했다. 서버 수 N이 바뀌면 `hash(key) % N`의 결과가 대부분 달라지기 때문이다. 5장은 이 문제를 해시 링(Hash Ring) 하나로 해결하는 방법을 다룬다.

## 나머지 연산 해시의 한계

분산 캐시를 처음 설계하면 자연스럽게 이런 공식을 떠올린다:

```
serverIndex = hash(key) % N
```

서버가 4개면 각 키는 0~3번 서버 중 하나에 배치된다. 작동은 잘 한다. **서버 수 N이 바뀌기 전까지는.**

서버가 4개 → 3개로 줄어들면? `hash(key) % 4` 결과와 `hash(key) % 3` 결과가 다른 키가 대부분이다. 결국 거의 모든 키를 다시 배치해야 하고, 캐시 미스가 폭발한다.

분산 시스템에서 서버 추가·제거는 일상적인 일이다. 이 공식은 현실에서 쓰기 어렵다.

## 해시 링: 아이디어는 단순하다

안정 해시(Consistent Hashing)의 핵심 아이디어는 두 가지다.

**첫째, 해시 공간을 원으로 만든다.**

SHA-1 해시 함수의 출력 공간은 `0 ~ 2^160 - 1`이다. 이 공간의 양 끝을 붙이면 원(ring)이 된다.

**둘째, 서버와 키를 같은 링 위에 배치한다.**

서버 IP나 이름을 해시해서 링 위 특정 위치에 놓는다. 키도 같은 방식으로 링 위에 배치한다. 그리고 규칙은 하나:

> **시계 방향으로 탐색해서 만나는 첫 번째 서버에 키를 저장한다.**

server0, server1, server2, server3이 링 위에 있고 key0이 server0과 server1 사이에 있다면, key0은 server1에 저장된다.

## 서버 추가/제거: 영향받는 키가 최소화된다

**server4를 추가한다면:**

server4가 링 위 server0~server1 사이에 배치된다고 하자. 이제 그 구간에 있던 키 중 일부만 server4로 이동하면 된다. 나머지 키는 그대로다.

**server1을 제거한다면:**

server1이 담당하던 구간의 키들이 시계 방향 다음 서버(server2)로 이동한다. 역시 나머지 키는 영향 없다.

단순 나머지 해시와 비교하면: 영향받는 키 수는 전체의 약 `1/n`(n = 서버 수)에 불과하다.

## 기본 구현의 두 가지 문제

링 위에 서버 4개만 있으면 현실적인 문제가 생긴다.

**1. 파티션 크기 불균등**

서버를 하나 제거하면 남은 서버의 담당 구간이 갑자기 2배가 될 수 있다. 링 위 간격이 균등하게 유지된다는 보장이 없다.

**2. 키 쏠림**

server2 구간이 링의 절반을 차지하면, 전체 키의 절반이 server2로 쏠린다. 나머지 서버는 놀고 있는 셈이다.

## 가상 노드: 균등 분포를 만드는 방법

해결책은 각 서버를 링 위 여러 위치에 동시에 배치하는 것이다. 이것이 **가상 노드(Virtual Nodes)**다.

```
server0 → server0_0, server0_1, server0_2 (링 위 세 곳)
server1 → server1_0, server1_1, server1_2 (링 위 세 곳)
```

시계 방향으로 가장 가까운 가상 노드를 찾으면, 실제 서버가 결정된다. 가상 노드가 많을수록 키 분포가 균등해진다. 100~200개 수준이면 표준편차가 약 5~10%까지 줄어든다.

트레이드오프는 있다. 가상 노드 수가 늘수록 균등 분포는 좋아지지만, 가상 노드 정보를 저장하는 공간이 늘어난다. 시스템 요구사항에 따라 적정 수를 설정하면 된다.

## 실제로 어디에 쓰이나

이론이 아니다. 지금 운영 중인 시스템들에 들어가 있다:

| 시스템 | 역할 |
|--------|------|
| Amazon DynamoDB | 데이터 파티셔닝 |
| Apache Cassandra | 분산 KV 파티셔닝 |
| Discord | 5백만 동시 접속 처리 |
| Akamai CDN | 엣지 서버 트래픽 분산 |
| Maglev (Google) | 네트워크 로드 밸런서 |

## 핵심 정리

- `hash(key) % N`은 N이 바뀌면 대부분의 키를 재배치해야 한다
- 안정 해시는 링 구조로 이 문제를 해결한다 — 서버 변경 시 영향받는 키가 `k/n`으로 줄어든다
- 가상 노드를 쓰면 파티션 불균등과 키 쏠림 문제를 추가로 해결할 수 있다
- 6장 키-값 저장소 설계에서 이 개념이 바로 재활용된다

## 관련 페이지

- [[concepts/consistent-hashing]]
- [[sources/2026-04-20-system-design-interview-ch5]]
- [[topics/system-design-interview-04]]
- [[concepts/database-sharding]]
- [[concepts/load-balancer]]
- [[projects/study-system-design-interview]]
