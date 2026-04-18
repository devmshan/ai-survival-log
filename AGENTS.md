# AI Survival Log Agent Guide

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

- keep the wiki human-first and markdown-first
- preserve Obsidian-friendly structure and direct readability
- do not preemptively reshape the wiki around future RAG needs
- treat future RAG/vector DB work as a derived layer, not the source-of-truth structure

## Selective Adoption

Adopt only the useful operating principles from ECC and superpowers:
- plan before execute
- verification before completion
- systematic debugging
- documentation quality
- selective adoption over wholesale import

Do not introduce large agent catalogs, heavy MCP assumptions, or unnecessary multi-agent workflows just because the upstream harnesses support them.

## Documentation Consistency

Keep the project role and publishing boundary consistent across:
- `README.md`
- `CLAUDE.md`
- `.claude/*`
- `.codex/*`
- downstream-facing contract docs
