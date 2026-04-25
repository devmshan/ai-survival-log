---
title: "shared-agent-harness executable review gate"
created: "2026-04-25"
updated: "2026-04-25"
type: project
sources: []
tags: [project, harness, executable, review, validation, boundary]
status: active
published: false
slug: ""
description: "shared-agent-harness의 executable surface를 어디까지 허용하고 어떤 변경을 escalate해야 하는지 고정한 검토 게이트 문서."
---

# shared-agent-harness executable review gate

## Source Status

- 이 문서는 executable surface gate의 설계 배경과 검토 기준을 보관하는 `history retained here` 문서다.
- 현재 detached `operational source`는 `shared-agent-harness/docs/operating/executable-surface-gate.md`를 우선 기준으로 본다.
- 이 문서는 upstream 쪽 rationale과 검토 history를 남기는 역할로 읽는다.

이 문서는 `shared-agent-harness`에서 executable surface를 확장할 때 적용할 검토 게이트를 고정한다.

핵심 의도:

- executable surface를 열더라도 `shared`와 `domain` 경계를 흐리지 않는다
- artifact generation과 boundary-expanding execution을 명확히 구분한다
- 확장 속도보다 안전한 분류와 review gate를 우선한다

## 현재 허용 범위

현재 허용되는 executable surface는 `safe artifact generation`이다.

예:

- planning brief 생성
- cross-review report 생성
- source bundle 생성
- execution record 생성

공통점:

- shared template를 materialize한다
- explicit domain field를 받는다
- domain source-of-truth를 직접 수정하지 않는다
- credential이 필요 없다

## 현재 금지 범위

아래는 아직 `shared-agent-harness`에서 직접 열지 않는다.

- `company-wiki`, `company-assistant-ops`, `ai-survival-log`, `ai-survival-log-site` 직접 수정
- Gmail / Calendar / Sheets 실행
- credential-backed adapter
- arbitrary shell brokerage
- domain-specific source-of-truth mutation

## 검토 게이트

executable surface 관련 변경은 아래 순서를 반드시 통과해야 한다.

1. `scope classification`
   - artifact generation only
   - boundary-expanding execution
2. `explicit domain-boundary check`
3. `primary review`
4. `secondary review`
   - 가능한 경우 다른 surface 또는 materially different review path 사용
5. `explicit decision`
   - `warn`
   - `block`
   - `escalate`

## 자동 escalate 조건

아래 중 하나라도 포함되면 자동으로 `escalate` 대상이다.

- domain source-of-truth repo write
- credential / token handling
- external system action
- bounded template materialization을 넘는 shell execution
- shared와 domain repo 사이 ownership이 불명확한 변경

## 검토 질문

실행 범위를 확장하기 전에 최소한 아래 질문에 답해야 한다.

- 이 기능은 shared에 있어야 하나, domain repo에 있어야 하나
- source-of-truth를 직접 수정하는가
- approval 또는 audit가 필요한가
- 같은 목적을 handoff artifact 생성으로 달성할 수 없는가

## 기본 판정 규칙

ownership이 불명확하거나 경계를 넘는 실행이라면 기본은 `block` 또는 `escalate`다.

즉 `실행 가능하다`보다 `이 실행이 shared에 있어도 되는가`를 먼저 본다.

## 현재 연결 문서

- [[projects/shared-agent-harness-executable-surface-phase1]]
- [[projects/shared-agent-harness-internal-structure]]
- [[projects/shared-harness-phase1-review-2026-04-25]]
