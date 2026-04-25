---
title: "company-wiki 내부 구조 설계"
created: "2026-04-24"
updated: "2026-04-24"
type: project
sources: []
tags: [project, company, wiki, structure, operations, meetings, planning, review, testing]
status: active
published: false
slug: ""
description: "회사 도메인 authoring source로 사용할 company-wiki 저장소의 내부 구조, page type, lane handoff, 검수 규칙을 정의한 문서."
---

# company-wiki 내부 구조 설계

이 문서는 `~/workspace/claude/company-wiki`의 내부 구조를 정의한다.

## Source Status

- 현재 `company-wiki` 저장소의 `README.md`, `AGENTS.md`, `ARCHITECTURE.md`, `docs/operating/*`, `templates/*`가 회사 authoring 규칙의 detached `operational source`다.
- 이 문서는 설계 배경과 초기 구조 판단을 남기는 `history retained here` 문서다.
- 즉 실제 회사 도메인 authoring 규칙은 장기적으로 `company-wiki` 저장소 안에서 닫히게 만들고, 여기서는 그 판단의 배경을 유지한다.

핵심 전제:

- `company-wiki`는 회사 도메인의 `authoring source`다
- 회의록, 기획, 디렉팅, 검수 기준, 테스트 기록의 canonical markdown surface를 담당한다
- Gmail, Calendar, Sheets 원본과 OAuth token은 이 저장소에 두지 않는다
- 외부 시스템 상호작용은 `company-assistant-ops`에서 처리하고, 이 저장소에는 그 결과의 요약/결정만 남긴다
- 공용 `Planning / Review / Engineering / Research` lane을 참조하되, 데이터 surface는 회사 도메인으로 고정한다

## 목적

`company-wiki`는 다음을 위한 저장소다.

- 회의 내용을 durable note로 남긴다
- 전략/기획/디렉팅 산출물을 정리한다
- 검수 기준과 테스트 판단을 누적한다
- 회사 업무용 지식과 결정 맥락을 human-first markdown으로 유지한다
- `company-assistant-ops`와 `shared-agent-harness` 사이에서 회사 도메인의 source-of-truth 역할을 한다

즉 이 저장소는 `회사 업무의 기억과 판단`을 남기는 곳이지, 캘린더/메일/시트 동기화 저장소가 아니다.

## 이 저장소에 들어가야 하는 것

- 회의록 원문 또는 정리본
- 프로젝트/업무 기획 문서
- 디렉팅 메모
- 검수 기준과 review 결과
- 테스트 계획, 테스트 결과 요약, regression note
- 회사 도메인에서 재사용할 glossary와 concept note
- 외부 시스템에서 온 결과 중 회사 업무 판단에 필요한 summary

## 이 저장소에 들어가면 안 되는 것

- Gmail mailbox 원본 dump
- Calendar event 원본 export
- Sheets 데이터 원본 복제본
- OAuth token, API key, credential
- 개인 블로그/공부/콘텐츠 초안
- 공용 harness rule source
- 대규모 binary attachment 원본 저장소 역할

## 권장 최상위 구조

```text
company-wiki/
├── README.md
├── AGENTS.md
├── CLAUDE.md
├── ARCHITECTURE.md
├── inbox/
├── meetings/
├── projects/
├── planning/
├── reviews/
├── testing/
├── concepts/
├── entities/
├── templates/
└── archive/
```

## 파일/폴더별 책임

### 루트 문서

#### `README.md`

- 저장소 목적
- 무엇을 이 저장소에 저장하는지
- 무엇을 `company-assistant-ops`로 넘기는지
- 빠른 시작

#### `AGENTS.md`

- 회사 도메인 고유 규칙
- 민감정보 취급 금지 규칙
- 검수와 handoff 규칙

#### `CLAUDE.md`

- `@AGENTS.md`
- Claude surface에서의 회사 도메인 제약

#### `ARCHITECTURE.md`

- 저장소 계층 구조
- page type 정의
- `company-assistant-ops`와의 handoff
- review gate와 audit boundary

### `inbox/`

목적:

- 아직 정리되지 않은 초기 메모
- 임시 회의 조각
- 분류 전 raw-ish note

원칙:

- 장기 보관 장소로 쓰지 않는다
- 정리 후 `meetings/`, `projects/`, `planning/`, `reviews/`, `testing/` 중 하나로 이동

### `meetings/`

목적:

- 회의 note의 canonical markdown surface

포함:

- 회의 agenda
- 회의 note
- 결정 사항
- action item 요약

중요:

- 일정 생성/수정 자체는 `company-assistant-ops`
- 여기에는 `왜 그 일정이 필요한지`, `무슨 결정이 났는지`를 남긴다

### `projects/`

목적:

- 회사 업무 단위 프로젝트 문서
- long-running workstream 관리

포함:

- 프로젝트 개요
- scope
- milestone
- 관련 회의/검수/테스트 링크

### `planning/`

목적:

- 기획, 디렉팅, PT 구조, 실행 계획

포함:

- PRD
- 발표 구조 메모
- 우선순위 판단
- directing note

중요:

- `Planning Lane`의 주 출력 surface

### `reviews/`

목적:

- deliverable 검수
- 기준 문서
- cross-validation 결과 요약

포함:

- review checklist
- review findings
- `primary review` / `secondary review` 결과 요약
- resolved / unresolved 기록

중요:

- 공식 검수 게이트는 여기 기록을 남긴다
- 같은 모델 반복 검수는 교차검증으로 인정하지 않는다

### `testing/`

목적:

- 테스트 계획
- 테스트 결과
- regression note
- 품질 리스크

포함:

- test plan
- execution note
- failure summary
- retest condition

중요:

- 상세 자동화나 스크립트는 필요 시 별도 코드 저장소에서 관리하고, 여기에는 판단과 결과를 남긴다

### `concepts/`

목적:

- 회사 내부 공통 개념
- 반복적으로 나오는 정책/용어/판단 기준

예:

- 내부 review 단계 정의
- QA 의미
- approval level
- meeting note convention

### `entities/`

목적:

- 팀, 제품, 시스템, 파트너, 핵심 문서 같은 회사 도메인 entity note

주의:

- 민감도 높은 정보는 최소화하고, 내부 운영에 필요한 수준만 유지

### `templates/`

권장 템플릿:

- `meeting-note.md`
- `project-brief.md`
- `planning-brief.md`
- `review-report.md`
- `cross-review-report.md`
- `test-plan.md`
- `test-result.md`

### `archive/`

목적:

- 종료된 프로젝트
- 더 이상 active하지 않은 note
- 보존용 기록

원칙:

- archive는 삭제가 아니라 상태 전환이다

## page type과 기본 성격

권장 page type:

- `meeting`
- `project`
- `planning`
- `review`
- `test`
- `concept`
- `entity`

권장 공통 frontmatter:

```yaml
title: ""
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
type: meeting|project|planning|review|test|concept|entity
status: active|draft|archived
confidentiality: internal|restricted
owners: []
related_projects: []
related_meetings: []
related_reviews: []
related_tests: []
```

## lane별 진입 surface

### `Research Lane`

주 진입:

- `inbox/`
- `concepts/`
- 필요 시 `projects/`

출력:

- 조사 note
- 내부 참고 concept page

### `Planning Lane`

주 진입:

- `projects/`
- `planning/`

출력:

- 계획 문서
- directing note
- PT structure

### `Review Lane`

주 진입:

- `reviews/`
- 관련 `projects/`, `planning/`, `testing/`

출력:

- review findings
- cross-validation result
- resolved/unresolved state

### `Engineering Lane`

주 진입:

- `projects/`
- `testing/`
- `reviews/`

출력:

- 구현 관련 decision note
- test-related summary

주의:

- 코드 자체는 별도 engineering surface가 있을 수 있고, 이 저장소에는 업무 맥락과 결과 요약을 남긴다

## `company-assistant-ops`와의 handoff 규칙

`company-wiki`는 결정과 맥락을 남기고, `company-assistant-ops`는 외부 시스템 실행을 담당한다.

### `company-wiki -> company-assistant-ops`

넘길 수 있는 것:

- 회의 후 action item 요약
- 일정 후보 생성 요청
- follow-up 메일 초안 요청
- 보고 초안 요청

넘기면 안 되는 것:

- wiki 전체를 외부 시스템으로 복제
- 민감 note 원문 전체 전달
- credential이 필요한 동작을 wiki에서 직접 수행

### `company-assistant-ops -> company-wiki`

되돌아오는 것:

- 일정 반영 결과 요약
- follow-up 발송 여부
- 보고 제출 여부
- 외부 write 실행 결과 summary

원칙:

- 외부 시스템 원본은 `company-assistant-ops` 또는 외부 서비스에 남고
- `company-wiki`에는 decision-grade summary만 남긴다

## 검수와 2-agent cross-validation

기본 원칙:

- 회사 도메인의 공식 검수는 `primary review`와 `secondary review`를 남긴다
- 가능한 한 서로 다른 agent surface 또는 다른 review path를 사용한다
- 같은 모델 + 같은 checklist + 같은 prompt 반복은 교차검증으로 보지 않는다

최소 적용 범위:

- 구조 변경
- 계획 문서 승인 직전
- 검수 결과 확정
- 테스트 판정
- 외부 assistant write를 유발하는 중요 문서 변경

권장 기록 위치:

- `reviews/`
- 필요 시 관련 문서 본문 하단에 review summary 링크

## confidentiality와 최소 기록 원칙

원칙:

- `company-wiki`는 회사 문서 source-of-truth지만, 모든 민감정보를 과하게 적재하는 저장소가 아니다
- 필요한 결정과 맥락을 남기되, 과도한 개인정보/credential/외부 원본 dump는 피한다

권장 구분:

- `internal`
  - 일반 회사 운영 note
- `restricted`
  - 제한 접근이 필요한 note

민감도가 더 높은 데이터는 이 저장소 바깥의 적절한 시스템에 남기고, 여기엔 참조와 요약만 둔다.

## 구현 우선순위

### Phase 1

- 루트 문서 4개
- `meetings/`
- `projects/`
- `planning/`
- `reviews/`
- `testing/`
- `templates/`

### Phase 2

- `concepts/`
- `entities/`
- `archive/`
- frontmatter convention 고정

### Phase 3

- `company-assistant-ops` handoff 템플릿
- cross-review report 템플릿 정교화
- restricted note 운영 규칙 보강

## 다음 단계

- `company-assistant-ops` 내부 구조 설계
- `company-wiki`용 템플릿 초안 정의
- 회사 도메인 review/checklist 운영 규칙 분리

현재 반영:

- [[projects/company-domain-template-set]]

## 관련 페이지

- [[projects/dual-domain-agent-operating-model]]
- [[projects/shared-agent-harness-internal-structure]]
- [[projects/assistant-ops-lane-execution-draft]]
- [[projects/workspace-security-boundary]]
- [[projects/immediate-agent-operating-structure]]
