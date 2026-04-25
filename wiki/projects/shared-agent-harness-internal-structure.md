---
title: "shared-agent-harness 내부 구조 설계"
created: "2026-04-24"
updated: "2026-04-25"
type: project
sources: []
tags: [project, harness, structure, workflow, agents, shared, operations]
status: active
published: false
slug: ""
description: "개인/회사 도메인에서 공용으로 재사용할 role, lane, skill, workflow를 담는 shared-agent-harness 저장소의 내부 구조 설계."
---

# shared-agent-harness 내부 구조 설계

이 문서는 `~/workspace/claude/shared-agent-harness`의 내부 구조를 정의한다.

## Source Status

- 현재 `shared-agent-harness` 저장소의 `README.md`, `AGENTS.md`, `ARCHITECTURE.md`, `docs/operating/*`, `lanes/*`, `roles/*`가 공용 운영 원칙의 detached `operational source`다.
- 이 문서는 설계 배경, 초기 판단, 이주 맥락을 보관하는 `history retained here` 문서다.
- 즉 앞으로 실제 운영 규칙 확인은 가능하면 `shared-agent-harness` 저장소 문서를 우선하고, 이 문서는 왜 그런 구조가 되었는지 추적하는 데 쓴다.

핵심 전제:

- 이 저장소는 `공용 role/lane/skill/workflow`를 담는다
- 개인/회사 도메인 데이터 원본은 담지 않는다
- credentials, OAuth token, 일정 원본, 회의록 원본 같은 도메인 특정 정보는 저장하지 않는다
- `role/lane is shared, data/surface is isolated` 원칙을 실제 파일 구조에 반영한다

## 목적

`shared-agent-harness`는 다음을 위한 저장소다.

- 공용 role 정의
- 공용 lane workflow 정의
- skill / command 템플릿 관리
- approval / audit / validation 공통 규칙 관리
- 2-agent cross-validation 공통 규칙 관리
- 도메인별 실행 컨텍스트를 받는 broker / adapter / helper script 관리

즉 이 저장소는 `개인 프로젝트`도 아니고 `회사 프로젝트`도 아니다. 두 도메인이 공유하는 운영 장치의 source-of-truth다.

현재 상태 메모:

- 1차 bootstrap과 공용 원칙 이주는 완료됐다
- 현재는 `scripts/harness.py`를 통한 최소 executable surface가 추가된 상태다
- 다만 실행 범위는 아직 `공용 artifact 생성`으로 제한되고, 도메인 원본 수정이나 외부 시스템 write는 여기서 직접 열지 않는다

## 이 저장소에 들어가야 하는 것

- 공용 `Planning / Review / Engineering / Research` lane 정의
- role별 input / output / 금지 행위
- skill template
- command template
- workflow checklist
- audit/approval 규칙
- primary/secondary review 규칙
- 도메인별 실행 컨텍스트를 받는 helper script
- cross-domain safety rule

## 이 저장소에 들어가면 안 되는 것

- 회사 회의록 원본
- 회사 Gmail / Calendar / Sheets 데이터
- 개인 블로그 초안 원본
- 개인 콘텐츠 아이디어 원본
- 도메인 특정 OAuth token
- 실제 `.env` 값
- 특정 도메인 전용 memory 원본

## 권장 최상위 구조

```text
shared-agent-harness/
├── README.md
├── AGENTS.md
├── CLAUDE.md
├── ARCHITECTURE.md
├── docs/
│   ├── operating/
│   ├── templates/
│   └── adr/
├── roles/
├── lanes/
├── skills/
├── commands/
├── scripts/
├── tests/
└── examples/
```

## 파일/폴더별 책임

### 루트 문서

#### `README.md`

- 저장소 목적
- 어떤 도메인과 연결되는지
- 포함/제외 범위
- 빠른 시작

#### `AGENTS.md`

- 공용 핵심 규칙
- 절대 금지 사항
- role/lane 실행 원칙

#### `CLAUDE.md`

- `@AGENTS.md`
- Claude용 local surface 메모

#### `ARCHITECTURE.md`

- `shared-agent-harness`의 계층 구조
- domain context injection 방식
- approval / audit / validation 흐름

### `docs/operating/`

권장 문서:

- `operations.md`
  - 일상 운영 순서
- `domain-context-policy.md`
  - 개인/회사 도메인 선택 규칙
- `approval-matrix.md`
  - read / suggest / write-with-approval / high-risk write
- `validation-matrix.md`
  - lane별 최소 검증 규칙
- `cross-validation-policy.md`
  - 2-agent cross-validation 기본 정책

### `docs/templates/`

권장 템플릿:

- `planning-brief.md`
- `review-checklist.md`
- `cross-review-report.md`
- `meeting-followup.md`
- `assistant-action-report.md`
- `workflow-prd.md`

### `docs/adr/`

장기 판단 기록:

- why shared harness is separate
- why data/surface isolation is strict
- why Assistant Ops is company-domain-only

## `roles/`

각 역할의 정의 문서를 둔다.

권장 파일:

```text
roles/
  planning-agent.md
  research-agent.md
  engineering-agent.md
  review-agent.md
```

각 문서에 포함할 항목:

- 목적
- 입력
- 출력
- 허용 행동
- 금지 행동
- 도메인 컨텍스트 요구사항
- handoff 대상 lane
- cross-validation 참여 여부

중요:

- `Authoring Agent`, `Publish Agent`, `Assistant Ops Agent`는 도메인 전용 성격이 강하므로 여기서 공용 role로 정의하지 않는다
- 필요하면 `domain-specific extension`으로 참조만 걸고 실제 정의는 각 도메인 저장소에 둔다

## `lanes/`

공용 lane 정의를 둔다.

권장 파일:

```text
lanes/
  planning-lane.md
  research-lane.md
  engineering-lane.md
  review-lane.md
```

각 lane 문서에 포함할 항목:

- 진입 조건
- 입력
- 출력
- 참여 role
- 최소 검증
- 종료 조건
- 도메인별 차이
- cross-validation 방식

중요:

- `Assistant Ops Lane`은 회사 도메인 전용이므로 여기에는 두지 않는다
- 대신 `company-assistant-ops`에서 정의하고, 이 저장소에서는 reference만 둔다

## `skills/`

공용 skill template와 재사용 가능한 skill만 둔다.

권장 구조:

```text
skills/
  planning/
  review/
  engineering/
  research/
```

예:

- planning brief generation
- review findings formatter
- cross-review diff formatter
- engineering execution checklist
- research source collection template

중요:

- 도메인별 실제 credential을 요구하는 skill은 두지 않는다
- 그런 skill은 각 도메인 저장소에서 wrapper로 만든다

## `commands/`

공용 slash-command 또는 task command 템플릿을 둔다.

권장 구조:

```text
commands/
  planning/
  review/
  engineering/
  research/
```

예:

- `planning:new-brief`
- `review:run-checklist`
- `review:run-cross-validation`
- `engineering:execute-validated-task`
- `research:collect-sources`

## `scripts/`

이 저장소의 스크립트는 `공용 helper`와 `안전한 executable surface`만 둔다.

현재 executable surface:

- `scripts/harness.py`
  - `planning-new-brief`
  - `review-run-cross-validation`
  - `research-collect-sources`
  - `engineering-execute-validated-task`

현재 허용 범위:

- template-driven artifact generation
- explicit domain context injection
- review handoff packet generation

현재 금지 범위:

- company/personal source-of-truth 직접 수정
- Gmail / Calendar / Sheets write
- credential-backed action
- arbitrary shell brokerage
- template materializer
- cross-review result comparator

금지:

- 회사 Gmail 직접 호출 코드
- 개인 블로그 publish 직접 수행 코드
- 도메인 특정 credential을 직접 읽는 코드

즉 스크립트는 `adapter interface`까지만 두고, 실제 연결은 도메인 저장소에서 한다.

## `tests/`

공용 규칙 검증용 테스트를 둔다.

예:

- role 문서 schema 검사
- lane 문서 필수 섹션 검사
- command template completeness 검사
- domain isolation rule 검사

## `examples/`

예시만 둔다.

예:

- 개인 도메인 planning brief 예시
- 회사 도메인 planning brief 예시
- review checklist 예시

중요:

- 예시는 synthetic example만 사용
- 실제 회사 데이터/개인 민감 정보는 금지

## Positive / Negative List

### Positive

- 공용 role 정의
- 공용 lane 정의
- workflow template
- audit / approval rule
- 2-agent cross-validation policy
- review result comparator
- domain context injection interface
- 공용 validation helper

### Negative

- 회사 일정 원본
- 회사 회의록 원본
- 회사 OAuth token
- 개인 콘텐츠 초안 원본
- 특정 고객 데이터
- 도메인 전용 authoring source

## 도메인 저장소와의 관계

### `ai-survival-log`, `ai-survival-log-site`

- 개인 도메인 authoring / publish source
- shared harness의 공용 lane/role을 참조해 사용

### `company-wiki`

- 회사 도메인 authoring source
- shared harness의 planning/review/engineering/research lane을 참조

### `company-assistant-ops`

- 회사 assistant 전용 surface
- shared harness의 approval / audit / planning rule을 참조

## 이중 agent 교차검증 정책

기본 원칙:

- 모든 공식 검수 게이트는 `primary review`와 `secondary review` 두 결과를 남긴다
- 두 검수는 가능한 한 다른 agent surface 또는 다른 review path로 실행한다
- 같은 모델을 쓰더라도 prompt, checklist, skill, evaluation focus가 다르면 다른 review path로 인정할 수 있다
- 같은 모델 + 같은 checklist + 같은 prompt 조합의 반복 실행은 교차검증으로 보지 않는다
- 검수 결과가 충돌하면 `resolved / unresolved`로 정리하기 전까지 완료 처리하지 않는다

최소 적용 범위:

- Engineering Lane
- Publish Lane
- 구조 변경
- contract-sensitive 변경
- 보안/권한 변경

권장 확장 범위:

- company assistant write 정책 변경
- shared-agent-harness 공용 rule 변경
- lane 정의 변경

## 구현 우선순위

### Phase 1

- 루트 문서 4개
- `roles/`
- `lanes/`
- `docs/operating/operations.md`
- `docs/operating/domain-context-policy.md`

### Phase 2

- `skills/`
- `commands/`
- `docs/templates/`
- `docs/operating/cross-validation-policy.md`

### Phase 3

- `scripts/`
- `tests/`
- `examples/`

## 다음 단계

- `company-wiki` 내부 구조 설계
- `company-assistant-ops` 내부 구조 설계
- shared/domain-specific wrapper 경계 정의

## 관련 페이지

- [[projects/dual-domain-agent-operating-model]]
- [[projects/workspace-security-boundary]]
- [[projects/immediate-agent-operating-structure]]
- [[projects/managed-agent-harness-draft]]
