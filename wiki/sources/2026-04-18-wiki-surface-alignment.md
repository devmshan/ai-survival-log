---
title: "Wiki 명령 surface와 운영 문서 정합성 보정 세션"
created: "2026-04-18"
updated: "2026-04-18"
type: source
sources: []
tags: [wiki, commands, operating-docs, syntheses, output-blog, assets-intake]
status: active
published: false
slug: ""
description: ""
---

# Wiki 명령 surface와 운영 문서 정합성 보정 세션

**원본:** `raw/journals/2026-04-18-wiki-surface-and-operating-docs-alignment-conversation-backup.md`
**날짜:** 2026-04-18
**성격:** 구조 변경 후 wiki 관련 명령/스킬과 운영 문서가 현재 프로젝트 구조에 맞게 정렬되도록 문서 surface를 재조정한 세션

## 핵심 요약

폴더 구조 변경과 Web Clipper 도입이 완료된 후, `/wiki:query`, `/wiki:file-answer`, `/wiki:lint`, `/wiki:publish`, `CLAUDE.md`가 이전 흐름을 전제하는 부분을 일괄 수정했다. 핵심은 `wiki/sources/`에 대응하는 `raw/{type}` 원본 확인 흐름, `wiki/syntheses/` 우선 검토 기준, `output/blog` artifact 계층, `assets/intake → assets/blog` 승격 원칙을 문서에 명확히 반영하는 것이었다.

## 수정된 파일

- `.claude/commands/wiki/query.md` — `raw/{type}` 원본 확인, `syntheses/` 우선 검토 추가
- `.claude/commands/wiki/file-answer.md` — `syntheses/` vs `projects/` 선택 기준 추가
- `.claude/commands/wiki/lint.md` — `synthesis` 타입, generated surface 제외 기준 추가
- `.claude/commands/wiki/publish.md` — `output/blog` 기본 경로, `assets/intake → assets/blog` 승격 원칙 추가
- `CLAUDE.md` — 전체 커맨드 워크플로우와 publish 파이프라인 재서술

## 핵심 원칙

- **문서 정합성**: 구조 변경 후 명령 surface가 따라오지 않으면 agent는 오래된 모델로 행동한다
- **syntheses의 지위**: 단순 보조 카테고리가 아니라 비교/통합/판단 문서의 핵심 저장 위치
- **이중 artifact 경계**: `output/blog/` = publish 기본 산출물, `ai-survival-log-site/content/posts/` = downstream 동기화 대상

## 관련 페이지

- [[sources/2026-04-18-raw-immutability-codex-skills]]
- [[projects/repo-structure-refactor]]
- [[concepts/assets-intake-pattern]]
