# AI Survival Log Agent Guide

## Project Role

This repository is the upstream wiki authoring source for the AI Survival Log system.

Primary flow:
`sources -> wiki -> publish -> ai-survival-log-site/content/posts`

Do not treat this repository as the final presentation layer. Its responsibility is to preserve source material, maintain the wiki graph, and emit publish-ready content for the downstream site.

## Working Loop

Use this default loop for non-trivial changes:
1. Plan
2. Implement
3. Verify

## Publishing Compatibility

`wiki/` is the source of truth.

When changing publishable wiki pages or publishing rules, preserve:
- frontmatter required by `CLAUDE.md`
- stable `slug` and `description`
- downstream compatibility with `ai-survival-log-site/content/posts/YYYY-MM-DD-{slug}.mdx`
- book-study and social-expansion lanes when the page participates in them

## Selective Adoption

Adopt only the useful operating principles from ECC and superpowers:
- plan before execute
- verification before completion
- systematic debugging
- documentation quality
- selective adoption over wholesale import

Do not introduce large agent catalogs, heavy MCP assumptions, or unnecessary multi-agent workflows just because the upstream harnesses support them.

## Documentation Consistency

Keep the project role and publishing boundary consistent across:
- `README.md`
- `CLAUDE.md`
- `.claude/*`
- `.codex/*`
- downstream-facing contract docs
