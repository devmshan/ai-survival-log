---
title: "시스템 설계 면접 9장 — 웹 크롤러 설계"
created: "2026-04-21"
updated: "2026-04-21"
type: topic
sources: ["[[sources/2026-04-21-system-design-interview-ch9]]"]
tags: [system-design, web-crawler, bfs, bloom-filter, distributed-systems, study, backend, interview]
status: active
published: false
slug: ""
description: ""
---

# 시스템 설계 면접 9장 — 웹 크롤러 설계

웹 크롤러는 "단순히 페이지 다운로드" 이상이다. 수십억 페이지를 공손하게, 중복 없이, 우선순위를 지켜 수집하는 것이 핵심이다. BFS, 미수집 URL 저장소(Frontier), 블룸 필터, 분산 크롤러 설계를 연결한다.

## 규모 추정

- 월 10억 페이지 수집 → 초당 약 400 QPS (최대 800)
- 평균 페이지 500KB → 월 500TB, 5년 보관 시 30PB

## 핵심 컴포넌트와 역할

```
시작 URL → Frontier(우선순위 큐)
         → HTML 다운로더(DNS 리졸버)
         → 콘텐츠 파서
         → 중복 확인 → 콘텐츠 저장소
         → URL 추출기 → URL 필터
         → 블룸 필터(중복 URL 제거)
         → Frontier로 피드백
```

## Frontier 설계 — 이 장의 핵심

### 1. Politeness (예의 바름)
같은 호스트에 과도한 요청 금지. 큐마다 특정 호스트에 매핑, 요청 간 딜레이 삽입.

### 2. 우선순위
PageRank, 트래픽, 갱신 빈도 → 우선순위 큐. 중요 페이지를 먼저 수집.

### 3. 신선도
이미 수집한 페이지도 갱신 주기에 따라 재수집. 사이트맵 활용.

## 중복 제거 전략

- **URL 중복:** [[concepts/bloom-filter]]로 수십억 URL 메모리 효율적 확인
- **콘텐츠 중복:** SimHash 등으로 유사 페이지 탐지 (30%가 중복)

## robots.txt

모든 크롤러는 반드시 robots.txt를 읽고 준수해야 한다. Disallow 된 경로는 절대 수집하지 않음.

## 확장 포인트

- 분산 크롤러: 여러 서버가 Frontier 공유
- DNS 캐시: IP 조회 오버헤드 감소
- 지역성: 크롤러 서버와 대상 서버를 같은 리전에 배치
- 짧은 타임아웃: 응답 없는 서버 신속히 건너뜀
- 서버 사이드 렌더링: Headless browser로 동적 페이지 처리

## 마무리 고려사항

- **URL 필터링:** 스팸, 광고, 악성 URL 제외
- **DB 다중화·샤딩**
- **수평 확장**
- **데이터 분석:** 수집 통계, 크롤링 커버리지 모니터링

## 면접 포인트

- DFS가 아닌 BFS를 쓰는 이유를 "한 도메인 집중 방지 + 균형 있는 수집"으로 설명
- Politeness와 Priority를 Frontier의 두 별도 관심사로 분리 설명
- 블룸 필터의 False Positive를 "허용 가능한 트레이드오프"로 정당화

## 관련 페이지

- [[concepts/web-crawler]]
- [[concepts/bloom-filter]]
- [[sources/2026-04-21-system-design-interview-ch9]]
- [[projects/study-system-design-interview]]
