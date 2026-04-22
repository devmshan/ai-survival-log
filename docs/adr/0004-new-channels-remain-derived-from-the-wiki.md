# ADR 0004: New Channels Remain Derived From the Wiki

## Status

Accepted

## Context

The repository is already expanding beyond core blog publishing into study-series, social, and future lanes such as YouTube, webtoon, and presentation outputs.

Without a clear rule, each new lane could pressure the wiki to adopt channel-specific structure or create ad hoc artifact paths with no contract owner.

## Decision

New channels must remain derived from the existing source-of-truth model unless a separate canonical system is explicitly approved.

Specifically:

- `raw/` remains intake
- `wiki/` remains canonical authoring and planning
- `assets/{channel}/` stores channel asset sources
- `output/{channel}/` stores derived artifacts
- each new lane needs an explicit contract or PRD before official adoption

## Consequences

Positive:

- preserves one canonical authoring model
- keeps channel expansion reviewable
- reduces silent coupling between blog workflows and future lanes

Negative:

- new lanes require more upfront definition
- experimental lanes cannot skip contract thinking once they become official

## Rejected Alternatives

- let each channel define its own canonical storage immediately
- embed channel-specific structure directly into wiki organization
- treat asset directories as sufficient documentation

These were rejected because they create drift, duplicate authoring logic, and hide contract assumptions.

## Rollback / Exit Criteria

Revisit this decision only if a future lane proves that wiki-backed authoring is no longer the right canonical model for that lane.

Any rollback requires:

- a separate canonical contract
- a migration plan
- clear boundary docs showing why the lane no longer derives from the wiki

## Revisit Trigger

Re-review this ADR when:

- a lane needs canonical data the wiki cannot express safely
- multiple channels begin overriding the same wiki fields differently
- a new consumer requires its own long-lived authoring model

## Edge Cases / Non-Goals

This ADR does not require every lane to be fully automated.
It does require every official lane to declare its authoring surface, artifact path, and contract owner.
