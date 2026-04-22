# ADR 0002: JSON Is Derived State Only

## Status

Accepted

## Context

The repository needs machine-readable summaries for lint results, publish manifests, inventories, and agent-surface checks. JSON is a better fit for those outputs than markdown.

At the same time, introducing JSON as a canonical state layer would create drift from the markdown authoring model.

## Decision

JSON is allowed only as derived state.

Rules:

- derived JSON belongs in `output/state/` by default
- derived JSON must be script-generated
- derived JSON must be reproducible from source-of-truth layers
- if JSON conflicts with markdown, markdown wins

## Git Tracking Policy

Track only JSON files that are:

- stable enough for review
- useful in diffs
- non-sensitive

Examples:

- manifests
- inventories
- summaries

Do not track:

- local caches
- machine-specific paths
- raw runtime dumps
- stack traces
- secret-bearing output

## Security Constraints

Never include:

- tokens
- API keys
- env values
- private user data
- absolute local filesystem paths
- raw request metadata that could expose sensitive context

## Consequences

Positive:

- supports automation without changing canonical storage
- keeps sensitive or noisy outputs out of the main authoring surface

Negative:

- requires explicit generation and review policy
- adds another artifact class to maintain

## Rejected Alternatives

- storing state under `docs/`
- tracking every generated JSON file in git
- allowing hand-edited JSON for convenience

These were rejected because they blur document vs artifact boundaries and make review noise or secret leakage more likely.

## Rollback / Exit Criteria

Revisit this decision only if derived JSON can no longer stay:

- reproducible
- non-sensitive
- clearly subordinate to markdown or runtime truth

A rollback would require a documented schema migration and consumer review.

## Revisit Trigger

Re-review this ADR when:

- a new state consumer needs stronger schema guarantees
- tracked state diffs become noisy or non-deterministic
- a proposal requires JSON to carry canonical editorial decisions

## Edge Cases / Non-Goals

This ADR does not require every useful JSON file to be git-tracked.
It also does not allow caches, stack traces, or machine-specific dumps to masquerade as reviewable state.
