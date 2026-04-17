---
title: "Canonical URL"
created: "2026-04-18"
updated: "2026-04-18"
type: concept
sources: []
tags: [seo, publishing, blog, nextjs]
status: active
published: false
slug: ""
description: ""
---

# Canonical URL

`canonical`은 검색엔진에 "이 페이지의 대표 URL은 이것이다"라고 알려주는 표준 URL 신호다.

보통 HTML 문서 안에 아래처럼 들어간다.

```html
<link rel="canonical" href="https://example.com/posts/pr-summary" />
```

## 왜 필요한가

같은 내용이 여러 URL로 접근될 수 있기 때문이다.

예:

- `https://example.com/posts/pr-summary`
- `https://example.com/posts/pr-summary?utm_source=x`
- `https://www.example.com/posts/pr-summary`
- `https://example.com/posts/pr-summary/`

검색엔진 입장에서는 이 URL들이 서로 다른 페이지인지, 같은 페이지인지 헷갈릴 수 있다.

이때 canonical은 "이 중에서 대표로 봐야 할 주소는 이것"이라고 알려준다.

## 어떤 효과가 있는가

- 중복 URL로 인한 검색 신호 분산 완화
- 검색 결과에 노출할 대표 URL 정리
- 추적 파라미터가 붙은 URL이 원본처럼 취급되는 문제 완화

즉 canonical은 중복 가능성이 있는 여러 URL 사이에서 "정식 주소"를 지정하는 역할에 가깝다.

## 주의할 점

canonical은 강제 명령이 아니라 검색엔진에 주는 강한 힌트다.

대부분은 잘 반영되지만, 검색엔진이 실제 내용을 보고 다른 URL을 대표로 판단할 수도 있다.

## 블로그에서 특히 중요한 경우

- UTM 파라미터가 많이 붙는 공유 링크가 있을 때
- 태그, 정렬, 필터 URL이 생길 때
- `www` / non-`www` 혼용 가능성이 있을 때
- trailing slash 차이가 있을 때

## 이 프로젝트에서의 연결

`ai-survival-log-site`에서는 홈, 태그, 시리즈, 포스트 페이지마다 canonical을 명시해 검색엔진이 대표 URL을 안정적으로 이해하도록 정비했다.

이 작업은 [[projects/site-seo-foundation-and-content-rewrite]] 프로젝트의 기술 SEO 기반 정비에 포함된다.

## 관련 페이지

- [[projects/site-seo-foundation-and-content-rewrite]]
- [[projects/blog-ai-study-site]]
