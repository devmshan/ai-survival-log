# AI Survival Log Agent Guide

## Essential (Post-Compact)

> 컨텍스트 압축 후에도 유지할 핵심 규칙:
> 1. 기본 흐름은 `raw -> wiki -> output/blog -> ai-survival-log-site/content/posts` 이다.
> 2. `raw/`는 불변 원본 계층이고, 요약과 해설은 `wiki/`에서 한다.
> 3. `wiki/`가 source of truth다. `output/`은 재생성 가능한 artifact 계층이다.
> 4. `published: true` 페이지는 안정적인 `slug`와 구체적인 `description`을 유지해야 한다.
> 5. publishable 페이지는 `docs/content-seo-guide.md`를 따른다.
> 6. 위키는 human-first, Obsidian-friendly 구조를 유지하고 future RAG는 파생 계층으로 다룬다.

## Project Role

This repository is the upstream wiki authoring source for the AI Survival Log system.

Primary flow:
`raw -> wiki -> output/blog -> ai-survival-log-site/content/posts`

Do not treat this repository as the final presentation layer. Its responsibility is to preserve source material, maintain the wiki graph, and emit publish-ready content for the downstream site.

Current structural refactor planning is tracked in `wiki/projects/repo-structure-refactor.md`.
Future RAG/vector DB expansion is deferred and tracked separately in `wiki/projects/wiki-rag-expansion-roadmap.md`.

## Working Loop

Use this default loop for non-trivial changes:
1. Plan
2. Implement
3. Verify

## Rule Precedence

When documents overlap, follow this order:

1. `AGENTS.md`
2. `ARCHITECTURE.md`
3. `docs/operating/*`
4. domain-specific contract docs such as `docs/publishing-contract.md` and `docs/content-seo-guide.md`
5. `docs/adr/*`

`CLAUDE.md` and `.codex/AGENTS.md` are adapter surfaces. They should not silently override shared repository rules.

## Rule Strength

Interpret rules with these levels:

- `MUST`: required contract, safety, and verification rules
- `SHOULD`: default operating behavior unless there is a documented reason not to follow it
- `MAY`: optional enrichment or convenience guidance

## Publishing Compatibility

When authoring or rewriting publishable pages, follow `docs/content-seo-guide.md` so blog-writing and series-writing decisions already reflect search priorities before publish.

`wiki/` is the source of truth.

When changing publishable wiki pages or publishing rules, preserve:
- frontmatter required by `CLAUDE.md`
- stable `slug` and `description`
- downstream compatibility with `ai-survival-log-site/content/posts/YYYY-MM-DD-{slug}.mdx`
- book-study and social-expansion lanes when the page participates in them

When a publishable page embeds screenshots or other images, preserve:
- an upstream source copy in `assets/blog/`
- a downstream-served copy in `ai-survival-log-site/public/images/{slug-or-series}/`
- site-facing markdown image paths like `/images/{slug-or-series}/{file}.png`
- ASCII kebab-case filenames for publish-facing assets

## Wiki Principles

`MUST`

- keep the wiki human-first and markdown-first
- preserve Obsidian-friendly structure and direct readability
- treat future RAG/vector DB work as a derived layer, not the source-of-truth structure

`SHOULD`

- avoid introducing machine-first structure into authoring pages
- keep publishable writing aligned with `docs/content-seo-guide.md`

`MUST NOT`

- preemptively reshape the wiki around future RAG needs
- let derived JSON or downstream artifacts become the authoring source of truth

## Selective Adoption

Adopt only the useful operating principles from ECC and superpowers:
- plan before execute
- verification before completion
- systematic debugging
- documentation quality
- selective adoption over wholesale import

Do not introduce large agent catalogs, heavy MCP assumptions, or unnecessary multi-agent workflows just because the upstream harnesses support them.

## Verification Policy

`MUST`

- verify the changed scope before completion
- run the checks required by [docs/operating/validation-matrix.md](/Users/ms/workspace/claude/ai-survival-log/docs/operating/validation-matrix.md)
- block completion when source-of-truth, publishing contract, or state schema rules fail

`SHOULD`

- prefer test-first for regression-prone code paths such as `scripts/`, parsers, and publish logic
- review generated state diffs when tracked `output/state/*.json` files change

`MAY`

- add extra spot checks when a change spans both upstream and downstream contracts

## Documentation Consistency

Keep the project role and publishing boundary consistent across:
- `README.md`
- `CLAUDE.md`
- `.claude/*`
- `.codex/*`
- downstream-facing contract docs

## Detailed References

Use these documents as the authoritative detailed references instead of expanding this file:

- [ARCHITECTURE.md](/Users/ms/workspace/claude/ai-survival-log/ARCHITECTURE.md) — repository boundaries, layer model, publish and state policy
- [docs/operating/operations.md](/Users/ms/workspace/claude/ai-survival-log/docs/operating/operations.md) — operating loop, verification flow, state export responsibility
- [docs/operating/validation-matrix.md](/Users/ms/workspace/claude/ai-survival-log/docs/operating/validation-matrix.md) — change-type-to-required-check map
- [docs/operating/channel-lanes.md](/Users/ms/workspace/claude/ai-survival-log/docs/operating/channel-lanes.md) — multi-channel lane rules and expansion checklist
- [docs/publishing-contract.md](/Users/ms/workspace/claude/ai-survival-log/docs/publishing-contract.md) — upstream to downstream publishing contract
- [docs/content-seo-guide.md](/Users/ms/workspace/claude/ai-survival-log/docs/content-seo-guide.md) — publishable writing and SEO rules
- [docs/templates/prd.md](/Users/ms/workspace/claude/ai-survival-log/docs/templates/prd.md) — feature-level PRD template for contract-sensitive work
- [docs/adr/0001-markdown-source-of-truth.md](/Users/ms/workspace/claude/ai-survival-log/docs/adr/0001-markdown-source-of-truth.md) — canonical markdown decision
- [docs/adr/0002-json-derived-state-only.md](/Users/ms/workspace/claude/ai-survival-log/docs/adr/0002-json-derived-state-only.md) — JSON derived-state policy
- [docs/adr/0003-harness-layering-for-upstream-repo.md](/Users/ms/workspace/claude/ai-survival-log/docs/adr/0003-harness-layering-for-upstream-repo.md) — harness layering decision
- [docs/adr/0004-new-channels-remain-derived-from-the-wiki.md](/Users/ms/workspace/claude/ai-survival-log/docs/adr/0004-new-channels-remain-derived-from-the-wiki.md) — multi-channel expansion boundary
