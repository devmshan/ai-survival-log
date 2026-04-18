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

### `seoTitle`

**Required** when `title` prioritizes brand tone, narrative hook, or personal voice over search clarity.

This field is the HTML `<title>` override used by the downstream site for search engine visibility. It does not change the visible heading in the post.

#### Format rule

```
[primary concept or action] + [specific modifier or context] + [outcome or qualifier if needed]
```

- put the main searchable concept in the first 15 characters
- Korean target length: 30–50 characters
- English target length: 50–60 characters
- do not start with a brand name the reader would not search for
- do not start with a narrative hook or rhetorical phrase

#### When to write seoTitle

| `title` type | seoTitle needed? |
|---|---|
| Narrative hook ("Claude가 짜고 Codex가 깼다") | **Yes** |
| Emotional / reflective ("그래도 안 쓴 이유") | **Yes** |
| Personal record tone ("~해봤다") | Depends — add if the concept is buried |
| Already concept-first and specific | No |

#### Series posts vs standalone posts

- **Series post:** focus seoTitle on the episode-specific concept; the series name provides shared context
- **Standalone post:** front-load the broader category keyword before the specific tool or topic name

#### Examples

| title | seoTitle |
|---|---|
| "Claude가 짜고 Codex가 깼다 — 저장소 구조 리팩토링" | "Claude로 계획하고 Codex로 검증하는 저장소 구조 리팩토링" |
| "Graphify는 마크다운도 된다 — 그래도 안 쓴 이유" | "마크다운 위키를 지식 그래프로 변환하는 Graphify — 직접 평가해봤다" |
| "Claude Code만 쓰던 프로젝트에 Codex를 넣어봤다" | "Claude Code만 쓰던 프로젝트에 Codex를 넣어본 이유와 운영 모델 변화" |

#### Anti-patterns

| Anti-pattern | Fix |
|---|---|
| `seoTitle: "Claude가 짜고 Codex가 깼다"` | 서사 훅을 그대로 복사함 — 검색어 없음 |
| `seoTitle: "저장소 구조를 바꿔봤다"` | 주체(도구/방법)가 없음 |
| `seoTitle: "Graphify 평가"` | 너무 단편적 — 맥락과 가치가 없음 |

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

### Internal Link Slug Format

All internal post links must include the full date-prefixed slug:

```
✓ /posts/2026-04-15-claude-code-to-codex
✗ /posts/claude-code-to-codex
```

Slugs without the date prefix produce 404s because the downstream routing is keyed on the full filename.

### "함께 읽으면 좋은 글" Section

Every published post must end with a `## 함께 읽으면 좋은 글` section containing at least 2–3 manually curated links.

This is separate from the automatic "관련 글" card section (see below). The automatic section may produce zero results when a post's tags do not overlap with other posts. In that case the manual section is the only reader navigation available.

### Related Posts Automatic Logic

The site auto-generates a "관련 글" card section using this scoring model:

| Signal | Score |
|---|---|
| Same series (`seriesSlug` match) | +100 |
| Each shared tag | +10 |
| Score = 0 | section hidden |

Implication for authoring: posts with unique or isolated tags will produce no automatic related posts. Tag design directly affects whether the "관련 글" section appears. When writing a post whose tags do not overlap with existing posts, add the manual "함께 읽으면 좋은 글" section to compensate.

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

## Section Header Rules

Section headers (`##`) are not navigation labels. They are the single most visible signal of what a reader gains from each section.

### Rule

Each `##` header should communicate the **insight, discovery, or pivot** of that section — not just name what happens.

**Never use numeric prefixes** (`## 1.`, `## 2.`, `## 3.`). This applies to all page types including reference guides. Numbers add no meaning and force readers to mentally strip them before reading. Use the section title alone.

### Bad headers (labels)

These describe activity without meaning:

- "설치하고 돌려봤다" — describes an action, gives no insight
- "부수 효과들" — categorizes without revealing the discovery
- "시작은 Web Clipper였다" — states context with no signal of value

### Good headers (insight)

These carry the key finding or turning point:

- "`pip install` 한 줄, 그리고 바로 막혔다" — shows the gap between expectation and reality
- "마크다운이 이미 그 문제를 풀고 있었다" — reveals the core insight
- "문서만 읽으면 충돌이 보이지 않는다" — names the lesson earned

### Test

Read only the headers of the post. Can you follow the argument? If the headers could apply to any generic blog post, they are labels and need revision.

---

## Narrative Quality Rules

These rules address issues that SEO metadata rules alone do not catch.

### Opening paragraph: establish WHY before WHAT

The first 2-3 paragraphs should answer: **why does this topic matter now?**

Structure:
1. Name the broader trend, pressure, or problem
2. Introduce the specific situation or tool
3. Signal what the reader will learn

Avoid opening directly with personal action ("오늘 X를 해봤다") without first establishing why the reader should care.

**Before:** "개인 위키를 만들기 시작하면, Graphify 추천을 꽤 자주 만난다."

**After:** "개인 위키를 구축하는 사람이 늘면서, 방법론도 다양해지고 있다. … Graphify는 이 수요를 겨냥해서 나온 도구다. … 나도 궁금해서 직접 써봤다."

### Section motivation: WHY before WHAT

Each section should make clear **why the action or discovery happened** — not just report what happened.

If a section starts a new action, the previous section or a transition sentence should explain the motivation.

**Missing motivation:** "파이프라인이 준비되자 첫 자료를 수집했다." (why this particular source?)

**With motivation:** "마침 Graphify에 관심이 생긴 시점이었다 … 위키가 계속 커지고 있었고, 관계 구조를 더 잘 볼 수 있는 방법이 없을까 찾아보던 중이었다."

### Technical depth: explain WHY not just WHAT

For tool evaluations, CLI results, or technical findings, do not stop at "it failed." Explain the mechanism.

**Shallow:** "`graphify update wiki`가 실패했다."

**With depth:** "`update` 명령은 소스 코드 파일(.py, .js, .ts)을 스캔하는 용도다. `.md` 파일은 처음부터 처리 대상이 아니다. '코드 파일 없음' 에러는 그 의미 그대로였다."

### Noise filter: remove details that don't serve the reader

Remove:
- LLM agent internal process details (sandbox constraints, tool workarounds)
- One-time environment details the reader cannot reproduce
- Intermediate steps that do not contribute to the conclusion

Keep:
- CLI commands and outputs the reader can run themselves
- Technical reasoning that explains WHY the conclusion was reached
- Discoveries that directly informed the decision

---

## Authoring Checklist

Before publishing or preparing a page for `/wiki:publish`, confirm:

- [ ] the page type is clear
- [ ] the title communicates the topic well enough
- [ ] the description summarizes the practical subject clearly
- [ ] the first 1 to 3 paragraphs surface the main topic early **and explain WHY the topic matters**
- [ ] each `##` header communicates an insight or finding, not just a label
- [ ] each section shows the motivation behind the action or discovery
- [ ] technical evaluations explain the underlying mechanism, not just the outcome
- [ ] no implementation details that are irrelevant to the reader
- [ ] the narrative arc is complete — no missing context
- [ ] the post scope reads as coherent for a single blog post
- [ ] the page links to related pages that help topic continuation
- [ ] all internal links use the full date-prefixed slug (`/posts/YYYY-MM-DD-slug`)
- [ ] a `## 함께 읽으면 좋은 글` section with at least 2 links is present
- [ ] no `##` headers use numeric prefixes (`## 1.`, `## 2.`, etc.)
- [ ] series suitability has been considered when applicable
- [ ] image handling follows the publish asset rules when screenshots are used

Run `/content:review-blog-draft` to verify these items before publishing.

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
