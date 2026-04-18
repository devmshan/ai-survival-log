---
name: wiki-publish
description: Publish wiki pages from the source-of-truth wiki into output/blog artifacts, while preserving downstream compatibility with ai-survival-log-site content/posts and current image rules for this repository.
---

# Wiki Publish

Use this skill when a publishable wiki page should become a blog artifact.

## Workflow

1. Confirm the page has:
   - `published: true`
   - `slug`
   - `description`
   - `status: active`
2. Check image rules:
   - actual blog source images live in `assets/blog/`
   - channel-undecided assets stay in `assets/intake/`
   - downstream served images live in `ai-survival-log-site/public/images/{slug-or-series}/`
3. Run publish through the repo workflow.
4. Treat `output/blog/YYYY-MM-DD-{slug}.mdx` as the primary upstream artifact.
5. Keep downstream compatibility with `ai-survival-log-site/content/posts/YYYY-MM-DD-{slug}.mdx`.

## Rules

- `wiki/` is source of truth.
- `output/blog/` is not manually authoritative.
- Remove wiki-only sections such as `## 관련 페이지` from the published artifact.
