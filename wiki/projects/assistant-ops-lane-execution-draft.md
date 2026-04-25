---
title: "Assistant Ops Lane 실행안 초안"
created: "2026-04-23"
updated: "2026-04-23"
type: project
sources: []
tags: [project, assistant, workflow, ops, calendar, gmail, sheets, harness]
status: draft
published: false
slug: ""
description: "일정관리, 할 일 보고, 회의 follow-up을 다루는 Assistant Ops Lane의 실행 흐름과 독립 agent 분리 기준을 정리한 초안."
---

# Assistant Ops Lane 실행안 초안

## Source Status

- 이 문서는 `Assistant Ops Lane`의 초기 설계 이유와 단계별 도입 판단을 보관하는 `history retained here` 문서다.
- 현재 회사 도메인 execution/approval/audit의 detached `operational source`는 `company-assistant-ops` 저장소 문서를 우선 기준으로 본다.
- 특히 다음 문서를 우선 참조한다.
  - `company-assistant-ops/README.md`
  - `company-assistant-ops/ARCHITECTURE.md`
  - `company-assistant-ops/docs/operating/operations.md`
  - `company-assistant-ops/docs/operating/approval-matrix.md`

`Assistant Ops Lane`은 Gmail, Google Calendar, Google Sheets, 회의 메모 같은 외부 운영 시스템을 다루는 lane이다. 현재 계획에서는 회사 도메인 전용 lane으로 본다. 이 lane은 저장소 작업과 권한 경계가 다르므로, planning이나 authoring보다 더 보수적으로 분리한다.

## 목적

- 일정관리와 할 일 보고를 구조화한다
- 회의 메모를 action item과 follow-up으로 바꾼다
- 외부 시스템과 상호작용할 때 approval, audit, secrets boundary를 먼저 세운다

## 입력

- 회의록 또는 메모
- 일정 관련 요청
- 보고 요청
- Gmail/Calendar/Sheets의 read 결과

## 출력

- 일정 후보
- action item 목록
- follow-up 초안
- 보고용 summary
- 시트 반영 초안

## 기본 실행 흐름

1. 요청을 `meeting`, `schedule`, `report`, `follow-up` 중 하나로 분류한다
2. 필요한 외부 시스템이 Gmail, Calendar, Sheets 중 무엇인지 결정한다
3. 먼저 read-only 컨텍스트를 수집한다
4. 모델은 suggestion 초안만 만든다
5. 사용자가 승인하면 외부 write로 넘긴다
6. 실행 결과는 audit-friendly 형태로 기록한다

## 단계별 도입 원칙

### Phase A. Read-only

- Gmail 읽기
- Calendar 읽기
- Sheets 읽기
- 회의 메모와 기존 일정 파악

### Phase B. Suggest-only

- 메일 초안 제안
- 일정 후보 제안
- 시트 업데이트 초안 제안
- 주간 보고 초안 제안

### Phase C. Write-with-approval

- Calendar event 생성
- Sheets 행 추가/수정
- 메일 draft 저장

### Phase D. High-risk write

- Gmail send
- Calendar update/delete
- 외부 공유 권한 변경

이 단계는 가장 나중에 연다.

## 현재 단계의 운영 방식

초기에는 독립 `Assistant Ops Agent`를 만들지 않는다.

- 주 에이전트가 assistant mode로 수행
- 외부 시스템은 read-first, suggest-first만 허용
- 실제 write는 전부 명시적 승인 뒤에만 가능

## 독립 agent 분리 기준

다음 중 3개 이상이 동시에 성립하면 독립 `Assistant Ops Agent` 분리를 검토한다.

- 일정관리/회의 follow-up 작업이 주 3회 이상 반복된다
- Gmail, Calendar, Sheets를 동시에 다루는 요청이 잦다
- read 결과를 바탕으로 반복적인 suggestion 포맷이 생긴다
- audit log와 approval trace를 별도 관리할 필요가 커진다
- assistant 작업이 repo 작업과 다른 cadence로 지속된다

다음 중 하나라도 성립하면 분리를 강하게 권장한다.

- 외부 write 액션이 일상화된다
- 개인 일정/보고 데이터와 프로젝트 데이터의 경계를 강하게 분리해야 한다
- 사용자가 assistant lane만 별도로 위임하고 싶어 한다

## 분리 후 권한 경계

독립 `Assistant Ops Agent`는 다음 권한만 가진다.

- 외부 시스템 read
- draft/suggestion 생성
- approval 이후 제한적 write

직접 가지지 않는 권한:

- repo 코드 수정
- publish 실행
- source-of-truth wiki 직접 변경

필수 정책:

- secrets와 OAuth token은 모델 컨텍스트에 직접 주지 않음
- write 전 preview 제공
- high-risk write는 항상 explicit approval 필요

## Review 연결

Assistant Ops Lane에서도 review가 필요하다.

- 요청이 외부 write를 요구하는가
- 일정/보고 초안에 누락이 있는가
- 민감정보가 summary에 노출되는가
- repo 작업과 외부 assistant 작업이 섞였는가

## 다음 단계

- Calendar read/suggest 시나리오 1건 시범 적용
- meeting note -> action items 템플릿 정의
- Sheets update preview 포맷 정의

현재 반영:

- [[projects/company-assistant-ops-internal-structure]]

## 관련 페이지

- [[projects/dual-domain-agent-operating-model]]
- [[projects/managed-agent-harness-draft]]
- [[projects/cross-repo-ai-automation-lab]]
