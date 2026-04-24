---
title: "회사 도메인 템플릿 materialize 계획"
created: "2026-04-24"
updated: "2026-04-24"
type: project
sources: []
tags: [project, company, templates, materialize, rollout, wiki, assistant]
status: active
published: false
slug: ""
description: "company-wiki와 company-assistant-ops 저장소를 실제 생성할 때 어떤 템플릿을 어떤 순서로 파일로 materialize할지 정리한 계획 문서."
---

# 회사 도메인 템플릿 materialize 계획

이 문서는 실제 `company-wiki`, `company-assistant-ops` 저장소를 만들 때 어떤 템플릿을 어떤 순서로 materialize할지 정리한다.

## 목표

- 구조 설계를 실제 파일 세트로 옮길 순서를 고정
- 처음부터 모든 템플릿을 만들지 않고, 운영상 가장 필요한 것부터 만든다
- `company-wiki`와 `company-assistant-ops`의 경계가 파일 구조에서도 유지되게 한다

## 원칙

- 먼저 `company-wiki`의 판단/기록 surface를 만든다
- 그 다음 `company-assistant-ops`의 실행/승인 surface를 만든다
- 템플릿 파일명은 ASCII kebab-case를 유지한다
- materialize 전에도 source-of-truth는 현재 `ai-survival-log/wiki/projects/`의 설계 문서다

## Phase 1. 즉시 필요한 템플릿

### `company-wiki`

- `templates/meeting-note.md`
- `templates/cross-review-report.md`
- `templates/test-plan.md`

### `company-assistant-ops`

- `docs/templates/approval-record.md`
- `docs/templates/execution-report.md`

이유:

- 회의 note와 공식 검수, 실행 승인/결과 기록이 가장 먼저 필요하다

## Phase 2. 운영을 안정화하는 템플릿

### `company-wiki`

- `templates/project-brief.md`
- `templates/planning-brief.md`
- `templates/review-report.md`
- `templates/test-result.md`

### `company-assistant-ops`

- `docs/templates/calendar-request.md`
- `docs/templates/followup-request.md`
- `docs/templates/report-request.md`

이유:

- 프로젝트/기획/검수와 assistant request 흐름이 붙기 시작하면 이 단계가 필요하다

## Phase 3. 실패/예외 대응 템플릿

### `company-assistant-ops`

- `docs/templates/failure-report.md`

### 공통 보강

- handoff example note
- dry-run example file

이유:

- 실제 운영에서 실패와 retry가 생긴 뒤에야 필요성이 커진다

## materialize 순서

1. 저장소 루트 문서 4개 생성
2. 폴더 구조 생성
3. Phase 1 템플릿 생성
4. 시범 workflow 1건 적용
5. Phase 2 템플릿 생성
6. dry-run 예시를 example 파일로 추가
7. 필요 시 Phase 3 템플릿 생성

## 시범 적용 추천 순서

1. `meeting-note` 작성
2. `cross-review-report` 작성
3. `approval-record` / `execution-report` mock 작성
4. `calendar-request` 또는 `followup-request` 추가

## 검증 기준

- 템플릿만으로 실제 note를 만들 수 있는가
- `company-wiki`에서 `company-assistant-ops`로 handoff가 자연스러운가
- approval/audit가 템플릿만으로 누락 없이 남는가
- 회사 도메인 review/checklist 운영 규칙과 충돌하지 않는가

## 다음 단계

- approval matrix 세부안 반영
- 실제 저장소 생성 시 copy set 정의

## 관련 페이지

- [[projects/company-domain-template-set]]
- [[projects/company-assistant-dry-run-scenarios]]
- [[projects/company-domain-review-checklist-operations]]
