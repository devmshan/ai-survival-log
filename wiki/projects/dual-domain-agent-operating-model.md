---
title: "개인/회사 이중 도메인 Agent 운영 모델"
created: "2026-04-23"
updated: "2026-04-24"
type: project
sources: []
tags: [project, harness, operations, personal, company, security, agents]
status: active
published: false
slug: ""
description: "개인 일상업무와 회사업무를 분리하되, 공용 lane/agent와 도메인 전용 data/surface를 구분해 운영하는 구조 초안."
---

# 개인/회사 이중 도메인 Agent 운영 모델

이 문서는 업무를 `개인 일상업무`와 `회사업무` 두 도메인으로 분리하고, 어떤 프로젝트와 agent가 공용인지 전용인지 고정한다.

핵심 전제:

- `ai-survival-log`, `ai-survival-log-site`는 개인 일상업무 전용이다
- 회사 데이터는 개인 저장소와 섞지 않는다
- 회사업무용 wiki와 assistant surface는 별도로 둔다
- `Planning`, `Review`, `Engineering`, 일부 `Research`는 공용 역할과 lane으로 사용한다
- 분리의 기준은 역할이 아니라 `data`, `surface`, `account`, `permission`이다

## 도메인 구분

### 1. 개인 일상업무 도메인

포함 업무:

- wiki 지식수집
- 공부
- 블로그, 웹툰, 유튜브 콘텐츠 생산

사용 저장소:

- `ai-survival-log`
- `ai-survival-log-site`

허용 데이터:

- 개인 학습 자료
- 개인 콘텐츠 기획
- 공개 가능한 조사/초안/콘텐츠 자산

금지 데이터:

- 회사 회의록
- 회사 일정
- 회사 내부 검토 문서
- 회사 테스트/기획 데이터

### 2. 회사업무 도메인

포함 업무:

- 회의록
- 디렉팅
- 검수
- 테스트
- 기획
- 일정관리
- 보고와 follow-up

필요 저장소:

- 회사업무용 wiki 저장소
- 회사업무용 assistant/ops 저장소 또는 surface

사용 외부 시스템:

- 회사 Google Mail
- 회사 Google Calendar
- 회사 Google Sheets

보안 원칙:

- 회사 데이터는 개인 도메인으로 복사하지 않는다
- 회사 assistant access token과 credential은 개인 도메인에서 쓰지 않는다

## 공용과 전용 agent 구분

기본 원칙:

`role/lane is shared, data/surface is isolated`

즉:

- 같은 `Planning Lane`, `Review Lane`, `Engineering Lane`을 개인/회사 모두에서 재사용할 수 있다
- 하지만 그 lane이 접근하는 저장소, 계정, 캘린더, 문서 surface는 도메인별로 분리된다

### 공용 agent / lane

- `Planning Agent` / `Planning Lane`
- `Review Agent` / `Review Lane`
- `Engineering Agent` / `Engineering Lane`
- `Research Agent` / `Research Lane`의 기본 역할 정의

공용이라는 뜻:

- 역할 정의, workflow, checklist, quality bar를 공유한다
- 실행할 때는 개인/회사 도메인 컨텍스트를 명시적으로 선택한다

### 도메인 전용 agent / lane

- 개인 도메인 전용
  - `Authoring Agent`
  - `Publish Agent`
  - 개인 콘텐츠용 publish flow

- 회사 도메인 전용
  - 회사업무용 `Authoring Agent`
  - `Assistant Ops Agent` / `Assistant Ops Lane`
  - 회사 Gmail/Calendar/Sheets flow

전용이라는 뜻:

- 같은 역할 이름을 써도 연결되는 저장소와 데이터 경계가 다르다
- 특히 `Authoring`과 `Assistant Ops`는 도메인 분리가 강하다

## 프로젝트 구조 재정의

### 개인 도메인 프로젝트

1. `Personal Strategic Planning Project`
2. `Personal Upstream Knowledge Project`
3. `Personal Downstream Publishing Project`
4. `Personal Review and QA Project`
5. `Personal Engineering Execution Project`

### 회사 도메인 프로젝트

1. `Company Strategic Planning Project`
2. `Company Work Wiki Project`
3. `Company Review and QA Project`
4. `Company Assistant Operations Project`
5. `Company Engineering Execution Project`

### 공용 운영 모델

1. `Shared Planning Lane`
2. `Shared Review Lane`
3. `Shared Engineering Lane`
4. `Shared Research Lane`

## 새로 필요한 것

### 회사업무용 wiki

회사 업무를 위해 별도 wiki가 필요하다.

목적:

- 회의록 정리
- 기획 메모 관리
- 디렉팅/검수 기준 축적
- 내부 학습과 테스트 기록 정리

중요:

- 개인용 `ai-survival-log`와 물리적으로 분리
- 회사 보안 정책에 맞는 위치에 저장
- 개인 콘텐츠 프로젝트와 링크/동기화하지 않음

현재 반영:

- [[projects/company-wiki-internal-structure]]

### 회사용 Assistant Ops surface

목적:

- 회사 Gmail/Calendar/Sheets 관리
- action item과 일정 관리
- 보고 초안과 follow-up 생성

중요:

- 회사 계정만 연결
- read/suggest/write 권한을 별도 정책으로 관리
- audit trail 필요

현재 반영:

- [[projects/company-assistant-ops-internal-structure]]

## 역할 매핑

| 역할 | 개인 도메인 | 회사 도메인 | 공용 여부 |
|------|------|------|------|
| `Planning Agent` | 개인 콘텐츠/학습 계획 | 회사 기획/디렉팅/회의 follow-up 계획 | 공용 |
| `Research Agent` | 개인 학습/콘텐츠 조사 | 회사 업무 조사, 내부 허용 자료 조사 | 공용 |
| `Authoring Agent` | wiki/source/blog 초안 | 회사 wiki/회의록/기획 문서 | 전용 |
| `Engineering Agent` | scripts, site, automation 구현 | 회사용 automation/tooling 구현 | 공용 |
| `Review Agent` | publish/content/quality 검수 | 회사 문서/프로세스/테스트 검수 | 공용 |
| `Publish Agent` | 블로그/site handoff | 일반적으로 불필요 또는 회사 publishing 체계에 따라 별도 | 전용 |
| `Assistant Ops Agent` | 현재 미사용 | 회사 Gmail/Calendar/Sheets 관리 | 전용 |

## 공용 lane 재사용 방식

### `Planning Lane`

- 개인: 학습 계획, 콘텐츠 기획, PT 구조, 블로그/웹툰/유튜브 방향 정리
- 회사: 회의 후속, 업무 기획, 디렉팅, 프로젝트 실행 계획

### `Review Lane`

- 개인: 콘텐츠 품질, publish readiness, wiki consistency
- 회사: 문서 검수, 테스트 검토, deliverable quality check

공통 규칙:

- 공식 검수는 `2-agent cross-validation`을 기본으로 한다
- 가능한 한 서로 다른 surface 또는 다른 review path를 사용한다

### `Engineering Lane`

- 개인: `ai-survival-log`, `ai-survival-log-site`의 코드/자동화/테스트
- 회사: 회사 wiki/assistant/tooling 자동화와 테스트

### `Research Lane`

- 개인: 공개 자료 조사, 학습 자료 수집
- 회사: 허용된 범위의 업무 조사와 참고자료 수집

Research는 역할 정의는 공용이지만, 회사 도메인에서는 더 강한 출처/보안 규칙을 적용한다.

## 단계별 실행 순서

### Step 1. 도메인 분리 고정

- 개인 도메인과 회사 도메인의 데이터 경계를 문서로 확정
- `ai-survival-log`, `ai-survival-log-site`는 개인 전용으로 고정

### Step 2. 회사업무용 wiki 프로젝트 생성

- 회사용 wiki 저장소/폴더 구조 정의
- 회의록, 기획, 검수, 테스트 기록 저장 위치 정리

현재 반영:

- [[projects/company-wiki-internal-structure]]

### Step 3. 회사용 Assistant Ops 구조 정의

- Gmail/Calendar/Sheets는 회사 계정만 연결
- assistant flow는 회사 도메인에만 배치

현재 반영:

- [[projects/company-assistant-ops-internal-structure]]

### Step 4. 공용 lane/agent 규칙 정의

- shared `Planning/Review/Engineering/Research`의 실행 컨텍스트 분리
- 개인 도메인 실행 중 회사 데이터 접근 금지
- 회사 도메인 실행 중 개인 콘텐츠 저장소 접근 최소화
- shared `Review Lane`은 2-agent cross-validation을 기본 품질 게이트로 사용

### Step 5. 도메인별 workflow 분리 운영

- 개인: research -> planning -> authoring -> review -> publish
- 회사: meeting/research -> planning -> authoring/engineering -> review -> assistant follow-up

## 권장 폴더/저장소 방향

개인 도메인:

- `~/workspace/claude/ai-survival-log`
- `~/workspace/claude/ai-survival-log-site`

회사 도메인:

- `~/workspace/claude/company-wiki`
- `~/workspace/claude/company-assistant-ops`

공용:

- `~/workspace/claude/shared-agent-harness`

## 제안하는 최상위 폴더 구조

```text
~/workspace/claude/
  ai-survival-log
  ai-survival-log-site
  company-wiki
  company-assistant-ops
  shared-agent-harness
```

### `ai-survival-log`

- 개인 도메인 upstream
- 지식수집, 공부, 콘텐츠 source-of-truth
- `raw -> wiki -> output/blog`

### `ai-survival-log-site`

- 개인 도메인 downstream
- 블로그/콘텐츠 presentation layer
- `content/posts`, rendering, SEO

### `company-wiki`

- 회사 도메인 wiki
- 회의록, 기획, 디렉팅, 검수 기준, 테스트 기록
- 회사 문서 source-of-truth
- 내부 구조 초안: [[projects/company-wiki-internal-structure]]

### `company-assistant-ops`

- 회사 도메인 assistant surface
- Gmail, Calendar, Sheets, follow-up, 보고, 일정관리
- approval/audit 중심 운영
- 내부 구조 초안: [[projects/company-assistant-ops-internal-structure]]

### `shared-agent-harness`

- 공용 `Planning/Review/Engineering/Research` lane의 role 정의·skill·workflow 지원
- broker, validation, integration adapter, 공통 command/skill의 후보 위치

**positive list (담을 것)**

- role 정의 문서 (Planning/Review/Engineering/Research)
- skill template과 workflow checklist
- 공통 lint/audit script
- 공용 quality gate 템플릿

**negative list (담지 않을 것)**

- 도메인 특정 credential/OAuth token
- 회사 데이터 또는 개인 데이터 원본
- 도메인 고유 secret이 필요한 script
- 어느 한 도메인에만 해당하는 authoring/publish surface

## 이 단계의 결정 포인트

이번 단계에서는 실제 폴더 생성보다 다음을 먼저 확정한다.

- 폴더 이름이 역할과 권한 경계를 잘 드러내는가
- 개인/회사 데이터가 물리적으로 분리되는가
- 회사 assistant와 회사 wiki가 개인 프로젝트와 섞이지 않는가
- 공용 engineering/harness가 두 도메인의 공통 역할을 담기에 적절한가

## 현재 진행 상태

완료:

- 개인/회사 도메인 분리 원칙 고정
- 공용 lane/agent와 도메인 전용 surface 원칙 고정
- 최상위 폴더 이름 확정
- `workspace-security-boundary` 정책 문서 추가

다음:

- `shared-agent-harness` 내부 구조 설계
- `company-wiki` 내부 구조 설계

현재 반영:

- [[projects/shared-agent-harness-internal-structure]]

보류:

- 실제 폴더 생성
- 회사 assistant credential/OAuth 연결
- 도메인별 pre-commit / audit script 구현

## 향후 이주 계획

현재 개인 저장소(`ai-survival-log`)에 보관 중인 이중 도메인 설계 문서들(이 문서, `immediate-agent-operating-structure.md`, `assistant-ops-lane-execution-draft.md` 등)은 `shared-agent-harness` 저장소가 생성되는 시점에 해당 저장소로 이주하는 것이 정합적이다. 그 전까지는 `ai-survival-log/wiki/projects/`가 임시 보관 위치다.

## 관련 페이지

- [[projects/immediate-agent-operating-structure]]
- [[projects/managed-agent-harness-draft]]
- [[projects/assistant-ops-lane-execution-draft]]
- [[projects/executive-assistant-harness-business-idea]]
- [[projects/workspace-folder-structure-review-sheet]]
- [[projects/workspace-security-boundary]]
- [[projects/shared-agent-harness-internal-structure]]
