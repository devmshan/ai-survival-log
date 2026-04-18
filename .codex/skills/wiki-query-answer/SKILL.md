---
name: wiki-query-answer
description: Answer repository questions from wiki knowledge by searching wiki/index.md, relevant wiki pages, and when needed the raw source behind wiki/sources, while citing wiki pages and surfacing when information is missing.
---

# Wiki Query Answer

Use this skill when the user asks a knowledge question grounded in this repository.

## Workflow

1. Start with `wiki/index.md`.
2. Read the most relevant pages in `wiki/`.
3. If needed, follow `wiki/sources/` to the corresponding `raw/{type}` source.
4. Answer with explicit page citations such as `[[concepts/...]]` or file links when useful.

## Rules

- Do not invent facts not present in the wiki or raw source.
- If the wiki does not contain the answer, say so directly.
- If new outside material is needed, recommend ingesting it first.
