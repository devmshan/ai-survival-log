---
name: wiki-ingest
description: Ingest raw source material from raw/articles, raw/videos, raw/podcasts, raw/books, or raw/journals into the wiki by creating or updating wiki/sources, entities, concepts, topics, and related links for this repository.
---

# Wiki Ingest

Use this skill when the task is to turn raw source material into durable wiki knowledge.

## Scope

- Read from `raw/{type}/`
- Keep `raw/` immutable
- Write summaries and knowledge pages in `wiki/`
- Update `wiki/index.md` and `wiki/log.md` when the ingest is material enough

## Workflow

1. Read the raw source file and identify:
   - summary
   - entities
   - concepts
   - related topics or projects
2. Create or update the corresponding page in `wiki/sources/`.
3. Create or update `wiki/entities/`, `wiki/concepts/`, `wiki/topics/`, or `wiki/projects/` as needed.
4. Add `[[wikilink]]` references and backlinks.
5. Run `python3 scripts/wiki sync`.
6. Run `python3 scripts/wiki lint --summary`.

## Rules

- Never rewrite the original file in `raw/`.
- If the material is mostly comparison or judgment, consider expanding an existing `wiki/topics/` page or creating a new one.
- If the source came from Web Clipper and is still ambiguous, classify it before ingesting.
