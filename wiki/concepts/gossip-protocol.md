---
title: "가십 프로토콜 (Gossip Protocol)"
created: "2026-04-21"
updated: "2026-04-21"
type: concept
sources: ["[[sources/2026-04-21-system-design-interview-ch6]]"]
tags: [system-design, gossip-protocol, distributed-systems, failure-detection, membership]
status: active
published: false
slug: ""
description: ""
---

# 가십 프로토콜 (Gossip Protocol)

분산 시스템에서 노드 간 정보를 전파하는 분산화된 프로토콜. 전염병이 퍼지는 방식에서 이름을 따왔다. 멤버십 관리, 장애 감지, 데이터 동기화에 사용된다.

## 장애 감지에서의 역할

대규모 분산 시스템에서 중앙 집중식 장애 감지(멀티캐스트)는 트래픽 비효율적. 가십 프로토콜은 분산 방식으로 해결.

## 동작 방식

1. 각 노드는 **멤버십 목록**을 유지 (노드 ID + heartbeat 카운터)
2. 각 노드는 주기적으로 카운터를 증가
3. 무작위로 선택한 이웃 노드에게 자신의 멤버십 목록을 전송
4. 목록을 수신한 노드는 자신의 목록과 병합 (최신 카운터 유지)
5. 일정 시간 동안 카운터가 갱신되지 않은 노드 → **장애로 판단**

## 특성

- **분산성:** 단일 장애점(SPOF) 없음
- **확장성:** 노드 수에 비례해 트래픽이 소폭 증가
- **최종 일관성:** 충분한 라운드 후 모든 노드가 동일 상태 파악
- **내결함성:** 일부 메시지 유실에도 동작

## 활용 사례

- Apache Cassandra: 멤버십 관리 및 장애 감지
- Amazon DynamoDB: 분산 키-값 저장소의 내부 통신
- Consul: 서비스 디스커버리

## 단순 타임아웃 방식과의 차이

단순 타임아웃은 느린 네트워크를 장애로 오판 가능. 가십은 여러 노드의 관찰을 종합하므로 더 신뢰성 있는 판단.

## 관련 페이지

- [[concepts/key-value-store]]
- [[concepts/cap-theorem]]
- [[concepts/vector-clock]]
- [[sources/2026-04-21-system-design-interview-ch6]]
