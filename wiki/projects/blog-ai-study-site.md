---
title: "블로그 & AI 학습 사이트"
created: "2026-04-09"
updated: "2026-04-12"
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

## 개요

- **상태:** 설계 완료 / 구현 대기
- **레퍼런스:** 우아한기술블로그 스타일
- **콘텐츠 소스:** 이 위키의 `published: true` 페이지 → `/wiki:publish` → `ai-survival-log-site/content/posts/`

## 기술 스택

| 역할 | 기술 |
|------|------|
| 프레임워크 | Next.js 15 (App Router) |
| MDX 처리 | next-mdx-remote v5 |
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
Next.js 15 App Router (SSG)
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
date: "2026-04-09"
tags: ["tag1", "tag2"]
description: "카드에 표시될 요약"
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

## 구현 상태

- [x] 설계 완료 (`wiki/projects/blog-ai-study-site.md`)
- [x] 위키 → 블로그 파이프라인 설계 (`/wiki:publish`)
- [ ] Next.js 프로젝트 초기 설정
- [ ] 핵심 컴포넌트 구현
- [ ] 배포 (Vercel)

## 관련 페이지

- [[topics/ai-era-survival]] — 블로그의 핵심 주제
- [[entities/claude-code]] — 개발에 사용하는 도구
- [[concepts/llm-wiki-pattern]] — 위키 → 블로그 파이프라인의 기반
- [[projects/cross-repo-ai-automation-lab]] — upstream/downstream 협업 자동화 실습
