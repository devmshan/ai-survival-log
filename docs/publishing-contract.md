# Publishing Contract

## Role

`ai-survival-log` is the upstream authoring repository.
`ai-survival-log-site` consumes publish-ready outputs.

The publishing interface is:
- publishable wiki pages in `wiki/`
- emitted site posts in `ai-survival-log-site/content/posts/`

## Upstream Publishable Page Requirements

Publishable wiki pages must include:
- `published: true`
- `slug`
- `description`
- `status`
- `updated`

They should also preserve:
- standalone readability for downstream readers
- stable tags suitable for site filtering
- valid related-page structure while in the wiki

## Output Rule

Default downstream output path:

`ai-survival-log-site/content/posts/YYYY-MM-DD-{slug}.mdx`

The publish step is responsible for:
- converting wiki frontmatter to site frontmatter
- removing wiki-only sections such as `## 관련 페이지`
- translating `[[wikilink]]` references for site consumption

## Book Study Lane

Book-study posts are still upstream-authored here, but must stay compatible with the downstream site's series-aware content model.

Recommended downstream fields:
- `series`
- `seriesSlug`
- `seriesOrder`

## Compatibility Rule

Manual downstream edits may happen in the site repository, but upstream publishing rules should remain compatible with the downstream site contract and should not silently break content loading, series navigation, or publish workflows.

## Verification

When changing publishing rules, verify:
- `README.md`, `AGENTS.md`, `CLAUDE.md`, `.claude/*`, and `.codex/*` describe the same source-of-truth boundary
- publishable wiki page requirements are still documented correctly
- downstream site path conventions are still reflected accurately
