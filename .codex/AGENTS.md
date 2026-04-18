# Codex Local Operating Guide

## Project Role

This repository is the upstream wiki authoring source for the AI Survival Log publishing workflow.

Primary flow:
`raw -> wiki -> output/blog -> ai-survival-log-site/content/posts`

Do not treat this repository as the final presentation layer or the primary site runtime.

Current structural refactor planning is tracked in `wiki/projects/repo-structure-refactor.md`.
Future RAG/vector DB expansion is deferred and tracked separately in `wiki/projects/wiki-rag-expansion-roadmap.md`.

## Local Skill Surface

These skills are available in `.codex/skills/`:

- `conversation-backup` — 현재 대화를 `raw/journals/`에 백업 파일로 저장
- `wiki-ingest` — `raw/{type}/` 소스를 위키로 흡수
- `wiki-query-answer` — 위키 검색과 인용 답변
- `wiki-file-answer` — 답변을 위키 페이지로 저장
- `wiki-lint` — 위키 무결성 검사
- `wiki-publish` — `output/blog/` artifact 생성
- `recommend-clipper-template` — URL 기반 Web Clipper 템플릿 추천

## Working Loop

Use this default loop for non-trivial changes:
1. Plan
2. Implement
3. Verify

## Publishing Compatibility

`wiki/` is the source of truth.

Direct edits should preserve:
- required wiki frontmatter
- stable `slug` and `description` for publishable pages
- compatibility with the downstream site contract
- book-study and downstream content expansion rules when applicable

When a publishable page embeds screenshots or other images, preserve:
- an upstream source copy in `assets/blog/`
- a downstream-served copy in `ai-survival-log-site/public/images/{slug-or-series}/`
- site-facing markdown image paths like `/images/{slug-or-series}/{file}.png`
- ASCII kebab-case filenames for publish-facing assets

## Wiki Principles

- keep the wiki human-first and markdown-first
- preserve Obsidian-friendly structure and direct readability
- do not preemptively reshape the wiki around future RAG needs
- treat future RAG/vector DB work as a derived layer, not the source-of-truth structure

## Selective Adoption

Adopt only the useful parts of ECC and superpowers:
- writing plans
- verification before completion
- systematic debugging
- documentation quality
- selective adoption

Do not introduce large agent catalogs, heavy MCP assumptions, or unnecessary multi-agent workflows.
