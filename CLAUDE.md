# AI Survival Log — Claude Adapter Surface

@AGENTS.md

## Essential (Post-Compact)

> 컨텍스트 압축 후에도 반드시 유지해야 할 핵심 규칙:
> 1. 저장소 기본 흐름은 `raw -> wiki -> output/blog -> ai-survival-log-site/content/posts` 이다.
> 2. `raw/`는 불변 원본 계층이고, 요약, 해설, 태깅, 재작성은 `wiki/`에서 한다.
> 3. `wiki/`가 source of truth이고 `output/`은 재생성 가능한 artifact 계층이다.
> 4. `published: true` 페이지는 `slug`와 `description`이 반드시 채워져 있어야 한다.
> 5. publishable 페이지는 `docs/content-seo-guide.md`를 따른다.
> 6. 공식 검수 게이트는 가능한 한 서로 다른 surface 또는 review path를 쓰는 `2-agent cross-validation`을 따른다.
> 7. 위키는 human-first, markdown-first, Obsidian-friendly 구조를 유지하고 future RAG는 파생 계층으로 다룬다.

## Adapter Role

- 이 파일은 Claude용 adapter surface다.
- top-level repository rules는 `AGENTS.md`를 우선 따른다.
- 구조 경계와 운영 규칙의 원문은 `ARCHITECTURE.md`와 `docs/operating/*`를 우선한다.
- 위키 스키마와 로컬 command surface는 아래 reference 문서로 분리돼 있다.

## Claude Local Operating Notes

- Treat this repository as the upstream authoring and source-of-truth layer, not the final presentation layer.
- Keep compatibility with the downstream site contract when changing publishable content.
- Before changing structure, publish rules, or local agent surface, write or update a short plan first.
- Before completion, verify the changed scope explicitly.
- Keep `README.md`, `AGENTS.md`, `CLAUDE.md`, `.codex/*`, and publish-related docs aligned.

## Reference Documents

### Core Rules

- [AGENTS.md](/Users/ms/workspace/claude/ai-survival-log/AGENTS.md)
- [ARCHITECTURE.md](/Users/ms/workspace/claude/ai-survival-log/ARCHITECTURE.md)
- [docs/operating/operations.md](/Users/ms/workspace/claude/ai-survival-log/docs/operating/operations.md)
- [docs/operating/validation-matrix.md](/Users/ms/workspace/claude/ai-survival-log/docs/operating/validation-matrix.md)
- [docs/operating/channel-lanes.md](/Users/ms/workspace/claude/ai-survival-log/docs/operating/channel-lanes.md)
- [docs/publishing-contract.md](/Users/ms/workspace/claude/ai-survival-log/docs/publishing-contract.md)
- [docs/content-seo-guide.md](/Users/ms/workspace/claude/ai-survival-log/docs/content-seo-guide.md)
- [docs/blog-draft-review-rules.md](/Users/ms/workspace/claude/ai-survival-log/docs/blog-draft-review-rules.md)

### Reference Split

- [docs/reference/wiki-schema.md](/Users/ms/workspace/claude/ai-survival-log/docs/reference/wiki-schema.md)
- [docs/reference/local-command-surface.md](/Users/ms/workspace/claude/ai-survival-log/docs/reference/local-command-surface.md)

### ADRs

- [docs/adr/0001-markdown-source-of-truth.md](/Users/ms/workspace/claude/ai-survival-log/docs/adr/0001-markdown-source-of-truth.md)
- [docs/adr/0002-json-derived-state-only.md](/Users/ms/workspace/claude/ai-survival-log/docs/adr/0002-json-derived-state-only.md)
- [docs/adr/0003-harness-layering-for-upstream-repo.md](/Users/ms/workspace/claude/ai-survival-log/docs/adr/0003-harness-layering-for-upstream-repo.md)
- [docs/adr/0004-new-channels-remain-derived-from-the-wiki.md](/Users/ms/workspace/claude/ai-survival-log/docs/adr/0004-new-channels-remain-derived-from-the-wiki.md)
