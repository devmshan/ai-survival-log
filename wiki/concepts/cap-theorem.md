---
title: "CAP 정리 (CAP Theorem)"
created: "2026-04-21"
updated: "2026-04-21"
type: concept
sources: ["[[sources/2026-04-21-system-design-interview-ch6]]"]
tags: [system-design, cap-theorem, distributed-systems, consistency, availability]
status: active
published: false
slug: ""
description: ""
---

# CAP 정리 (CAP Theorem)

분산 시스템은 일관성(Consistency), 가용성(Availability), 파티션 감내(Partition Tolerance) 세 가지 속성 중 **두 가지만 동시에 만족**할 수 있다는 정리. Eric Brewer가 2000년에 제안.

## 세 가지 속성

| 속성 | 설명 |
|------|------|
| **일관성(Consistency)** | 모든 노드가 동시에 동일 데이터를 반환. 쓰기 후 모든 읽기에서 최신 값 조회 |
| **가용성(Availability)** | 일부 노드에 장애가 발생해도 모든 요청에 응답 반환 (단, 최신 데이터 보장 불가) |
| **파티션 감내(Partition Tolerance)** | 네트워크 파티션(노드 간 통신 단절) 상황에서도 시스템 동작 |

## 실세계 선택

네트워크 파티션은 현실적으로 피할 수 없으므로 **P는 항상 필요**. 따라서 실제 선택은:

- **CP 시스템:** 파티션 발생 시 가용성 포기 → 일관성 유지. 예: HBase, Zookeeper, MongoDB(강한 일관성 모드)
- **AP 시스템:** 파티션 발생 시 일관성 포기 → 가용성 유지 (최종 일관성). 예: DynamoDB, Cassandra, CouchDB

## CA 조합은 왜 불가능한가?

네트워크 파티션이 없다면 CA 가능하지만, 분산 시스템에서 파티션은 필연적. 단일 서버 DB(MySQL 등)는 CA에 가깝지만 분산이 아님.

## 일관성 스펙트럼

강한 일관성 ↔ 최종 일관성(Eventual Consistency) 사이에 다양한 수준이 존재:
- **강한 일관성:** 쓰기 완료 후 모든 읽기에서 최신 값
- **약한 일관성:** 쓰기 후 즉시 읽어도 최신 값 보장 안 됨
- **최종 일관성:** 충분한 시간이 지나면 모든 복제본이 동일

## 관련 패턴

- 정족수 합의(Quorum Consensus) → W+R > N이면 강한 일관성
- 벡터 시계 → 충돌 감지 및 해소
- 가십 프로토콜 → 장애 감지

## 관련 페이지

- [[concepts/key-value-store]]
- [[concepts/vector-clock]]
- [[concepts/gossip-protocol]]
- [[concepts/db-replication]]
- [[concepts/consistent-hashing]]
- [[sources/2026-04-21-system-design-interview-ch6]]
