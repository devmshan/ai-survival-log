# Operations Guide

## Purpose

This document defines the day-to-day operating workflow for `ai-survival-log`.

Use this document for:

- ingest and authoring flow
- sync, lint, and publish flow
- document consistency checks
- derived state generation boundaries
- lane expansion decisions for new channel workflows

## Default Loop

For non-trivial work:

1. Plan
2. Implement
3. Verify

## Authoring Flow

### Source Intake

1. Capture source material into `raw/`
2. Keep raw files immutable after intake
3. Create or update corresponding pages in `wiki/`
4. If the material belongs to a future lane such as YouTube, webtoon, or presentation, still record the canonical concept or plan in `wiki/` before creating lane-specific artifacts

### Wiki Authoring

When editing wiki pages:

- keep required frontmatter complete
- update `updated` dates when content changes
- maintain `[[wikilink]]` relationships
- avoid orphan pages

### Publishable Pages

When editing `published: true` pages:

- keep `slug` stable
- keep `description` concrete
- follow `docs/content-seo-guide.md`
- preserve downstream compatibility

## Verification Flow

### Required Checks

Run the relevant checks before completion:

- `python3 scripts/wiki sync`
- `python3 scripts/wiki lint --summary`

Add deeper verification when changes touch code:

- relevant tests for `scripts/`
- publish validation when publish rules change
- downstream contract verification when artifact behavior changes
- use [validation-matrix.md](/Users/ms/workspace/claude/ai-survival-log/docs/operating/validation-matrix.md) to decide the minimum required checks for each change type

### Self-Review

Before completion, review the changed scope for:

- bugs
- regressions
- contract drift
- security mistakes
- documentation inconsistency

For formal review gates, prefer 2-agent cross-validation when the workflow supports it, especially for code, contract, structure, and security-sensitive changes.
When possible, use different agent surfaces or different review paths rather than repeating the same model with the same checklist.

## Engineering Guardrails

- check existing code, docs, and reusable tools before adding new implementation
- use tests for code changes that can regress behavior
- prefer test-first for automation scripts, parsers, transformers, and publish/lint/sync logic
- do not force TDD for wiki content or metadata-only edits, but still verify the changed scope
- do not hardcode secrets
- validate external input
- do not leak sensitive data through error messages

## Failure Policy

Classify verification outcomes as `warn`, `block`, or `escalate`.

### `warn`

Use `warn` when quality is weaker than desired but the contract still holds.

Examples:

- title or intro can be improved for SEO clarity
- related links are thin but not absent
- tags are weak but not misleading

Warnings should be called out in the final review or follow-up notes.

### `block`

Use `block` when the change breaks the upstream authoring or downstream publishing contract.

Examples:

- malformed frontmatter
- missing required `slug` or `description` on a publishable page
- duplicate slug for a publishable route
- broken date-prefixed internal post links
- invalid image paths for publish-facing assets
- tracked state JSON that no longer matches its documented schema

Blocked work should not be treated as complete until fixed.

### `escalate`

Use `escalate` when the change is intentionally altering a long-lived contract or design decision.

Examples:

- changing publishable frontmatter requirements
- changing `output/state/` schema in a breaking way
- allowing a new path convention that affects the downstream site
- making SEO rules diverge from the downstream site on purpose

Escalated changes should update the relevant ADR or contract documents in the same change set.

## State Export Policy

Derived state belongs in `output/state/`.

Use state exports for:

- machine-readable summaries
- publish manifests
- lint summaries
- agent-surface consistency checks

Do not use state exports as source-of-truth.

Rules:

- generate by script
- do not hand-edit
- do not place JSON state under `docs/`
- do not include env values, tokens, private data, or absolute local paths
- keep tracked files deterministic so diffs reflect state changes rather than regeneration noise
- preserve backward compatibility for state consumers when possible
- treat schema removal or rename as an escalated change

Tracked state files in this repo:

- `output/state/wiki-index.json`
- `output/state/publish-manifest.json`
- `output/state/agent-surface-summary.json`

Official command:

```bash
python3 scripts/state export
```

## Responsibility Split

### `scripts/wiki`

Use for source-of-truth workflow:

- `sync`
- `lint`
- `publish`

### `scripts/state`

Use for derived state generation:

- state export
- machine-readable summary generation
- contract-facing inventories

If `scripts/wiki` ever emits state, it should call separate state logic rather than absorbing that responsibility directly.

## Lane Expansion

Use [channel-lanes.md](/Users/ms/workspace/claude/ai-survival-log/docs/operating/channel-lanes.md) before adding a new official workflow lane.

At minimum, define:

- canonical authoring surface
- `assets/{channel}/` source path
- `output/{channel}/` artifact path
- consumer surface
- contract owner
- required validation path

Treat an undefined lane as `escalate`, not normal implementation.

## Document Consistency

When operational rules change, check for consistency across:

- `README.md`
- `AGENTS.md`
- `CLAUDE.md`
- `.claude/*`
- `.codex/*`
- `ARCHITECTURE.md`
- `docs/operating/*`
- publishing and SEO contract docs

## Common Error Cases

Treat these as first-class operating cases rather than unusual exceptions:

- malformed frontmatter in a wiki page
- `published: true` without `slug` or `description`
- duplicate publishable slugs
- `series` present without valid `seriesSlug` in publish artifacts
- isolated tags that remove all automatic related-post coverage downstream
- broken downstream image path conventions
- partial state generation failure

When one of these cases appears, prefer explicit failure with file context over silent fallback.

## Related Docs

- [ARCHITECTURE.md](/Users/ms/workspace/claude/ai-survival-log/ARCHITECTURE.md)
- [docs/operating/validation-matrix.md](/Users/ms/workspace/claude/ai-survival-log/docs/operating/validation-matrix.md)
- [docs/operating/channel-lanes.md](/Users/ms/workspace/claude/ai-survival-log/docs/operating/channel-lanes.md)
- [docs/publishing-contract.md](/Users/ms/workspace/claude/ai-survival-log/docs/publishing-contract.md)
- [docs/content-seo-guide.md](/Users/ms/workspace/claude/ai-survival-log/docs/content-seo-guide.md)
- [docs/operating-playbook.md](/Users/ms/workspace/claude/ai-survival-log/docs/operating-playbook.md)
