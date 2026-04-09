# 개인 블로그 & AI 학습 사이트 설계

**작성일:** 2026-04-09
**상태:** 승인됨
**레퍼런스:** https://techblog.woowahan.com/

---

## 개요

개인 블로그와 AI 학습 정리를 함께 운영하는 사이트.
Claude와 나눈 대화 MD 파일, Mermaid 다이어그램, 이미지 파일을 그대로 업로드하여 포스트로 사용한다.

---

## 기술 스택

| 역할 | 기술 |
|---|---|
| 프레임워크 | Next.js 15 (App Router) |
| MDX 처리 | next-mdx-remote v5 |
| UI | Tailwind CSS v4 + shadcn/ui |
| 다이어그램 | Mermaid.js |
| 댓글 | Giscus (GitHub Discussions) |
| 뉴스레터 | Resend API |
| 검색 | Fuse.js |
| 배포 | Vercel |

---

## 아키텍처

```
[content/posts/*.mdx]
    ↓ next-mdx-remote 파싱
[Next.js 15 App Router — 빌드 타임 정적 생성(SSG)]
    ↓
[Vercel 배포]
    ↓
[사용자 브라우저]
    ├── Giscus (GitHub Discussions → 댓글)
    └── Resend API Route (뉴스레터 구독)
```

**핵심 원칙:**
- 글은 파일 기반 — `content/posts/`에 MDX 추가하면 자동으로 포스트 생성
- 빌드 타임 정적 생성 → 빠른 로딩, SEO 유리
- 동적 기능(댓글, 뉴스레터)만 클라이언트/API Routes 사용

---

## 프로젝트 디렉토리 구조

```
ai-survival-log/
├── content/
│   └── posts/                        # 모든 글 한 곳에 관리
│       ├── 2026-04-09-claude-tips.mdx
│       ├── 2026-04-01-dev-diary.mdx
│       └── 2026-03-20-gpt-arch.mdx
│
├── src/
│   ├── app/
│   │   ├── page.tsx                  # 메인 (최신 글 목록)
│   │   ├── posts/
│   │   │   └── [slug]/page.tsx       # 개별 포스트
│   │   ├── tags/
│   │   │   └── [tag]/page.tsx        # 태그별 모아보기
│   │   ├── about/page.tsx            # 소개 페이지
│   │   └── api/
│   │       └── newsletter/route.ts   # 뉴스레터 구독 API
│   │
│   ├── components/
│   │   ├── ui/                       # shadcn 컴포넌트
│   │   ├── PostCard.tsx              # 글 카드
│   │   ├── TagFilter.tsx             # 태그 필터
│   │   ├── SearchBar.tsx             # ⌘K 검색 팝업
│   │   ├── MermaidRenderer.tsx       # Mermaid 다이어그램
│   │   ├── TableOfContents.tsx       # 목차 자동 생성
│   │   └── NewsletterForm.tsx        # 뉴스레터 구독 폼
│   │
│   └── lib/
│       ├── mdx.ts                    # MDX 파싱 유틸
│       └── search.ts                 # Fuse.js 검색 설정
│
└── public/
    └── images/                       # 포스트 이미지
```

---

## 페이지 구성

| 경로 | 설명 |
|---|---|
| `/` | 메인 — 최신 글 목록, 태그 필터 |
| `/posts/[slug]` | 개별 포스트 상세 |
| `/tags/[tag]` | 태그별 글 모아보기 |
| `/about` | 소개 페이지 |

---

## 주요 기능

### 글 목록 (메인)
- 카드형 레이아웃 (우아한기술블로그 스타일)
- 태그 배지 클릭 → 필터링
- 최신순 정렬

### 포스트 상세
- MDX 렌더링
- Mermaid 다이어그램 렌더링
- 이미지 최적화 (next/image)
- 목차(TOC) 자동 생성
- 이전/다음 글 네비게이션
- Giscus 댓글

### 검색 (⌘K)
- shadcn `Command` 팝업
- Fuse.js로 제목/태그/본문 전체 검색

### 뉴스레터
- 하단 구독 폼
- Resend API로 이메일 발송

### 다크모드
- next-themes + shadcn 기본 지원

---

## Frontmatter 스펙

모든 포스트가 따르는 형식:

```mdx
---
title: "제목"
date: "2026-04-09"
tags: ["tag1", "tag2", "tag3"]   # 복수 태그 가능
description: "카드에 표시될 요약"
thumbnail: "/images/thumbnail.png"  # 선택
draft: false                         # true면 빌드에서 제외
---
```

**태그 운영 방식:**
- 단일 `content/posts/` 폴더에 모든 글 저장
- 태그로 카테고리 분류 (코드 수정 없이 파일에서만 관리)
- `/tags/[tag]` 페이지 자동 생성
