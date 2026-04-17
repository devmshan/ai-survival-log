---
title: "Site SEO Foundation and Content Rewrite"
created: "2026-04-18"
updated: "2026-04-18"
type: project
sources: []
tags: [seo, blog, project, nextjs, publishing, search-console, content]
status: active
published: false
slug: ""
description: ""
---

# Site SEO Foundation and Content Rewrite

`ai-survival-log-site`의 검색 노출 기반을 정비하고, 이미 발행된 포스트 전체를 검색 친화적으로 다시 다듬은 작업 묶음.

이번 작업은 단순히 meta tag 몇 개를 추가하는 수준이 아니라, 아래 세 층을 한 번에 정리한 프로젝트였다.

- 기술 SEO 기반
- 콘텐츠 SEO 작성 규칙
- 검색엔진 제출 및 초기 색인 운영

## 왜 시작했는가

출발점은 단순했다.

- 블로그 글이 외부 검색엔진에서 잘 노출되지 않는 것 같았다
- `ai-survival-log-site`에는 기본 `title`/`description` 정도만 있고, `robots`, `sitemap`, canonical, OG/Twitter, JSON-LD가 부족했다
- 기존 글들도 검색형 제목, 요약, 도입부, 내부 링크 관점에서 다시 다듬을 필요가 있었다

즉 문제는 “글이 나빠서”보다 먼저, **검색엔진이 사이트를 충분히 이해할 신호가 부족했다**는 쪽에 가까웠다.

## 무엇을 했는가

### 1. 기술 SEO 기반 정비

`ai-survival-log-site`에서 아래를 구현했다.

- 전역 `metadataBase`
- 홈/소개/태그/시리즈/포스트 canonical
- `robots.txt`
- `sitemap.xml`
- 포스트 상세 Open Graph / Twitter metadata
- 포스트 상세 `BlogPosting` JSON-LD
- 절대 URL 처리를 위한 공통 site URL 유틸

이 단계의 목적은 검색엔진이 사이트 구조와 대표 URL을 안정적으로 이해하게 만드는 것이었다.

### 2. 콘텐츠 계약 확장

`content/posts` frontmatter에 optional SEO 필드를 수용하도록 downstream contract를 확장했다.

- `seoTitle`
- `seoDescription`
- `thumbnail` 재사용 원칙 명시

중요한 점은 upstream `ai-survival-log` publish 산출물이 이 필드를 아직 생산하지 않더라도,
site runtime이 기본 `title`/`description`으로 안전하게 fallback 해야 한다는 점이었다.

### 3. 내부 링크 구조 강화

검색 유입이 단일 글에서 끝나지 않도록 아래를 추가했다.

- 태그를 실제 링크로 연결
- 포스트 하단 관련 글 블록
- 시리즈/토픽 흐름을 따라가는 탐색 강화

즉 태그만 달아두는 방식이 아니라, 독자가 다음 글로 이동할 수 있는 구조를 만들었다.

### 4. 운영 문서화

site repo에 아래 문서를 정리했다.

- SEO foundation plan
- SEO operations guide
- content SEO writing guide

그리고 이 작성 규칙이 downstream에만 남지 않도록, upstream `ai-survival-log`에도 같은 authoring guide를 미러링했다.

핵심 판단:

- 검색 대응 규칙은 downstream 보정으로만 남기면 늦다
- 실제 글 작성과 시리즈 기획이 upstream에서 먼저 일어나므로, 같은 규칙이 upstream authoring 단계에도 있어야 한다

### 5. 기존 포스트 전체 리라이트

이미 발행된 `content/posts` 전부를 1차 리라이트했다.

공통 변경:

- `seoTitle` 추가
- `seoDescription` 추가
- 도입부에서 “이 글이 무엇을 설명하는가”를 더 빨리 드러내도록 수정
- 관련 글 링크 추가

이 단계에서 검색형 글과 브랜딩/회고형 글을 같은 방식으로 다루지 않고, 톤을 살리되 검색 대응력을 높이는 방향으로 조정했다.

### 6. 실제 제출과 초기 색인 확인

배포 환경에 `NEXT_PUBLIC_SITE_URL=https://devsurvivallog.com`을 설정하고 재배포했다.

이후 실제 운영 환경에서 아래를 확인했다.

- `https://devsurvivallog.com/robots.txt` 정상
- `https://devsurvivallog.com/sitemap.xml` 정상
- 대표 포스트의 `og:title`, `og:image`, canonical, JSON-LD 확인
- Google Search Console 도메인 속성 인증
- `sitemap.xml` 제출 성공
- 대표 글 URL 검사 및 색인 생성 요청

즉 이 프로젝트는 코드 수정으로 끝나지 않고, 실제 검색엔진 제출까지 한 사이클을 닫았다.

## 교훈

### 기술 SEO와 콘텐츠 SEO는 따로 보면 안 된다

검색 노출 문제는 종종 “제목만 고치면 된다” 또는 “sitemap만 넣으면 된다”로 오해된다.

하지만 실제로는:

- 검색엔진이 페이지를 이해할 기술 신호
- 독자가 클릭할 만한 제목/요약
- 다음 글로 이어지는 내부 링크

이 세 가지가 같이 맞물려야 했다.

### 작성 규칙은 upstream에서 먼저 잡아야 한다

`ai-survival-log-site`에서만 SEO writing rule을 두면 이미 늦다.

실제 글 초안, 시리즈 구조, publish 전 설명문은 upstream `ai-survival-log`에서 먼저 결정된다.
따라서 content SEO guide는 upstream에도 미러링되어야 했다.

### 검색엔진 제출은 문서가 아니라 운영이다

`robots.txt`와 `sitemap.xml`이 있다고 끝나지 않았다.

실제 Google Search Console에서:

- 도메인 인증
- sitemap 제출
- URL 검사
- 색인 생성 요청

까지 가야 “검색 노출 작업을 했다”고 말할 수 있었다.

## 결과

이번 작업 결과, `ai-survival-log-site`는 다음 상태가 되었다.

- 기술 SEO 기본기 확보
- 콘텐츠 SEO 작성 규칙 문서화
- 기존 포스트 전체 1차 리라이트 완료
- Search Console 제출 및 초기 색인 요청 완료
- upstream/downstream 작성 규칙 정합성 확보

GitHub 기준으로는 `feat/seo-foundation` 브랜치에서 작업했고,
site repo에는 SEO foundation PR과 content rewrite PR이 순차적으로 merge 되었다.

## 다음 단계

- Search Console에서 색인/노출/CTR 변화 관찰
- 어떤 글이 impressions는 있는데 CTR이 낮은지 확인
- 필요하면 `seoTitle`/`seoDescription` 2차 조정
- upstream publish 흐름에서도 새 글이 처음부터 content SEO guide를 따르도록 습관화

## 관련 페이지

- [[concepts/canonical-url]]
- [[projects/blog-ai-study-site]]
- [[projects/cross-repo-ai-automation-lab]]
- [[entities/devsurvivallog]]
- [[topics/how-llm-works]]
- [[topics/claude-code-to-codex]]
- [[topics/developer-automation-lab-01-pr-summary]]
