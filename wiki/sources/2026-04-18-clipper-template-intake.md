---
title: "Web Clipper 템플릿 설계와 intake 구조 재정의 세션"
created: "2026-04-18"
updated: "2026-04-18"
type: source
sources: []
tags: [obsidian-web-clipper, clipper-templates, assets-intake, wiki-ingest, raw-layer]
status: active
published: false
slug: ""
description: ""
---

# Web Clipper 템플릿 설계와 intake 구조 재정의 세션

**원본:** `raw/journals/2026-04-18-clipper-template-intake-and-recommendation-conversation-backup.md`
**날짜:** 2026-04-18
**성격:** Obsidian Web Clipper 템플릿을 `raw/wiki/assets/output` 흐름에 맞게 설계하고, 채널 미정 자산의 intake 구조를 재정의하고, URL 기반 템플릿 추천 스킬을 추가한 세션

## 핵심 요약

기존 단일 기본 클리퍼 템플릿을 분석해, `raw/{type}` 별로 최적화된 10종 템플릿 세트를 설계했다. 각 템플릿에는 `Why This Matters`, `Summary Seed`, `Extraction Priorities`, `Recommended Harness` 같은 힌트 섹션을 포함해 `/wiki:ingest`가 후속 분석 방향을 빠르게 잡을 수 있도록 했다. 채널 미정 비텍스트 자산을 위한 `assets/intake/` 구조도 이 세션에서 도입됐다.

## 설계된 템플릿 10종

| 템플릿 | 용도 | 저장 위치 |
|--------|------|---------|
| `article-deep-research` | 깊게 읽을 기술/리서치 글 | `raw/articles/` |
| `article-quick-capture` | 가볍게 저장하는 웹 글 | `raw/articles/` |
| `video-transcript-notes` | 유튜브/강의/인터뷰 | `raw/videos/` |
| `podcast-episode-notes` | 팟캐스트 에피소드 | `raw/podcasts/` |
| `book-chapter-notes` | 책 챕터 학습 | `raw/books/` |
| `book-quote-capture` | 책 인용/발췌 | `raw/books/` |
| `journal-insight-capture` | 개인 인사이트 메모 | `raw/journals/` |
| `conversation-backup` | 긴 대화 백업 | `raw/journals/` |
| `asset-reference-note` | 이미지/첨부파일 맥락 메모 | `assets/intake/reference-notes/` |
| `generic-source-capture` | 분류가 애매한 자료 | (수동 분류) |

## 핵심 결정

- 텍스트 기반 소스 → `raw/{type}/`으로 직접 저장
- 채널 미정 비텍스트 자산 → `assets/intake/*`에 먼저 모음
- 채널 결정 후에만 `assets/blog/`, `assets/youtube/` 등으로 승격
- URL 기반 추천 스킬은 Claude command와 Codex skill 양쪽에 모두 배치

## 추가된 자산

- `assets/clipper-templates/` — 템플릿 10종 + README
- `assets/intake/reference-notes/`, `assets/intake/reference-images/`, `assets/intake/attachments/`
- `.claude/commands/content/recommend-clipper-template.md`
- `.codex/skills/recommend-clipper-template/SKILL.md`

## 관련 페이지

- [[entities/obsidian-web-clipper]]
- [[concepts/assets-intake-pattern]]
- [[sources/2026-04-18-codex-folder-structure-execution]]
- [[sources/2026-04-18-web-clipper-setup]]
