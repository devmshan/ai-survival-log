---
name: wiki-lint
description: Validate wiki integrity for this repository by checking links, index coverage, frontmatter, publish readiness, and the current raw/wiki/assets/output boundary before finishing work.
---

# Wiki Lint

Use this skill when changes touch the wiki surface, publishing rules, or source-of-truth boundaries.

## Workflow

1. Run `python3 scripts/wiki lint --summary`.
2. If deeper validation is needed, inspect:
   - broken `[[wikilink]]`
   - orphan pages
   - frontmatter completeness
   - `published: true` requirements
   - folder/type consistency including `synthesis`
3. Treat `wiki/tags/` and `.obsidian/` as generated or local surface, not primary wiki content.

## Boundary Checks

- `raw/` remains immutable
- `wiki/` remains source of truth
- `assets/intake/` is channel-undecided asset intake
- `assets/blog/` holds actual upstream blog image sources
- `output/blog/` is a reproducible artifact, not source of truth
