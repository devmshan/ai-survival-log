# Content SEO Guide

## Purpose

This document defines the content SEO writing rules for publishable wiki pages and downstream blog-ready outputs in `ai-survival-log`.

Targets:

- new blog-oriented wiki pages
- series-oriented wiki pages
- existing publishable page rewrites
- upstream authoring before `/wiki:publish`

This document is about authoring quality for search visibility, not runtime metadata implementation.

---

## Why This Exists

In this system, many blog posts and series posts are authored upstream first and only later emitted to `ai-survival-log-site`.
Because of that, search-aware writing rules should not live only in the downstream site repository.
They need to be applied at the upstream authoring stage so the publish pipeline starts from better titles, summaries, introductions, and link structure.

---

## Core Principles

- Search traffic is earned through clear topic definition, not accidental discovery.
- A reader should understand what the page explains within the first 10 seconds.
- Brand tone can remain, but search-oriented pages should not rely on abstract or purely emotional titles alone.
- Publishable pages should connect to other pages so the downstream site can support topic-cluster navigation.
- Not every page needs to be aggressively search-driven, but any page expected to attract search traffic should follow these rules by default.

---

## Page Types

Decide the page type before writing or rewriting.

### 1. Search-Oriented Page

Examples:

- concept explanation
- comparison
- guide
- troubleshooting page
- tool overview

Rules:

- include the main query or concept in `title` or a search-oriented override if the downstream lane supports one
- make the scope of the answer explicit in the first 1 to 3 paragraphs
- keep `description` concrete and useful

### 2. Hybrid Page

Examples:

- personal experience + technical explanation
- retrospective + practical lessons

Rules:

- the page may keep a personal tone
- but the introduction should surface the practical subject early
- `description` should describe the technical or practical value, not only the emotion of the piece

### 3. Brand / Reflection Page

Examples:

- manifesto
- start-of-blog page
- personal philosophy

Rules:

- tone may take priority over raw search traffic
- still make the subject understandable in `description`
- add explicit links to related technical or thematic pages when possible

---

## Title Rules

### `title`

- this is the primary visible title in the authoring source
- it may preserve tone and voice
- but it should still communicate enough meaning for a downstream reader to predict the topic

Use titles that:

- include the main concept when the page is search-oriented
- narrow the scope enough to match a real query or problem
- avoid ambiguity when the page is meant to teach something

Avoid titles that:

- are purely emotional with no clear concept
- ask a vague question without signaling the answer scope
- are too broad for the actual content

---

## Description Rules

### `description`

- required for publishable pages
- should act as a concise summary of what the page explains
- should be concrete enough to work as the downstream card summary and search snippet basis

Good descriptions usually include:

- the main topic
- what the reader will learn
- enough specificity to distinguish the page from nearby topics

Avoid descriptions that:

- are only poetic or emotional
- describe motivation without summarizing the actual content
- are too generic to help downstream presentation

---

## Introduction Rules

The first 1 to 3 paragraphs should answer:

- what question this page addresses
- what scope it covers
- who this is useful for

Recommended structure:

1. state the problem or question
2. define what this page will explain
3. provide brief context before entering the body

Avoid:

- long narrative buildup before the topic appears
- technical pages where the main subject appears too late

---

## Internal Linking Rules

Publishable pages should be written so they can support downstream topic clustering.

When possible, include:

- at least 2 related wiki links to nearby concepts or topics
- series-aware linkage when the page belongs to an obvious sequence
- one clear next step for readers who want deeper material

Authoring rule:

- do not rely only on tags
- the page body and related-page structure should help readers continue the topic path

---

## Topic Cluster Rules

Priority clusters currently include:

- LLM fundamentals
- embeddings / vector DB / RAG
- system design
- AI coding workflow / automation

Upstream authoring approach:

- create or maintain a clear entry page for each major topic cluster
- connect deeper pages back to the entry page
- when a sequence is natural, structure it so downstream series metadata can be added cleanly

---

## Series Authoring Rules

When a page is likely to become part of a public downstream series:

- write each part so it stands alone
- still make the sequence explicit in the body or related-page structure
- keep ordering logic stable so downstream `series`, `seriesSlug`, and `seriesOrder` can be added without ambiguity

Series pages should answer both:

- what this individual part covers
- where it sits in the broader sequence

---

## Image Rules

If a publishable page uses screenshots or diagrams:

- keep the upstream source copy in `assets/blog/`
- preserve a downstream-served copy in `ai-survival-log-site/public/images/{slug-or-series}/`
- use stable, publish-facing markdown image paths
- prefer images that clarify the topic, not decorative images only

Downstream-served paths and publish-facing markdown paths should remain stable even as upstream asset organization evolves.

---

## Authoring Checklist

Before publishing or preparing a page for `/wiki:publish`, confirm:

- [ ] the page type is clear
- [ ] the title communicates the topic well enough
- [ ] the description summarizes the practical subject clearly
- [ ] the first 1 to 3 paragraphs surface the main topic early
- [ ] the page links to related pages that help topic continuation
- [ ] series suitability has been considered when applicable
- [ ] image handling follows the publish asset rules when screenshots are used

---

## Rewrite Prioritization

When rewriting older publishable pages, prioritize in this order:

1. clearly search-oriented technical pages
2. series or cluster hub pages
3. hybrid pages that can become stronger search entries
4. brand / reflection pages

Judge priority by:

- clarity of search intent
- value as an internal-link hub
- likely CTR gain from better titles and summaries

---

## Cross-Repo Alignment

The downstream site repository also carries related SEO writing and runtime guidance.
These rules should stay aligned with:

- `ai-survival-log-site/docs/content-seo-guide.md`
- `ai-survival-log-site/docs/content-contract.md`
- `ai-survival-log-site/docs/automation/seo-operations.md`

Do not let upstream authoring guidance drift from downstream SEO presentation rules.

---

## Maintenance Rule

- use this document as the default writing guide for publishable upstream pages
- when publishing rules change, re-check this document together with `docs/publishing-contract.md`
- when downstream SEO writing rules evolve, mirror the relevant authoring guidance here
