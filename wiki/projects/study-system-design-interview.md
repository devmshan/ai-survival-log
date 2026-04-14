---
title: "시스템 설계 면접 스터디 플랜"
created: "2026-04-14"
updated: "2026-04-14"
type: project
sources: ["[[sources/2026-04-14-system-design-interview-v1]]"]
tags: ["system-design", "study", "backend", "distributed-systems", "interview"]
status: active
published: false
slug: ""
description: ""
---

# 시스템 설계 면접 스터디 플랜

> 책: 가상 면접 사례로 배우는 대규모 시스템 설계 기초 (Alex Xu)
> 방식: 사용자 질문 → 설명 + 역질문 → 위키 저장

## 스터디 방식

### 진행 흐름

```
사용자: 책 읽다가 궁금한 개념 질문
  ↓
Claude: 개념 설명 (트레이드오프 포함) + 빠진 부분 역질문
  ↓
챕터 마무리 시: wiki/concepts/에 정리 저장
```

### 규칙

- **사용자 주도**: 사용자가 책을 읽으며 궁금한 것을 질문, 순서는 자유
- **역질문**: Claude가 설명 후 빠진 핵심 개념 있으면 추가 질문으로 유도
- **위키 저장**: 한 챕터 관련 개념이 충분히 쌓이면 `wiki/concepts/`에 저장
- **이어서 진행**: 새 세션 시작 시 이 문서 + `wiki/index.md`로 진행 상황 파악

### 현재 진행 상황

| 챕터 | 상태 | 생성된 위키 페이지 |
|------|------|-------------------|
| 1장 | ⬜ 미시작 | - |
| 2장 | ⬜ 미시작 | - |
| 3장 | ⬜ 미시작 | - |
| 4장 | ⬜ 미시작 | - |
| 5장 | ⬜ 미시작 | - |
| 6장 | ⬜ 미시작 | - |
| 7장 | ⬜ 미시작 | - |
| 8장 | ⬜ 미시작 | - |
| 9장 | ⬜ 미시작 | - |
| 10장 | ⬜ 미시작 | - |
| 11장 | ⬜ 미시작 | - |
| 12장 | ⬜ 미시작 | - |
| 13장 | ⬜ 미시작 | - |
| 14장 | ⬜ 미시작 | - |
| 15장 | ⬜ 미시작 | - |

> 챕터 완료 시: ✅ 로 변경 + 생성된 위키 페이지 링크 기록

---

## Phase 1: 기초 다지기 (1~3장)

> 전체 맥락과 사고법을 익히는 단계. 이후 모든 챕터의 기반이 됨.

### 1장 — 사용자 수에 따른 규모 확장성

**학습 목표:** 서비스가 1명 → 수백만 명으로 성장할 때 아키텍처가 어떻게 진화하는지 이해

| 단계 | 다룰 개념 | 위키 페이지 | 상태 |
|------|-----------|-------------|------|
| 1-1 | 단일 서버 → DB 분리 (웹/데이터 계층 분리 이유) | - | ⬜ |
| 1-2 | 수직 확장(Scale Up) vs 수평 확장(Scale Out) 트레이드오프 | `concepts/vertical-vs-horizontal-scaling` | ⬜ |
| 1-3 | 로드 밸런서 — 역할, 동작 방식, 이중화 | `concepts/load-balancer` | ⬜ |
| 1-4 | DB 다중화 — 주(Master)/부(Replica) 구조, 장애 처리 | `concepts/db-replication` | ⬜ |
| 1-5 | 캐시 — 캐시 계층, Read-Through/Write-Through 전략 | `concepts/cache-strategies` | ⬜ |
| 1-6 | CDN — 정적 콘텐츠 캐싱, 동작 원리 | `concepts/cdn` | ⬜ |
| 1-7 | 무상태(Stateless) 계층 — 세션 공유 문제, Stateless 설계 | `concepts/stateless-architecture` | ⬜ |
| 1-8 | 데이터센터 — 지리적 라우팅, 장애 복구 | - | ⬜ |
| 1-9 | 메시지 큐 — 비동기 처리, 생산자/소비자 모델 | `concepts/message-queue` | ⬜ |
| 1-10 | 로그·지표·자동화 — 운영 관점 모니터링 기초 | - | ⬜ |

---

### 2장 — 개략적인 규모 추정

**학습 목표:** 면접에서 "이 시스템의 QPS는?" "저장소는 얼마나 필요해?" 를 빠르게 추정하는 감각 훈련

| 단계 | 다룰 개념 | 위키 페이지 | 상태 |
|------|-----------|-------------|------|
| 2-1 | 2의 제곱수 — KB/MB/GB/TB/PB 단위 감각 | `concepts/back-of-envelope-estimation` | ⬜ |
| 2-2 | 응답지연(Latency) 기준값 — L1 캐시~디스크~네트워크 숫자 암기 | `concepts/back-of-envelope-estimation` | ⬜ |
| 2-3 | 가용성(Availability) 수치 — 99%, 99.9%, 99.999% 연간 다운타임 | `concepts/availability` | ⬜ |
| 2-4 | QPS 추정 실습 — DAU → 초당 요청수 계산 공식 | `concepts/back-of-envelope-estimation` | ⬜ |
| 2-5 | 저장소 추정 실습 — 트위터 예제로 5년치 저장소 계산 | `concepts/back-of-envelope-estimation` | ⬜ |

---

### 3장 — 시스템 설계 면접 공략법

**학습 목표:** 실제 면접에서 쓰는 4단계 프레임워크 체득. 정답이 없는 문제를 다루는 사고 방식

| 단계 | 다룰 개념 | 위키 페이지 | 상태 |
|------|-----------|-------------|------|
| 3-1 | 시스템 설계 면접의 특성 — 왜 정답이 없는가 | `concepts/system-design-interview-framework` | ⬜ |
| 3-2 | Step 1: 문제 이해 및 설계 범위 확정 — 올바른 질문하기 | `concepts/system-design-interview-framework` | ⬜ |
| 3-3 | Step 2: 개략적 설계안 제시 — 화이트보드 스케치, 핵심 API | `concepts/system-design-interview-framework` | ⬜ |
| 3-4 | Step 3: 상세 설계 — 병목 찾기, 우선순위 결정 | `concepts/system-design-interview-framework` | ⬜ |
| 3-5 | Step 4: 마무리 — 병목 지적, 운영 이슈, 미래 확장 논의 | `concepts/system-design-interview-framework` | ⬜ |
| 3-6 | 해야 할 것 / 하지 말아야 할 것 체크리스트 | `concepts/system-design-interview-framework` | ⬜ |

---

## Phase 2: 핵심 컴포넌트 (4~7장)

> 재사용되는 빌딩 블록. 이후 실전 설계 챕터에서 반복 등장.

### 4장 — 처리율 제한 장치 (Rate Limiter)

**학습 목표:** API 남용 방지 장치를 5가지 알고리즘으로 설계. 분산 환경에서의 구현까지

| 단계 | 다룰 개념 | 위키 페이지 | 상태 |
|------|-----------|-------------|------|
| 4-1 | Rate Limiter가 필요한 이유 — DoS, 비용, 서버 과부하 | `concepts/rate-limiter` | ⬜ |
| 4-2 | 배치 위치 — 클라이언트 / 서버 사이드 / 미들웨어(API Gateway) | `concepts/rate-limiter` | ⬜ |
| 4-3 | 알고리즘 1: 토큰 버킷 (Token Bucket) | `concepts/rate-limiter` | ⬜ |
| 4-4 | 알고리즘 2: 누출 버킷 (Leaky Bucket) | `concepts/rate-limiter` | ⬜ |
| 4-5 | 알고리즘 3: 고정 윈도우 카운터 (Fixed Window Counter) | `concepts/rate-limiter` | ⬜ |
| 4-6 | 알고리즘 4: 이동 윈도우 로그 (Sliding Window Log) | `concepts/rate-limiter` | ⬜ |
| 4-7 | 알고리즘 5: 이동 윈도우 카운터 (Sliding Window Counter) | `concepts/rate-limiter` | ⬜ |
| 4-8 | 상세 설계 — Redis 활용, 분산 환경 경쟁 조건, HTTP 헤더 응답 | `concepts/rate-limiter` | ⬜ |

---

### 5장 — 안정 해시 (Consistent Hashing)

**학습 목표:** 서버 추가/제거 시 데이터 재배치 최소화. 분산 시스템의 핵심 기법

| 단계 | 다룰 개념 | 위키 페이지 | 상태 |
|------|-----------|-------------|------|
| 5-1 | 해시 키 재배치 문제 — 나머지 연산 해시의 한계 | `concepts/consistent-hashing` | ⬜ |
| 5-2 | 안정 해시 — 해시 링(Hash Ring) 구조 | `concepts/consistent-hashing` | ⬜ |
| 5-3 | 기본 구현의 문제 — 불균등 분포, 키 쏠림 | `concepts/consistent-hashing` | ⬜ |
| 5-4 | 가상 노드 (Virtual Nodes) — 균등 분포 해결 | `concepts/consistent-hashing` | ⬜ |
| 5-5 | 활용 사례 — Amazon DynamoDB, Apache Cassandra, CDN | `concepts/consistent-hashing` | ⬜ |

---

### 6장 — 키-값 저장소 (Key-Value Store)

**학습 목표:** DynamoDB/Cassandra 같은 분산 KV 스토어를 직접 설계. CAP 정리 체화

| 단계 | 다룰 개념 | 위키 페이지 | 상태 |
|------|-----------|-------------|------|
| 6-1 | CAP 정리 — 일관성/가용성/파티션 허용, 왜 셋 다 불가능한가 | `concepts/cap-theorem` | ⬜ |
| 6-2 | 데이터 파티셔닝 — 안정 해시로 노드 분산 | `concepts/key-value-store` | ⬜ |
| 6-3 | 데이터 다중화 — N개 서버에 복사본 저장 | `concepts/key-value-store` | ⬜ |
| 6-4 | 일관성 모델 — 강한/약한/최종 일관성 트레이드오프 | `concepts/consistency-models` | ⬜ |
| 6-5 | 쿼럼 합의 (Quorum Consensus) — N, W, R 설정의 의미 | `concepts/key-value-store` | ⬜ |
| 6-6 | 일관성 불일치 해소 — 버저닝, 벡터 시계 | `concepts/key-value-store` | ⬜ |
| 6-7 | 장애 감지 — 가십 프로토콜 (Gossip Protocol) | `concepts/key-value-store` | ⬜ |
| 6-8 | 장애 처리 — 느슨한 정족수, 단서 후 인계 | `concepts/key-value-store` | ⬜ |
| 6-9 | 영구 저장소 — LSM 트리, SSTable, 블룸 필터 | `concepts/key-value-store` | ⬜ |
| 6-10 | 머클 트리 (Merkle Tree) — 반-엔트로피 수선 프로토콜 | `concepts/key-value-store` | ⬜ |

---

### 7장 — 분산 유일 ID 생성기

**학습 목표:** 분산 환경에서 전역 유일한 ID를 만드는 4가지 접근법 비교

| 단계 | 다룰 개념 | 위키 페이지 | 상태 |
|------|-----------|-------------|------|
| 7-1 | 요구사항 — 유일성, 숫자만, 64비트, 시간순 정렬, 초당 10,000개 | `concepts/distributed-id-generator` | ⬜ |
| 7-2 | 접근법 1: 다중 마스터 복제 — auto_increment 한계 | `concepts/distributed-id-generator` | ⬜ |
| 7-3 | 접근법 2: UUID — 128비트, 독립 생성, 정렬 불가 문제 | `concepts/distributed-id-generator` | ⬜ |
| 7-4 | 접근법 3: 티켓 서버 — Flickr 방식, SPOF 문제 | `concepts/distributed-id-generator` | ⬜ |
| 7-5 | 접근법 4: 트위터 스노플레이크 — 64비트 구조 (타임스탬프/데이터센터/머신/시퀀스) | `concepts/distributed-id-generator` | ⬜ |

---

## Phase 3: 시스템 설계 실전 I (8~11장)

> 3장에서 배운 프레임워크 + Phase 2의 빌딩 블록으로 실전 시스템 설계

### 8장 — URL 단축기

| 단계 | 다룰 개념 | 위키 페이지 | 상태 |
|------|-----------|-------------|------|
| 8-1 | API 설계 — POST (단축), GET (리다이렉션) | `concepts/url-shortener` | ⬜ |
| 8-2 | URL 리다이렉션 — 301(영구) vs 302(임시) 트레이드오프 | `concepts/url-shortener` | ⬜ |
| 8-3 | 해시 함수 — CRC32/MD5/SHA-1, 충돌 해소 전략 | `concepts/url-shortener` | ⬜ |
| 8-4 | Base62 인코딩 — 62진법으로 짧은 URL 생성 | `concepts/url-shortener` | ⬜ |
| 8-5 | 캐싱 전략 — 조회 빈도 높은 URL 캐싱, 블룸 필터 | `concepts/url-shortener` | ⬜ |

### 9장 — 웹 크롤러

| 단계 | 다룰 개념 | 위키 페이지 | 상태 |
|------|-----------|-------------|------|
| 9-1 | 구성 요소 — URL Frontier, HTML Downloader, Content Parser | `concepts/web-crawler` | ⬜ |
| 9-2 | BFS vs DFS — 왜 크롤러는 BFS를 쓰는가 | `concepts/web-crawler` | ⬜ |
| 9-3 | 예의 바른 크롤러 — Robots.txt, 크롤 딜레이, 도메인별 우선순위 | `concepts/web-crawler` | ⬜ |
| 9-4 | 중복 제거 — 이미 수집한 URL·콘텐츠 판별 (블룸 필터) | `concepts/web-crawler` | ⬜ |
| 9-5 | 성능 최적화 — 분산 크롤링, DNS 캐싱, locality | `concepts/web-crawler` | ⬜ |

### 10장 — 알림 시스템

| 단계 | 다룰 개념 | 위키 페이지 | 상태 |
|------|-----------|-------------|------|
| 10-1 | 알림 유형별 흐름 — iOS(APNs), Android(FCM), SMS, Email | `concepts/notification-system` | ⬜ |
| 10-2 | 연락처 수집 — 토큰/번호/이메일 수집 시점 | `concepts/notification-system` | ⬜ |
| 10-3 | 안정성 — 소실 방지(영속 큐), 중복 전송 방지(멱등성 키) | `concepts/notification-system` | ⬜ |
| 10-4 | 추가 컴포넌트 — 알림 설정, 전송률 제한, 재시도, 이벤트 추적 | `concepts/notification-system` | ⬜ |

### 11장 — 뉴스 피드 시스템

| 단계 | 다룰 개념 | 위키 페이지 | 상태 |
|------|-----------|-------------|------|
| 11-1 | 피드 발행(Feed Publishing) 흐름 | `concepts/news-feed` | ⬜ |
| 11-2 | 팬아웃 — 쓰기 시점(Push) vs 읽기 시점(Pull) 트레이드오프 | `concepts/fan-out` | ⬜ |
| 11-3 | 혼합 접근법 — 인플루언서 vs 일반 사용자 다르게 처리 | `concepts/fan-out` | ⬜ |
| 11-4 | 캐시 계층 5단계 — 뉴스피드/콘텐츠/소셜그래프/액션/카운터 | `concepts/news-feed` | ⬜ |

---

## Phase 4: 시스템 설계 실전 II (12~15장)

> 더 복잡한 실시간·대용량 시스템 설계

### 12장 — 채팅 시스템

| 단계 | 다룰 개념 | 위키 페이지 | 상태 |
|------|-----------|-------------|------|
| 12-1 | 폴링 vs 롱 폴링 vs WebSocket — 왜 채팅은 WebSocket인가 | `concepts/websocket-vs-polling` | ⬜ |
| 12-2 | 저장소 선택 — 일반 데이터(RDB) vs 채팅 이력(Cassandra) | `concepts/chat-system` | ⬜ |
| 12-3 | 메시지 동기화 — cur_max_message_id로 새 메시지 판별 | `concepts/chat-system` | ⬜ |
| 12-4 | 소규모 vs 대규모 그룹 채팅 — 설계 차이 | `concepts/chat-system` | ⬜ |
| 12-5 | 접속 상태 표시 — 하트비트 메커니즘 | `concepts/chat-system` | ⬜ |

### 13장 — 검색어 자동완성

| 단계 | 다룰 개념 | 위키 페이지 | 상태 |
|------|-----------|-------------|------|
| 13-1 | Trie 자료구조 — 접두사 탐색, 시간 복잡도 | `concepts/trie` | ⬜ |
| 13-2 | 트라이 최적화 — 각 노드에 상위 k개 검색어 캐싱 | `concepts/trie` | ⬜ |
| 13-3 | 데이터 수집 서비스 — 로그 집계, 빈도수 계산 파이프라인 | `concepts/typeahead-system` | ⬜ |
| 13-4 | 쿼리 서비스 — 트라이 캐시, 필터링(욕설 등), 다국어 | `concepts/typeahead-system` | ⬜ |

### 14장 — 유튜브 설계

| 단계 | 다룰 개념 | 위키 페이지 | 상태 |
|------|-----------|-------------|------|
| 14-1 | 비디오 업로드 흐름 — 원본 저장소, 트랜스코딩, CDN 배포 | `concepts/video-streaming-platform` | ⬜ |
| 14-2 | DAG 파이프라인 — 병렬 인코딩 작업 그래프 | `concepts/video-streaming-platform` | ⬜ |
| 14-3 | 스트리밍 프로토콜 — MPEG-DASH, HLS, RTMP 비교 | `concepts/video-streaming-platform` | ⬜ |
| 14-4 | 안전성 — Pre-signed URL, DRM, 워터마크 | `concepts/video-streaming-platform` | ⬜ |
| 14-5 | 비용 절감 — CDN 비용 최적화, 인기도별 차등 저장 | `concepts/video-streaming-platform` | ⬜ |

### 15장 — 구글 드라이브

| 단계 | 다룰 개념 | 위키 페이지 | 상태 |
|------|-----------|-------------|------|
| 15-1 | 블록 저장소 서버 — 파일을 블록으로 분할, 압축, 암호화 | `concepts/google-drive` | ⬜ |
| 15-2 | 델타 동기화 — 변경된 블록만 전송 | `concepts/google-drive` | ⬜ |
| 15-3 | 알림 서비스 — 롱 폴링으로 파일 변경 감지 | `concepts/google-drive` | ⬜ |
| 15-4 | 오프라인 백업 큐 — 오프라인 중 변경사항 처리 | `concepts/google-drive` | ⬜ |

---

## 생성될 위키 Concepts 페이지 목록

| 페이지 | 생성 챕터 |
|--------|-----------|
| `concepts/vertical-vs-horizontal-scaling` | 1장 |
| `concepts/load-balancer` | 1장 |
| `concepts/db-replication` | 1장 |
| `concepts/cache-strategies` | 1장 |
| `concepts/cdn` | 1장 |
| `concepts/stateless-architecture` | 1장 |
| `concepts/message-queue` | 1장 |
| `concepts/back-of-envelope-estimation` | 2장 |
| `concepts/availability` | 2장 |
| `concepts/system-design-interview-framework` | 3장 |
| `concepts/rate-limiter` | 4장 |
| `concepts/consistent-hashing` | 5장 |
| `concepts/cap-theorem` | 6장 |
| `concepts/key-value-store` | 6장 |
| `concepts/consistency-models` | 6장 |
| `concepts/distributed-id-generator` | 7장 |
| `concepts/url-shortener` | 8장 |
| `concepts/web-crawler` | 9장 |
| `concepts/notification-system` | 10장 |
| `concepts/news-feed` | 11장 |
| `concepts/fan-out` | 11장 |
| `concepts/websocket-vs-polling` | 12장 |
| `concepts/chat-system` | 12장 |
| `concepts/trie` | 13장 |
| `concepts/typeahead-system` | 13장 |
| `concepts/video-streaming-platform` | 14장 |
| `concepts/google-drive` | 15장 |

## 관련 페이지

- [[sources/2026-04-14-system-design-interview-v1]]
- [[topics/ai-era-survival]]
