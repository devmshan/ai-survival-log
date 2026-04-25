---
title: "shared-agent-harness 이주 대상 문서 목록"
created: "2026-04-24"
updated: "2026-04-25"
type: project
sources: []
tags: [project, harness, migration, documents, shared]
status: active
published: false
slug: ""
description: "shared-agent-harness 저장소 생성 후 ai-survival-log/wiki/projects 에서 옮길 설계 문서 후보와 이주 우선순위를 정리한 목록."
---

# shared-agent-harness 이주 대상 문서 목록

## Source Status

- 이 문서는 `shared-agent-harness` 승격 과정의 이주 메모와 진행 추적을 남기는 `history retained here` 문서다.
- 현재 공용 detached `operational source`는 `shared-agent-harness` 저장소 자체를 우선 기준으로 본다.
- 따라서 이 문서는 “무엇을 왜 옮겼는가”를 추적하는 migration ledger로 읽고, 현재 운영 규칙은 detached repo 문서를 기준으로 판단한다.

이 문서는 `shared-agent-harness` 저장소 생성 후 현재 `ai-survival-log/wiki/projects/`에서 옮길 설계 문서 후보를 정리한다.

핵심 원칙:

- 개인 도메인 전용 문서와 회사 도메인 전용 문서는 옮기지 않는다
- 공용 role/lane/skill/workflow/validation/audit 규칙만 옮긴다
- 이주 전 source-of-truth는 여전히 현재 저장소의 위키 문서다

## 1차 이주 후보

- [[projects/shared-agent-harness-internal-structure]]
- [[projects/immediate-agent-operating-structure]]
- [[projects/planning-lane-execution-draft]]
- [[projects/managed-agent-harness-draft]]

이유:

- 공용 lane/role/harness 구조를 직접 다룬다

현재 반영:

- `shared-agent-harness/README.md`
- `shared-agent-harness/AGENTS.md`
- `shared-agent-harness/ARCHITECTURE.md`
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
- `shared-agent-harness/commands/planning/new-brief.md`
- `shared-agent-harness/commands/review/run-cross-validation.md`
- `shared-agent-harness/commands/engineering/execute-validated-task.md`
- `shared-agent-harness/commands/research/collect-sources.md`
- `shared-agent-harness/skills/planning/README.md`
- `shared-agent-harness/skills/review/README.md`
- `shared-agent-harness/skills/engineering/README.md`
- `shared-agent-harness/skills/research/README.md`
- `shared-agent-harness/docs/adr/0001-shared-harness-separates-rules-from-domain-data.md`
- `shared-agent-harness/docs/adr/0002-cross-validation-prefers-surface-variance.md`
- `shared-agent-harness/docs/adr/0003-domain-context-must-be-explicit.md`
- `shared-agent-harness/docs/templates/source-bundle.md`
- `shared-agent-harness/docs/templates/execution-record.md`
- `shared-agent-harness/scripts/harness.py`
- `shared-agent-harness/tests/test_harness.py`

메모:

- 현재는 `placeholder -> shared summary` 단계를 넘어, 공용 운영 원칙의 detached operational source 승격 단계까지 반영됐다
- `shared-agent-harness`는 이제 `safe artifact generation` 범위의 최소 executable surface를 가진다
- 현재 공용 운영 판단은 `shared-agent-harness`의 `README`, `ARCHITECTURE`, 핵심 `docs/operating/*`, `lanes/*`, `roles/*`를 우선 기준으로 본다

## 2차 분리 검토 후보

- [[projects/dual-domain-agent-operating-model]]

메모:

- 이 문서는 공용 원칙과 도메인 전용 경계가 섞여 있다
- 전체 이주보다 `공용 부분 분리`가 더 적절할 수 있다

## 회사 도메인 전용으로 남길 것

- [[projects/company-wiki-internal-structure]]
- [[projects/company-assistant-ops-internal-structure]]
- [[projects/company-domain-template-set]]
- [[projects/company-domain-review-checklist-operations]]
- [[projects/company-assistant-dry-run-scenarios]]
- [[projects/company-domain-template-materialization-plan]]
- [[projects/company-assistant-approval-matrix]]

이유:

- 회사 도메인 전용 surface와 policy를 직접 다룬다

## 개인 도메인 전용으로 남길 것

- `ai-survival-log` publish / blog / site 관련 설계 문서
- `도서관과 교수님의 뇌` 등 글쓰기/콘텐츠 계획

## 이주 방식

1. `shared-agent-harness`에 대응 문서 생성
2. 현재 위키 문서 내용을 요약 또는 분할 이주
3. 현재 문서에는 이동 사실과 새 위치를 남김
4. 완전 이주 전까지는 현재 문서를 reference source로 유지

## 다음 단계

- 실제 `shared-agent-harness` 생성 후 1차 후보부터 이주
- 공용/도메인 전용 경계가 애매한 문서는 분할 여부 먼저 판단

다음 추천:

1. executable surface review gate 문서화
2. `skills`를 runtime surface로 올릴지 판단
3. company/domain-specific 문서에서 shared 참조 링크 정리
4. 위키 쪽 공용 설계 문서의 축약/정리 여부 판단

진행 상태 메모:

- `1. executable surface review gate 문서화`는 완료
- `Phase 2` shared 공용 원칙 승격은 진행 중
- `README`, `ARCHITECTURE`, 핵심 `docs/operating/*`, `lanes/*`, `roles/*`는 detached operational source 승격 방향으로 반영 중

## 관련 페이지

- [[projects/company-domain-repo-bootstrap-plan]]
- [[projects/shared-agent-harness-internal-structure]]
- [[projects/shared-agent-harness-executable-surface-phase1]]
- [[projects/shared-agent-harness-executable-review-gate]]
- [[projects/detached-workspace-repo-migration-review-and-plan]]
- [[projects/dual-domain-agent-operating-model]]
- [[projects/shared-harness-phase1-review-2026-04-25]]
