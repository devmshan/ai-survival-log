---
title: "Post-Compact Essential 섹션"
created: "2026-04-19"
updated: "2026-04-19"
type: concept
sources: ["[[sources/2026-04-19-cmds-system-files]]"]
tags: [documentation, agent-guide, claude, codex, context-management]
status: active
published: false
slug: ""
description: "긴 agent guide 문서에서 컨텍스트 압축 후에도 남아야 할 핵심 규칙만 별도 블록으로 재선언하는 패턴. CLAUDE.md, AGENTS.md, Codex guide 같은 상위 규칙 문서에 적용한다."
---

# Post-Compact Essential 섹션

긴 agent guide 문서에서 컨텍스트 압축이나 요약이 일어난 뒤에도 반드시 유지되어야 할 규칙만 따로 모아두는 문서 패턴. 보통 `## Essential (Post-Compact)` 같은 헤딩과 blockquote 또는 짧은 규칙 목록으로 구현한다.

## 왜 필요한가

- 상위 규칙 문서가 길어질수록 핵심 경계가 뒤쪽 세부 규칙에 묻히기 쉽다.
- 에이전트가 긴 문서를 요약해 기억할 때, 실제로 가장 중요한 규칙이 빠질 수 있다.
- 핵심 규칙을 별도 블록으로 재선언하면 "무엇이 절대 우선인지"를 명시적으로 드러낼 수 있다.

## 이 프로젝트에서 유지한 핵심 규칙

- `raw -> wiki -> output/blog -> ai-survival-log-site/content/posts` 흐름
- `raw/`는 불변 원본 계층이라는 점
- `wiki/`가 source of truth라는 점
- `published: true` 페이지는 안정적인 `slug`와 구체적인 `description`이 필요하다는 점
- publishable 페이지는 `docs/content-seo-guide.md`를 따른다는 점

## 적용 기준

- `CLAUDE.md`처럼 길고 규칙 밀도가 높은 문서에는 우선 적용 가치가 높다.
- `AGENTS.md`나 `.codex/AGENTS.md`처럼 더 짧은 문서라도, 여러 surface 사이에서 같은 핵심 경계를 반복 확인시켜야 할 때는 대칭적으로 넣을 수 있다.
- 세부 워크플로우 전체를 다시 복사하는 용도가 아니라, "이 문서를 다 잊어도 이것만은 남아야 한다"는 규칙을 추리는 용도로 써야 한다.

## 적용하지 않은 연계 패턴

이번 검토에서는 `STATIC/DYNAMIC` 주석 패턴은 보류했다. 현재 저장소에서는 문서 길이 대비 효과가 아직 명확하지 않았기 때문이다. 또한 `precedence`, `token-estimate` 같은 추가 메타데이터는 현재 운영 규모에 비해 과하다고 판단했다.

## 관련 페이지

- [[sources/2026-04-19-cmds-system-files]]
- [[concepts/claude-codex-collaboration]]
- [[concepts/llm-wiki-pattern]]
- [[projects/repo-structure-refactor]]
