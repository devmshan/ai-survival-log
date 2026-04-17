---
title: "블로그 & AI 학습 사이트"
created: "2026-04-09"
updated: "2026-04-18"
type: project
sources: []
tags: [blog, nextjs, project]
status: active
published: false
slug: ""
description: ""
---

# 블로그 & AI 학습 사이트

개인 블로그와 AI 학습 정리를 함께 운영하는 사이트. [[topics/ai-era-survival|AI 시대 생존 전략]]의 일환으로 지식을 공유한다.

2026-04-18 기준으로 기술 SEO 기반, 콘텐츠 SEO 작성 규칙, Search Console 제출, 전체 포스트 리라이트 1차가 반영된 상태다.

## 개요

- **상태:** 구현 및 운영 진행 중
- **레퍼런스:** 우아한기술블로그 스타일
- **콘텐츠 소스:** 이 위키의 `published: true` 페이지 → `/wiki:publish` → `ai-survival-log-site/content/posts/`

## 기술 스택

| 역할 | 기술 |
|------|------|
| 프레임워크 | Next.js 16 (App Router) |
| MDX 처리 | next-mdx-remote v6 |
| UI | Tailwind CSS v4 + shadcn/ui |
| 다이어그램 | Mermaid.js |
| 댓글 | Giscus (GitHub Discussions) |
| 뉴스레터 | Resend API |
| 검색 | Fuse.js |
| 배포 | Vercel |

## 아키텍처

```
wiki/ (published: true 페이지)
    ↓ /wiki:publish
ai-survival-log-site/content/posts/*.mdx
    ↓ next-mdx-remote 파싱
Next.js 16 App Router (SSG)
    ↓ Vercel 배포
사용자 브라우저
    ├── Giscus (댓글)
    └── Resend API (뉴스레터)
```

**핵심 원칙:**
- 위키가 source of truth — `ai-survival-log-site/content/posts/`는 생성된 출력물
- 파일 기반 콘텐츠 — MDX 추가하면 자동 포스트 생성
- 빌드 타임 정적 생성(SSG) → 빠른 로딩, SEO 유리

## 디렉토리 구조

```
ai-survival-log/              # upstream authoring repo
├── wiki/                     # 위키 (source of truth)
└── /wiki:publish
    ↓
ai-survival-log-site/         # downstream presentation repo
├── content/
│   └── posts/                # publish 출력물 (*.mdx)
├── src/
│   ├── app/
│   │   ├── page.tsx              # 메인 (글 목록 + 태그 필터)
│   │   ├── posts/[slug]/page.tsx # 개별 포스트
│   │   ├── tags/[tag]/page.tsx   # 태그별 목록
│   │   ├── about/page.tsx
│   │   └── api/newsletter/route.ts
│   ├── components/
│   │   ├── PostCard.tsx, PostList.tsx, TagFilter.tsx
│   │   ├── TableOfContents.tsx, MermaidRenderer.tsx
│   │   ├── GiscusComments.tsx, NewsletterForm.tsx
│   │   └── SearchBar.tsx (⌘K)
│   └── lib/
│       ├── mdx.ts
│       └── search.ts
└── public/images/
```

## 블로그 Frontmatter 스펙

```mdx
---
title: "제목"
seoTitle: "검색 노출용 제목 (optional)"
date: "2026-04-09"
tags: ["tag1", "tag2"]
description: "카드에 표시될 요약"
seoDescription: "검색 노출용 요약 (optional)"
thumbnail: "/images/thumbnail.png"
draft: false
---
```

## 주요 기능

| 기능 | 구현 방법 |
|------|----------|
| 글 목록 | 카드형 레이아웃, 태그 필터, 최신순 |
| 검색 (⌘K) | Fuse.js, shadcn Command 팝업 |
| 다크모드 | next-themes + shadcn |
| 댓글 | Giscus (GitHub Discussions) |
| 뉴스레터 | Resend API Route |
| Mermaid | 클라이언트 사이드 렌더링 |
| TOC | 헤딩 자동 추출 |
| 기술 SEO | metadataBase, canonical, robots, sitemap, OG/Twitter, JSON-LD |
| 내부 링크 | 태그 링크, 관련 글, 시리즈 탐색 |

## 구현 상태

- [x] 설계 완료 (`wiki/projects/blog-ai-study-site.md`)
- [x] 위키 → 블로그 파이프라인 설계 (`/wiki:publish`)
- [x] Next.js 프로젝트 초기 설정
- [x] 핵심 컴포넌트 구현
- [x] 배포 (Vercel)
- [x] 기술 SEO 1차 구현
- [x] Search Console 제출 및 초기 색인 요청
- [x] 기존 포스트 전체 1차 리라이트
- [ ] Search Console 반응 기반 2차 카피 조정

## 관련 페이지

- [[topics/ai-era-survival]] — 블로그의 핵심 주제
- [[entities/claude-code]] — 개발에 사용하는 도구
- [[concepts/llm-wiki-pattern]] — 위키 → 블로그 파이프라인의 기반
- [[projects/cross-repo-ai-automation-lab]] — upstream/downstream 협업 자동화 실습
- [[projects/site-seo-foundation-and-content-rewrite]] — SEO 기반 정비와 전체 포스트 리라이트 작업
