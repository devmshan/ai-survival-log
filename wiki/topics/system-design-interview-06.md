---
title: "시스템 설계 면접 6장 — 키-값 저장소 설계"
created: "2026-04-21"
updated: "2026-04-21"
type: topic
sources: ["[[sources/2026-04-21-system-design-interview-ch6]]"]
tags: [system-design, key-value-store, cap-theorem, distributed-systems, study, backend, interview]
status: active
published: false
slug: ""
description: ""
---

# 시스템 설계 면접 6장 — 키-값 저장소 설계

분산 키-값 저장소 설계의 핵심은 "어떻게 데이터를 여러 서버에 나누고, 복제하고, 일관성을 유지하면서도 장애를 버티는가"다. 이 장은 CAP 정리부터 벡터 시계, 가십 프로토콜, SSTable까지 분산 시스템의 핵심 개념을 실제 설계로 연결한다.

## 핵심 설계 질문

"키-값 저장소를 설계하라"는 요청에서 먼저 답해야 할 것:
- 단일 서버? 분산?
- 강한 일관성 vs 높은 가용성 — CAP 트레이드오프 어디에?
- 읽기 vs 쓰기 중 어느 쪽이 많은가?
- 데이터 크기와 수명?

## 분산 설계 핵심 원칙

### 데이터 파티션 — 안정 해시(Consistent Hashing)
노드 추가/삭제 시 최소한의 데이터만 재배치. 가상 노드로 불균형 완화. ([[concepts/consistent-hashing]])

### CAP 정리 — 트레이드오프 선택
[[concepts/cap-theorem]]에 따라 CP(일관성 우선) 또는 AP(가용성 우선) 선택.
네트워크 파티션은 피할 수 없으므로 P는 기본.

### 정족수 합의 (Quorum Consensus)
- N개 복제 서버, W개 쓰기 응답, R개 읽기 응답
- W+R > N → 강한 일관성
- W=1, R=1 → 빠른 응답 (최종 일관성)

### 불일치 해소 — 벡터 시계
[[concepts/vector-clock]]으로 버전 충돌 감지, 클라이언트가 해소.

### 장애 감지 — 가십 프로토콜
[[concepts/gossip-protocol]]으로 중앙화 없이 노드 장애를 분산 감지.

### 장애 처리
- **단순 장애:** 느슨한 정족수(Sloppy Quorum) + hinted handoff로 처리
- **영구 장애:** 머클 트리(Merkle Tree)로 복제 서버 간 불일치 효율 탐지·동기화

## 쓰기/읽기 경로

```
쓰기: 커밋 로그 → 메모리 캐시 → (가득 차면) SSTable 플러시
읽기: 메모리 캐시 → 없으면 블룸 필터로 SSTable 탐색
```

이 패턴은 LSM 트리(Log-Structured Merge Tree)의 핵심으로, HBase와 Cassandra가 채택.

## 면접 포인트

- CAP 정리를 말할 때 "CA는 불가능"이 아니라 "P가 필수이므로 CP 또는 AP 선택"으로 설명
- 정족수 공식 W+R > N을 W, R, N 값으로 구체화
- 읽기 성능을 위해 블룸 필터가 어떻게 디스크 I/O를 줄이는지 설명

## 관련 페이지

- [[concepts/key-value-store]]
- [[concepts/cap-theorem]]
- [[concepts/vector-clock]]
- [[concepts/gossip-protocol]]
- [[concepts/consistent-hashing]]
- [[concepts/bloom-filter]]
- [[sources/2026-04-21-system-design-interview-ch6]]
- [[projects/study-system-design-interview]]
