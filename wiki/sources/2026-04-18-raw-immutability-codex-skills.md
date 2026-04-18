---
title: "raw 불변 규칙 강화와 Codex용 wiki skill 추가 세션"
created: "2026-04-18"
updated: "2026-04-18"
type: source
sources: []
tags: [raw-layer, immutability, codex, wiki-skill, claude-command]
status: active
published: false
slug: ""
description: ""
---

# raw 불변 규칙 강화와 Codex용 wiki skill 추가 세션

**원본:** `raw/journals/2026-04-18-raw-immutability-and-codex-wiki-skills-conversation-backup.md`
**날짜:** 2026-04-18
**성격:** `raw/` 폴더의 불변 원칙을 강하게 재문서화하고, Claude command에 대응하는 Codex용 wiki skill 5종을 추가한 세션

## 핵심 요약

`raw/` 불변 원칙은 이미 문서화되어 있었지만 "직접 수정하지 않는다" 수준이었다. 이를 "절대 직접 수정하지 않는다 — 요약, 재서술, 태깅, 해설은 모두 `wiki/`에서 한다 — 예외는 명시적으로 승인된 구조 마이그레이션뿐"으로 강화했다. 또한 Claude의 `/wiki:*` command에 대응하는 Codex용 skill 5종을 별도로 추가했다. 이 과정에서 Claude command와 Codex skill이 경쟁이 아니라 상호 보완 구조임을 확인했다.

## 추가된 Codex Skill 5종

| Skill | 역할 |
|-------|------|
| `wiki-ingest` | `raw/{type}` → `wiki/sources`, entities, concepts, syntheses |
| `wiki-query-answer` | `wiki/index.md` 기반 검색, `raw/{type}` 원본 확인, `syntheses/` 우선 검토 |
| `wiki-file-answer` | 답변/분석을 적절한 wiki 카테고리에 저장 |
| `wiki-lint` | 위키 무결성 검사, 경계 검토 |
| `wiki-publish` | `output/blog/` artifact 생성, downstream 호환성 유지 |

## Claude command vs Codex skill 정리

- **Claude command**: slash command UX가 강점 — 실행 절차형 작업에 적합 (`/wiki:ingest`, `/wiki:lint`, `/wiki:publish`)
- **Codex skill**: 문서 + 스크립트 + skill 중심 — 판단형/재사용형 지식에 적합
- **결론**: 두 surface는 대체 관계가 아니라 병행 구조가 맞다

## 강화된 raw 불변 원칙

```
raw/는 불변 원본 계층이다.
- 한 번 저장한 원본은 절대 직접 수정하지 않는다.
- 요약, 재서술, 태깅, 해설은 wiki/에서 한다.
- 예외는 구조 마이그레이션처럼 명시적으로 승인된 이동/이관 작업뿐이다.
```

## 관련 페이지

- [[concepts/claude-codex-collaboration]]
- [[sources/2026-04-18-wiki-surface-alignment]]
- [[projects/repo-structure-refactor]]
