# AI Survival Log — Claude Surface

@AGENTS.md

## Essential (Post-Compact)

> 컨텍스트 압축 후에도 반드시 유지해야 할 핵심 규칙:
> 1. 저장소 기본 흐름은 `raw -> wiki -> output/blog -> ai-survival-log-site/content/posts` 이다.
> 2. `raw/`는 불변 원본 계층이다. 요약, 해설, 태깅, 재작성은 `wiki/`에서 한다.
> 3. `published: true` 페이지는 `slug`와 `description`이 반드시 채워져 있어야 한다.
> 4. publishable 페이지는 `docs/content-seo-guide.md`를 따라 제목, description, 도입부를 구체적으로 쓴다.
> 5. publishable 페이지의 이미지는 upstream `assets/blog/`, downstream `ai-survival-log-site/public/images/{slug-or-series}/` 경로 규칙을 지킨다.
> 6. 위키는 human-first, markdown-first, Obsidian-friendly 구조를 유지하고, future RAG는 파생 계층으로 다룬다.

## Claude Local Operating Notes

- 이 저장소는 `ai-survival-log-site`의 상위 authoring/source-of-truth 저장소다.
- 기본 흐름은 `raw -> wiki -> output/blog -> ai-survival-log-site/content/posts` 이다.
- 발산 lane는 일반 블로그, 책 스터디 시리즈, 인스타그램 캐러셀까지 포함한다.
- 구조 변경, publish 계약 변경, 로컬 agent surface 변경 전에는 짧은 계획을 먼저 작성한다.
- publishable wiki 페이지를 쓰거나 고칠 때는 `docs/content-seo-guide.md`를 따라 제목, 설명, 도입부, 시리즈 구조가 검색 우선순위도 반영하도록 한다.
- 작업 완료 전에는 변경 범위에 맞는 검증을 명시적으로 수행한다.
- `README.md`, `AGENTS.md`, `.claude/*`, `.codex/*`, publish 관련 문서는 같은 저장소 역할을 설명해야 한다.

## Local Command Surface

- `/journals:backup` — 현재 대화를 `raw/journals/`에 백업 파일로 저장
- `/wiki:ingest` — source를 위키에 흡수
- `/wiki:query` — 위키 검색과 인용 답변
- `/wiki:file-answer` — 답변을 위키 페이지로 저장
- `/wiki:lint` — 위키 무결성 검사
- `/wiki:publish` — downstream site용 MDX 출력 준비
- `/content:book-study-blog` — 책 스터디 대화에서 시리즈형 블로그 lane 연결
- `/content:blog-to-instagram` — 블로그 포스트에서 인스타그램 lane 연결
- `/content:review-blog-draft` — `/wiki:publish` 전 블로그 초안 글쓰기 품질 리뷰

## Detailed References

- 아키텍처와 계층 경계: [ARCHITECTURE.md](/Users/ms/workspace/claude/ai-survival-log/ARCHITECTURE.md)
- 운영 절차와 검증 루프: [docs/operating/operations.md](/Users/ms/workspace/claude/ai-survival-log/docs/operating/operations.md)
- lane 확장 규칙: [docs/operating/channel-lanes.md](/Users/ms/workspace/claude/ai-survival-log/docs/operating/channel-lanes.md)
- 위키 스키마와 구조: [docs/operating/wiki-schema.md](/Users/ms/workspace/claude/ai-survival-log/docs/operating/wiki-schema.md)
- 위키 커맨드 워크플로우: [docs/operating/wiki-commands.md](/Users/ms/workspace/claude/ai-survival-log/docs/operating/wiki-commands.md)
- publish 계약: [docs/publishing-contract.md](/Users/ms/workspace/claude/ai-survival-log/docs/publishing-contract.md)
- 장기 결정: [docs/adr/0001-markdown-source-of-truth.md](/Users/ms/workspace/claude/ai-survival-log/docs/adr/0001-markdown-source-of-truth.md), [docs/adr/0002-json-derived-state-only.md](/Users/ms/workspace/claude/ai-survival-log/docs/adr/0002-json-derived-state-only.md), [docs/adr/0003-harness-layering-for-upstream-repo.md](/Users/ms/workspace/claude/ai-survival-log/docs/adr/0003-harness-layering-for-upstream-repo.md), [docs/adr/0004-new-channels-remain-derived-from-the-wiki.md](/Users/ms/workspace/claude/ai-survival-log/docs/adr/0004-new-channels-remain-derived-from-the-wiki.md)

이 파일은 Claude 작업면 메모와 명령 surface를 우선 다룬다. 위키 스키마, frontmatter, wikilink, `index.md`, `log.md`, `/wiki:*` 세부 워크플로우의 원문은 상세 문서를 우선한다.
