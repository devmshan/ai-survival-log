---
title: "Workspace 폴더 구조 검수 시트"
created: "2026-04-24"
updated: "2026-04-24"
type: project
sources: []
tags: [project, review, workspace, folder-structure, harness, operations]
status: draft
published: false
slug: ""
description: "workspace 최상위 폴더 구조 초안을 검토할 때 확인해야 할 문서 목록과 핵심 판단 포인트를 한 장으로 정리한 시트."
---

# Workspace 폴더 구조 검수 시트

이 문서는 `~/workspace/claude/` 아래 최상위 폴더 구조 초안을 검토할 때 한 번에 확인할 문서와 판단 포인트를 요약한다.

## 이번에 검토할 제안 구조

```text
~/workspace/claude/
  ai-survival-log
  ai-survival-log-site
  company-wiki
  company-assistant-ops
  shared-agent-harness
```

## 먼저 읽을 문서

1. [[projects/dual-domain-agent-operating-model]]
2. [[projects/immediate-agent-operating-structure]]
3. [[projects/planning-lane-execution-draft]]
4. [[projects/assistant-ops-lane-execution-draft]]

## 이번 단계에서 핵심 확인 사항

### 1. 도메인 분리

- `ai-survival-log`, `ai-survival-log-site`가 개인 도메인 전용으로 충분히 분리되어 있는가
- 회사 데이터가 개인 프로젝트와 섞이지 않도록 `company-wiki`, `company-assistant-ops`가 분리되어 있는가

### 2. 공용 역할의 위치

- `Planning`, `Review`, `Engineering`, `Research`의 공용 workflow를 담을 위치로 `shared-agent-harness`가 적절한가
- 공용 role/lane은 공유하되 data/surface는 분리한다는 원칙이 폴더 이름에도 드러나는가

### 3. 회사 도메인 운영성

- 회사 업무용 wiki 이름으로 `company-wiki`가 충분히 명확한가
- 회사 Gmail/Calendar/Sheets 업무를 담는 이름으로 `company-assistant-ops`가 적절한가
- 회사 보안과 approval/audit 흐름을 고려했을 때 assistant surface가 별도 폴더인 것이 맞는가

### 4. 향후 확장성

- 앞으로 회사용 site/publish 계층이 생겨도 이 구조가 확장 가능한가
- 개인/회사 각각 authoring surface가 늘어나도 최상위 폴더가 과도하게 복잡해지지 않는가

## 이번 단계에서 아직 결정하지 않는 것

- 각 폴더 내부 디렉토리 구조
- 실제 새 폴더 생성 여부
- 회사용 wiki의 세부 frontmatter 규칙
- 회사 assistant의 실제 credential / OAuth 연결 방식

## 검수 후 결정해야 할 것

1. 제안한 5개 최상위 폴더 이름을 그대로 쓸지
2. `shared-agent-harness`를 지금 바로 둘지, 나중 단계에서 만들지
3. `company-wiki`와 `company-assistant-ops`의 내부 구조 설계를 다음 단계로 진행할지

## 현재 상태

- 검수 완료
- 폴더 이름 확정:
  - `ai-survival-log`
  - `ai-survival-log-site`
  - `company-wiki`
  - `company-assistant-ops`
  - `shared-agent-harness`
- `workspace-security-boundary` 정책 문서 반영 완료
- `dual-domain-agent-operating-model`과 관련 문서 이름 반영 완료

## 내일 이어갈 다음 단계

우선순위 후보:

1. `shared-agent-harness` 내부 구조 설계
2. `company-wiki` 내부 구조 설계

현재 상태 기준 권장 순서:

- 먼저 `shared-agent-harness` 내부 구조 설계
- 그 다음 `company-wiki` 내부 구조 설계

이유:

- 공용 role/lane/skill/workflow 뼈대를 먼저 고정해야 회사/개인 도메인 양쪽에 같은 운영 모델을 적용하기 쉽다
- `company-wiki` 내부 구조는 실제 회사 작업 패턴에 더 가까운 입력이 필요하므로 하루 뒤에 이어도 무방하다

현재 반영:

- [[projects/shared-agent-harness-internal-structure]]
- [[projects/company-wiki-internal-structure]]

## 빠른 체크리스트

- [ ] 개인/회사 도메인 경계가 충분히 명확하다
- [ ] 회사 데이터가 개인 저장소와 섞이지 않는 구조다
- [ ] 공용 engineering/harness 위치가 납득된다
- [ ] 폴더 이름이 역할과 용도를 직관적으로 설명한다
- [ ] 다음 단계로 내부 구조 설계를 진행해도 된다

## 한 줄 요약

이번 검수의 목표는 `최상위 폴더 이름과 도메인 경계가 맞는지`를 확인하는 것이다. 내부 구조와 실제 생성은 그 다음 단계다.

## 진행 업데이트

- `shared-agent-harness` 내부 구조 설계 완료
- `company-wiki` 내부 구조 설계 완료
- `company-assistant-ops` 내부 구조 설계 완료

다음 우선순위:

1. bootstrap 결과 검수
2. `shared-agent-harness` 1차 이주 계속 진행
3. 각 저장소 `git init` 및 identity 연결 시점 결정

현재 반영:

- `company-wiki` 실제 폴더와 초기 파일 생성 완료
- `company-assistant-ops` 실제 폴더와 초기 파일 생성 완료
- `shared-agent-harness` 실제 폴더와 초기 파일 생성 완료
- `shared-agent-harness` 1차 이주 시작 (`architecture / operations / planning`)
- `shared-agent-harness` 1차 이주 확장 (`review / engineering`)
- `shared-agent-harness` 1차 이주 확장 (`research`)
- `shared-agent-harness` 1차 이주 확장 (`cross-validation / templates / commands / skills`)
- `shared-agent-harness` 1차 이주 확장 (`README / AGENTS / operating docs / ADR`)
- `shared-agent-harness` 1차 이주 확장 (`adoption strategy / stop conditions / workflow gates`)

필수 게이트:

- `company-wiki`, `company-assistant-ops`는 `git init + git identity + pre-commit hook` 완료 전까지 실제 회사 프로젝트 개시 금지
