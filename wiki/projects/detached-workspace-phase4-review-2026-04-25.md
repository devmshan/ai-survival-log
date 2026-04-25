---
title: "Detached Workspace Phase 4 Review"
created: "2026-04-25"
updated: "2026-04-25"
type: project
sources: []
tags: [project, review, migration, detached-workspace, history-source, operations]
status: active
published: false
slug: ""
description: "upstream 위키가 operational source가 아니라 history/rationale/meta planning 역할로 충분히 내려갔는지 점검한 Phase 4 합동 리뷰 문서."
---

# Detached Workspace Phase 4 Review

## Review Scope

이번 리뷰는 `ai-survival-log/wiki/projects/` 안의 상위 구조 문서들이 이제 정말 `history/rationale/meta planning` 역할로 읽히는지 점검한다.

즉 질문은 하나다.

`upstream 위키를 먼저 열어도, 현재 운영 규칙은 detached repo를 먼저 봐야 한다는 사실이 충분히 드러나는가`

주요 검토 대상:

- [[projects/dual-domain-agent-operating-model]]
- [[projects/workspace-folder-structure-review-sheet]]
- [[projects/shared-agent-harness-migration-list]]
- [[projects/shared-agent-harness-executable-surface-phase1]]
- [[projects/shared-agent-harness-executable-review-gate]]
- [[projects/workspace-security-boundary]]
- [[projects/detached-workspace-repo-migration-review-and-plan]]

## Findings

초기 리뷰 시 경고 2개가 있었지만, 둘 다 수리됐다.

### fixed 1. `warn` — 일부 upstream 문서가 여전히 detached repo보다 upstream 읽기 순서를 암묵적으로 앞세운다

조치:

- [[projects/workspace-folder-structure-review-sheet]]의 읽기 순서를 detached repo 우선 구조로 재정렬

현재 상태:

- upstream에서 시작해도 detached repo 운영 문서를 먼저 보게 만드는 흐름이 더 분명해졌다.

### fixed 2. `warn` — 일부 문서의 표현이 아직 “승격 중”이라 현재 상태를 약하게 보이게 한다

조치:

- [[projects/company-wiki-internal-structure]]
- [[projects/company-assistant-ops-internal-structure]]
- [[projects/shared-agent-harness-internal-structure]]
의 `Source Status`를 현재형으로 정리

현재 상태:

- 핵심 internal-structure 문서도 detached repo가 현재 operational source라는 점을 더 단호하게 표현한다.

## Planner Review

기획자 관점에서는 큰 방향이 맞다.

좋은 점:

- 이제 upstream 문서 다수가 `왜 이렇게 됐는가`를 설명하는 역할로 읽힌다
- detached repo를 현재 운영 source로 보라는 문장이 문서 상단에 들어가 있다
- shared/company 분리와 source ownership이 문서적으로 정리됐다

부족한 점:

- 사용자가 빠르게 읽을 때는 섹션 배치가 더 중요하다
- `먼저 읽을 문서` 같은 옛 구조가 남아 있으면, history source라 해도 사실상 upstream 문서를 다시 operational entry로 쓰게 된다

기획자 판정:

- `approved`

## Engineer Review

엔지니어 관점에서는 구조적 목표는 거의 달성됐다.

좋은 점:

- detached repo와 upstream 위키 사이 역할 분담이 명시적이다
- `shared-agent-harness`는 공용 rule source
- `company-wiki`는 authoring source
- `company-assistant-ops`는 execution/approval/audit source

부족한 점:

- 상태 표현이 일부 문서에서 과도하게 과도기적이다
- 문장 하나 차이지만, 운영자가 읽을 때 “아직 upstream이 기준인가?”라는 오해를 남길 수 있다

엔지니어 판정:

- 설계는 `sound`
- Phase 4는 `almost closed`

## Reviewer Review

검수자 관점의 핵심 기준은 두 가지다.

1. upstream 문서가 detached repo보다 앞에 서지 않는가
2. 현재 operational source 위치가 빠르게 식별 가능한가

판단:

- 1번은 대부분 해결됐지만 `workspace-folder-structure-review-sheet`에서 부분적으로 흔적이 남아 있다
- 2번도 대부분 해결됐지만, 몇몇 문서의 상태 표현이 덜 단호하다

검수자 판정:

- `block 없음`
- `warn 없음`

## Director Review

디렉터 관점에서 이번 단계의 질문은 이겁니다.

`이제 ai-survival-log/wiki/projects는 운영 설명서가 아니라 구조적 히스토리 문서로 이해해도 되는가`

답:

- 그렇다

좋은 점:

- detached repo 중심 운영 모델이 문서상으로도 보이기 시작했다
- upstream 위키는 이제 설계 배경과 migration rationale 역할로 읽힌다

디렉터 최종 판정:

- `Phase 4 approved`

## Final Status

- `block`: 0
- `warn`: 0
- `final`: `Phase 4 approved`

## Related

- [[projects/detached-workspace-repo-migration-review-and-plan]]
- [[projects/detached-company-domain-phase3-review-2026-04-25]]
