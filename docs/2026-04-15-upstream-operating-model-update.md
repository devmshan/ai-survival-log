# 2026-04-15 Upstream Operating Model Update

## Summary

This document records the operating-model changes applied to `ai-survival-log` so the repository now acts as the explicit upstream wiki authoring source for the broader AI Survival Log system.

The main outcome is a clearer separation:
- `ai-survival-log` as upstream authoring and source-of-truth
- `ai-survival-log-site` as downstream presentation and publishing consumer

## Why This Change Was Needed

Before this update:
- the repository did not have a root `README.md`
- there was no root `AGENTS.md`
- there was no local `.codex/` surface
- some publish-facing documentation still implied same-repo `content/posts/` output
- book-study and Instagram expansion lanes existed as scattered project notes, not as explicit local operating surfaces

That made the publishing boundary unclear and made it harder for Claude and Codex to follow the same working model.

## What Changed

### 1. Root Operating Surface Added

Added:
- `README.md`
- `AGENTS.md`
- `.codex/AGENTS.md`
- `.codex/config.toml`

These files now describe:
- the upstream role of this repository
- the downstream relationship to `ai-survival-log-site`
- the default `plan -> implement -> verify` loop
- selective adoption of ECC and superpowers principles

### 2. Publishing Contract Was Made Explicit

Added:
- `docs/publishing-contract.md`

This document defines:
- what a publishable wiki page must contain
- the downstream output path convention
- how book-study posts should remain compatible with series-aware downstream content
- what to verify when publishing rules change

### 3. Practical Operating Workflow Was Documented

Added:
- `docs/operating-playbook.md`

This playbook combines:
- real operating scenarios
- start-point guidance across the two repositories
- a day-to-day working rhythm
- end-of-day verification expectations

### 4. Claude Local Surface Was Cleaned Up

Added:
- `.claude/settings.json`

Adjusted:
- `.claude/settings.local.json`

Result:
- shared project hooks now live in the non-local settings file
- local permissions remain local
- official operating behavior no longer depends on personal local settings

### 5. Existing Publish Documentation Was Corrected

Updated:
- `CLAUDE.md`
- `.claude/commands/wiki/publish.md`
- `wiki/projects/blog-ai-study-site.md`

These changes removed the implicit same-repo output assumption and aligned the docs with the real downstream path:

`ai-survival-log-site/content/posts/YYYY-MM-DD-{slug}.mdx`

### 6. Content Expansion Lanes Were Promoted To First-Class Commands

Added:
- `.claude/commands/content/book-study-blog.md`
- `.claude/commands/content/blog-to-instagram.md`

Result:
- book-study publishing is now an explicit upstream lane
- Instagram expansion is now documented as a downstream derivative lane
- these flows are no longer only implied by scattered notes

## Adopted Principles

The repository now explicitly adopts a reduced set of principles inspired by ECC and superpowers:

- plan before structural or contract changes
- verify before completion
- systematic debugging when diagnosing content or publishing issues
- documentation consistency across local surfaces
- selective adoption instead of wholesale harness import

## Explicit Non-Goals

This update does not introduce:
- a large agent catalog
- heavy MCP assumptions
- mandatory multi-agent workflows
- full ECC runtime surfaces
- full superpowers workflow replication

The goal is a project-specific operating model, not a cloned external harness.

## Intended Effect

After this update, a contributor or agent should be able to answer the following unambiguously:

- Where is knowledge authored?
- Where is published content consumed?
- Which repo should a task start in?
- What is the publishing boundary?
- How do book-study and Instagram expansions fit into the system?
- What must be verified before calling work complete?

## Related Documents

- [README.md](/Users/ms/workspace/claude/ai-survival-log/README.md:1)
- [AGENTS.md](/Users/ms/workspace/claude/ai-survival-log/AGENTS.md:1)
- [CLAUDE.md](/Users/ms/workspace/claude/ai-survival-log/CLAUDE.md:1)
- [docs/publishing-contract.md](/Users/ms/workspace/claude/ai-survival-log/docs/publishing-contract.md:1)
- [docs/operating-playbook.md](/Users/ms/workspace/claude/ai-survival-log/docs/operating-playbook.md:1)
