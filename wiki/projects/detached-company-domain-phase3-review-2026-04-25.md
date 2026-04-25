---
title: "Detached Company Domain Phase 3 Review"
created: "2026-04-25"
updated: "2026-04-25"
type: project
sources: []
tags: [project, review, company, detached-workspace, harness, operations]
status: active
published: false
slug: ""
description: "company-wiki와 company-assistant-ops만 기준으로 회사 도메인 운영 설명력이 충분한지 검토한 Phase 3 합동 리뷰 문서."
---

# Detached Company Domain Phase 3 Review

## Review Scope

이번 리뷰는 `ai-survival-log`의 upstream 설계 문서를 잠시 치우고, 아래 두 저장소만 열었을 때 회사 도메인 운영 구조를 이해할 수 있는지를 보는 검토다.

- `~/workspace/claude/company-wiki`
- `~/workspace/claude/company-assistant-ops`

리뷰 목적은 세 가지다.

1. `company-wiki`만 봐도 회사 authoring source 경계를 이해할 수 있는가
2. `company-assistant-ops`만 봐도 execution / approval / audit 구조를 이해할 수 있는가
3. 두 저장소를 함께 보면 `handoff -> approval -> execution -> return` 흐름이 닫히는가

## Findings

초기 리뷰 시 경고 2개가 있었지만, 둘 다 수리됐다.

### fixed 1. `warn` — failure report가 문서에는 나오지만 detached 템플릿에는 없다

조치:

- `/Users/ms/workspace/claude/company-assistant-ops/docs/templates/failure-report.md` 추가

현재 상태:

- `approval-record`, `execution-report`, `failure-report`가 모두 존재해 성공/실패 경로를 detached 저장소만으로 따라갈 수 있다.

### fixed 2. `warn` — company-wiki 상위 문서가 detached operating docs 전체를 가리키지 않는다

조치:

- `/Users/ms/workspace/claude/company-wiki/README.md`에 `Read Next` 섹션 추가
- `/Users/ms/workspace/claude/company-wiki/ARCHITECTURE.md`에 `Operating Documents` 섹션 추가
- `/Users/ms/workspace/claude/company-wiki/CLAUDE.md`에서 detached operating docs 세트를 직접 안내

현재 상태:

- detached 실무자가 `README -> AGENTS/ARCHITECTURE -> docs/operating/*` 경로로 자연스럽게 들어갈 수 있다.

## Planner Review

기획자 관점에서 보면 방향은 적절하다.

- `company-wiki`는 durable authoring source
- `company-assistant-ops`는 execution / approval / audit surface
- 두 저장소 사이 handoff 필드도 이제 상당히 정렬됐다

좋은 점:

- `company-wiki`는 “왜 이 저장소가 존재하는지”가 분명하다
- `company-assistant-ops`는 approval matrix와 audit/credential/handoff 역할이 분리됐다
- `meeting-note`, `approval-record`, `execution-report`가 같은 필드 체계로 맞아 가고 있다

부족한 점:

- 실패 경로 템플릿이 빠져 있어 planning 상 `happy path 중심`으로 보인다
- `company-wiki` 첫 화면에서 operating docs 전체를 더 직접적으로 안내하면 온보딩 비용이 줄어든다

기획자 판정:

- `approved`

## Engineer Review

엔지니어 관점에서는 저장소 역할과 데이터 경계가 명확하다.

좋은 점:

- 두 저장소 모두 `bootstrapped but not operational` 게이트가 살아 있다
- credential은 repo 밖, execution은 assistant ops, durable context는 wiki라는 분리가 일관된다
- `approval-matrix`, `audit-policy`, `credential-policy`, `handoff-policy`가 문서 역할상 겹치지 않게 됐다

부족한 점:

- failure path에 대한 템플릿 surface가 없다
- `company-wiki` 상위 문서의 operating doc discoverability가 상대적으로 약하다

엔지니어 판정:

- 설계 자체는 sound
- detached repo-only 운영 설명력은 `usable`

## Reviewer Review

검수자 관점에서 가장 중요하게 본 것은 세 가지다.

1. source-of-truth ownership이 헷갈리지 않는가
2. external action에 approval / audit gate가 붙는가
3. 두 저장소만 봐도 운영자가 잘못된 surface에서 행동하지 않도록 막는가

판단:

- 1번은 충분히 통과
- 2번도 문서 수준에서는 통과
- 3번은 대부분 통과하지만, failure report 부재와 company-wiki 상위 문서 discoverability가 경고 수준으로 남아 있다

검수자 판정:

- `block 없음`
- `warn 없음`

## Director Review

디렉터 관점에서 이번 단계의 질문은 단순하다.

`이제 detached 회사 저장소 두 개만 열어도, 실제 업무 시작 전까지의 운영 설명이 독립적으로 가능한가`

답:

- 거의 가능하다
- 다만 아직 `완전히 닫혔다`고 말하기에는 작은 빈틈이 있다

좋은 점:

- 구조 언어가 일관되다
- authoring / execution / approval / audit 경계가 이제 다른 데스크탑에서도 따라가기 쉬워졌다
- upstream 위키를 안 봐도 큰 그림을 이해하기 시작했다

디렉터 최종 판정:

- `Phase 3 approved`

## Final Status

- `block`: 0
- `warn`: 0
- `final`: `Phase 3 approved`

## Related

- [[projects/detached-workspace-repo-migration-review-and-plan]]
- [[projects/company-wiki-internal-structure]]
- [[projects/company-assistant-ops-internal-structure]]
- [[projects/company-domain-template-set]]
