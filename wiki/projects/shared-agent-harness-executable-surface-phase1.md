---
title: "shared-agent-harness executable surface 1차 전환"
created: "2026-04-25"
updated: "2026-04-25"
type: project
sources: []
tags: [project, harness, executable, scripts, commands, shared]
status: active
published: false
slug: ""
description: "shared-agent-harness를 reference repository에서 최소 executable surface로 전환한 1차 범위와 제약을 정리한 문서."
---

# shared-agent-harness executable surface 1차 전환

## Source Status

- 이 문서는 `shared-agent-harness` executable surface 1차 전환의 배경과 범위 판단을 남기는 `history retained here` 문서다.
- 현재 executable behavior의 detached `operational source`는 `shared-agent-harness/scripts/harness.py`와 `shared-agent-harness` 내부 command/operating 문서를 우선 기준으로 본다.
- 따라서 이 문서는 실행 범위가 왜 여기서 멈췄는지를 설명하는 migration note로 읽는다.

이 문서는 `shared-agent-harness`를 reference repository에서 `최소 executable surface`로 올린 1차 전환 범위를 정리한다.

핵심 판단:

- 바로 전체 실행 하네스로 확장하지 않는다
- 먼저 `공용 artifact 생성`만 runnable하게 만든다
- 도메인 원본 수정과 외부 시스템 write는 여전히 도메인 저장소와 approval boundary 밖에서만 다룬다

## 현재 추가된 실행 표면

실행 스크립트:

- `shared-agent-harness/scripts/harness.py`

현재 subcommand:

- `planning-new-brief`
- `review-run-cross-validation`
- `research-collect-sources`
- `engineering-execute-validated-task`

## 현재 가능한 것

- planning brief 생성
- cross-review report 생성
- source bundle 생성
- execution record 생성
- explicit domain field를 받는 shared artifact 생성

즉 현재는 `shared template를 실제 artifact로 materialize하는 레이어`까지 runnable하다.

현재 구현 보강:

- output path는 shared repo 내부 artifact 루트로 제한된다
- explicit domain field가 필수다
- negative test로 경계 위반 케이스를 검증한다

## 현재 일부러 열지 않은 것

- `company-wiki` 또는 `ai-survival-log` 원본 markdown 직접 수정
- Gmail / Calendar / Sheets 실행
- credential-required action
- arbitrary shell execution broker
- domain-specific adapter invocation

## 왜 이 범위로 멈췄는가

이 저장소는 여전히 `shared operating layer`다.

따라서 executable surface를 바로 크게 열면 다음 문제가 생긴다.

- shared와 domain boundary가 흐려짐
- company 보안 경계가 약해짐
- source-of-truth 저장소 역할이 흔들림
- 검수/approval 없이 실행이 커질 수 있음

그래서 1차 전환은 `safe artifact generation only`로 제한했다.

## command와 script의 관계

현재 `commands/*`는 설명 문서가 아니라 `scripts/harness.py`에 연결된 executable entry description으로 바뀌었다.

다만 `skills/*`는 아직 runnable skill이 아니라 `operating guide` 성격이다.

즉 현재 상태는:

- `commands`: executable usage 문서
- `scripts`: 실제 실행 표면
- `skills`: 아직 참조/운영 가이드

## 다음 확장 후보

다음 단계 후보는 아래 중 하나다.

1. `skills`를 실제 runtime skill surface로 연결
2. shared validation helper를 script로 추가
3. domain handoff packet을 `company-wiki`, `company-assistant-ops`와 더 엄격히 연결
4. executable surface의 review gate를 별도 문서로 고정

현재는 이 게이트를 별도 문서로 고정했다:

- [[projects/shared-agent-harness-executable-review-gate]]

## 운영 원칙

- executable surface가 생겨도 `role/lane is shared, data/surface is isolated`는 유지한다
- shared repo는 domain write를 직접 수행하지 않는다
- executable 범위가 확장될수록 review gate와 approval boundary도 같이 강화해야 한다

## 관련 페이지

- [[projects/shared-agent-harness-internal-structure]]
- [[projects/shared-agent-harness-migration-list]]
- [[projects/shared-harness-phase1-review-2026-04-25]]
- [[projects/shared-agent-harness-executable-review-gate]]
- [[projects/shared-harness-executable-surface-review-2026-04-25]]
