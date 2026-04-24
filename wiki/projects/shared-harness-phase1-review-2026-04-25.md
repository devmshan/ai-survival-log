---
title: "shared-agent-harness 1차 설계 합동 최종 검수"
created: "2026-04-25"
updated: "2026-04-25"
type: project
sources: []
tags: [project, review, harness, company, shared, operations, qa]
status: active
published: false
slug: ""
description: "shared-agent-harness 1차 설계와 company 도메인 bootstrap 상태를 디렉터, 기획자, 엔지니어, 검수자 합동 회의 형태로 최종 검수한 기록."
---

# shared-agent-harness 1차 설계 합동 최종 검수

이 문서는 현재까지의 `shared-agent-harness` 1차 이주와 `company-wiki`, `company-assistant-ops` bootstrap 상태를 디렉터, 기획자, 엔지니어, 검수자가 함께 회의하는 방식으로 최종 검수한 기록이다.

검토 목표:

- 구조가 실제 운영 가능한 수준까지 닫혔는지 확인
- 공용 원칙과 도메인 전용 경계가 문서와 로컬 저장소에 일관되게 내려왔는지 점검
- 실제 프로젝트 시작 전에 막아야 할 `block` 이슈를 식별
- `warn` 이슈는 이후 어떤 순서로 수리해야 하는지 합의

검토 범위:

- upstream 위키 문서
- 실제 생성된 로컬 저장소 문서
- shared harness의 역할/레인/운영/command/skill 표면

검토에 사용한 대표 문서:

- [[projects/shared-agent-harness-migration-list]]
- [company-wiki/README.md](/Users/ms/workspace/claude/company-wiki/README.md:1)
- [company-wiki/AGENTS.md](/Users/ms/workspace/claude/company-wiki/AGENTS.md:1)
- [company-assistant-ops/README.md](/Users/ms/workspace/claude/company-assistant-ops/README.md:1)
- [company-assistant-ops/AGENTS.md](/Users/ms/workspace/claude/company-assistant-ops/AGENTS.md:1)
- [company-assistant-ops/docs/operating/approval-matrix.md](/Users/ms/workspace/claude/company-assistant-ops/docs/operating/approval-matrix.md:1)
- [shared-agent-harness/README.md](/Users/ms/workspace/claude/shared-agent-harness/README.md:1)
- [shared-agent-harness/docs/operating/workflow-gates.md](/Users/ms/workspace/claude/shared-agent-harness/docs/operating/workflow-gates.md:1)
- [shared-agent-harness/commands/review/run-cross-validation.md](</Users/ms/workspace/claude/shared-agent-harness/commands/review/run-cross-validation.md:1>)
- [shared-agent-harness/skills/review/README.md](</Users/ms/workspace/claude/shared-agent-harness/skills/review/README.md:1>)

## 최종 판정

판정: `phase 1 review closed`

의미:

- 방향, 구조, 문서 계층은 전반적으로 타당하다
- `shared-agent-harness`는 공용 운영 레이어의 1차 참조 저장소로 이미 usable하다
- 초기 `block`이었던 로컬 회사 저장소 운영 금지 게이트 누락은 수리됐다
- 남아 있던 `warn` 2개도 수리됐다
- 실제 회사 작업 개시는 여전히 `git init -> company identity -> pre-commit` 완료 전까지 금지다

## 핵심 Findings

### 1. `company` 저장소 로컬 문서에 `not operational` 게이트가 빠져 있었다

이전 심각도: `block`
현재 상태: `fixed`

대상:

- [company-wiki/README.md](/Users/ms/workspace/claude/company-wiki/README.md:1)
- [company-wiki/AGENTS.md](/Users/ms/workspace/claude/company-wiki/AGENTS.md:1)
- [company-assistant-ops/README.md](/Users/ms/workspace/claude/company-assistant-ops/README.md:1)
- [company-assistant-ops/AGENTS.md](/Users/ms/workspace/claude/company-assistant-ops/AGENTS.md:1)

문제:

- upstream 위키에는 `git init -> 회사 git identity -> pre-commit hook` 완료 전까지 회사 저장소를 `bootstrapped but not operational`로 본다는 강한 게이트가 있다
- 하지만 실제 생성된 회사 저장소 로컬 문서에는 이 강한 금지 문구가 없다
- 따라서 사용자가 새 저장소만 단독으로 열어 보면, 아직 회사 작업을 시작하면 안 된다는 핵심 안전 규칙을 놓칠 수 있다

영향:

- 회사 note 작성 선행
- 잘못된 git identity로 초기 commit
- hook 없이 secret 또는 잘못된 데이터가 staging 되는 위험

조치 결과:

- 두 저장소의 `README.md`, `AGENTS.md`에 `bootstrapped but not operational` 문구와 필수 게이트를 반영했다
- 현재는 로컬 저장소만 열어도 실제 회사 작업 시작 금지 규칙을 확인할 수 있다

### 2. `company-assistant-ops` 로컬 approval matrix가 너무 추상적이었다

이전 심각도: `warn`
현재 상태: `fixed`

대상:

- [company-assistant-ops/docs/operating/approval-matrix.md](/Users/ms/workspace/claude/company-assistant-ops/docs/operating/approval-matrix.md:1)
- 비교 기준: [[projects/company-assistant-approval-matrix]]

문제:

- upstream 위키에는 Gmail/Calendar/Sheets별로 `Level 0~3` 매핑이 구체적으로 있다
- 하지만 실제 저장소의 로컬 `approval-matrix.md`는 레벨 이름만 있고 시스템별 작업 매핑이 없다

영향:

- `Gmail send`, `Calendar create`, `Sheets row update`를 어느 레벨로 볼지 저장소 로컬만 봐서는 일관되게 판단하기 어렵다

조치 결과:

- 로컬 `approval-matrix.md`에 Gmail / Calendar / Sheets 액션별 레벨 매핑을 추가했다
- `block conditions`, `escalate conditions`, `default rule`도 함께 추가했다
- 이제 로컬 저장소만 봐도 기본 승인 판단을 할 수 있다

### 3. shared `command/skill` 표면이 아직 reference라는 점이 충분히 드러나지 않았다

이전 심각도: `warn`
현재 상태: `fixed`

대상:

- [shared-agent-harness/commands/review/run-cross-validation.md](</Users/ms/workspace/claude/shared-agent-harness/commands/review/run-cross-validation.md:1>)
- [shared-agent-harness/skills/review/README.md](</Users/ms/workspace/claude/shared-agent-harness/skills/review/README.md:1>)

문제:

- 현재 command/skill은 설명용 reference다
- 그런데 command 파일은 실제 실행 entrypoint처럼 읽힐 수 있다

영향:

- 운영자가 이 파일을 바로 runnable command로 오해할 수 있다

조치 결과:

- shared `commands/*` 상단에 `reference-only for now` 상태 문구를 추가했다
- shared `skills/*/README.md`에도 동일한 상태 문구를 추가했다
- 현재는 shared 저장소를 실행 레이어가 아니라 설계/참조 레이어로 읽어야 한다는 점이 더 명확해졌다

## 합동 회의 메모

아래 메모는 각 역할이 따로 말한 의견이 아니라, 서로의 시각을 확인하고 반박하거나 보완한 흐름을 요약한 것이다.

### 1단계. 구조와 경계 검토

디렉터:

- 개인, 회사, shared를 물리적으로 나눈 방향은 맞다.
- 특히 `company-wiki`와 `company-assistant-ops`를 나눈 것이 조직 운영상 가장 큰 안정 장치다.

기획자:

- role/lane 공유와 data/surface 분리는 개념적으로 깔끔하다.
- dry-run, approval matrix, template set까지 이어져 있어서 `설계 -> 운영` 흐름이 이미 보인다.

엔지니어:

- shared 저장소가 단순 placeholder 모음이 아니라 `roles/lanes/templates/commands/skills/ADR`까지 갖췄다.
- bootstrap 수준을 넘어서 공용 참조 저장소의 최소 형태는 갖췄다.

검수자:

- 경계가 문서상으로는 잘 내려왔다.
- 다만 실제 운영자는 로컬 저장소 문서를 먼저 보므로, upstream 위키에만 규칙이 있는 상태는 안전 기준상 충분하지 않다.

중간 합의:

- 구조 방향성은 `pass`
- 경계 문구의 최종 전달 위치는 아직 미완

### 2단계. 회사 도메인 개시 가능성 검토

디렉터:

- 지금 단계에서 가장 중요한 것은 `실수로 회사 작업을 시작하지 못하게 막는 것`이다.
- bootstrap이 끝났다는 이유로 운영 개시로 오해되면 안 된다.

기획자:

- 운영 문서를 풍부하게 만든 것 자체는 좋지만, 핵심 중단 조건이 첫 화면에 안 보이면 사용자는 절차를 건너뛴다.
- 특히 `README`와 `AGENTS`가 안전 게이트를 반복해줘야 한다.

엔지니어:

- upstream 위키에는 `bootstrapped but not operational` 규칙이 이미 있다.
- 문제는 그 사실이 로컬 저장소로 materialize되지 않았다는 점이다.

검수자:

- 이것은 단순 누락이 아니라 `block`이다.
- 이유는 실제 저장소만 열어도 운영 시작 금지 규칙을 알 수 있어야 하기 때문이다.

중간 합의:

- 로컬 문서에 강한 게이트가 없는 상태에서는 회사 프로젝트 개시 금지
- 해당 이슈는 이번 라운드에서 수리 완료

### 3단계. shared harness의 실행 가능성 오해 검토

디렉터:

- shared 저장소가 잘 자라고 있지만, 지금은 아직 `실행 레이어`보다 `설계 레이어`에 더 가깝다.

기획자:

- command/skill 이름이 좋아서 오히려 runnable처럼 보일 수 있다.
- 지금은 참조용이라는 표식이 더 분명해야 온보딩이 덜 혼란스럽다.

엔지니어:

- 실제로 현재 command/skill은 reference다.
- 추후 executable surface로 바꾸는 단계가 따로 필요하다.

검수자:

- 이건 지금 바로 사고를 내는 `block`은 아니지만, 저장소가 커질수록 오해 비용이 커진다.

중간 합의:

- shared `commands/`, `skills/`에는 `reference-only` 표기가 필요하다

## 역할별 최종 의견

### 디렉터 관점

좋은 점:

- `개인 / 회사 / shared` 3축 분리가 명확하다
- `role/lane is shared, data/surface is isolated` 원칙이 실제 폴더 구조까지 내려왔다
- `company-wiki`와 `company-assistant-ops`를 분리한 판단이 조직 운영 관점에서 타당하다

우려:

- 현장 운영자는 upstream 위키보다 실제 생성된 저장소 로컬 문서를 먼저 본다
- 그래서 안전 규칙은 upstream에만 있으면 부족하고, 로컬 저장소에도 재기재되어야 한다
- 지금 상태는 `설계가 맞다`이지 `곧바로 운영해도 된다`가 아니다

디렉터 판정:

- `방향 승인, 운영 개시 보류`

### 기획자 관점

좋은 점:

- planning / review / engineering / research 공용 역할이 잘 정리됐다
- 회사 도메인 템플릿과 dry-run 시나리오, approval matrix까지 연결돼 흐름이 보인다
- `shared -> company-wiki -> company-assistant-ops` handoff의 개념이 보인다

우려:

- bootstrap 이후 실제 운영자가 보는 문서의 밀도 차이가 생겼다
- 특히 `company-assistant-ops`의 approval matrix는 설계 의도 대비 로컬 버전이 너무 얇다
- 규칙의 전달력이 아직 upstream 위키에 편중돼 있다

기획자 판정:

- `설계 완성도는 높지만, 사용자가 처음 보는 진입 문서가 더 강해야 한다`

### 엔지니어 관점

좋은 점:

- shared 쪽은 `architecture / operating / roles / lanes / templates / commands / skills / ADR`까지 최소 구조가 닫혔다
- 회사 저장소도 phase 1 bootstrap이 일관되게 생성됐다
- 구조적 refactor의 단계 구분이 명확하다
  - bootstrap
  - not operational
  - git identity/hook
  - operational

우려:

- command/skill이 reference인지 executable인지 경계가 아직 흐리다
- 현재 상태로는 future implementation point는 맞지만, 오해 방지 문구가 더 필요하다
- 일부 로컬 문서는 upstream 설계의 요약본으로는 충분하지만 운영 안전장치로는 아직 약하다

엔지니어 판정:

- `설계 저장소와 실행 저장소 구분은 성공, 그러나 실행 오해 방지 문구 보강 필요`

### 검수자 관점

좋은 점:

- cross-validation 원칙이 shared와 company 양쪽에 잘 내려왔다
- `block / warn / escalate` 사고방식이 설계 전반에 일관되게 보인다
- 이번 검토에서 `실제 로컬 저장소 문서`까지 범위를 넓힌 것은 적절했다

우려:

- 실제 회사 프로젝트 개시 금지 규칙이 로컬 저장소에 없는 것은 검수 관점에서 가장 큰 gap이다
- 이 부분은 문서 중복을 감수하고라도 로컬 저장소 쪽에 강하게 써야 한다
- 로컬 approval matrix와 shared command/skill 오해 가능성은 지금 수정 비용이 낮을 때 잡아야 한다

검수자 판정:

- `초기 block 해소, warn 2개 수리 완료`

## 결론

현재 구조는 방향이 맞고 1차 이주도 충분히 usable하다.

다만 아래 항목을 기준으로 운영 상태를 더 명확히 구분해야 한다.

### 운영 상태 판정

- `shared-agent-harness`: `usable as shared reference`
- `company-wiki`: `bootstrapped but not operational`
- `company-assistant-ops`: `bootstrapped but not operational`

### 실제 회사 작업 시작 전 필수 조치

1. `git init -> company git identity -> pre-commit` 3단계 완료

### 이후 정리 권장 조치

2. `shared-agent-harness`에서 executable surface로 넘어가는 시점과 기준을 별도 문서로 고정

## 닫힌 이슈

- 회사 로컬 저장소 운영 금지 게이트 누락 `fixed`
- 로컬 approval matrix 추상성 `fixed`
- shared command/skill reference 상태 불명확 `fixed`

## 관련 페이지

- [[projects/shared-agent-harness-migration-list]]
- [[projects/company-domain-repo-bootstrap-plan]]
- [[projects/workspace-security-boundary]]
- [[projects/company-assistant-approval-matrix]]
