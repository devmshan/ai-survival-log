---
title: "Wiki 자동화 패턴"
created: "2026-04-22"
updated: "2026-04-22"
type: concept
sources: ["[[sources/2026-04-22-project-state-management-analysis]]"]
tags: [wiki-automation, hooks, claude-code, state-management, python, wiki]
status: active
published: false
slug: ""
description: ""
---

# Wiki 자동화 패턴

`ai-survival-log` 프로젝트에서 채택한 위키 상태 관리 자동화 구조. Claude Code 훅과 Python 스크립트로 파일 변경 시마다 인덱스·태그·무결성을 자동으로 유지한다.

## 핵심 원칙

- 상태는 **JSON이 아닌 마크다운**으로 관리 (`index.md`, `log.md`)
- 파일 변경 시 **즉시 자동 재생성** — 인덱스가 항상 최신 상태
- **자동 커밋 없음** — 커밋은 사용자가 명시적으로 요청할 때만

## Claude Code Hooks

`.claude/settings.json`에 정의된 훅 2가지:

```json
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "Write|Edit",
      "hooks": [{"type": "command", "command": "scripts/wiki sync"}]
    }],
    "Stop": [{
      "matcher": "",
      "hooks": [{"type": "command", "command": "scripts/wiki lint --summary || true"}]
    }]
  }
}
```

- `Write` 또는 `Edit` 툴 실행 후 → `wiki sync` 자동 실행
- 세션 종료(`Stop`) 시 → `wiki lint --summary` 자동 실행

## scripts/wiki_lib.py 명령

| 명령 | 역할 | 트리거 |
|------|------|--------|
| `wiki sync` | `index.md` + `tags/` 재생성 | PostToolUse 훅 (자동) |
| `wiki lint` | 깨진 링크·고아 페이지·frontmatter 검사 | Stop 훅 (자동) / 수동 |
| `wiki tags` | `tags/` 단독 재생성 | 수동 |
| `wiki publish` | wiki → downstream MDX 변환 | `/wiki:publish` 명령 시 |

## 상태 추적 파일

### `wiki/index.md`

전체 페이지 카탈로그. 벡터 DB 없이 이 파일이 검색 인덱스 역할.
`wiki sync` 실행 시마다 자동 재생성.

### `wiki/log.md`

모든 위키 조작의 시간순 기록. 인제스트·쿼리·publish 등 조작 이력을 역순으로 누적.

## GitHub Actions

`.github/workflows/pr-summary.yml`:
PR 생성/업데이트 시 `scripts/pr-summary.mjs`로 변경 요약을 자동 생성해 PR 코멘트로 달아줌.

## 테스트

`scripts/wiki_lib.py`에 대한 pytest 기반 테스트 (`tests/test_wiki_lib.py`, 395줄).
`scan_pages`, `cmd_sync`, `cmd_lint`, `cmd_publish` 핵심 함수 전체 커버.
자동화 로직 변경 시 TDD 적용 대상.

## 관련 페이지

- [[concepts/llm-wiki-pattern]] — 이 자동화가 기반하는 LLM Wiki 패턴
- [[concepts/engineering-guardrails]] — 자동화 코드에 적용되는 TDD 범위 정의
- [[entities/claude-code]] — 훅과 커맨드를 실행하는 도구
- [[sources/2026-04-22-project-state-management-analysis]] — 이 패턴을 분석한 원본 기록
