---
title: "URL 단축기 (URL Shortener)"
created: "2026-04-21"
updated: "2026-04-21"
type: concept
sources: ["[[sources/2026-04-21-system-design-interview-ch8]]"]
tags: [system-design, url-shortener, hash, base62, redirect, backend]
status: active
published: false
slug: ""
description: ""
---

# URL 단축기 (URL Shortener)

긴 URL을 짧은 URL로 변환하고 짧은 URL로 접근 시 원래 URL로 리다이렉션하는 서비스. bit.ly, tinyurl.com이 대표적.

## 핵심 기능

1. 긴 URL → 짧은 URL 변환
2. 짧은 URL → 원래 URL로 리다이렉션

## API 설계

- `POST /api/v1/data/shorten` — `{ longUrl }` → `{ shortUrl }`
- `GET /api/v1/{shortUrl}` → 301/302 리다이렉션

## 리다이렉션: 301 vs 302

| | 301 Moved Permanently | 302 Found |
|---|---|---|
| 캐싱 | 브라우저가 캐시 → 이후 서버 미경유 | 매 요청 서버 경유 |
| 서버 부하 | 낮음 | 높음 |
| 통계 수집 | 불가 | 가능 |

트래픽 분석이 중요하면 302, 부하 감소가 우선이면 301.

## 단축 방식

### 해시 함수 방식
hashValue 길이 7자리 선택(36^7 ≈ 3.5조, 10년치 수용).
CRC32/MD5 해시 후 앞 7자리 취함 → 충돌 가능.
충돌 시: 미리 정한 문자열 덧붙여 재해시. 블룸 필터로 DB 조회 전 확인.

### Base 62 인코딩 방식 ✓
유일 ID 생성기([[concepts/unique-id-generator]])로 ID 생성 → Base 62 인코딩.
`[0-9, a-z, A-Z]` 62가지 문자 → 7자리면 62^7 ≈ 3.5조개.
ID가 유일하므로 충돌 없음. 단, ID 노출 시 다음 URL 예측 가능.

## 데이터 모델

```
shortURL (PK) | longURL | createdAt
```

## 캐시 전략

자주 접근하는 shortURL을 캐시에 저장. 캐시 히트율 80/20 법칙 적용 (상위 20%가 80% 트래픽).

## 관련 페이지

- [[concepts/unique-id-generator]]
- [[concepts/cache-strategies]]
- [[sources/2026-04-21-system-design-interview-ch8]]
- [[topics/system-design-interview-08]]
