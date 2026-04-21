---
title: "대규모 시스템 설계 기초 — 8장: URL 단축기 설계"
created: "2026-04-21"
updated: "2026-04-21"
type: source
sources: []
tags: [system-design, url-shortener, hash, base62, redirect, book]
status: active
published: false
slug: ""
description: ""
---

# 대규모 시스템 설계 기초 — 8장: URL 단축기 설계

**원본:** `raw/books/system-design-interview-ch8-01.png` ~ `ch8-07.png`
**페이지:** 127–139

## 핵심 요약

URL 단축기(bit.ly 류)는 긴 URL을 짧은 URL로 변환하고, 짧은 URL로 접근 시 원래 URL로 리다이렉션한다. 이 장은 API 설계, 리다이렉션 방식(301 vs 302), 해시 충돌 전략, Base 62 인코딩을 다루고 전체 시스템 흐름을 설계한다.

## API 설계

- **URL 단축:** `POST /api/v1/data/shorten` — 긴 URL 입력 → 짧은 URL 반환
- **URL 리다이렉션:** `GET /api/v1/shortUrl` — 짧은 URL → 원래 URL로 리다이렉션

## 리다이렉션 방식

| 방식 | 상태코드 | 특징 |
|------|---------|------|
| 301 Permanently Moved | 301 | 브라우저가 캐시 → 이후 요청은 서버 우회. 서버 부하 감소 |
| 302 Found | 302 | 매 요청이 서버 경유 → 클릭 통계 수집 가능 |

트래픽 분석이 중요하면 302, 서버 부하 감소가 우선이면 301.

## URL 단축 방식

### 해시 함수 방식
hashValue 길이 7자리(36^7 ≈ 3.5조개, 10년치 URL 수용).

**문제: 충돌**
- CRC32/MD5/SHA-1은 해시 값이 7자리보다 길어 자름 → 충돌 가능
- 해결: 충돌 감지 후 미리 정한 문자열을 덧붙여 재해시 → 성능 저하 우려
- 개선: 블룸 필터로 충돌 빠르게 확인

### Base 62 인코딩 방식 ✓
- ID 생성기(7장 Snowflake)로 유일 ID 생성 → Base 62 인코딩
- `[0-9, a-z, A-Z]` 62가지 문자 사용
- ID는 유일하므로 충돌 없음
- 단점: ID 노출 시 다음 shortURL 예측 가능

## 상세 설계

### 데이터 모델
```
shortURL(PK) | longURL | createdAt
```

### URL 단축 순서도
1. shortURL이 DB에 있으면 → 바로 반환
2. 없으면 → ID 생성 → Base 62 인코딩 → DB 저장 → 반환

### 캐시
- 자주 쓰는 URL은 캐시에 저장
- 캐시 미스 시 DB 조회 후 캐시 갱신

### URL 리다이렉션 순서도
1. shortURL 수신
2. 캐시 조회 → 있으면 longURL 반환
3. 캐시 미스 → DB 조회 → 반환 및 캐시 저장

## 마무리 고려사항

- **처리율 제한 장치:** 악의적 사용자의 단축 URL 남용 방지
- **웹 서버 수평 확장:** stateless 구조
- **DB 다중화·샤딩**
- **분석 기능:** 클릭 횟수, 리다이렉션 위치 등 통계
- **가용성·일관성·확장성**

## 관련 페이지

- [[concepts/url-shortener]]
- [[concepts/consistent-hashing]]
- [[concepts/cache-strategies]]
- [[topics/system-design-interview-08]]
