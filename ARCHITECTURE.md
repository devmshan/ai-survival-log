# AI Survival Log Architecture

## Role

`ai-survival-log` is the upstream wiki authoring system for the broader AI Survival Log workflow.

Primary flow:
`raw -> wiki -> output/blog -> ai-survival-log-site/content/posts`

This repository is not the final presentation layer. Its responsibility is to preserve source material, maintain the wiki graph, and emit publish-ready artifacts for the downstream site.

## Document Precedence

When repository documents overlap, follow this order:

1. `AGENTS.md`
2. `ARCHITECTURE.md`
3. `docs/operating/*`
4. domain-specific contract docs such as `docs/publishing-contract.md` and `docs/content-seo-guide.md`
5. `docs/adr/*`

`CLAUDE.md` and `.codex/AGENTS.md` adapt these rules for their execution surfaces. They must stay aligned with shared repository rules.

## Core Boundaries

### Source of Truth

- `raw/` holds immutable source material.
- `wiki/` is the source of truth for summaries, links, concepts, topics, and publishable authoring pages.
- `assets/` holds upstream media and channel asset sources.
- `output/` holds reproducible artifacts, not canonical authoring content.

### Derived Layers

- `output/blog/` is a publish artifact layer.
- future RAG/vector indexing remains a derived layer and must not redefine the wiki structure.
- JSON state exports belong to `output/state/` and must remain derived from the source-of-truth layers.

## Layer Model

### 1. `raw/`

- Immutable inputs from articles, books, journals, videos, podcasts, and other captures
- Do not rewrite summaries or editorial interpretation here
- New source material enters the system here first

### 2. `wiki/`

- Human-first markdown knowledge graph
- Entities, concepts, sources, topics, and projects live here
- Publishable authoring pages are maintained here
- `wiki/index.md` and `wiki/log.md` are human-readable operating surfaces

### 3. `assets/`

- Upstream asset source layer
- `assets/blog/` holds upstream blog image sources
- publish-facing assets should preserve ASCII kebab-case naming

### 4. `output/`

- Reproducible artifact layer
- `output/blog/` contains generated publish artifacts
- `output/state/` contains derived machine-readable state summaries
- other lane outputs such as `output/instagram/`, `output/youtube/`, `output/webtoon/`, or `output/presentation/` must remain derived artifact layers too

## Channel Expansion Boundary

When new lanes are introduced, preserve the same boundary model:

- `wiki/` stays canonical
- `assets/{channel}/` stores source assets for that lane
- `output/{channel}/` stores derived artifacts for that lane
- each lane must declare its consumer and contract owner before it becomes official

Do not let a new lane bypass this model by writing canonical planning data into `output/` or ad hoc files.

## Publishing Contract

Wiki pages with `published: true` form the contract boundary to the downstream site.

Preserve:

- stable `slug`
- non-empty `description`
- downstream compatibility with `ai-survival-log-site/content/posts/YYYY-MM-DD-{slug}.mdx`
- site-facing image paths like `/images/{slug-or-series}/{file}.png`

For publishable pages with images:

- keep the upstream source asset in `assets/blog/`
- keep the downstream-served asset in `ai-survival-log-site/public/images/{slug-or-series}/`
- keep image naming stable and publish-safe

## Agent Surface Model

Top-level operating surfaces:

- `README.md` explains repository role and flow
- `AGENTS.md` defines cross-agent top-level rules
- `CLAUDE.md` inherits `AGENTS.md` and adds Claude-specific behavior
- `.codex/AGENTS.md` provides a compact Codex-safe operating view

Detailed rules should live outside those top-level files:

- architecture and boundary rules in `ARCHITECTURE.md`
- operational workflow in `docs/operating/operations.md`
- long-lived design decisions in `docs/adr/`

## Contract Severity

Use these policy levels when evaluating changes:

- `warn`: quality drift that does not break publish or runtime contracts yet
- `block`: source-of-truth, publish, path, frontmatter, or state-schema violations
- `escalate`: intentional contract change, schema break, or cross-repo rule divergence

## State Policy

Markdown remains canonical. JSON is allowed only as derived state.

Examples for `output/state/`:

- `wiki-index.json`
- `wiki-lint-summary.json`
- `publish-manifest.json`
- `agent-surface-summary.json`

Rules:

- generate from scripts, never hand-edit
- do not store secrets, tokens, env values, personal data, or absolute local paths
- if JSON conflicts with markdown, markdown wins
- keep tracked JSON stable, reviewable, and deterministic
- preserve field naming and ordering unless a deliberate schema change is approved
- require a documented review for breaking schema changes that affect automation or downstream consumers

## Design Constraints

- keep the wiki human-first and Obsidian-friendly
- do not redesign the repo around future RAG needs
- do not let artifact layers become authoring layers
- keep cross-repo contracts explicit and stable

## Related Docs

- [AGENTS.md](/Users/ms/workspace/claude/ai-survival-log/AGENTS.md)
- [CLAUDE.md](/Users/ms/workspace/claude/ai-survival-log/CLAUDE.md)
- [docs/operating/operations.md](/Users/ms/workspace/claude/ai-survival-log/docs/operating/operations.md)
- [docs/operating/channel-lanes.md](/Users/ms/workspace/claude/ai-survival-log/docs/operating/channel-lanes.md)
- [docs/publishing-contract.md](/Users/ms/workspace/claude/ai-survival-log/docs/publishing-contract.md)
- [wiki/projects/repo-structure-refactor.md](/Users/ms/workspace/claude/ai-survival-log/wiki/projects/repo-structure-refactor.md:1)
- [wiki/projects/harness-layering-and-json-derived-state.md](/Users/ms/workspace/claude/ai-survival-log/wiki/projects/harness-layering-and-json-derived-state.md:1)
