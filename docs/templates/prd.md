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

## Proposed Change

- Summarize the change
- Note any new files, commands, or schemas

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
