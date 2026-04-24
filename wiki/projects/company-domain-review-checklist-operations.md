---
title: "회사 도메인 review/checklist 운영 규칙"
created: "2026-04-24"
updated: "2026-04-24"
type: project
sources: []
tags: [project, company, review, checklist, qa, validation, audit, operations]
status: active
published: false
slug: ""
description: "company-wiki와 company-assistant-ops에서 공식 검수 게이트를 어떻게 운영할지, primary/secondary review, checklist, severity 규칙을 정의한 문서."
---

# 회사 도메인 review/checklist 운영 규칙

이 문서는 회사 도메인에서 공식 검수 게이트를 어떻게 운영할지 정의한다.

범위:

- `company-wiki`
- `company-assistant-ops`
- 두 저장소를 연결하는 handoff와 execution 정책

핵심 전제:

- 공식 완료 처리는 `primary review`와 `secondary review`를 모두 거친 뒤에만 가능하다
- 가능한 한 서로 다른 agent surface 또는 다른 review path를 사용한다
- 같은 모델 + 같은 checklist + 같은 prompt 반복은 교차검증으로 보지 않는다
- 회사 도메인에서는 품질뿐 아니라 `보안`, `승인`, `감사 추적`이 같이 검수 대상이다

## 목적

이 규칙의 목적은 세 가지다.

- 회사 도메인에서 검수 누락을 줄인다
- 외부 시스템 write와 연결되는 변경에 보수적으로 대응한다
- `company-wiki`와 `company-assistant-ops`의 역할 경계를 흔들지 않는다

## 검수 대상 분류

### A. 문서성 변경

예:

- 회의록 정리
- planning brief 수정
- project brief 업데이트
- review report 작성
- test result 정리

기본 성격:

- `company-wiki` 중심
- 구조보다 내용 품질과 누락 여부가 중요

### B. 구조/정책 변경

예:

- page type 변경
- frontmatter 규칙 변경
- handoff 필드 변경
- approval matrix 변경
- audit policy 변경

기본 성격:

- `company-wiki`와 `company-assistant-ops` 모두 영향 가능
- contract-sensitive 변경

### C. 실행/외부 시스템 변경

예:

- Gmail/Calendar/Sheets request 흐름 추가
- adapter payload schema 변경
- execution script 변경
- write policy 변경

기본 성격:

- `company-assistant-ops` 중심
- approval/audit/security 점검이 필수

## review path 정의

### `primary review`

목적:

- 변경이 의도한 목표를 충족하는지 먼저 확인

주로 본다:

- 범위 적합성
- 누락된 필드
- 문서 구조
- 명백한 정책 위반

### `secondary review`

목적:

- 다른 관점에서 다시 본다

주로 본다:

- 보안/승인 누락
- handoff 경계 위반
- checklist 사각지대
- unresolved risk

원칙:

- 가능하면 다른 agent surface 사용
- 같은 surface를 써야 하면 checklist, prompt, evaluation focus를 다르게 한다

## checklist 묶음

### 1. `company-wiki content checklist`

대상:

- `meeting-note`
- `project-brief`
- `planning-brief`
- `review-report`
- `test-plan`
- `test-result`

질문:

- 목적과 범위가 선명한가
- 관련 프로젝트/회의/테스트 링크가 필요한 만큼 연결됐는가
- action item이 실행 가능한 단위인가
- 외부 시스템 실행이 필요한 경우 `company-assistant-ops` handoff가 명확한가
- 민감 원문을 과하게 넣지 않았는가

### 2. `cross-review checklist`

대상:

- `cross-review-report`
- 구조 변경
- 공식 completion gate

질문:

- `primary`와 `secondary`가 다른 surface 또는 다른 review path를 탔는가
- 두 검수 결과의 agreement/conflict가 정리됐는가
- unresolved finding이 남아 있지 않은가
- final gate decision이 명시됐는가

### 3. `assistant execution checklist`

대상:

- `calendar-request`
- `followup-request`
- `report-request`
- `approval-record`
- `execution-report`

질문:

- source wiki page가 있는가
- requested action과 target system이 명확한가
- approval level이 맞는가
- preview 또는 draft가 있는가
- audit 기록이 남는가
- 원문 전체 복제 없이 최소 필드만 전달하는가

### 4. `security and boundary checklist`

대상:

- approval policy 변경
- credential policy 변경
- adapter/schema 변경
- high-risk write 관련 변경

질문:

- credential이 저장소 안으로 들어오지 않는가
- `company-wiki`와 `company-assistant-ops`의 경계가 흐려지지 않는가
- 고위험 write에 escalation 경로가 있는가
- audit 필수 필드가 유지되는가

## 최소 검수 조합

### 문서성 변경

최소:

- `primary review`
- 필요 시 `company-wiki content checklist`

강화 조건:

- 외부 실행을 유발하면 `secondary review` 추가
- `restricted` note면 `secondary review` 권장

### 구조/정책 변경

최소:

- `primary review`
- `secondary review`
- `cross-review checklist`

필수:

- unresolved finding이 있으면 완료 불가

### 실행/외부 시스템 변경

최소:

- `primary review`
- `secondary review`
- `assistant execution checklist`
- `security and boundary checklist`

필수:

- approval/audit 누락 시 `block`
- high-risk write 경로 변경이면 `escalate`

## severity 규칙

### `warn`

예:

- 문서 표현은 거칠지만 구조와 정책은 유지
- related links가 다소 약함
- 템플릿 필드 일부가 권장 수준 미달

### `block`

예:

- required field 누락
- `company-wiki`와 `company-assistant-ops` 경계 위반
- approval 없이 write가 가능해지는 변경
- audit 필수 필드 누락
- 교차검증 없이 공식 completion 처리

### `escalate`

예:

- high-risk write 정책 변경
- approval matrix의 기준 변경
- handoff contract 변경
- credential policy 변경
- restricted note 운영 원칙 변경

## 기록 위치

### `company-wiki`

기록:

- `review-report`
- `cross-review-report`
- test 관련 판단 기록

적합:

- 판단과 결론을 남길 때

### `company-assistant-ops`

기록:

- `approval-record`
- `execution-report`
- `failure-report`

적합:

- 외부 실행과 승인, audit를 남길 때

## 운영 순서

### 문서 작업

1. 초안 작성
2. `primary review`
3. 필요 시 `secondary review`
4. conflict 정리
5. 최종 반영

### 외부 실행 연결 작업

1. request 작성
2. preview 생성
3. `primary review`
4. `secondary review`
5. approval 기록
6. 실행
7. execution report 작성
8. `company-wiki`에 summary 반영

## anti-pattern

금지:

- 같은 모델로 같은 프롬프트를 두 번 돌리고 교차검증이라 부르기
- approval 없이 write 실행
- `company-wiki`에 외부 시스템 원문 dump 남기기
- `company-assistant-ops`를 source-of-truth처럼 쓰기
- unresolved finding이 있는데 완료 처리하기

## 다음 단계

- 이 규칙을 실제 `company-wiki/templates/`와 `company-assistant-ops/docs/templates/` 파일로 materialize
- assistant workflow별 dry-run 예시 추가
- approval matrix 세부안 분리

현재 반영:

- [[projects/company-assistant-dry-run-scenarios]]
- [[projects/company-assistant-approval-matrix]]

## 관련 페이지

- [[projects/company-domain-template-set]]
- [[projects/company-wiki-internal-structure]]
- [[projects/company-assistant-ops-internal-structure]]
- [[projects/shared-agent-harness-internal-structure]]
- [[projects/workspace-security-boundary]]
