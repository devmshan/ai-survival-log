---
title: "Cross-Repo AI 자동화 실습"
created: "2026-04-16"
updated: "2026-04-23"
type: project
sources: []
tags: [automation, workflow, project, developer, wiki]
status: active
published: false
slug: ""
description: ""
---

# Cross-Repo AI 자동화 실습

`ai-survival-log`와 `ai-survival-log-site`를 함께 다루는 AI 업무 자동화 실습 프로젝트.

핵심 구조:
- `ai-survival-log`는 upstream authoring/source-of-truth
- `ai-survival-log-site`는 downstream presentation/consumer

따라서 같은 자동화라도 두 저장소에 동일하게 복붙하지 않고, 각 저장소 역할에 맞게 변형해서 적용한다.

## 현재 상태

### 완료

- `1. PR 요약 + 리뷰 포인트 생성기`
  - 공통 기준 문서 작성
  - `ai-survival-log-site` 구현 완료
  - `ai-survival-log` 축소 적용 완료
  - 샘플 실행 검증 완료

### 진행 예정

- `2. Jira 이슈 구현 계획 초안 생성기`
- `3. 배포 체크리스트 자동 수행 에이전트`
- `4. Managed Agent Harness 역할 분리 시범 적용`
- `5. Web Research / Assistant Lane 확장 설계`

현재는 구현을 잠시 멈추고, PR summary 실습 결과를 다시 공부하는 단계다.
다음 단계 착수 전에 각 항목의 입력 형식, 출력 형식, 검증 계획을 먼저 고정한다.

## 이번 실습의 핵심 학습

### 같은 자동화라도 저장소 역할에 따라 질문이 달라진다

`ai-survival-log-site`는 runtime, API, 렌더링, build를 먼저 본다.

`ai-survival-log`는 wiki 구조, publish contract, docs consistency를 먼저 본다.

즉, 자동화의 목적은 같지만 해석 기준이 다르다.

### 축소 적용의 의미

`ai-survival-log`에 PR summary를 "축소 적용"한다는 것은:
- site 버전을 그대로 옮기는 것이 아니라
- upstream 저장소에 맞는 범주와 검증 기준으로 다시 설계하는 것이다

## 학습 문서

- [PR Summary 실습 정리](/Users/ms/workspace/claude/ai-survival-log/docs/2026-04-16-pr-summary-practice-review.md:1)
- [PR Summary Standard](/Users/ms/workspace/claude/ai-survival-log/docs/2026-04-16-pr-summary-standard.md:1)
- [Cross-Repo AI Automation Collaboration Plan](/Users/ms/workspace/claude/ai-survival-log/docs/2026-04-16-cross-repo-ai-automation-collaboration-plan.md:1)

## 구현 결과

### `ai-survival-log`

- [scripts/pr-summary.mjs](/Users/ms/workspace/claude/ai-survival-log/scripts/pr-summary.mjs:1)
- [docs/automation/pr-summary.md](/Users/ms/workspace/claude/ai-survival-log/docs/automation/pr-summary.md:1)
- [.github/workflows/pr-summary.yml](/Users/ms/workspace/claude/ai-survival-log/.github/workflows/pr-summary.yml:1)

### `ai-survival-log-site`

- [site 실행 계획](</Users/ms/workspace/claude/ai-survival-log-site/docs/superpowers/plans/2026-04-16-cross-repo-execution-plan.md:1>)
- [site automation lab plan](</Users/ms/workspace/claude/ai-survival-log-site/docs/superpowers/plans/2026-04-16-ai-automation-lab-plan.md:1>)

## 다음 단계

다음 구현 후보는 `2. Jira 이슈 구현 계획 초안 생성기`다.

이 단계에서는:
- issue intake 형식
- 구현 계획 템플릿
- 변경 파일 후보/테스트 계획/확인 질문 생성

을 다루게 된다.

바로 이어서 검토할 항목은 `3. 배포 체크리스트 자동 수행 에이전트`다.

이 단계에서는:
- upstream publish contract 체크
- downstream lint/test/build gate
- 실패 리포트 형식

을 함께 정의해야 한다.

그다음 후보는 `4. Managed Agent Harness 역할 분리 시범 적용`이다.

이 단계에서는:
- intake / authoring / review / publish 역할 경계 정의
- 단일 런타임 기반 역할 전환 방식 검토
- validation gate를 workflow 순서에 연결
- `raw -> wiki`, `wiki edit`, `wiki -> publish` 3개 흐름에 시범 적용

관련 초안:
- [[projects/managed-agent-harness-draft]]

그다음 후보는 `5. Web Research / Assistant Lane 확장 설계`다.

이 단계에서는:
- 웹서핑 기반 자료수집 agent의 출처 규칙과 intake 연결
- `ai-survival-log`와 `ai-survival-log-site`를 함께 다루는 역할 매핑
- planning, authoring, engineering, publish를 lane 단위 workflow로 재정리
- Gmail, Calendar, Sheets 연동은 read-first / suggest-first 원칙으로 별도 assistant lane 정의

주의점:
- 프로젝트마다 agent를 복제하기보다 공통 역할이 저장소별 surface를 다루게 유지
- 외부 write 액션은 후속 단계로 미룸

선행 분리안:
- [[projects/immediate-agent-operating-structure]]
- [[projects/dual-domain-agent-operating-model]]
- [[projects/planning-lane-execution-draft]]
- [[projects/assistant-ops-lane-execution-draft]]

## 관련 페이지

- [[projects/blog-ai-study-site]]
- [[concepts/agentic-workflow]]
- [[concepts/pull-request]]
- [[topics/developer-automation-lab-01-pr-summary]]
- [[topics/claude-code-to-codex]]
