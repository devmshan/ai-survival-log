---
title: "대규모 시스템 설계 기초 — 9장: 웹 크롤러 설계"
created: "2026-04-21"
updated: "2026-04-21"
type: source
sources: []
tags: [system-design, web-crawler, bfs, bloom-filter, distributed-systems, book]
status: active
published: false
slug: ""
description: ""
---

# 대규모 시스템 설계 기초 — 9장: 웹 크롤러 설계

**원본:** `raw/books/system-design-interview-ch9-01.png` ~ `ch9-12.png`
**페이지:** 141–163

## 핵심 요약

웹 크롤러는 시작 URL 집합에서 시작해 웹 페이지를 다운로드하고, 새 URL을 추출해 수집 범위를 넓혀간다. 주요 용도는 검색엔진 인덱싱, 웹 아카이빙, 웹 마이닝, 웹 모니터링이다. 이 장은 규모 추정부터 미수집 URL 저장소(Frontier) 설계, 크롤링 정책(Politeness, Priority), 중복 제거 전략까지 전체 설계를 다룬다.

## 규모 추정

- QPS: 매달 10억 페이지 수집 → 초당 약 400페이지
- 최대 QPS: 800
- 평균 페이지 크기 500KB → 월 500TB 저장소
- 5년 보관 시 30PB 필요

## 개략적 설계 — 주요 컴포넌트

```
시작 URL 집합
    ↓
미수집 URL 저장소(Frontier)
    ↓
HTML 다운로더 ← DNS 리졸버
    ↓
콘텐츠 파서 → 콘텐츠 저장소
    ↓
중복 콘텐츠 확인
    ↓
URL 추출기 → URL 필터 → URL 중복 확인 → URL 저장소
                                ↑
                          (다시 Frontier로)
```

## 상세 설계

### 미수집 URL 저장소(Frontier) — 핵심 컴포넌트
- **예의 바름(Politeness):** 같은 웹사이트에 너무 잦은 요청 금지 → 큐와 매핑 테이블로 호스트별 다운로더 분리
- **우선순위 지정:** 유용도(PageRank, 트래픽, 갱신 빈도 기반) → 우선순위 큐
- **신선도(Freshness):** 이미 수집한 페이지도 주기적 재수집 — 갱신 이력, 사이트맵 활용

### DFS vs BFS
- DFS: 깊이 우선 → 크롤러에 부적합 (한 도메인에 과도한 집중)
- BFS: 너비 우선 ✓ → 대부분의 크롤러가 BFS 기반

### HTML 다운로더
- **robots.txt:** 크롤러가 수집 가능한 페이지 규칙 명시 — 반드시 준수
- **성능 최적화:** 분산 크롤링, DNS 캐시, 지역성(크롤링 서버 ↔ 대상 서버), 짧은 타임아웃

### 중복 콘텐츠 처리
- 웹 페이지의 약 30%가 중복 콘텐츠
- 해시 비교(SimHash 등)로 유사 페이지 탐지

### URL 중복 제거
- **블룸 필터(Bloom Filter):** 수십억 URL을 메모리 효율적으로 중복 검사 (False Positive 허용, False Negative 없음)

### 도메인별 다운로드 속도 제한(Politeness Queue)
큐마다 특정 도메인에 매핑 → 같은 도메인 요청 사이에 딜레이 삽입.

### 수집 대상 확대 전략
- 서버 사이드 렌더링: JavaScript 실행 후 동적 콘텐츠 수집 (Headless browser 활용)
- 콘텐츠 타입별 필터링
- 수집 기간 동안 데이터 일관성 유지

### 확장 가능한 설계 포인트
1. 분산 크롤링 서버
2. Frontier 큐 서버 분리
3. HTML 다운로더 수평 확장
4. 콘텐츠 저장소 샤딩
5. DNS 리졸버 캐시

## 마무리 고려사항

- **서버 사이드 렌더링:** 동적 페이지 크롤링 필수
- **원치 않는 페이지 필터링:** 스팸, 광고 탐지
- **DB 다중화·샤딩**
- **수평 확장**
- **가용성·일관성·확장성**

## 관련 페이지

- [[concepts/web-crawler]]
- [[concepts/bloom-filter]]
- [[topics/system-design-interview-09]]
