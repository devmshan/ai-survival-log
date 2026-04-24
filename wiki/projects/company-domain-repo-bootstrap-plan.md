---
title: "회사 도메인 저장소 bootstrap 계획"
created: "2026-04-24"
updated: "2026-04-24"
type: project
sources: []
tags: [project, company, bootstrap, repo, scaffold, harness]
status: active
published: false
slug: ""
description: "company-wiki, company-assistant-ops, shared-agent-harness를 실제 생성할 때 어떤 초기 파일 세트와 폴더 구조를 만들지 정리한 bootstrap 계획."
---

# 회사 도메인 저장소 bootstrap 계획

이 문서는 실제 폴더 생성 시 만들 초기 파일 세트와 최소 디렉토리 구조를 정의한다.

목표:

- 설계 문서를 바로 반영할 수 있는 최소 실행 단위를 만든다
- 너무 많은 파일을 한 번에 생성하지 않는다
- 이후 `materialize`와 `migration`이 쉬운 구조로 시작한다

## 1. `company-wiki` 초기 파일 세트

루트 문서:

- `README.md`
- `AGENTS.md`
- `CLAUDE.md`
- `ARCHITECTURE.md`

초기 디렉토리:

- `inbox/`
- `meetings/`
- `projects/`
- `planning/`
- `reviews/`
- `testing/`
- `concepts/`
- `entities/`
- `templates/`
- `archive/`

Phase 1 템플릿:

- `templates/meeting-note.md`
- `templates/cross-review-report.md`
- `templates/test-plan.md`

보조 파일:

- 각 비어 있는 디렉토리에 `.gitkeep`

## 2. `company-assistant-ops` 초기 파일 세트

루트 문서:

- `README.md`
- `AGENTS.md`
- `CLAUDE.md`
- `ARCHITECTURE.md`

초기 디렉토리:

- `docs/operating/`
- `docs/templates/`
- `docs/adr/`
- `inbox/`
- `actions/`
- `approvals/`
- `audit/`
- `adapters/gmail/`
- `adapters/calendar/`
- `adapters/sheets/`
- `state/`
- `scripts/`
- `tests/`

Phase 1 문서:

- `docs/operating/operations.md`
- `docs/operating/approval-matrix.md`
- `docs/operating/audit-policy.md`
- `docs/operating/handoff-policy.md`
- `docs/operating/credential-policy.md`

Phase 1 템플릿:

- `docs/templates/approval-record.md`
- `docs/templates/execution-report.md`

보조 파일:

- `adapters/gmail/README.md`
- `adapters/calendar/README.md`
- `adapters/sheets/README.md`
- 필요한 디렉토리에 `.gitkeep`

## 3. `shared-agent-harness` 초기 파일 세트

루트 문서:

- `README.md`
- `AGENTS.md`
- `CLAUDE.md`
- `ARCHITECTURE.md`

초기 디렉토리:

- `docs/operating/`
- `docs/templates/`
- `docs/adr/`
- `roles/`
- `lanes/`
- `skills/planning/`
- `skills/review/`
- `skills/engineering/`
- `skills/research/`
- `commands/planning/`
- `commands/review/`
- `commands/engineering/`
- `commands/research/`
- `scripts/`
- `tests/`
- `examples/`

Phase 1 운영 문서:

- `docs/operating/operations.md`
- `docs/operating/domain-context-policy.md`
- `docs/operating/approval-matrix.md`
- `docs/operating/validation-matrix.md`
- `docs/operating/cross-validation-policy.md`

Phase 1 role/lane 문서:

- `roles/planning-agent.md`
- `roles/research-agent.md`
- `roles/engineering-agent.md`
- `roles/review-agent.md`
- `lanes/planning-lane.md`
- `lanes/research-lane.md`
- `lanes/engineering-lane.md`
- `lanes/review-lane.md`

Phase 1 템플릿:

- `docs/templates/planning-brief.md`
- `docs/templates/review-checklist.md`
- `docs/templates/cross-review-report.md`
- `docs/templates/meeting-followup.md`
- `docs/templates/assistant-action-report.md`
- `docs/templates/workflow-prd.md`

## 4. bootstrap 원칙

- 실제 credential은 넣지 않는다
- 도메인별 source-of-truth 원문은 넣지 않는다
- 초기 파일은 `reference-first`로 작성하고, 상세 source는 현재 `ai-survival-log/wiki/projects/` 설계 문서를 참조하게 한다
- `git init`은 현재 단계에서 필수가 아니다

## 4-1. 회사 프로젝트 개시 전 필수 게이트

`company-wiki`, `company-assistant-ops`는 실제 업무를 시작하기 전에 아래 3단계를 반드시 완료해야 한다.

1. `git init`
2. `~/.gitconfig` `includeIf`와 `~/.gitconfig-company`로 회사 git identity 연결
3. `.git/hooks/pre-commit`에 최소 2개 검사 연결
   - `user.email`이 회사 메일인지 확인
   - staged diff에 token/secret 패턴이 없는지 확인

이유:

- 폴더 분리만으로는 도메인 격리가 완성되지 않는다
- 실제 회사 작업은 commit identity와 secret 방지 장치가 있어야 시작할 수 있다

강제 원칙:

- 이 게이트 완료 전에는 회사 프로젝트를 `bootstrapped but not operational` 상태로 본다
- 실제 회사 note 작성, commit, external write workflow 개시는 금지한다

## 5. 생성 순서

1. `company-wiki`
2. `company-assistant-ops`
3. `shared-agent-harness`

이유:

- 회사 도메인의 authoring / execution surface를 먼저 만들고
- 공용 harness는 그 다음에 이주 기준까지 고려해 생성하는 편이 정합적이다

## 다음 단계

- 실제 폴더와 초기 파일 생성
- `shared-agent-harness` 이주 대상 문서 목록 정리
- 생성 완료 후 bootstrap 결과 검수

관련 이주 목록:

- [[projects/shared-agent-harness-migration-list]]

현재 반영:

- `~/workspace/claude/company-wiki` 생성 완료
- `~/workspace/claude/company-assistant-ops` 생성 완료
- `~/workspace/claude/shared-agent-harness` 생성 완료

보류:

- 각 저장소 `git init`
- 회사 git identity 연결
- 실제 credential/OAuth 연결

운영상 의미:

- 현재 세 저장소는 생성만 완료된 상태다
- `company-wiki`, `company-assistant-ops`는 아직 `operational` 상태가 아니다

현재 이주 시작:

- `shared-agent-harness/README.md`
- `shared-agent-harness/AGENTS.md`
- `shared-agent-harness`의 `ARCHITECTURE.md`
- `shared-agent-harness/docs/operating/operations.md`
- `shared-agent-harness/docs/operating/cross-validation-policy.md`
- `shared-agent-harness/docs/operating/domain-context-policy.md`
- `shared-agent-harness/docs/operating/approval-matrix.md`
- `shared-agent-harness/docs/operating/validation-matrix.md`
- `shared-agent-harness/docs/operating/adoption-strategy.md`
- `shared-agent-harness/docs/operating/stop-conditions.md`
- `shared-agent-harness/docs/operating/workflow-gates.md`
- `shared-agent-harness/lanes/planning-lane.md`
- `shared-agent-harness/roles/planning-agent.md`
- `shared-agent-harness/lanes/review-lane.md`
- `shared-agent-harness/roles/review-agent.md`
- `shared-agent-harness/lanes/engineering-lane.md`
- `shared-agent-harness/roles/engineering-agent.md`
- `shared-agent-harness/lanes/research-lane.md`
- `shared-agent-harness/roles/research-agent.md`
- `shared-agent-harness/docs/templates/review-checklist.md`
- `shared-agent-harness/docs/templates/cross-review-report.md`
- `shared-agent-harness/docs/templates/assistant-action-report.md`
- `shared-agent-harness/commands/*`
- `shared-agent-harness/skills/*`
- `shared-agent-harness/docs/adr/*`

## 관련 페이지

- [[projects/company-domain-template-materialization-plan]]
- [[projects/shared-agent-harness-internal-structure]]
- [[projects/company-wiki-internal-structure]]
- [[projects/company-assistant-ops-internal-structure]]
