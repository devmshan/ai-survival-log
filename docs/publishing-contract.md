# Publishing Contract

## Role

`ai-survival-log` is the upstream authoring repository.
`ai-survival-log-site` consumes publish-ready outputs.

The publishing interface is:
- publishable wiki pages in `wiki/`
- publish artifacts in `output/blog/`
- emitted site posts in `ai-survival-log-site/content/posts/`

## Upstream Publishable Page Requirements

Publishable wiki pages must include:
- `published: true`
- `slug`
- `description`
- `status`
- `updated`

They should also preserve:
- titles and descriptions that remain strong enough for downstream SEO presentation
- introductions that surface the page topic early for downstream readers
- link structure that supports downstream topic-cluster navigation
- standalone readability for downstream readers
- stable tags suitable for site filtering
- valid related-page structure while in the wiki

Blog-oriented topic pages must pass the Axis A (source fidelity) and Axis B (writing craft) 2-axis review defined in `docs/blog-draft-review-rules.md` before `/wiki:publish` is run.

If a publishable page contains screenshots or other inline images, it should also preserve:
- an upstream source copy under `assets/blog/`
- a downstream-served copy under `ai-survival-log-site/public/images/{slug-or-series}/`
- publish-facing markdown paths in the form `/images/{slug-or-series}/{file}.png`
- ASCII kebab-case asset filenames

## Output Rule

Default upstream artifact path:

`output/blog/YYYY-MM-DD-{slug}.mdx`

Default downstream output path:

`ai-survival-log-site/content/posts/YYYY-MM-DD-{slug}.mdx`

The publish step is responsible for:
- converting wiki frontmatter to site frontmatter
- removing wiki-only sections such as `## 관련 페이지`
- translating `[[wikilink]]` references for site consumption
- keeping inline image references compatible with downstream site paths
- keeping the upstream artifact layer reproducible rather than hand-edited

## Book Study Lane

Book-study posts are still upstream-authored here, but must stay compatible with the downstream site's series-aware content model.

Recommended downstream fields:
- `series`
- `seriesSlug`
- `seriesOrder`

## Compatibility Rule

Manual downstream edits may happen in the site repository, but upstream publishing rules should remain compatible with the downstream site contract and should not silently break content loading, series navigation, or publish workflows.

`output/blog/` is now the upstream publish artifact layer, but the final downstream contract remains `ai-survival-log-site/content/posts/YYYY-MM-DD-{slug}.mdx`.

## Verification

When changing publishing rules, verify:
- `README.md`, `AGENTS.md`, `CLAUDE.md`, `.claude/*`, and `.codex/*` describe the same source-of-truth boundary
- publishable wiki page requirements are still documented correctly
- downstream site path conventions are still reflected accurately
- embedded screenshots or image assets have both upstream source copies and downstream-served copies
