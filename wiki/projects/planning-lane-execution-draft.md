---
title: "Planning Lane 실행안 초안"
created: "2026-04-23"
updated: "2026-04-23"
type: project
sources: []
tags: [project, planning, workflow, harness, agents, presentation, direction]
status: draft
published: false
slug: ""
description: "기획, 디렉팅, PT 구조, 실행 계획을 다루는 Planning Lane의 실행 흐름과 독립 agent 분리 기준을 정리한 초안."
---

# Planning Lane 실행안 초안

`Planning Lane`은 기획, 디렉팅, PT 구조, 우선순위 정리, 실행 계획 수립을 담당한다. 초기에는 독립 `Planning Agent`를 두지 않고 기존 역할 안에서 운영하되, 일정 기준을 넘으면 별도 agent로 분리한다.

## 목적

- 작업 착수 전에 목표, 범위, 검증 기준을 먼저 고정한다
- `ai-survival-log`와 `ai-survival-log-site` 양쪽에 걸친 변경을 한 장의 실행 계획으로 정리한다
- PT 발표, 문서 기획, 코딩 작업의 선행 판단을 공통 포맷으로 관리한다

## 입력

- 사용자 요청
- 관련 project/wiki 문서
- publish contract, validation matrix, architecture 문서
- 필요 시 Research Lane 산출물

## 출력

- 실행 계획
- PRD 초안
- PT 구조 초안
- 우선순위 및 범위 결정 메모
- 검증 계획

## 기본 실행 흐름

1. 요청을 `content`, `engineering`, `publish`, `assistant`, `presentation` 중 어떤 성격인지 분류한다
2. 관련 저장소가 `ai-survival-log`, `ai-survival-log-site`, 외부 assistant 시스템 중 어디인지 결정한다
3. 결과물과 계약을 정리한다
4. 변경 범위와 제외 범위를 적는다
5. 검증 경로를 붙인다
6. 이후 lane으로 handoff한다

## 현재 단계의 운영 방식

초기에는 독립 `Planning Agent`를 만들지 않는다.

- 주 에이전트 또는 `Authoring Agent`의 planning mode로 운영
- planning 결과물은 wiki project 문서 또는 관련 docs로 남김
- review 없이 곧바로 implementation으로 넘어가지 않음

## 독립 agent 분리 기준

다음 중 3개 이상이 동시에 성립하면 독립 `Planning Agent` 분리를 검토한다.

- 한 주에 planning 전용 작업이 3회 이상 반복된다
- PT/기획/디렉팅 결과물이 구현 작업과 별도 품질 기준을 갖기 시작한다
- `ai-survival-log`와 `ai-survival-log-site`를 동시에 건드리는 cross-repo 계획이 자주 생긴다
- planning 산출물의 포맷이 반복적으로 재사용된다
- planning 결과물 검토와 구현 검토를 분리할 필요가 커진다

다음 중 하나라도 성립하면 분리를 강하게 권장한다.

- 발표자료 구조와 엔지니어링 계획을 별도 owner가 검토해야 한다
- 사용자가 planning 산출물만 반복적으로 요청한다
- assistant ops와 연결되어 일정/회의/action item까지 planning 흐름에 포함되기 시작한다

## 분리 후 권한 경계

독립 `Planning Agent`는 다음 권한만 가진다.

- repo read
- 문서 초안 작성
- 계획 문서 생성/수정
- 외부 시스템 read 또는 suggest

직접 가지지 않는 권한:

- 코드 수정 확정
- publish 실행
- Gmail send
- Calendar/Sheets write without approval

## Review 연결

Planning Lane 산출물은 구현 전 다음을 확인해야 한다.

- 범위가 명확한가
- 검증 계획이 있는가
- source-of-truth와 derived artifact 경계를 침범하지 않는가
- cross-repo 변경이면 downstream 영향이 명시됐는가

## 다음 단계

- planning 템플릿 표준화
- PT 구조 초안용 포맷 정의
- cross-repo 변경용 planning checklist 정의

## 관련 페이지

- [[projects/managed-agent-harness-draft]]
- [[projects/cross-repo-ai-automation-lab]]
- [[projects/repo-structure-refactor]]
