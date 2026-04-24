---
title: "company-assistant-ops 내부 구조 설계"
created: "2026-04-24"
updated: "2026-04-24"
type: project
sources: []
tags: [project, company, assistant, ops, gmail, calendar, sheets, audit, approval]
status: active
published: false
slug: ""
description: "회사 Gmail, Calendar, Sheets와 follow-up 실행을 다루는 company-assistant-ops 저장소의 내부 구조, approval, audit, handoff 규칙을 정의한 문서."
---

# company-assistant-ops 내부 구조 설계

이 문서는 `~/workspace/claude/company-assistant-ops`의 내부 구조를 정의한다.

핵심 전제:

- `company-assistant-ops`는 회사 도메인의 `execution surface`다
- Gmail, Calendar, Sheets 같은 외부 시스템 상호작용을 담당한다
- 이 저장소는 원본 업무 지식의 source-of-truth가 아니라, `approval / audit / execution`의 운영 레이어다
- 회의록, 기획, 검수, 테스트의 canonical markdown은 `company-wiki`에 남긴다
- credential과 OAuth token은 저장소 밖에서 runtime 주입한다

## 목적

`company-assistant-ops`는 다음을 위한 저장소다.

- 회사 Gmail/Calendar/Sheets read 결과를 작업용 컨텍스트로 정리한다
- 일정 후보, follow-up, 보고 초안을 만든다
- 승인 후 외부 write를 실행한다
- 실행 결과를 audit-friendly 형태로 남긴다
- `company-wiki`와 `shared-agent-harness` 사이에서 회사 도메인의 외부 실행 게이트 역할을 한다

즉 이 저장소는 `회사 업무의 외부 시스템 실행 하네스`이지, 회사 위키나 업무 기록 저장소가 아니다.

## 이 저장소에 들어가야 하는 것

- approval matrix
- audit log
- action queue
- Gmail/Calendar/Sheets adapter 설정 템플릿
- preview payload
- execution report
- handoff template
- read/suggest/write 단계별 정책 문서

## 이 저장소에 들어가면 안 되는 것

- 회사 회의록 원문
- 기획 문서 원문
- 검수 결과 원문 source-of-truth
- 개인 도메인 데이터
- 실제 OAuth token, refresh token, API key
- mailbox full export
- calendar 전체 export를 canonical source처럼 보관하는 일

## 권장 최상위 구조

```text
company-assistant-ops/
├── README.md
├── AGENTS.md
├── CLAUDE.md
├── ARCHITECTURE.md
├── docs/
│   ├── operating/
│   ├── templates/
│   └── adr/
├── inbox/
├── actions/
├── approvals/
├── audit/
├── adapters/
├── state/
├── scripts/
└── tests/
```

## 파일/폴더별 책임

### 루트 문서

#### `README.md`

- 저장소 목적
- 다루는 외부 시스템
- `company-wiki`와의 경계
- 빠른 시작

#### `AGENTS.md`

- 외부 write 제약
- secrets boundary
- approval 없이는 실행하지 않는 규칙

#### `CLAUDE.md`

- `@AGENTS.md`
- Claude surface에서의 회사 assistant 실행 제약

#### `ARCHITECTURE.md`

- read / suggest / write-with-approval / high-risk write 계층
- `company-wiki` handoff 구조
- adapter boundary
- audit와 state 책임

### `docs/operating/`

권장 문서:

- `operations.md`
  - assistant 실행 순서
- `approval-matrix.md`
  - Gmail/Calendar/Sheets별 승인 레벨
- `audit-policy.md`
  - 무엇을 언제 기록하는지
- `handoff-policy.md`
  - `company-wiki`와 주고받는 payload 규칙
- `credential-policy.md`
  - token/runtime 주입 규칙

### `docs/templates/`

권장 템플릿:

- `calendar-request.md`
- `followup-request.md`
- `report-request.md`
- `approval-record.md`
- `execution-report.md`
- `failure-report.md`

### `docs/adr/`

장기 판단 기록:

- why assistant ops is separate from company wiki
- why write actions require approval
- why tokens stay outside the repo

### `inbox/`

목적:

- 아직 분류되지 않은 assistant request
- 외부 시스템 read 결과 중 임시 정리본

원칙:

- 장기 보관용이 아니다
- 정리 후 `actions/`, `approvals/`, `audit/` 또는 `state/`로 이동

### `actions/`

목적:

- 실행 전 작업 단위 관리

포함:

- 일정 생성 요청
- follow-up 초안 요청
- 보고 초안 요청
- 시트 업데이트 요청

상태 예시:

- `draft`
- `awaiting-approval`
- `approved`
- `executed`
- `failed`

### `approvals/`

목적:

- 명시적 승인 기록

포함:

- 누가 승인했는지
- 언제 승인했는지
- 어떤 범위까지 승인했는지
- 어떤 payload를 기준으로 승인했는지

중요:

- write-with-approval 이상 단계는 여기 기록이 없으면 실행하지 않는다

### `audit/`

목적:

- 실행 결과와 예외 상황 기록

포함:

- 외부 write 실행 결과
- 실패 이유
- 재시도 여부
- 민감정보 노출 여부 점검

원칙:

- audit는 최소 충분성으로 남긴다
- token 값, 메일 본문 전체, 민감 원문 dump는 피한다

### `adapters/`

목적:

- 외부 시스템 wrapper/adapter 정의

권장 구조:

```text
adapters/
  gmail/
  calendar/
  sheets/
```

포함:

- adapter readme
- env/keychain variable name
- dry-run 규칙
- payload schema

중요:

- 실제 token은 두지 않는다
- adapter는 runtime credential injection을 전제로 한다

### `state/`

목적:

- 실행용 파생 상태
- queue summary
- recent execution summary

원칙:

- canonical source가 아니다
- 스크립트 또는 실행 흐름으로 생성한다
- hand-edit를 피한다

예:

- `action-queue.json`
- `recent-executions.json`
- `approval-summary.json`

### `scripts/`

허용:

- dry-run helper
- payload validator
- approval checker
- execution logger
- adapter smoke test

금지:

- token을 하드코딩한 스크립트
- 승인 없이 바로 high-risk write를 실행하는 스크립트

### `tests/`

목적:

- adapter payload validation
- approval gate validation
- audit log schema validation

## 실행 계층

### Phase A. Read-only

허용:

- Gmail 읽기
- Calendar 읽기
- Sheets 읽기
- 회의 follow-up에 필요한 컨텍스트 수집

### Phase B. Suggest-only

허용:

- 메일 초안 제안
- 일정 후보 제안
- 시트 업데이트 초안 제안
- 보고 초안 제안

### Phase C. Write-with-approval

허용:

- Calendar event 생성
- Sheets 행 추가/수정
- 메일 draft 저장

조건:

- 명시적 승인 필요
- approval record 필요
- audit 기록 필요

### Phase D. High-risk write

허용 가능:

- Gmail send
- Calendar update/delete
- 외부 공유 권한 변경

조건:

- 별도 승인 정책
- dry-run 또는 preview 선행
- failure rollback 또는 대응 절차 정의

## `company-wiki`와의 handoff 규칙

### `company-wiki -> company-assistant-ops`

받는 것:

- action item 요약
- 일정 반영 요청
- follow-up 메일 요청
- 보고 초안 요청

형식:

- decision-grade summary
- 필요한 최소 필드만
- 원문 전체 복제 금지

### `company-assistant-ops -> company-wiki`

돌려주는 것:

- 실행 결과 요약
- 일정 반영 여부
- follow-up 발송 여부
- 실패/보류 사유

원칙:

- 외부 시스템 원본은 외부 시스템에 남기고
- `company-wiki`에는 업무 판단에 필요한 summary만 남긴다

## approval와 audit 원칙

기본 원칙:

- read-only는 audit 간소화 가능
- suggest-only는 preview 중심
- write-with-approval 이상은 approval + audit 둘 다 필수
- high-risk write는 별도 escalation 절차 필요

필수 항목:

- 요청자
- 승인자
- 대상 시스템
- 실행 시각
- 결과 상태
- 후속 조치 필요 여부

## 검수와 2-agent cross-validation

`company-assistant-ops`도 공식 변경과 실행 정책 검수에는 2-agent cross-validation을 적용한다.

최소 적용 범위:

- approval matrix 변경
- credential policy 변경
- adapter payload schema 변경
- high-risk write 정책 변경
- audit schema 변경

권장 적용 범위:

- 새로운 Gmail/Calendar/Sheets workflow 추가
- automation script 변경

원칙:

- 가능한 한 다른 agent surface 또는 다른 review path 사용
- 같은 모델 + 같은 checklist + 같은 prompt 반복은 교차검증이 아니다

## confidentiality와 최소 저장 원칙

원칙:

- 이 저장소는 실행 레이어이므로 민감한 원문을 오래 들고 있으면 안 된다
- 필요한 최소 실행 정보와 audit summary만 저장한다
- credentials는 저장소 밖에서 runtime 주입한다

권장 구분:

- `internal`
  - 일반 실행 메타데이터
- `restricted`
  - 승인 기록, 실패 원인, 제한적 payload summary

## 구현 우선순위

### Phase 1

- 루트 문서 4개
- `docs/operating/`
- `actions/`
- `approvals/`
- `audit/`
- `adapters/`

### Phase 2

- `state/`
- `scripts/`
- `tests/`
- Gmail/Calendar/Sheets adapter 템플릿

### Phase 3

- high-risk write escalation flow
- rollback / failure handling 강화
- assistant workflow별 세부 템플릿

## 다음 단계

- `company-wiki`용 handoff 템플릿 정의
- assistant request / approval / execution report 템플릿 초안 작성
- 회사 도메인 approval matrix 분리

현재 반영:

- [[projects/company-domain-template-set]]

## 관련 페이지

- [[projects/assistant-ops-lane-execution-draft]]
- [[projects/company-wiki-internal-structure]]
- [[projects/dual-domain-agent-operating-model]]
- [[projects/shared-agent-harness-internal-structure]]
- [[projects/workspace-security-boundary]]
- [[projects/immediate-agent-operating-structure]]
