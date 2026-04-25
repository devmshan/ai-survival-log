---
title: "Workspace 보안 경계 정책"
created: "2026-04-24"
updated: "2026-04-24"
type: project
sources: []
tags: [project, security, workspace, operations, harness, company, personal]
status: active
published: false
slug: ""
description: "개인/회사 이중 도메인 운영 시 file system, git identity, credentials, harness context 4축 보안 경계를 고정하는 정책 문서."
---

# Workspace 보안 경계 정책

## Source Status

- 이 문서는 detached workspace 분리 시점의 보안 경계 원칙과 필수 게이트를 남기는 `history retained here` 문서다.
- 현재 detached `operational source`는 역할별로 나뉜다.
  - 공용 경계/실행 규칙: `shared-agent-harness`
  - 회사 authoring gate: `company-wiki`
  - 회사 execution gate: `company-assistant-ops`
- 따라서 이 문서는 보안 정책의 원문 rationale과 초기 강제 조건을 추적하는 문서로 읽고, 실제 운영 시에는 detached repo 내부 문서를 먼저 본다.

이 문서는 `~/workspace/claude/` 이하 개인/회사 이중 도메인 운영 시 4축 보안 경계를 고정한다.

핵심 원칙: **폴더 분리만으로 도메인 격리가 완성되지 않는다.** File system, Identity, Credentials, Harness context 4축이 모두 분리되어야 한다.

## 1. File System 경계

폴더 배치:

```text
~/workspace/claude/
  ai-survival-log          → 개인 upstream (raw/wiki/output)
  ai-survival-log-site     → 개인 downstream (presentation)
  company-wiki             → 회사 wiki (회의록/기획/검수/테스트)
  company-assistant-ops    → 회사 assistant surface (Gmail/Calendar/Sheets)
  shared-agent-harness     → 공용 role/lane/skill/workflow
```

금지:
- 개인 저장소에 회사 데이터(회의록/일정/검토/테스트/기획) 저장
- 회사 저장소에 개인 콘텐츠(블로그/웹툰/유튜브) 저장
- `shared-agent-harness`에 도메인 특정 데이터 원본 저장

## 2. Git Identity 경계

원칙: 도메인별로 다른 `user.email`을 사용한다.

프로젝트 개시 전 필수:

- `company-wiki`, `company-assistant-ops`는 실제 업무를 시작하기 전에 반드시 다음 3단계를 완료한다
  1. `git init`
  2. `~/.gitconfig` `includeIf` + `~/.gitconfig-company` 설정
  3. `.git/hooks/pre-commit`에 `user.email` 검사와 secret scan 연결

이 3단계가 끝나기 전에는:

- 회사 데이터 authoring 시작 금지
- 회사 저장소 commit 금지
- 회사 assistant write workflow 시작 금지

`~/.gitconfig`에 `includeIf` 패턴 적용:

```ini
[user]
  email = bestfriend1562@gmail.com    # 기본 (개인)
  name = Minsung Han

[includeIf "gitdir:~/workspace/claude/company-wiki/"]
  path = ~/.gitconfig-company

[includeIf "gitdir:~/workspace/claude/company-assistant-ops/"]
  path = ~/.gitconfig-company
```

`~/.gitconfig-company`:

```ini
[user]
  email = {회사_email}
  name = Minsung Han
```

금지:
- 개인 email로 회사 저장소에 commit
- 회사 email로 개인 저장소에 commit
- 회사 저장소에 최초 commit 전 `git config user.email` 미확인

감지 방법:
- 회사 저장소 `.git/hooks/pre-commit`에서 `user.email` 패턴 검사 (다음 단계 예약)

## 3. Credentials 경계

원칙: OAuth token, API key, secrets는 저장소 밖에만 둔다.

허용 저장 위치:
- macOS Keychain (기본 권장)
- 1Password 같은 암호 관리자
- `~/.config/{service}/` (git-ignored)

저장소에 허용:
- `.env.example` (변수명만, 값은 없음)
- keychain reference key 이름
- OAuth redirect URI 같은 비밀이 아닌 설정값

금지:
- 저장소 안 `.env`에 실제 token/key 값 commit
- `shared-agent-harness`에 도메인 특정 credential 저장
- 개인 저장소 `.env`에 회사 credential 기입

`company-assistant-ops` 추가 원칙:
- Gmail/Calendar/Sheets OAuth token은 macOS Keychain에만 저장
- token 값은 runtime 주입, commit 금지
- Phase D (High-risk write) 실행 전 항상 저장된 token으로 검증

감지 방법:
- pre-commit hook에서 `.env`의 token 패턴 secret scan (다음 단계 예약)

## 4. Harness Context 경계

원칙: `~/.claude/`는 전역이다. 도메인 고유 정보가 전역 설정에 스며들지 않도록 관리한다.

### 전역 (`~/.claude/`) 허용

허용:
- 일반 운영 원칙 (coding style, git workflow 등)
- 도메인에 무관한 공용 규칙
- 사용자 일반 profile (이름, 날짜 등)

금지:
- 회사명, 회사 계정 정보를 `~/.claude/CLAUDE.md`에 기입
- 회사 도메인 고유 workflow 규칙을 전역 rules에 추가
- 회사 저장소 경로나 내부 시스템 이름을 전역 memory에 hard-code

### Project memory 경계

경로: `~/.claude/projects/-Users-ms-workspace-claude-{repo}/memory/`

원칙:
- 각 저장소의 project memory는 해당 도메인에 한정된 정보만 저장
- 개인 도메인 memory(`ai-survival-log/`)에 회사 정보(회사명, 내부 일정, 업무 세부사항) 저장 금지
- 회사 도메인 memory에 개인 콘텐츠 context 저장 금지

감지 방법:
- 분기별 각 저장소 `memory/MEMORY.md` 육안 검사

### `shared-agent-harness` harness context

- CLAUDE.md/AGENTS.md는 도메인 중립적으로 작성
- 개인/회사 저장소 경로를 shared 설정에 hard-code 금지
- shared skill/workflow는 실행 시 도메인 컨텍스트를 인자로 받는 구조로 설계

## 위반 감지 요약

| 축 | 현재 감지 방법 | 다음 단계 예약 |
|------|------|------|
| File system | `git status` + 육안 | cross-domain diff scan script |
| Identity | commit 전 수동 확인 | pre-commit hook (user.email 패턴) |
| Credentials | `.env.example` 규칙 + 육안 | pre-commit hook (secret scan) |
| Harness context | 분기별 memory 육안 검사 | 공용 audit script (`shared-agent-harness`) |

## 관련 페이지

- [[projects/dual-domain-agent-operating-model]]
- [[projects/workspace-folder-structure-review-sheet]]
- [[projects/immediate-agent-operating-structure]]
- [[projects/assistant-ops-lane-execution-draft]]
