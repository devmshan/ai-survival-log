# Validation Matrix

## Purpose

This document defines the minimum required verification for common change types in `ai-survival-log`.

Use it to turn "verify the changed scope" into explicit operating checks.

## Severity Rules

- `warn`: the change can proceed, but follow-up quality work is still needed
- `block`: do not complete the change until the issue is fixed
- `escalate`: update contract docs or ADRs in the same change set

## Change Types

### Wiki Content Edit

Examples:

- concept page rewrite
- topic expansion
- source summary improvement

Required checks:

- `python3 scripts/wiki sync`
- `python3 scripts/wiki lint --summary`

Typical severity:

- missing wikilinks or weak summaries: `warn`
- malformed frontmatter or broken wiki structure: `block`

### Publishable Page Edit

Examples:

- `published: true` page rewrite
- title, intro, or description changes
- manual internal link updates

Required checks:

- `python3 scripts/wiki sync`
- `python3 scripts/wiki lint --summary`
- review against `docs/content-seo-guide.md`
- verify full date-prefixed internal post links

Typical severity:

- weak SEO polish: `warn`
- missing `slug`, missing `description`, or broken publish link paths: `block`
- intentional publish contract change: `escalate`

### Publish Rule or Contract Change

Examples:

- publish script behavior
- frontmatter contract changes
- image path convention changes

Required checks:

- relevant tests for `scripts/`
- `python3 scripts/wiki sync`
- `python3 scripts/wiki lint --summary`
- `python3 scripts/state export`
- downstream compatibility review against `ai-survival-log-site`

Typical severity:

- accidental contract drift: `block`
- deliberate contract break: `escalate`

### State Export Change

Examples:

- `scripts/state` logic changes
- `output/state/*.json` schema changes

Required checks:

- `pytest tests/test_state_lib.py`
- `python3 scripts/state export`
- review tracked `output/state/*.json` diffs
- update architecture or ADR docs if schema changes

Typical severity:

- non-deterministic tracked output: `block`
- backward-compatible field addition: `warn` unless a consumer depends on strict schema
- field removal, rename, or semantic change: `escalate`

### Agent Surface Change

Examples:

- `AGENTS.md`
- `CLAUDE.md`
- `.codex/AGENTS.md`
- operating document references

Required checks:

- confirm consistency with `ARCHITECTURE.md`
- `python3 scripts/state export`
- review `output/state/agent-surface-summary.json`

Typical severity:

- wording improvement with no rule drift: `warn`
- contradictory cross-surface rules: `block`
- intentional divergence between Claude and Codex guidance: `escalate`

### New Lane or Channel Workflow

Examples:

- YouTube workflow
- webtoon production lane
- presentation deck output
- new social expansion lane

Required checks:

- define the lane in `docs/operating/channel-lanes.md` or an equivalent PRD
- update `ARCHITECTURE.md` if repository boundaries change
- define asset source, artifact path, consumer, and contract owner
- add validation expectations for the lane

Typical severity:

- experimental notes without official workflow status: `warn`
- official lane with no contract owner or no boundary definition: `block`
- lane that changes canonical authoring structure or introduces a new consumer contract: `escalate`

## Notes

- If a change spans multiple categories, run the union of required checks.
- When in doubt, choose the stricter validation path.
