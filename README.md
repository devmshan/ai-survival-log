# ai-survival-log

`ai-survival-log` is the upstream wiki authoring system for the broader AI Survival Log publishing workflow.

Core flow:
`sources -> wiki -> publish -> ai-survival-log-site/content/posts`

## Role

This repository focuses on:
- curating immutable source material in `sources/`
- maintaining the wiki knowledge base in `wiki/`
- turning selected wiki pages into publish-ready outputs
- supporting downstream expansion into blog posts, study-series posts, and Instagram assets

## Relationship To ai-survival-log-site

- `ai-survival-log` is the source-of-truth authoring system
- `ai-survival-log-site` is the presentation and publishing-consumer layer
- `published: true` wiki pages are the contract boundary between the two repositories
- downstream site content may be refined for presentation, but should stay compatible with the upstream publishing contract

## Publishing Lanes

### General Wiki To Blog

- input: `sources/` or direct wiki updates
- authoring: `wiki/topics/*.md` with `published: true`
- output: `ai-survival-log-site/content/posts/YYYY-MM-DD-{slug}.mdx`

### Book Study To Blog

- input: study conversation, notes, follow-up questions
- authoring: wiki topic plus linked source pages
- output: series-aware study post in `ai-survival-log-site/content/posts/`

### Blog To Instagram

- input: published blog post
- output: Instagram carousel assets generated from the site-facing article structure

## Publishing Contract

The upstream contract lives in [docs/publishing-contract.md](/Users/ms/workspace/claude/ai-survival-log/docs/publishing-contract.md:1).
The practical operating scenarios and daily workflow live in [docs/operating-playbook.md](/Users/ms/workspace/claude/ai-survival-log/docs/operating-playbook.md:1).
The documentation record for this operating-model change lives in [docs/2026-04-15-upstream-operating-model-update.md](/Users/ms/workspace/claude/ai-survival-log/docs/2026-04-15-upstream-operating-model-update.md:1).
The final cross-repository consistency review lives in [docs/2026-04-15-final-consistency-review.md](/Users/ms/workspace/claude/ai-survival-log/docs/2026-04-15-final-consistency-review.md:1).

At minimum, upstream publishable pages must preserve:
- stable `slug`
- `published: true`
- non-empty `description`
- correct `updated` date
- tags suitable for the downstream site

## Working Principles

- plan before structural or contract changes
- implement only the necessary change
- verify before completion
- selectively adopt ECC and superpowers principles instead of copying their full runtime surface
- keep documentation consistent across `README.md`, `AGENTS.md`, `CLAUDE.md`, `.claude/*`, and `.codex/*`

## Local Surfaces

- `.claude/`: Claude-facing project commands and hooks
- `.codex/`: Codex-facing local operating surface
- `CLAUDE.md`: wiki schema and workflow rules
- `AGENTS.md`: concise cross-agent operating model

Key local content lanes:
- `/wiki:*` for ingest, query, lint, publish, and file-answer
- `/content:book-study-blog` for study-session to series-post workflows
- `/content:blog-to-instagram` for downstream social expansion
