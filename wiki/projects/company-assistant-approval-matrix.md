---
title: "회사 Assistant approval matrix 세부안"
created: "2026-04-24"
updated: "2026-04-24"
type: project
sources: []
tags: [project, company, assistant, approval, matrix, gmail, calendar, sheets]
status: active
published: false
slug: ""
description: "company-assistant-ops에서 Gmail, Calendar, Sheets 작업에 어떤 승인 레벨을 적용할지 정리한 세부안."
---

# 회사 Assistant approval matrix 세부안

이 문서는 `company-assistant-ops`에서 Gmail, Calendar, Sheets 작업에 적용할 승인 레벨을 정리한다.

## 승인 레벨

### Level 0. Read-only

설명:

- 읽기만 가능
- 외부 상태 변경 없음

예:

- Gmail 읽기
- Calendar 읽기
- Sheets 읽기

기록:

- 간단한 audit 또는 access log 수준

### Level 1. Suggest-only

설명:

- 초안이나 후보만 생성
- 외부 상태 변경 없음

예:

- 메일 초안 제안
- 일정 후보 제안
- 시트 업데이트 초안 제안

기록:

- request
- preview

### Level 2. Write-with-approval

설명:

- 승인 후 제한적 write 가능

예:

- Calendar event 생성
- Sheets 행 추가/수정
- Gmail draft 저장

필수:

- approval-record
- execution-report

### Level 3. High-risk write

설명:

- 실질적 외부 영향이 큰 write

예:

- Gmail send
- Calendar update/delete
- 외부 공유 권한 변경

필수:

- 별도 승인
- dry-run 또는 preview
- execution-report
- 필요 시 failure/rollback 절차

## 시스템별 적용

### Gmail

| 작업 | 승인 레벨 | 비고 |
|---|---|---|
| 메일 읽기 | Level 0 | 원문 dump 금지 |
| 메일 초안 생성 | Level 1 | preview만 |
| draft 저장 | Level 2 | 명시적 승인 필요 |
| 메일 발송 | Level 3 | 가장 보수적으로 운영 |

### Google Calendar

| 작업 | 승인 레벨 | 비고 |
|---|---|---|
| 일정 읽기 | Level 0 | read-only |
| 일정 후보 제안 | Level 1 | 시간/참석자/제약만 정리 |
| event 생성 | Level 2 | 승인 후 생성 |
| event 수정/삭제 | Level 3 | high-risk write |

### Google Sheets

| 작업 | 승인 레벨 | 비고 |
|---|---|---|
| 시트 읽기 | Level 0 | read-only |
| row/column update 초안 | Level 1 | preview only |
| row 추가/수정 | Level 2 | 승인 필요 |
| 구조 변경/공유 변경 | Level 3 | high-risk write |

## 시나리오별 권장 레벨

### 회의 후 일정 후보 생성

- 후보 제안: Level 1
- 실제 event 생성: Level 2

### 회의 후 follow-up 메일

- 초안 생성: Level 1
- draft 저장: Level 2
- send: Level 3

### 주간 보고 + 시트 반영

- 보고 초안: Level 1
- 시트 반영: Level 2
- 공유 권한 변경 포함 시: Level 3

## block 조건

- Level 2 이상인데 approval-record가 없음
- Level 3인데 dry-run 또는 preview 없이 실행
- 요청 system과 승인 level이 맞지 않음
- Gmail send를 Level 2처럼 취급

## escalate 조건

- 승인 레벨 기준 자체를 바꾸는 경우
- Level 3 범위를 넓히거나 줄이는 경우
- 새로운 외부 시스템을 추가하는 경우

## 다음 단계

- `company-assistant-ops/docs/operating/approval-matrix.md`로 materialize
- dry-run 시나리오에 이 레벨을 연결

## 관련 페이지

- [[projects/company-assistant-ops-internal-structure]]
- [[projects/company-assistant-dry-run-scenarios]]
- [[projects/company-domain-review-checklist-operations]]
