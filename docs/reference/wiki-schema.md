# Wiki Schema Reference

이 문서는 `ai-survival-log` 위키의 스키마, frontmatter, wikilink, `index.md` / `log.md` 규칙을 정리한 reference 문서다.

## Project Overview

- 이름: AI Survival Log
- 언어: 한국어, 기술 용어는 영문 유지
- 목적: 지식 축적 아카이브 + 블로그 퍼블리싱 upstream

## Wiki Architecture

```text
Human → source curation, exploration direction, questions
  ↓
LLM Agent → reading, summarizing, cross-referencing, file management
  ↓
Raw Layer → immutable originals
  ↓
Wiki Layer → markdown + index + log
  ↓
Assets / Output Layer → channel assets + publish artifacts
```

### Layer 1. `raw/`

- external articles, PDFs, notes, video memos
- immutable once added
- typical folders: `articles/`, `books/`, `journals/`, `videos/`, `podcasts/`
- do not directly edit source material here

### Layer 2. `wiki/`

- markdown knowledge base managed by agents
- pages connect with `[[wikilink]]`
- main folders: `entities/`, `concepts/`, `sources/`, `topics/`, `projects/`

### Layer 3. `assets/` / `output/`

- `assets/` keeps channel asset sources
- `output/blog/` keeps reproducible publish artifacts
- downstream site contract lives in `ai-survival-log-site/content/posts/`

### Layer 4. Agent Surface

- `AGENTS.md` defines top-level repository rules
- `CLAUDE.md` is the adapter surface for Claude
- detailed schema and operating references live in `docs/`

## Page Types

### `entities/`

- named things such as tools, frameworks, people, companies
- filename: `kebab-case-name.md`

### `concepts/`

- abstract ideas such as reasoning, RAG, prompt engineering
- filename: `kebab-case-concept.md`

### `sources/`

- summaries and analyses of `raw/` materials
- filename mirrors the corresponding source name

### `topics/`

- synthetic pages that connect multiple sources, entities, and concepts
- filename: `kebab-case-topic.md`

### `projects/`

- design notes, review notes, migration plans, implementation plans
- filename: `kebab-case-project.md`

## Frontmatter Spec

All wiki pages must include:

```yaml
---
title: "Page Title"
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
type: entity | concept | source | topic | project
sources: []
tags: []
status: draft | active | archived
published: false
slug: ""
description: ""
---
```

### Rules

- `created`: first creation date, do not change
- `updated`: must change when content changes
- `status`: `draft`, `active`, `archived`
- `published: true` requires `slug` and `description`
- `description` should say what the page contains and when it is useful
- `tags` use lowercase kebab-case
- `sources` stores referenced source-page wikilinks

### Publishable Image Rules

- upstream source copy in `assets/blog/`
- downstream served copy in `ai-survival-log-site/public/images/{slug-or-series}/`
- body path uses `/images/{slug-or-series}/{file}.png`
- publish-facing filenames should be ASCII kebab-case

## Cross-Referencing Rules

### Wikilinks

Use Obsidian-compatible wikilinks:

```markdown
[[entities/claude-code]]
[[entities/claude-code|Claude Code]]
[[concepts/ax-ai-transformation]]
```

### Link Management Principles

1. add backlinks when creating a new page
2. wikilink terms that correspond to existing wiki pages
3. keep a `## 관련 페이지` section at the bottom
4. avoid orphan pages

### Bottom Section

```markdown
## 관련 페이지

- [[entities/related-entity]]
- [[concepts/related-concept]]
- [[topics/related-topic]]
```

## `wiki/index.md` Rules

`wiki/index.md` is the central catalog and practical search index.

### Expectations

- update when pages are created, removed, or change state
- sort alphabetically inside categories
- keep one-line descriptions concise

## `wiki/log.md` Rules

`wiki/log.md` is the chronological record of wiki operations.

### Expectations

- newest items first
- grouped by date
- typical operation types:
  - `ingest`
  - `query`
  - `file-answer`
  - `lint`
  - `publish`
  - `edit`
  - `review`

## Naming and Writing Conventions

- filenames use kebab-case
- English filenames preferred for portability
- Korean prose is default, technical terms may stay in English
- pages start with `# Title`
- use `##` sections
- specify language for code fences

## Scale Guidance

- expected scale: roughly 50 to 200 pages
- if it grows much larger, review structure to avoid false coherence
- page count is shown near the top of `wiki/index.md`
