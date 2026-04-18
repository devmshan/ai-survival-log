---
title: "Codex 폴더 구조 실행 적용 세션"
created: "2026-04-18"
updated: "2026-04-18"
type: source
sources: []
tags: [repo-structure, codex, refactor, migration, wiki, synthesis]
status: active
published: false
slug: ""
description: ""
---

# Codex 폴더 구조 실행 적용 세션

**원본:** `raw/journals/2026-04-18-codex-folder-structure-execution-and-publish-conversation-backup.md`
**날짜:** 2026-04-18
**성격:** 계획된 폴더 구조 변경을 실제 저장소에 적용하고, 스크립트/테스트/문서/대칭 구조까지 완성한 실행 세션

## 핵심 요약

`wiki/projects/repo-structure-refactor.md` 계획을 실제 저장소에 적용한 세션. `sources/` → `raw/articles/`, `book/` → `raw/books/`, `docs/images/` → `assets/blog/`, `docs/webtoon/` → `assets/webtoon/` 파일 이동을 수행했다. `git mv`가 샌드박스에서 막혀 일반 `mv`로 우회하는 실무적 처리도 포함됐다. 마지막으로 `raw/`, `assets/`, `output/` 각각에 `CLAUDE.md`와 `AGENTS.md`를 대칭적으로 추가해 Claude/Codex 운영 경계를 완성했다.

## 주요 반영 항목

- 파일 이동: `sources/` → `raw/articles/`, `book/` → `raw/books/`, `docs/images/` → `assets/blog/`, `docs/webtoon/` → `assets/webtoon/`
- 신규 디렉토리: `wiki/syntheses/`, `assets/shared/`, `assets/youtube/`, `assets/instagram/`, `output/blog/`, `output/youtube/`, `output/instagram/`, `output/threads/`, `output/webtoon/`, `raw/videos/`, `raw/podcasts/`
- 스크립트 반영: `scripts/wiki_lib.py`에 `synthesis` 타입, `output/blog` 경로, `assets/blog` 이미지 검증 추가
- 테스트: `pytest tests/test_wiki_lib.py` → 27 passed
- 대칭 구조: `raw/AGENTS.md`, `assets/AGENTS.md`, `output/AGENTS.md` 추가

## 핵심 결정

- `raw/wiki/assets/output` 4계층을 실제 저장소 구조로 채택
- `output/blog`는 재생성 가능한 publish artifact 계층 (source of truth 아님)
- `CLAUDE.md`와 `AGENTS.md`를 각 최상위 디렉토리에 대칭적으로 배치

## 관련 페이지

- [[projects/repo-structure-refactor]]
- [[concepts/assets-intake-pattern]]
- [[sources/2026-04-18-claude-plan-codex-validation]]
- [[sources/2026-04-18-clipper-template-intake]]
