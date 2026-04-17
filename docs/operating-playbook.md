# Operating Playbook

## Purpose

This document combines the practical operating scenarios and the day-to-day working rhythm for the AI Survival Log system.

System boundary:
- `ai-survival-log` is the upstream authoring and wiki source-of-truth repository
- `ai-survival-log-site` is the downstream presentation and publishing-consumer repository

Core flow:
`sources -> wiki -> publish -> ai-survival-log-site/content/posts`

## Operating Model

- Create and preserve knowledge in `ai-survival-log`
- Consume and present publish-ready outputs in `ai-survival-log-site`
- Treat `wiki/` as the default source of truth
- Allow downstream refinements, but keep them compatible with the upstream publishing contract
- Use the default loop for non-trivial work:
  1. Plan
  2. Implement
  3. Verify

## Operating Scenarios

### 1. Read New Material And Absorb It Into The Wiki

Start in `ai-survival-log`.

Flow:
1. Save the material in `sources/`
2. Run `/wiki:ingest` to update `wiki/sources`, `wiki/entities`, `wiki/concepts`, and `wiki/topics`
3. Use `/wiki:query` when you want a wiki-grounded answer from accumulated knowledge
4. If the answer adds durable value, use `/wiki:file-answer` to store it back into the wiki

Use this when the goal is knowledge accumulation rather than publishing.

### 2. Publish A Wiki Topic As A Blog Post

Start in `ai-survival-log`.

Flow:
1. Refine the target page in `wiki/topics/*.md` or another publishable wiki page
2. Confirm `published: true`, `slug`, `description`, and standalone readability
3. If the page embeds screenshots or images:
   keep the source asset in `docs/images/`
   copy the site-facing asset to `ai-survival-log-site/public/images/{slug-or-series}/`
   use markdown image paths like `/images/{slug-or-series}/{file}.png`
   prefer ASCII kebab-case filenames
4. Run `/wiki:publish`
5. Emit or update the downstream post at `ai-survival-log-site/content/posts/YYYY-MM-DD-{slug}.mdx`
6. Move to `ai-survival-log-site` only for presentation-layer refinement if needed

Use this as the default wiki-to-blog path.

### 3. Turn A Book Study Session Into A Series Post

Start in `ai-survival-log`.

Flow:
1. Preserve the study conversation, notes, or chapter Q&A in `sources/`
2. Update related concept and topic pages in the wiki
3. Use `/content:book-study-blog` to structure the learning path, questions, explanations, and reverse questions
4. Run `/wiki:publish` to connect the upstream topic to a downstream post
5. In `ai-survival-log-site`, confirm `series`, `seriesSlug`, and `seriesOrder` if the post belongs to a visible study series

Use this for study-journal plus technical-blog hybrid posts.

### 4. Expand A Blog Post Into Instagram Slides

Usually start in `ai-survival-log`, sometimes finish in `ai-survival-log-site`.

Flow:
1. Choose the upstream wiki topic or the published downstream post as the source
2. Use `/content:blog-to-instagram` to extract the hook, key points, examples, and closing message
3. Treat the Instagram carousel as a compressed downstream expansion of the blog post
4. Keep the relationship between the source post and derived social assets explicit

Use this when a blog post should be repurposed into social content.

### 5. Change Site Rendering Or Content Loading

Start in `ai-survival-log-site`.

Flow:
1. Write a short plan before structural changes
2. Confirm the `content/posts` contract and series rules
3. Implement the change
4. Verify lint, tests, build, and any affected draft or series behavior

Use this for consumer-layer maintenance, not knowledge creation.

## Quick Start Decision Guide

Start in `ai-survival-log` for:
- new knowledge
- new interpretation
- new topic authoring
- wiki-grounded publishing
- book-study authoring
- social-content planning from a source post

Start in `ai-survival-log-site` for:
- rendering changes
- series UI and navigation changes
- content loading and filtering changes
- presentation-specific refinement after publish

## Daily Operating Routine

### Morning: Rebuild Context In The Upstream Repo

Start in `ai-survival-log`.

Check:
- `sources/`
- `wiki/log.md`
- recent `wiki/topics/`

Then decide:
- what new material needs ingest
- what existing wiki page needs expansion
- what publishing candidate is becoming ready

If new material exists, preserve it in `sources/` and run `/wiki:ingest`.
If you want to think through existing accumulated knowledge, use `/wiki:query`.
If the resulting answer is worth keeping, use `/wiki:file-answer`.

The purpose of this block is to ensure new understanding becomes upstream knowledge instead of staying only in conversation history.

### Midday: Pick A Publishing Lane

Stay in `ai-survival-log`.

Review which topic is ready to move outward:
- general blog post
- book-study series post
- not ready yet and still needs wiki refinement

For a normal post:
- refine the topic page
- confirm `published: true`, `slug`, `description`, and readable structure
- if images exist, keep `docs/images/` as the upstream source copy and `ai-survival-log-site/public/images/{slug-or-series}/` as the downstream-served copy
- run `/wiki:publish`

For a study-series post:
- use `/content:book-study-blog`
- structure the chapter flow, questions, examples, and reverse questions
- publish only after the upstream shape is stable

The purpose of this block is to convert selected upstream knowledge into downstream-ready outputs.

### Afternoon: Validate The Downstream Consumer

Move to `ai-survival-log-site`.

Check:
- newly added or updated MDX files in `content/posts/`
- frontmatter compatibility
- series metadata when applicable
- image asset paths and existence under `public/images/` when the post embeds screenshots
- draft filtering behavior
- any affected rendering or navigation

If a site-layer change is needed:
- plan first
- implement
- verify

The purpose of this block is to keep the consumer layer aligned with the publishing contract.

### Evening: Create Derived Content

Usually return to `ai-survival-log`.

Pick a published post with strong expansion value.
Use `/content:blog-to-instagram` to extract:
- the hook
- core message
- supporting example
- closing line

Treat the Instagram lane as a derivative of the source post, not as a separate source of truth.

### End Of Day: Verify And Leave A Clean State

In `ai-survival-log`:
- run `python3 scripts/wiki lint --summary`
- check that upstream docs still describe the same source-of-truth boundary

In `ai-survival-log-site`:
- confirm the content contract, series rules, and rendering behavior still match the documentation

Across both repositories:
- confirm that plan, implementation, and verification actually happened
- record durable context in the wiki or project docs rather than relying on memory

The end-of-day question is not only "what changed?" but also:
- what is now fixed upstream
- what safely flowed downstream
- what still needs to be carried into the next session
