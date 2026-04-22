# ADR 0003: Harness Layering for the Upstream Repo

## Status

Accepted

## Context

`AGENTS.md` alone is not sufficient for long-term growth. It needs to remain compact and cross-agent readable, but detailed architecture, operations, and design decisions also need stable homes.

Claude and Codex both need to operate on the same repository without maintaining separate full rulebooks.

## Decision

Adopt a layered harness model.

Top-level documents:

- `README.md`
- `AGENTS.md`
- `CLAUDE.md`
- `ARCHITECTURE.md`

Detailed documents:

- `docs/operating/operations.md`
- `docs/adr/*.md`

Agent surface policy:

- `AGENTS.md` contains shared top-level operating rules
- `CLAUDE.md` inherits `AGENTS.md` and adds Claude-specific behavior
- `.codex/AGENTS.md` stays compact and points to shared detailed docs
- detailed rules should not be duplicated in full across all surfaces

## Consequences

Positive:

- shared rules have a single authoritative home
- Claude and Codex can stay aligned without full duplication
- top-level agent guides remain compact and easier to retain after context compression

Negative:

- links between documents must be maintained carefully
- moving existing rules into layered documents requires staged cleanup

## Rejected Alternatives

- keep all rules in `AGENTS.md`
- maintain separate full rulebooks for Claude and Codex
- create a large agent catalog before the shared operating model is stable

These were rejected because they either overload the top-level surface or create drift between agent-specific rule sets.

## Rollback / Exit Criteria

Revisit this decision only if the layered model causes more ambiguity than it removes.

Rollback signals include:

- persistent rule conflicts across surfaces
- top-level documents becoming large again despite layering
- operators no longer knowing where the authoritative rule lives

## Revisit Trigger

Re-review this ADR when:

- a new top-level surface is introduced
- document ownership becomes unclear
- cross-agent behavior starts to diverge in practice

## Edge Cases / Non-Goals

This ADR does not require every workflow detail to live in `AGENTS.md`.
It also does not justify duplicating the same long rule text into `CLAUDE.md` and `.codex/AGENTS.md`.

## Follow-Up

- create shared detailed documents before shrinking existing top-level surfaces
- update top-level surfaces to point to detailed docs in a later pass
