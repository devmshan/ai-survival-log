---
title: "CDN (콘텐츠 전송 네트워크)"
created: "2026-04-14"
updated: "2026-04-14"
type: concept
sources: ["[[sources/2026-04-14-system-design-interview-v1]]"]
tags: ["system-design", "cdn", "performance", "static-content", "distributed-systems"]
status: active
published: false
slug: ""
description: ""
---

# CDN (콘텐츠 전송 네트워크)

CDN(Content Delivery Network)은 정적 콘텐츠를 전송하기 위해 지리적으로 분산된 서버 네트워크.

## 역할

- 이미지, 비디오, CSS, JavaScript 파일 등 **정적 콘텐츠** 전송
- 사용자와 지리적으로 가까운 CDN 서버에서 콘텐츠 전달 → 응답 속도 향상
- 오리진 서버(origin server)의 부하 감소

## 동작 원리

```
사용자 → CDN 서버(사용자 근처) → 콘텐츠 있으면 즉시 반환
                               → 없으면 → 오리진 서버에서 가져와 캐시 후 반환
```

1. 사용자가 CDN URL로 이미지 요청
2. CDN 서버에 캐시된 이미지가 없으면 오리진 서버에서 파일 가져옴
3. 가져온 파일을 TTL(Time-To-Live) 기간 동안 CDN에 캐시
4. 같은 이미지 요청 시 CDN에서 바로 반환

## CDN 사용 시 고려사항

### 1. 비용
- CDN은 제3 사업자(Akamai, CloudFront, Fastly 등)가 운영
- 데이터 전송량에 따라 비용 발생
- 자주 사용되지 않는 콘텐츠를 CDN에 올리는 것은 비효율적

### 2. 만료 시한 (TTL)
- TTL이 너무 길면: 콘텐츠가 오래되어도 계속 서빙
- TTL이 너무 짧으면: 오리진 서버 요청 빈번 → CDN 효과 감소
- 콘텐츠 특성에 따라 적절히 설정

### 3. CDN 장애 대처
- CDN 자체가 다운될 경우를 대비해야 함
- 클라이언트가 CDN 장애를 감지하면 오리진 서버에서 직접 콘텐츠 요청하도록 처리

### 4. 콘텐츠 무효화 (Cache Invalidation)
캐시된 콘텐츠를 만료 전에 강제로 갱신하는 방법:

- **버전 쿼리 파라미터:** `image.png?v=2` — URL 변경으로 새 버전 강제 로딩
- **URL에 해시값 포함:** `image-abc123.png`
- **CDN 무효화 API:** CDN 사업자가 제공하는 API로 특정 파일 즉시 만료

## CDN vs 캐시 비교

| | CDN | 캐시 |
|--|-----|------|
| 대상 | 주로 정적 콘텐츠 | 정적 + 동적 데이터 |
| 위치 | 사용자 근처 지역 서버 | 웹 서버와 DB 사이 |
| 목적 | 지리적 응답 속도 향상 | DB 부하 감소 |

## 관련 페이지

- [[concepts/cache-strategies]] — 동적 데이터를 위한 캐시
- [[concepts/stateless-architecture]] — 정적 콘텐츠 분리 전략
- [[projects/study-system-design-interview]] — 시스템 설계 스터디
