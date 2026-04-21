---
title: "벡터 시계 (Vector Clock)"
created: "2026-04-21"
updated: "2026-04-21"
type: concept
sources: ["[[sources/2026-04-21-system-design-interview-ch6]]"]
tags: [system-design, vector-clock, distributed-systems, consistency, conflict-resolution]
status: active
published: false
slug: ""
description: ""
---

# 벡터 시계 (Vector Clock)

분산 시스템에서 데이터 버전 간의 인과관계를 추적하고 충돌을 감지하는 알고리즘. `[서버, 버전]` 쌍의 리스트로 표현된다.

## 표기

```
D([S1, v1], [S2, v2], ..., [Sn, vn])
```

- D: 데이터 항목
- Si: 서버 이름
- vi: 버전 번호

## 동작 원리

1. 서버 Si에서 데이터가 쓰이면 Si의 버전 카운터를 1 증가
2. 다른 서버에서 복제받은 데이터는 해당 서버의 카운터를 동기화
3. 두 벡터를 비교해 선후 관계 판단:
   - X의 모든 카운터가 Y 이하 → X는 Y의 이전 버전 (X를 버려도 됨)
   - X와 Y 어느 쪽도 상대방의 이전 버전이 아님 → 충돌 → 클라이언트가 해소

## 충돌 해소

충돌 감지 후 해소 책임은 **클라이언트**에게 있음. Amazon DynamoDB가 이 방식을 사용.

## 단점

- 클라이언트 로직 복잡도 증가
- `[서버, 버전]` 쌍이 빠르게 늘어남 → 크기 제한 필요 (제일 오래된 쌍 삭제, 단 정확성 저하 가능)

## 타임스탬프와의 차이

물리 시계는 네트워크 지연, 시계 드리프트로 인과관계 보장 불가. 벡터 시계는 논리적 인과관계를 정확하게 추적.

## 관련 페이지

- [[concepts/key-value-store]]
- [[concepts/cap-theorem]]
- [[concepts/gossip-protocol]]
- [[sources/2026-04-21-system-design-interview-ch6]]
