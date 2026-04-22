# Channel Lanes Guide

## Purpose

This document defines how `ai-survival-log` should expand beyond the current blog workflow without losing source-of-truth clarity.

Use this document when adding or revising lanes such as:

- blog
- book-study series
- Instagram
- YouTube
- webtoon
- presentation or slide output

## Core Rule

New lanes do not get to redefine the canonical authoring model.

`raw/` remains the immutable intake layer.
`wiki/` remains the canonical human-authored knowledge and planning layer.
`assets/` holds channel asset sources.
`output/` holds derived channel artifacts.

If a new lane needs structure, add it as a derived workflow with an explicit contract instead of mutating the wiki into a channel-specific schema.

## Required Lane Definition

Every lane must define all of the following before it is treated as an official workflow:

1. source intake
2. canonical authoring surface
3. upstream asset source path
4. derived output path
5. downstream consumer or publication surface
6. contract document owner
7. required validation steps
8. optional derived state outputs

Do not add a new lane based only on a folder name or one-off script.

## Lane Registry

### Blog

- intake: `raw/*`, direct wiki authoring
- canonical authoring: `wiki/`
- asset source: `assets/blog/`
- derived output: `output/blog/`
- consumer: `ai-survival-log-site/content/posts/`
- contract docs: `docs/publishing-contract.md`, `docs/content-seo-guide.md`

### Book Study

- intake: `raw/books/`, study conversations, source notes
- canonical authoring: `wiki/` plus linked source pages
- asset source: `assets/blog/` or `assets/shared/` as needed
- derived output: `output/blog/` with series-aware structure
- consumer: `ai-survival-log-site/content/posts/`
- contract docs: blog contract docs plus series rules

### Instagram

- intake: published blog post or wiki-backed post concept
- canonical authoring: upstream wiki page and blog post remain canonical
- asset source: `assets/instagram/` or `assets/shared/`
- derived output: `output/instagram/`
- consumer: social publishing workflow outside the wiki
- contract docs: lane-specific guide or future social contract

### YouTube

- intake: source notes, scripts, references, transcript materials
- canonical authoring: `wiki/` for concepts and script planning
- asset source: `assets/youtube/`
- derived output: `output/youtube/`
- consumer: video publishing workflow
- contract docs: lane-specific brief required before official adoption

### Webtoon

- intake: story notes, reference captures, design notes
- canonical authoring: `wiki/` for story/concept structure
- asset source: `assets/webtoon/`
- derived output: `output/webtoon/`
- consumer: webtoon production workflow
- contract docs: lane-specific brief required before official adoption

### Presentation

- intake: wiki topics, talk notes, workshop plans
- canonical authoring: `wiki/`
- asset source: `assets/presentation/` or `assets/shared/`
- derived output: `output/presentation/`
- consumer: slides, decks, talk notes, or downloadable presentation artifacts
- contract docs: lane-specific brief required before official adoption

## Lane Addition Checklist

Before adding a new official lane:

- define the canonical authoring surface
- define asset source and output paths
- define the consumer surface
- define the lane contract doc or PRD
- define the minimum validation path
- define whether derived state is needed
- define whether the lane lives in this repo, `ai-survival-log-site`, or a separate consumer

If any item is missing, treat the lane as `escalate`, not normal implementation.

## Failure Policy

### `warn`

- a lane exists experimentally but lacks automation
- a lane uses shared assets while the dedicated asset directory is still pending

### `block`

- a lane writes derived output into `wiki/`
- asset sources and derived outputs are mixed together
- the lane has no defined contract or consumer
- a new lane changes blog or site contracts unintentionally

### `escalate`

- the lane introduces a new downstream consumer
- the lane requires a new canonical field in wiki frontmatter
- the lane needs separate publication or synchronization rules

## State Policy For New Lanes

Only add `output/state/*` for a lane when it has a real review or automation consumer.

Examples:

- manifest of generated presentation decks
- YouTube script or episode inventory
- webtoon panel production summary

Do not add state files just because a lane exists conceptually.

## Related Docs

- [ARCHITECTURE.md](/Users/ms/workspace/claude/ai-survival-log/ARCHITECTURE.md)
- [docs/operating/operations.md](/Users/ms/workspace/claude/ai-survival-log/docs/operating/operations.md)
- [docs/operating/validation-matrix.md](/Users/ms/workspace/claude/ai-survival-log/docs/operating/validation-matrix.md)
- [docs/templates/prd.md](/Users/ms/workspace/claude/ai-survival-log/docs/templates/prd.md)
