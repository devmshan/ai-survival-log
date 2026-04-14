---
title: "로드밸런서"
created: "2026-04-14"
updated: "2026-04-14"
type: concept
sources: ["[[sources/2026-04-14-system-design-interview-v1]]"]
tags: ["system-design", "load-balancer", "scalability", "high-availability", "distributed-systems"]
status: active
published: false
slug: ""
description: ""
---

# 로드밸런서

여러 서버에 트래픽을 균등하게 분산하여 가용성과 확장성을 높이는 장치.

## 동작 원리

```
클라이언트 → 로드밸런서(공개 IP) → 서버1(사설 IP)
                                  → 서버2(사설 IP)
                                  → 서버3(사설 IP)
```

- 클라이언트는 로드밸런서의 **공개 IP 주소**로만 접속
- 서버들은 **사설 IP 주소**를 가짐 — 클라이언트가 직접 접근 불가
- 로드밸런서가 각 서버의 상태를 감지하고 요청을 분배

## 주요 기능

### 장애 대처 (Failover)

- 서버1이 다운되면 → 자동으로 서버2, 서버3으로만 트래픽 전달
- 웹사이트 전체 다운 방지
- 자동 복구(auto-recovery) 지원

### 가용성 향상

- 트래픽이 증가하면 서버 풀에 새 서버 추가
- 로드밸런서가 자동으로 새 서버에도 트래픽 분배
- 다운타임 없이 수평 확장(scale out) 가능

## 로드밸런싱 알고리즘

- **Round Robin (라운드 로빈):** 순서대로 순환 분배
- **Least Connections:** 현재 연결이 가장 적은 서버로
- **IP Hash:** 같은 클라이언트 IP → 항상 같은 서버 (세션 유지 필요 시)
- **Weighted:** 서버 스펙에 따라 가중치 부여

## 고려사항

- 로드밸런서 자체도 단일 장애 지점(SPOF)이 될 수 있음 → 로드밸런서 이중화 필요
- 세션(Session) 데이터: 여러 서버에 요청이 분산되면 세션 유지 문제 발생 → [[concepts/stateless-architecture]]로 해결

## 관련 페이지

- [[concepts/vertical-vs-horizontal-scaling]] — 수평 확장을 위한 기반
- [[concepts/stateless-architecture]] — 로드밸런서와 함께 사용되는 아키텍처
- [[concepts/db-replication]] — 데이터베이스 계층의 다중화
- [[projects/study-system-design-interview]] — 시스템 설계 스터디
