---
title: "회사 Assistant workflow dry-run 시나리오"
created: "2026-04-24"
updated: "2026-04-24"
type: project
sources: []
tags: [project, company, assistant, dry-run, workflow, gmail, calendar, sheets]
status: active
published: false
slug: ""
description: "company-assistant-ops를 실제로 운영하기 전에 검증할 수 있도록 일정, follow-up, 보고 흐름의 dry-run 시나리오를 정의한 문서."
---

# 회사 Assistant workflow dry-run 시나리오

이 문서는 `company-assistant-ops`를 실제 외부 시스템과 연결하기 전에 검증할 dry-run 시나리오를 정의한다.

목적:

- handoff 필드가 충분한지 확인
- approval / audit 흐름이 자연스러운지 확인
- `company-wiki`와 `company-assistant-ops`의 경계가 잘 지켜지는지 확인

## 공통 원칙

- 실제 Gmail/Calendar/Sheets write는 하지 않는다
- 모든 시나리오는 `preview payload`와 `execution report mock`까지만 생성한다
- 결과는 `company-wiki` summary와 `company-assistant-ops` action/approval/audit 관점으로 함께 점검한다

## 시나리오 1. 회의 후 일정 후보 생성

### 상황

- 주간 회의가 끝났다
- 다음 주 follow-up 미팅 1회가 필요하다
- 참석자는 4명이다

### 입력

- `company-wiki/meetings/`의 `meeting-note`
- `Action Items`
- `Follow-up for Assistant Ops`

### dry-run 단계

1. `meeting-note`에서 일정 관련 action item만 추출
2. `calendar-request` 초안 생성
3. 참석자, 희망 시간대, 제약 조건을 payload summary로 정리
4. approval 필요 여부를 판단
5. 실행 대신 `execution-report mock` 생성
6. `company-wiki`에 `일정 후보 생성 완료, 실행 대기` summary를 남긴다고 가정

### 확인 포인트

- 회의 note만으로 일정 요청 필드가 충분한가
- 불필요한 원문 복제가 없는가
- approval 단계가 자연스럽게 끼어드는가

## 시나리오 2. 회의 후 follow-up 메일 초안

### 상황

- 회의 결정 사항을 참석자와 공유해야 한다
- 실제 발송은 승인 후에만 한다

### 입력

- `meeting-note`
- `Decisions`
- `Action Items`

### dry-run 단계

1. `followup-request` 초안 생성
2. 대상 그룹과 메시지 목적을 분리
3. 메일 초안을 payload preview로 생성
4. `approval-record draft` 생성
5. 발송 대신 `execution-report mock` 생성

### 확인 포인트

- `meeting-note`의 어떤 필드가 follow-up 초안 품질에 핵심인지
- 너무 긴 원문을 assistant surface로 넘기지 않는지
- 발송 전 검수 포인트가 충분한지

## 시나리오 3. 주간 보고 초안 + 시트 반영

### 상황

- 한 주간 진행 상황을 요약해야 한다
- 일부 항목은 Google Sheets에 반영해야 한다

### 입력

- 관련 `project-brief`
- 최근 `review-report`
- 최근 `test-result`

### dry-run 단계

1. `report-request` 초안 생성
2. 요약용 bullet과 시트 반영용 row payload를 분리
3. `Sheets update preview` 생성
4. 승인 필요 범위를 표시
5. 실행 대신 `failure-report / execution-report mock` 중 하나를 시뮬레이션

### 확인 포인트

- `company-wiki`의 어떤 page type 조합이 보고용으로 가장 자연스러운지
- summary와 structured update가 같은 템플릿으로 충분한지
- 시트 반영은 어떤 approval level이 필요한지

## 시나리오 4. 실행 실패와 재시도

### 상황

- approval은 받았지만 external adapter가 실패했다고 가정한다

### dry-run 단계

1. 실패 원인을 `failure-report`에 기록
2. retry 가능 여부를 판단
3. `company-wiki`에는 `실행 실패 / 재시도 필요` 요약만 남긴다고 가정

### 확인 포인트

- 실패를 `company-wiki`와 `company-assistant-ops`에 각각 어떻게 최소 기록할지
- token, raw payload, 민감 원문을 남기지 않고도 충분히 복기 가능한지

## 각 시나리오에서 공통으로 점검할 것

- source wiki page가 항상 존재하는가
- 요청이 `reason`, `target_system`, `approval_level`을 갖는가
- approval 없이 write로 넘어가는 경로가 없는가
- `execution-report mock`만으로도 audit 설계가 충분히 검토되는가

## 실행 우선순위

1. 시나리오 1: 일정 후보 생성
2. 시나리오 2: follow-up 메일 초안
3. 시나리오 3: 주간 보고 + 시트 반영
4. 시나리오 4: 실패와 재시도

## 다음 단계

- 각 시나리오를 템플릿 예시 파일로 materialize
- approval matrix 세부안에 시나리오별 승인 레벨 반영
- 실제 저장소 생성 순서는 [[projects/company-domain-template-materialization-plan]] 참고

## 관련 페이지

- [[projects/company-assistant-ops-internal-structure]]
- [[projects/company-domain-template-set]]
- [[projects/company-domain-review-checklist-operations]]
