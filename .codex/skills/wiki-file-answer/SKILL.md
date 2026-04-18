---
name: wiki-file-answer
description: Turn a useful answer or analysis into a durable wiki page in entities, concepts, topics, or projects, with frontmatter, wikilinks, related pages, and index/log updates for this repository.
---

# Wiki File Answer

Use this skill when a conversation result should become a durable wiki page.

## Category Rules

- `entities/`: named tools, companies, people, products
- `concepts/`: abstract ideas, patterns, definitions
- `topics/`: multi-concept explainers or hubs
- `projects/`: plans, execution docs, operational changes

## Workflow

1. Pick the right category.
2. Create a kebab-case filename.
3. Add required frontmatter from `CLAUDE.md`.
4. Write the page in wiki style with `## 관련 페이지`.
5. Add backlinks where obviously needed.
6. Run `python3 scripts/wiki sync`.

## Rules

- Prefer `projects/` when the output changes how the repo is operated.
