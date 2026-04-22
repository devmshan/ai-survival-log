# Wiki Commands Guide

## Purpose

This document defines the command-facing wiki workflows for `ai-survival-log`.

Use this document for:

- `/wiki:*` workflows
- publish transformation rules
- logging expectations for command-driven changes

## Local Command Surface

- `/journals:backup` — save the current conversation into `raw/journals/`
- `/wiki:ingest` — ingest source material into the wiki
- `/wiki:query` — answer from the wiki with citations
- `/wiki:file-answer` — save a useful answer into the wiki
- `/wiki:lint` — validate wiki integrity
- `/wiki:publish` — prepare downstream blog-ready MDX output
- `/content:book-study-blog` — connect study conversations into a series-ready lane
- `/content:blog-to-instagram` — connect a blog post into the Instagram lane
- `/content:review-blog-draft` — review publish-ready draft quality before `/wiki:publish`

## `/wiki:ingest`

1. Read the source material.
2. Preserve external source material in `raw/{type}/`.
3. Create or update the corresponding source page in `wiki/sources/`.
4. Create or update referenced entities.
5. Create or update referenced concepts.
6. Update related topics or projects when needed.
7. Add cross-references.
8. Update `wiki/index.md`.
9. Append a record to `wiki/log.md`.

Rules:

- one source may affect many wiki pages
- preserve existing knowledge when updating a page
- if sources conflict, record the disagreement with attribution

## `/wiki:query`

1. Read `wiki/index.md`.
2. Identify and read relevant pages.
3. Inspect matching raw source material if needed.
4. Answer with citations.
5. Offer to persist the result into the wiki when appropriate.

## `/wiki:file-answer`

1. Convert the answer into the appropriate wiki page.
2. Prefer `projects/` for operational or implementation changes.
3. add frontmatter
4. add cross-references
5. update `wiki/index.md`
6. append `wiki/log.md`

## `/wiki:lint`

Check at least:

1. broken `[[wikilink]]`
2. orphan pages
3. pages missing from `wiki/index.md`
4. pages listed in `wiki/index.md` but missing on disk
5. missing or incomplete frontmatter
6. stale `updated` dates
7. missing `## 관련 페이지` sections
8. `published: true` pages missing `slug` or `description`
9. generated or local-only surfaces staying outside canonical wiki checks

## `/wiki:publish`

1. Read the target wiki page and confirm `published: true`.
2. transform frontmatter to the blog-ready form
3. convert `[[wikilink]]` references into blog links or plain text
4. remove the `## 관련 페이지` section
5. verify downstream image path compatibility
6. write `output/blog/YYYY-MM-DD-{slug}.mdx`
7. sync to `ai-survival-log-site/content/posts/YYYY-MM-DD-{slug}.mdx` when required
8. append a publish record to `wiki/log.md`

Transformation rules:

- if a `[[wikilink]]` points to a published page, convert it to a full date-prefixed post path
- otherwise drop the blog link and keep readable text
- preserve Mermaid code blocks
- preserve both upstream source assets and downstream-served image copies
- keep site-facing image paths under `/images/{slug-or-series}/...`

## Blog Pipeline

```text
wiki/topic page
  -> /wiki:publish
  -> output/blog/YYYY-MM-DD-{slug}.mdx
  -> ai-survival-log-site/content/posts/YYYY-MM-DD-{slug}.mdx
```

Rules:

- the wiki remains the source of truth
- `output/blog/` and downstream `content/posts/` are generated outputs
- rerun `/wiki:publish` after meaningful upstream changes
- publishable pages should read as standalone posts
- screenshots and other inline images must preserve both source and downstream-served copies
- when a channel is not chosen yet, keep assets in `assets/intake/` until they become publish-facing blog assets
