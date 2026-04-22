---
title: "프로젝트 상태 관리 및 TDD 규칙 분석 (2026-04-22)"
created: "2026-04-22"
updated: "2026-04-22"
type: source
sources: []
tags: [wiki-automation, state-management, tdd, claude-code, hooks, engineering-guardrails]
status: active
published: false
slug: ""
description: ""
---

# 프로젝트 상태 관리 및 TDD 규칙 분석 (2026-04-22)

Claude Code 대화 세션에서 `ai-survival-log` 프로젝트의 상태 관리 구조와 TDD 규칙 현황을 분석한 기록.

## 핵심 요약

- 상태는 JSON이 아닌 마크다운(`index.md`, `log.md`)으로 관리
- 파일 변경 시마다 `wiki sync` 훅이 자동 실행되어 인덱스를 재생성
- 자동 커밋은 없음 — 사용자 명시 요청 시에만 실행
- TDD는 글로벌 MANDATORY 규칙이나, 이 프로젝트에서는 Python 자동화 코드에만 실질 적용
- `.codex/AGENTS.md`에 Engineering Guardrails 섹션이 추가됨 (TDD 범위 명확화)

## 상태 관리 구조

### Claude Code Hooks (`.claude/settings.json`)

| 이벤트 | 실행 명령 |
|--------|----------|
| `PostToolUse` (Write\|Edit) | `scripts/wiki sync` |
| `Stop` (세션 종료) | `scripts/wiki lint --summary` |

### `scripts/wiki_lib.py` 자동화 명령

| 명령 | 역할 |
|------|------|
| `wiki sync` | `index.md` + `tags/` 재생성 |
| `wiki lint` | 깨진 링크, 고아 페이지, frontmatter 무결성 검사 |
| `wiki tags` | `tags/` 재생성 |
| `wiki publish` | wiki → downstream MDX 변환 |

### 상태 추적 파일

- `wiki/index.md` — 전체 페이지 카탈로그 (벡터 DB 대용 검색 인덱스)
- `wiki/log.md` — 모든 위키 조작의 시간순 기록
- JSON 상태 파일 없음

### GitHub Actions

PR 생성 시 `scripts/pr-summary.mjs`로 변경 요약을 자동 생성해 PR 코멘트로 추가.

## TDD 규칙 현황

### 글로벌 규칙 (`~/.claude/rules/testing.md`)

Red → Green → Refactor 사이클 MANDATORY, 80% 커버리지 요구.

### 프로젝트 적용 범위

| 대상 | TDD 적용 여부 |
|------|--------------|
| `scripts/wiki_lib.py` (Python 자동화) | 적용 (`tests/test_wiki_lib.py` 395줄) |
| 위키 콘텐츠(마크다운) | 해당 없음 |
| raw 소스 인제스트 | 해당 없음 |
| 메타데이터 편집 | 해당 없음 |

## Engineering Guardrails 추가 (.codex/AGENTS.md)

이 분석 이후 `.codex/AGENTS.md`에 다음 가드레일이 추가됨:

- 구현 전 기존 코드/라이브러리 확인
- 코드 변경 후 버그·보안·회귀 검토
- automation, parsers, transformers, publish/lint/sync에는 테스트 우선 적용
- 위키 콘텐츠·raw 소스·메타데이터 편집에는 TDD 강제 안 함
- 시크릿 하드코딩 금지, 외부 입력 검증, 민감 정보 노출 방지
- TypeScript: 공개 API 타입 유지, `any` 금지, `console.log` 금지

## 관련 페이지

- [[concepts/wiki-automation]] — wiki sync 훅과 자동화 스크립트 패턴
- [[concepts/engineering-guardrails]] — 프로젝트 엔지니어링 가드레일
- [[concepts/llm-wiki-pattern]] — LLM Wiki 패턴 개요
- [[entities/claude-code]] — 훅과 커맨드를 실행하는 도구
