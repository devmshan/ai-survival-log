# PRD Template

## When to Use

Create a PRD for changes that:

- alter a publishing or content contract
- introduce a new user-facing workflow or major automation surface
- add a new derived-state schema or consumer
- change cross-repo behavior between `ai-survival-log` and `ai-survival-log-site`

Do not use a PRD for trivial copy edits, small bug fixes with no contract impact, or routine maintenance.

## Problem

- What problem exists now?
- Why does it matter to readers, authors, or operators?

## Goals

- Primary outcome
- Secondary outcome

## Non-Goals

- Explicitly list what this change will not solve

## Users and Surfaces

- Who is affected: author, operator, reader, agent, downstream consumer
- Which surfaces change: wiki, publish pipeline, site runtime, state export, docs
- Which lane changes: blog, series, Instagram, YouTube, webtoon, presentation, or other

## Constraints

- source-of-truth constraints
- publishing contract constraints
- SEO or UI constraints
- security and privacy constraints

## Documents To Read First

- List the architecture, operating, ADR, and contract documents that must be read before implementation
- List any files or outputs created by earlier steps that later steps must understand first

## Proposed Change

- Summarize the change
- Note any new files, commands, or schemas

## Step Plan

If the work is non-trivial, break it into small self-contained steps.

Rules:

- each step should change one layer, module, or contract surface at a time
- each step should be understandable without relying on unstated conversation context
- each step should name the files to read first
- interface or contract expectations should be explicit even when implementation details are left open

## Alternatives Considered

- Rejected option 1
- Rejected option 2

## Contract Impact

- frontmatter impact
- path or route impact
- state schema impact
- cross-repo alignment impact
- lane ownership impact
- consumer boundary impact

## Edge Cases

- malformed input
- missing metadata
- partial generation failure
- backward compatibility cases

## Validation Plan

- tests
- scripts
- manual checks
- state diff review
- executable acceptance criteria commands
- any required architecture or contract checklist review

## Prohibitions

- List concrete `do not X because Y` rules when the work needs hard guardrails
- Name the contract, schema, or source-of-truth boundaries that must not be crossed

## Rollout

- how the change is introduced
- whether migration is needed

## Rollback

- what would trigger rollback
- how to revert safely

## Follow-Up

- ADR updates
- document sync
- downstream cleanup
