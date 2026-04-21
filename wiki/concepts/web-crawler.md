---
title: "웹 크롤러 (Web Crawler)"
created: "2026-04-21"
updated: "2026-04-21"
type: concept
sources: ["[[sources/2026-04-21-system-design-interview-ch9]]"]
tags: [system-design, web-crawler, bfs, distributed-systems, search-engine, backend]
status: active
published: false
slug: ""
description: ""
---

# 웹 크롤러 (Web Crawler)

시작 URL 집합에서 출발해 웹 페이지를 자동으로 수집하고, 발견한 새 URL을 따라가며 수집 범위를 넓혀가는 시스템. 스파이더(spider)라고도 불린다.

## 주요 용도

- **검색엔진 인덱싱:** 구글, 네이버 등의 웹 인덱스 구축
- **웹 아카이빙:** 인터넷 역사 보존
- **웹 마이닝:** 데이터 분석, 패턴 추출
- **웹 모니터링:** 저작권 침해, 사이트 변경 감지

## 핵심 컴포넌트

| 컴포넌트 | 역할 |
|---------|------|
| 시작 URL 집합 | 크롤링 출발점 |
| 미수집 URL 저장소(Frontier) | 방문 예정 URL 큐 |
| HTML 다운로더 | 웹 페이지 다운로드 |
| DNS 리졸버 | URL → IP 변환 |
| 콘텐츠 파서 | HTML 파싱 및 검증 |
| 중복 콘텐츠 확인 | 동일 콘텐츠 중복 수집 방지 |
| URL 추출기 | 페이지에서 새 URL 추출 |
| 블룸 필터 | URL 중복 여부 확인 |
| 콘텐츠 저장소 | 수집한 HTML 저장 |

## 알고리즘

### BFS (너비 우선 탐색) ✓
대부분의 크롤러가 채택. 한 도메인에 집중되는 DFS보다 균형 있는 수집 가능.

## 미수집 URL 저장소(Frontier) 설계

### Politeness (예의 바름)
같은 도메인에 과도한 요청 금지. 큐 + 호스트-다운로더 매핑으로 도메인별 속도 제한.

### 우선순위
PageRank, 트래픽, 갱신 빈도 기반 우선순위 큐.

### 신선도(Freshness)
이미 수집한 페이지도 주기적 재수집. 갱신 이력·사이트맵 활용.

## 확장 포인트

- **robots.txt 준수:** 크롤링 허용 경로 규칙 반드시 준수
- **분산 크롤링:** 여러 서버가 Frontier를 공유
- **블룸 필터:** 수십억 URL 중복 검사를 메모리 효율적으로
- **서버 사이드 렌더링:** JavaScript 동적 페이지 수집을 위해 Headless browser 활용
- **DNS 캐싱:** DNS 조회 오버헤드 감소

## 관련 페이지

- [[concepts/bloom-filter]]
- [[sources/2026-04-21-system-design-interview-ch9]]
- [[topics/system-design-interview-09]]
