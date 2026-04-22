# Codex Local Operating Guide

## Essential (Post-Compact)

> 컨텍스트 압축 후에도 유지할 핵심 규칙:
> 1. 기본 흐름은 `raw -> wiki -> output/blog -> ai-survival-log-site/content/posts` 이다.
> 2. `raw/`는 불변 원본 계층이고, 요약과 해설은 `wiki/`에서 한다.
> 3. `wiki/`가 source of truth다. `output/`은 재생성 가능한 artifact 계층이다.
> 4. `published: true` 페이지는 안정적인 `slug`와 구체적인 `description`을 유지해야 한다.
> 5. publishable 페이지는 `docs/content-seo-guide.md`를 따른다.
> 6. 위키는 human-first, Obsidian-friendly 구조를 유지하고 future RAG는 파생 계층으로 다룬다.

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

## Engineering Guardrails

- Check existing code, docs, and reusable libraries before introducing net-new implementation.
- After changing code, review the changed scope for bugs, regressions, security issues, and contract drift before completion.
- Use tests for code changes that can regress behavior. Prefer test-first for automation scripts, parsers, transformers, and publish/lint/sync logic.
- Do not force TDD for wiki content, raw source intake, or metadata-only edits, but still run the relevant verification for the changed scope.
- Preserve security basics: no hardcoded secrets, validate external input, and avoid error messages that leak sensitive data.
- In TypeScript/JavaScript, keep exported or shared APIs typed, avoid `any` when possible, and do not leave `console.log` in production paths.

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

## Detailed References

Use these shared documents for detailed rules instead of expanding this file:

- [ARCHITECTURE.md](/Users/ms/workspace/claude/ai-survival-log/ARCHITECTURE.md) — repository boundaries, source-of-truth vs derived layers
- [docs/operating/operations.md](/Users/ms/workspace/claude/ai-survival-log/docs/operating/operations.md) — operating workflow, verification, state export boundaries
- [docs/operating/channel-lanes.md](/Users/ms/workspace/claude/ai-survival-log/docs/operating/channel-lanes.md) — channel-lane expansion rules
- [docs/publishing-contract.md](/Users/ms/workspace/claude/ai-survival-log/docs/publishing-contract.md) — downstream publishing contract
- [docs/content-seo-guide.md](/Users/ms/workspace/claude/ai-survival-log/docs/content-seo-guide.md) — publishable content rules
- [docs/adr/0001-markdown-source-of-truth.md](/Users/ms/workspace/claude/ai-survival-log/docs/adr/0001-markdown-source-of-truth.md)
- [docs/adr/0002-json-derived-state-only.md](/Users/ms/workspace/claude/ai-survival-log/docs/adr/0002-json-derived-state-only.md)
- [docs/adr/0003-harness-layering-for-upstream-repo.md](/Users/ms/workspace/claude/ai-survival-log/docs/adr/0003-harness-layering-for-upstream-repo.md)
- [docs/adr/0004-new-channels-remain-derived-from-the-wiki.md](/Users/ms/workspace/claude/ai-survival-log/docs/adr/0004-new-channels-remain-derived-from-the-wiki.md)
