# Codex Local Operating Guide

## Project Role

This repository is the upstream wiki authoring source for the AI Survival Log publishing workflow.

Primary flow:
`sources -> wiki -> publish -> ai-survival-log-site/content/posts`

Do not treat this repository as the final presentation layer or the primary site runtime.

## Working Loop

Use this default loop for non-trivial changes:
1. Plan
2. Implement
3. Verify

## Publishing Compatibility

`wiki/` is the source of truth.

Direct edits should preserve:
- required wiki frontmatter
- stable `slug` and `description` for publishable pages
- compatibility with the downstream site contract
- book-study and downstream content expansion rules when applicable

## Selective Adoption

Adopt only the useful parts of ECC and superpowers:
- writing plans
- verification before completion
- systematic debugging
- documentation quality
- selective adoption

Do not introduce large agent catalogs, heavy MCP assumptions, or unnecessary multi-agent workflows.
