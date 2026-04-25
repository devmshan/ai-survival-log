---
title: "detached workspace repo migration review and plan"
created: "2026-04-25"
updated: "2026-04-25"
type: project
sources: []
tags: [project, migration, harness, company, repo, review, plan]
status: active
published: false
slug: ""
description: "ai-survival-log 바깥의 company-wiki, company-assistant-ops, shared-agent-harness만으로도 운영 가능한 구조로 옮길 수 있는지 역할별로 재검토하고 실제 이전 계획을 정리한 문서."
---

# detached workspace repo migration review and plan

이 문서는 아래 질문에 답하기 위해 작성했다.

`company-wiki`, `company-assistant-ops`, `shared-agent-harness`만 다른 데스크탑으로 가져가도 업무에 문제가 없게 만들 수 있는가.

현재 답:

- `지금 당장은 아직 아니다`
- 하지만 `설계 source 재배치`는 지금 바로 시작할 수 있다
- 그리고 이 축은 `코드/OAuth`보다 먼저 해결하는 것이 맞다

## 현재 문제 정의

현재 세 저장소는 이미 물리적으로 분리되어 있다.

- `shared-agent-harness`
- `company-wiki`
- `company-assistant-ops`

하지만 설계의 source-of-truth는 아직 일부가 `ai-survival-log/wiki/projects/`에 남아 있다.

그래서 세 저장소만 따로 가져가면 아래 문제가 생긴다.

- 왜 이 구조가 이렇게 생겼는지의 배경이 약하다
- 어떤 경계가 강제되어야 하는지의 원문 맥락이 빠진다
- 무엇을 shared에 두고 무엇을 domain repo에 두면 안 되는지 판단 근거가 부족하다
- executable surface를 어디까지 허용할지의 상위 설계 판단이 분산돼 있다

즉 `실행 가능한 껍데기`는 생겼지만, `운영 판단의 원문`은 아직 upstream 위키에 더 많이 남아 있다.

## 합동 검토

### 디렉터 관점

판단:

- 방향은 맞다
- 특히 다른 데스크탑에서 세 저장소만 열어도 이해되게 만드는 것은 운영 확장성 측면에서 필요하다

이유:

- 실제 운영자는 히스토리 저장소보다 해당 저장소의 `README`, `AGENTS`, `ARCHITECTURE`, `docs/operating`를 먼저 본다
- 운영 문서가 해당 저장소 안에서 닫혀 있어야 사람과 에이전트 모두 실수 가능성이 줄어든다

우려:

- `ai-survival-log`가 현재 설계 히스토리와 운영 원칙의 혼합 source 역할을 하고 있다
- 이걸 한 번에 비우면 맥락을 잃는다

디렉터 결론:

- `방향 승인`
- 단, `이전`이 아니라 `승격 + 잔존 히스토리 보관` 방식으로 가야 한다

### 기획자 관점

판단:

- 지금 옮기기 가장 좋은 것은 `설계 설명력`이다

이유:

- 코드/OAuth/adapter보다 문서 source 정리가 더 빠르고 안전하다
- 세 저장소만 보고도 `무엇을 하면 되고 안 되는지` 이해되는 구조가 먼저 갖춰져야 한다

핵심 요구:

- `shared-agent-harness`는 공용 운영 원칙의 1차 source가 되어야 한다
- `company-wiki`, `company-assistant-ops`는 각자의 도메인 규칙을 저장소 내부 문서만으로 설명할 수 있어야 한다
- `ai-survival-log`는 최종 운영 source보다 `설계 히스토리와 상위 메모` 성격으로 후퇴해야 한다

기획 결론:

- 공용 원칙, 도메인 운영 원칙, 히스토리를 분리하는 방향이 맞다

### 엔지니어 관점

판단:

- 지금 상태는 `code split`은 어느 정도 됐지만 `design split`은 덜 됐다

이유:

- `shared-agent-harness`에는 이미 실행 표면과 운영 문서가 있다
- 하지만 상위 판단 근거 일부는 여전히 `wiki/projects/`에만 있다
- 다른 데스크탑에서 세 저장소만 clone할 경우, 코드 실행은 일부 가능해도 변경 판단 근거가 비어 있을 수 있다

엔지니어가 보는 핵심 부족분:

- shared repo의 ADR와 operating 문서가 더 완결되어야 한다
- company repo의 `docs/operating/`가 현재보다 더 자급자족 가능해야 한다
- upstream 위키에서 각 저장소로 `source 승격 완료/미완료` 상태가 명시돼야 한다

엔지니어 결론:

- 지금 바로 시작 가능
- 다만 `문서 source 승격`을 단계적으로 해야 한다

### 검수자 관점

판단:

- 이 작업은 맞지만, `옮겼다`와 `운영 source로 승격했다`를 구분해야 한다

검수 기준:

- 해당 저장소만 열어도 최소 운영 규칙을 이해할 수 있는가
- 금지 범위가 그 저장소 안에 명시돼 있는가
- 변경 시 review gate가 그 저장소 안에 존재하는가
- upstream 문서와 충돌 없이 우선순위가 명시돼 있는가

현재 문제:

- `shared-agent-harness`는 많이 좋아졌지만 여전히 일부 문서가 `bootstrap source currently lives in ai-survival-log`에 기대고 있다
- `company-wiki`, `company-assistant-ops`는 도메인 설명력은 올라왔지만 아직 운영 문서 세트가 완전히 닫히지 않았다

검수 결론:

- 방향은 맞다
- 단, `phase별 승격 기준`을 먼저 정하고 옮겨야 한다

## 회의 결론

합의:

1. 이 방향은 맞다
2. 지금 해결 가능한 문제다
3. 가장 먼저 옮겨야 하는 것은 `코드`가 아니라 `설계 source-of-truth`다
4. 하지만 한 번에 `ai-survival-log`를 비우면 안 된다
5. `승격된 문서`와 `히스토리 문서`를 분리해야 한다

즉:

- `shared-agent-harness`, `company-wiki`, `company-assistant-ops`를 `운영 source`로 승격
- `ai-survival-log`는 `설계 히스토리/메타 기록`으로 후퇴

이게 맞는 방향이다.

## 실제 이전 계획

### Phase 1. source 등급 명시

목표:

- 어떤 문서가 `운영 source`인지
- 어떤 문서가 `히스토리/참조`인지
  먼저 표시한다

작업:

- `ai-survival-log/wiki/projects/` 문서에 아래 상태를 추가
  - `operational source moved`
  - `history retained here`
- `shared-agent-harness`, `company-wiki`, `company-assistant-ops` 문서에는
  - `this repo is now the operational source for ...`
  같은 문장을 넣는다

완료 기준:

- 세 저장소만 열어도 “무엇이 현재 운영 source인지” 헷갈리지 않는다

현재 상태 메모:

- 이 Phase를 시작했다
- 우선 `shared-agent-harness-internal-structure`, `company-wiki-internal-structure`, `company-assistant-ops-internal-structure`에 `Source Status`를 추가해 upstream 문서의 역할을 먼저 명시한다
- 이어서 각 생성 저장소의 `README.md`, `ARCHITECTURE.md`, 핵심 `docs/operating/*`에도 같은 source status를 반영한다

### Phase 2. 공용 원칙 승격

목표:

- `shared-agent-harness`가 공용 운영 원칙의 실제 source가 되게 만든다

대상:

- lane/role 원칙
- cross-validation 원칙
- workflow gates
- executable surface gate
- adoption strategy
- stop conditions
- domain-context policy

작업:

- 이미 옮긴 문서를 `요약본`이 아니라 `운영 완결본`으로 다듬는다
- upstream 위키 문서는
  - 원문 히스토리
  - 변경 배경
  - 당시 판단 메모
  중심으로 축소한다

완료 기준:

- `shared-agent-harness`만 봐도 공용 운영 판단이 가능하다

현재 상태 메모:

- 이 Phase를 시작했다
- `shared-agent-harness`의 `README.md`, `ARCHITECTURE.md`, `docs/operating/operations.md` 등 핵심 문서에서 `bootstrap source` 표현을 줄이고 `operational source`와 `history source`를 분리하는 작업을 반영했다
- `docs/operating/source-of-truth-map.md`를 추가해 detached workspace 기준의 현재 소유권 지도를 명시했다
- `lanes/*`, `roles/*`에도 `Source Status`와 `History Source`를 반영해, shared repo만 보고도 공용 lane/role 판단이 가능하도록 승격을 시작했다
- upstream 위키의 `managed-agent-harness-draft.md`, `immediate-agent-operating-structure.md`, `planning-lane-execution-draft.md`, `assistant-ops-lane-execution-draft.md`에도 `history retained here` 표기와 detached operational source 우선 경로를 추가했다

### Phase 3. 회사 도메인 운영 원칙 승격

목표:

- `company-wiki`, `company-assistant-ops`가 각자 도메인 운영 규칙을 내부 문서만으로 설명하게 만든다

대상:

- company source-of-truth boundary
- authoring/execution 분리 원칙
- approval matrix
- audit / handoff / review checklist
- bootstrap but not operational gate

작업:

- `company-wiki/docs/operating/` 보강
- `company-assistant-ops/docs/operating/` 보강
- 현재 upstream 위키에만 남아 있는 회사 도메인 규칙 중 핵심 운영 항목을 각 저장소로 이관

완료 기준:

- 회사 저장소만 열어도 authoring / execution / approval boundary를 이해할 수 있다

현재 상태 메모:

- 이 Phase를 시작했다
- `company-wiki`에 `docs/operating/operations.md`, `source-boundary.md`, `review-policy.md`, `handoff-policy.md`를 추가해 회사 authoring 규칙을 detached repo 내부 문서만으로 설명할 수 있게 보강했다
- `company-wiki`의 `AGENTS.md`, `CLAUDE.md`도 같은 운영 문서 세트를 우선 보도록 갱신했다
- `company-assistant-ops`의 `AGENTS.md`, `CLAUDE.md`도 detached operational source라는 점과 `docs/operating/*` 우선 참조 구조를 더 명확히 했다
- `company-assistant-ops`의 `operations.md`, `audit-policy.md`, `credential-policy.md`, `handoff-policy.md`를 보강해 execution/approval/audit/credential 역할 분담을 더 직접적으로 설명하게 했다
- `company-wiki/docs/operating/handoff-policy.md`, `company-wiki/templates/meeting-note.md`, `company-assistant-ops/docs/templates/*`를 같은 handoff 필드 기준으로 정렬해 두 저장소 간 요청/응답 형태를 맞췄다
- `detached-company-domain-phase3-review-2026-04-25` 기준 남아 있던 경고 2개를 수리했고, 현재 Phase 3는 `approved` 상태다

### Phase 4. upstream 위키의 역할 축소

목표:

- `ai-survival-log`의 역할을 `운영 source`에서 `설계 히스토리`로 명확히 줄인다

작업:

- 해당 project 문서 상단에
  - 현재 operational source 위치
  - 이 문서가 히스토리인지 여부
  표시
- 중복된 운영 규칙은 가능한 한 저장소 문서 링크로 대체

완료 기준:

- upstream 위키를 안 봐도 운영은 가능
- upstream 위키를 보면 “왜 이런 구조가 되었는지”를 이해할 수 있음

현재 상태 메모:

- 이 Phase를 시작했다
- `dual-domain-agent-operating-model.md`, `workspace-folder-structure-review-sheet.md`, `shared-agent-harness-migration-list.md`, `shared-agent-harness-executable-surface-phase1.md`, `shared-agent-harness-executable-review-gate.md`, `workspace-security-boundary.md`에 `Source Status`를 추가해 upstream 문서를 `history retained here` 역할로 더 명확히 내렸다
- detached repo 내부 문서를 현재 `operational source`로 우선 보라는 경로를 문서 상단에서 직접 안내하도록 정리했다
- `workspace-folder-structure-review-sheet.md`의 읽기 순서를 detached repo 우선으로 재정렬했고, 핵심 internal-structure 문서의 상태 표현도 현재형으로 정리해 Phase 4 리뷰의 경고 2개를 닫았다

## 우선순위

가장 먼저 할 것:

1. `shared-agent-harness` 운영 문서 승격
2. `company-wiki`, `company-assistant-ops` 운영 source 표시
3. upstream 문서에 `history retained` 표기

나중으로 미룰 것:

- OAuth
- 실제 adapter 구현
- 외부 시스템 런타임 연결

## 최종 판단

이전 방향은 맞다.

다만 표현을 바꾸는 편이 정확하다.

`ai-survival-log에서 세 저장소로 설계를 옮긴다`
보다는

`세 저장소를 운영 source로 승격하고, ai-survival-log는 설계 히스토리 저장소로 재정의한다`

가 맞다.

## 관련 페이지

- [[projects/shared-agent-harness-migration-list]]
- [[projects/company-domain-repo-bootstrap-plan]]
- [[projects/shared-agent-harness-executable-surface-phase1]]
- [[projects/shared-agent-harness-executable-review-gate]]
- [[projects/detached-company-domain-phase3-review-2026-04-25]]
- [[projects/detached-workspace-phase4-review-2026-04-25]]
- [[projects/five-repo-harness-doc-structure-review-2026-04-25]]
