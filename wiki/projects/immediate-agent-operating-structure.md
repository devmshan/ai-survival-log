---
title: "즉시 운영용 Agent 프로젝트 구조"
created: "2026-04-23"
updated: "2026-04-23"
type: project
sources: []
tags: [project, harness, workflow, agents, operations, planning, engineering, assistant]
status: active
published: false
slug: ""
description: "지금부터 바로 운영할 수 있도록 공용 lane/agent와 도메인 전용 surface를 기준으로 정리한 즉시 운영 구조."
---

# 즉시 운영용 Agent 프로젝트 구조

업무 도메인 분리는 다음 문서를 함께 기준으로 본다.

- [[projects/dual-domain-agent-operating-model]]

이 문서는 `나중에 독립 agent로 분리할지 검토하는 초안`이 아니라, 지금부터 바로 사용할 운영 구조를 고정한다.

핵심 원칙은 두 가지다.

- 프로젝트는 `결과물`, `계약`, `권한 경계` 기준으로 나눈다
- 역할은 프로젝트를 가로질러 일하지만, 각 프로젝트 안에서 맡는 책임은 명확히 고정한다
- `Planning / Review / Engineering / 일부 Research`는 공용으로 재사용하고, `Authoring / Publish / Assistant Ops`는 도메인 전용 surface를 탄다

## 지금 바로 쓸 프로젝트 구조

이 문서는 기본 운영 구조를 설명한다. 개인/회사 도메인 분리는 [[projects/dual-domain-agent-operating-model]]에서 우선 고정한다.

### 1. Strategic Planning Project

목적:

- 전체 우선순위
- 디렉팅
- 기획
- PT 구조
- 실행 계획
- 일정 기준 업무 분해

주요 산출물:

- PRD
- 실행 계획
- 발표 구조 초안
- 우선순위 결정 메모

주요 저장 위치:

- `wiki/projects/`
- 필요 시 `raw/journals/`의 회의/생각 기록

### 2. Upstream Knowledge Project

목적:

- `ai-survival-log`의 `raw -> wiki -> output/blog` 흐름 관리
- source-of-truth 문서 작성
- 원천 자료 intake와 wiki authoring

주요 산출물:

- `raw/` source
- `wiki/` 문서
- `output/blog/` artifact

주요 저장 위치:

- `ai-survival-log/raw/`
- `ai-survival-log/wiki/`
- `ai-survival-log/output/blog/`

### 3. Downstream Publishing Project

목적:

- `ai-survival-log-site`에서 publish artifact 소비
- presentation, rendering, SEO, site contract 유지

주요 산출물:

- `content/posts/`
- site-facing images
- presentation/runtime adjustments

주요 저장 위치:

- `ai-survival-log-site/content/posts/`
- `ai-survival-log-site/public/images/`

### 4. Engineering Execution Project

목적:

- 코딩
- 리팩토링
- 테스트
- 스크립트 수정
- 자동화 구현

주요 산출물:

- 코드 변경
- 테스트 결과
- automation scripts
- validation/report outputs

주요 저장 위치:

- `ai-survival-log/scripts/`, `tests/`, `.github/`
- `ai-survival-log-site`의 관련 코드와 설정

### 5. Review and QA Project

목적:

- 검수
- publish readiness 확인
- cross-repo contract 점검
- 품질 게이트 운영
- 이중 agent 교차검증 운영

주요 산출물:

- review notes
- block/warn/escalate 판단
- verification results
- 교차검증 비교 결과

주요 저장 위치:

- wiki project docs
- docs/operating references
- PR/작업 단위 review 기록

### 6. Assistant Operations Project

목적:

- 일정관리
- 할 일 보고
- 회의록 정리
- 회의 follow-up
- Gmail/Calendar/Sheets 기반 운영 지원

주요 산출물:

- 일정 후보
- action items
- follow-up draft
- 보고 초안

주요 저장 위치:

- 외부 시스템 원본
- `raw/journals/`의 회의/세션 보관
- 필요 시 파생 상태 문서

## 역할 구조

지금부터는 역할을 별도 검토 대상이 아니라 `즉시 운영하는 업무 분담`으로 본다.

### Planning Agent

주 책임:

- Strategic Planning Project owner
- 모든 작업의 선행 계획 수립
- 디렉팅, 기획, PT 구조, 범위 정의
- 어떤 프로젝트가 연루되는지 판단

직접 하지 않는 일:

- 코드 구현 확정
- 최종 publish 실행
- 외부 high-risk write

공용 원칙:

- 개인/회사 도메인 모두에서 같은 역할 정의로 사용
- 단, 읽고 쓰는 문서 surface는 도메인별로 분리

### Research Agent

주 책임:

- 웹서핑
- 공식 문서와 1차 출처 수집
- 최신 정보 확인
- planning과 authoring에 필요한 조사

직접 하지 않는 일:

- source-of-truth 확정
- 외부 서비스 write

공용 원칙:

- 역할 정의는 공용
- 회사 도메인에서는 보안/출처 정책을 더 강하게 적용

### Authoring Agent

주 책임:

- Upstream Knowledge Project의 문서 작성
- 회의록, 보고서, source 요약, wiki 초안 작성
- Strategic Planning Project 문서화 보조

직접 하지 않는 일:

- 코드 구현 책임
- publish gate 통과 판정

### Engineering Agent

주 책임:

- Engineering Execution Project owner
- 코딩, 리팩토링, 테스트, 자동화 구현
- upstream/downstream/cross-repo 기술 변경 실행

직접 하지 않는 일:

- 우선순위 결정
- 최종 품질 승인
- 외부 assistant write

공용 원칙:

- 개인/회사 도메인 모두에서 사용
- 항상 현재 도메인의 저장소와 credential policy를 따름

### Review Agent

주 책임:

- Review and QA Project owner
- 검수, validation, publish readiness, contract consistency 확인
- block/warn/escalate 판정
- 별도 검수 agent와 교차검증 수행

직접 하지 않는 일:

- 자기 검토를 무시한 self-approval
- 구현 대체

공용 원칙:

- 개인/회사 도메인 모두에서 같은 quality gate 역할 수행

이중 검증 원칙:

- 모든 공식 검수는 `agent 2개 교차검증`을 기본값으로 한다
- 최소 구성은 `primary review` + `secondary review`
- 가능한 한 서로 다른 agent surface 또는 다른 review path를 사용한다
- 같은 모델을 반복 사용하더라도 checklist나 prompt가 같으면 교차검증으로 인정하지 않는다
- 두 검수 결과가 다르면 unresolved finding으로 남기고 정리 후에만 완료 처리한다

### Publish Agent

주 책임:

- Upstream artifact와 downstream site handoff
- `wiki -> output/blog -> ai-survival-log-site` 흐름 관리
- 이미지/frontmatter/slug/date contract 확인

직접 하지 않는 일:

- wiki source 직접 authoring source로 대체
- 검증 없이 배포 완료 선언

### Assistant Ops Agent

주 책임:

- Assistant Operations Project owner
- 일정관리, follow-up, 보고, 외부 시스템 기반 운영 지원

직접 하지 않는 일:

- repo 코드 수정
- publish 실행
- approval 없는 외부 high-risk write

## 도메인 적용 메모

- 개인 도메인에서는 `ai-survival-log`, `ai-survival-log-site`만 사용한다
- 회사 도메인에서는 별도 회사 wiki와 회사 assistant surface를 사용한다
- `Planning`, `Review`, `Engineering`, 일부 `Research`는 공용 역할로 유지한다
- `Authoring`, `Publish`, `Assistant Ops`는 도메인 전용 surface를 따라 운영한다

## 프로젝트별 owner 매핑

| 프로젝트 | 주 owner | 보조 역할 |
|------|------|------|
| Strategic Planning Project | `Planning Agent` | `Research Agent`, `Review Agent` |
| Upstream Knowledge Project | `Authoring Agent` | `Research Agent`, `Planning Agent`, `Review Agent` |
| Downstream Publishing Project | `Publish Agent` | `Engineering Agent`, `Review Agent` |
| Engineering Execution Project | `Engineering Agent` | `Planning Agent`, `Review Agent` |
| Review and QA Project | `Review Agent` | `Planning Agent`, `Publish Agent` |
| Assistant Operations Project | `Assistant Ops Agent` | `Planning Agent`, `Research Agent` |

## 현재 업무를 어디로 배분할지

사용자가 현재 부담하는 업무는 아래처럼 즉시 나눌 수 있다.

| 업무 | 1차 담당 프로젝트 | 1차 담당 agent |
|------|------|------|
| 디렉팅 | Strategic Planning Project | `Planning Agent` |
| 기획 | Strategic Planning Project | `Planning Agent` |
| PT 발표 구조 | Strategic Planning Project | `Planning Agent` |
| 자료조사/웹서핑 | Strategic Planning Project 또는 Upstream Knowledge Project | `Research Agent` |
| 회의록 작성/정리 | Assistant Operations Project 또는 Upstream Knowledge Project | `Assistant Ops Agent`, `Authoring Agent` |
| 할 일 정리 | Assistant Operations Project | `Assistant Ops Agent` |
| 일정관리 | Assistant Operations Project | `Assistant Ops Agent` |
| wiki/source 문서 작성 | Upstream Knowledge Project | `Authoring Agent` |
| 코딩 | Engineering Execution Project | `Engineering Agent` |
| 리팩토링 | Engineering Execution Project | `Engineering Agent` |
| 테스트 | Engineering Execution Project | `Engineering Agent` |
| 검수 | Review and QA Project | `Review Agent` |
| publish handoff | Downstream Publishing Project | `Publish Agent` |

## 즉시 운영 workflow

### Workflow 1. 새 작업 착수

1. `Planning Agent`가 작업을 프로젝트 단위로 분류
2. `Research Agent`가 필요한 자료를 수집
3. `Planning Agent`가 실행 계획과 검증 계획을 작성
4. `Authoring Agent` 또는 `Engineering Agent`로 handoff
5. `Review Agent`가 검수
6. 필요 시 `Publish Agent` 또는 `Assistant Ops Agent`가 마무리

### Workflow 2. 콘텐츠/문서 작업

1. `Planning Agent`가 목표와 범위 결정
2. `Research Agent`가 source 조사
3. `Authoring Agent`가 wiki/source/보고 초안 작성
4. `Review Agent`가 품질 게이트 수행
5. 필요 시 `Publish Agent`가 downstream 반영

### Workflow 3. 엔지니어링 작업

1. `Planning Agent`가 변경 범위와 검증 경로를 정의
2. `Engineering Agent`가 구현, 리팩토링, 테스트 수행
3. `Review Agent`가 1차 검수 수행
4. 별도 검수 agent가 2차 교차검증 수행
5. 두 검수 결과를 비교해 unresolved finding 정리
4. 필요 시 `Publish Agent`가 publish 관련 후속 작업 수행

### Workflow 4. 비서/운영 작업

1. `Planning Agent`가 중요도와 후속 action 성격 정리
2. `Assistant Ops Agent`가 일정, 할 일, follow-up 초안 생성
3. `Research Agent`가 필요한 외부 정보 조회 보조
4. 승인 후 외부 시스템 반영

## 운영 원칙

- planning은 모든 작업의 입구다
- engineering은 구현을 맡고, review는 승인 권한을 가진다
- 공식 completion gate는 항상 `2-agent cross-validation`을 거친다
- assistant ops는 repo 작업과 분리된 권한 체계로 운영한다
- publish는 upstream/downstream 계약을 알고 있는 별도 owner가 맡는다
- 웹서핑과 자료조사는 독립 업무로 인정하고 `Research Agent`에 명시적으로 배정한다

## 지금 당장 실행할 순서

1. 모든 새 요청은 먼저 Strategic Planning Project로 넣는다
2. 문서성 작업은 Upstream Knowledge Project로 넘긴다
3. 코드 작업은 Engineering Execution Project로 넘긴다
4. 검수는 항상 Review and QA Project에서 수행한다
5. 일정/회의/보고는 Assistant Operations Project로 분리한다

이 구조로 운영하면 사용자가 `혼자 모든 역할을 전환하면서` 버티는 대신, 작업을 프로젝트와 역할 단위로 바로 배분할 수 있다.

## 관련 페이지

- [[projects/dual-domain-agent-operating-model]]
- [[projects/managed-agent-harness-draft]]
- [[projects/planning-lane-execution-draft]]
- [[projects/assistant-ops-lane-execution-draft]]
- [[projects/cross-repo-ai-automation-lab]]
