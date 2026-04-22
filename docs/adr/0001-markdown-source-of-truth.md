# ADR 0001: Markdown Source of Truth

## Status

Accepted

## Context

`ai-survival-log` is designed as a human-first wiki authoring repository. The system needs to support direct reading and editing in markdown, Obsidian compatibility, stable publishing, and future agent consumption.

There is pressure to introduce more machine-readable formats for indexing, automation, and status tracking.

## Decision

Markdown remains the source of truth for authoring and knowledge structure.

Specifically:

- `raw/` remains the immutable input layer
- `wiki/` remains the canonical knowledge and authoring layer
- JSON may exist only as a derived output, not as canonical content

## Consequences

Positive:

- preserves human readability
- preserves Obsidian-friendly workflows
- keeps authoring, linking, and publishing centered on one canonical surface

Negative:

- some machine workflows require additional export steps
- scripts must generate derived views rather than reading a canonical JSON store

## Rejected Alternatives

- promote JSON to the canonical authoring layer
- split canonical state across markdown and JSON in parallel
- move source-of-truth status into a database-first system

These were rejected because they weaken human readability, increase drift risk, and break the current wiki-centered authoring model.

## Rollback / Exit Criteria

Revisit this decision only if the repository can no longer support:

- human-first markdown authoring
- Obsidian-friendly editing
- stable publish output from markdown sources

A rollback would require a deliberate migration plan, not ad hoc partial adoption.

## Revisit Trigger

Re-review this ADR when:

- a new canonical state layer is proposed
- multiple derived exports start mutating authoring decisions
- publishing can no longer be reproduced from markdown safely

## Edge Cases / Non-Goals

This ADR does not prohibit:

- derived JSON exports
- runtime indexes
- search or RAG layers built from markdown

This ADR does prohibit derived layers silently becoming the editing authority.

## Follow-Up

- keep machine-readable state in `output/state/`
- document any new derived state format separately
