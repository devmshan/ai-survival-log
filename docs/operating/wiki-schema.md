# Wiki Schema Guide

## Purpose

This document defines the wiki-facing schema and authoring structure for `ai-survival-log`.

Use this document for:

- wiki page types
- frontmatter requirements
- wikilink conventions
- `wiki/index.md` and `wiki/log.md` structure

## Project Overview

- Name: AI Survival Log
- Language: Korean for prose, English allowed for technical terms
- Goal: long-lived knowledge archive with publish-ready upstream authoring

## Wiki Layer Model

```
Human -> source curation, direction, questions
  ↓
LLM Agent -> reading, summarization, cross-referencing, file maintenance
  ↓
Raw Layer -> immutable inputs
  ↓
Wiki Layer -> persistent markdown knowledge graph
  ↓
Assets / Output Layer -> channel assets and derived artifacts
```

### `raw/`

- immutable source material
- representative folders: `articles/`, `books/`, `journals/`, `videos/`, `podcasts/`
- do not directly rewrite source interpretation here

### `wiki/`

- canonical human-first markdown knowledge base
- interlinked with `[[wikilink]]`
- main folders: `entities/`, `concepts/`, `sources/`, `topics/`, `projects/`

### `assets/` and `output/`

- `assets/` holds upstream channel asset sources
- `output/blog/` holds reproducible publish artifacts
- final downstream blog contract remains `ai-survival-log-site/content/posts/`

## Page Types

### `entities/`

- concrete named things such as tools, companies, frameworks, or people
- filename: kebab-case

### `concepts/`

- abstract concepts and practices
- filename: kebab-case

### `sources/`

- summaries and analysis for raw source material
- filename: match the corresponding source

### `topics/`

- synthesized pages that connect multiple sources, concepts, and entities
- filename: kebab-case

### `projects/`

- ongoing project design, planning, and implementation pages
- filename: kebab-case

## Frontmatter Spec

All wiki pages must keep this shape:

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

Rules:

- `created`: original creation date, do not rewrite it
- `updated`: refresh whenever content changes
- `status`: `draft`, `active`, or `archived`
- `published`: marks pages eligible for `/wiki:publish`
- `slug`: required when `published: true`
- `description`: required and concrete when `published: true`
- `tags`: lowercase, kebab-case
- `sources`: wikilink references to source pages

For publishable pages with images:

- preserve the source asset in `assets/blog/`
- preserve the downstream-served copy in `ai-survival-log-site/public/images/{slug-or-series}/`
- use `/images/{slug-or-series}/{file}.png` in publish-facing markdown
- prefer ASCII kebab-case filenames

## Cross-Referencing Rules

### Wikilink Format

Use Obsidian-compatible wikilinks:

```markdown
[[entities/claude-code]]
[[entities/claude-code|Claude Code]]
[[concepts/ax-ai-transformation]]
```

### Link Maintenance

1. Add backlinks when a new page creates a new relationship.
2. Convert relevant in-body concepts into `[[wikilink]]` references.
3. Keep a `## 관련 페이지` section.
4. Avoid orphan pages.

### Related Pages Section

```markdown
## 관련 페이지

- [[entities/related-entity]]
- [[concepts/related-concept]]
- [[topics/related-topic]]
```

## `wiki/index.md` Rules

`wiki/index.md` is the human-readable catalog of the wiki.

Shape:

```markdown
# Wiki Index

> 마지막 업데이트: YYYY-MM-DD | 총 N개 페이지
```

Maintain:

- category sections for `Entities`, `Concepts`, `Sources`, `Topics`, `Projects`
- category-level alphabetical ordering
- concise one-line descriptions

Update it when:

- pages are created
- pages are deleted
- status changes

## `wiki/log.md` Rules

`wiki/log.md` is the chronological operational record.

Shape:

```markdown
# Wiki Log

## YYYY-MM-DD

### HH:MM — 작업유형: 제목
- **source:** original source if present
- **created:** created pages
- **updated:** updated pages
- **summary:** 1-2 line summary
```

Rules:

- newest entries first
- group by date
- use stable operation labels such as `ingest`, `query`, `file-answer`, `lint`, `publish`, `edit`, `init`

## Conventions

### Filenames

- kebab-case
- English preferred for compatibility
- no date prefix in wiki filenames

### Content Writing

- Korean prose by default
- begin with `# Title`
- use `##` for sections
- specify code block languages

### Scale Review

- expected range: roughly 50-200 pages before structure pressure rises
- re-evaluate structure when the wiki grows beyond that level
- keep the total page count visible in `wiki/index.md`
