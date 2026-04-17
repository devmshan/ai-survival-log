---
title: "Pull Request"
created: "2026-04-17"
updated: "2026-04-17"
type: concept
sources: []
tags: [git, pull-request, code-review, workflow, collaboration, github]
status: active
published: false
slug: ""
description: ""
---

# Pull Request

개발자가 자신의 코드 변경을 메인 코드베이스에 합쳐달라고 요청하는 공식 절차.
혼자 개발할 때는 불필요하지만, 팀 협업에서는 품질 보증과 지식 공유의 핵심 수단이다.

## 기본 흐름

```
main에서 branch 생성
  → 코드 작성 & 커밋
  → 원격 저장소에 push
  → PR 생성 (병합 요청)
  → 팀원 리뷰
  → 승인 후 merge
```

## PR의 구성 요소

- **제목** — 한 줄로 무엇을 했는지 요약
- **설명(body)** — 변경 이유, 변경 내용, 테스트 방법, 주목할 부분
- **Changed Files** — 실제 변경된 파일 목록과 diff
- **Reviewers** — 이 PR을 검토할 사람 지정
- **Labels / Assignees** — PR 성격 분류 (bug, feature, docs 등)

## 리뷰 유형

| 유형 | 의미 |
|------|------|
| Comment | 질문이나 제안 (통과/차단 아님) |
| Approve | 문제 없음, merge 가능 |
| Request Changes | 수정 전까지 merge 불가 |

리뷰어는 코드 한 줄에 직접 코멘트를 달 수 있다.

## PR이 중요한 이유

- **품질 보증** — 혼자서는 못 보는 버그를 팀이 잡음
- **지식 공유** — 팀 전체가 코드 변경을 인지하게 됨
- **히스토리 기록** — 왜 이 코드를 썼는지 나중에 추적 가능
- **main 보호** — 검증 안 된 코드가 main에 직접 들어가지 않음
- **CI 연동** — PR 생성 시 자동으로 테스트/빌드 실행

## CI/CD와의 연결

PR을 열면 GitHub Actions 등을 통해 자동으로 검사가 실행된다.

```yaml
on:
  pull_request:
    types: [opened, synchronize]

jobs:
  test:       # 테스트 통과해야 merge 가능
  lint:       # 코드 스타일 검사
  build:      # 빌드 성공해야 merge 가능
  pr-summary: # PR 요약 자동 생성 (자동화 레이어)
```

## 좋은 PR vs 나쁜 PR

**좋은 PR**
- 변경 범위가 명확하게 한 가지 목적
- 리뷰하기 적당한 크기 (300~500줄 이내)
- 설명이 충분해서 컨텍스트 없이도 이해 가능
- 테스트 코드 포함

**나쁜 PR**
- 제목: "여러 가지 수정" (무엇인지 모름)
- 5,000줄 변경 (리뷰 불가능)
- 설명 없음
- 테스트 없이 런타임 코드만 변경

## PR Summary 자동화

[[projects/cross-repo-ai-automation-lab]] 프로젝트에서 PR 요약을 자동 생성하는 자동화를 구현했다.

핵심 아이디어: 리뷰어가 PR을 열면 "어디를 먼저 봐야 하는지"가 정리된 요약이 자동으로 붙어 있는 구조.

```
PR 생성
  → GitHub Actions 실행
  → scripts/pr-summary.mjs 실행
  → 변경 파일 수집 → 범주 분류 → 위험도 판단 → 리뷰 포인트 생성
  → PR 코멘트에 자동 게시
```

저장소 역할에 따라 분류 기준이 달라진다:
- `ai-survival-log-site` (runtime consumer) — `content`, `ui`, `api`, `data-loading`, `build-ci` 중심
- `ai-survival-log` (source-of-truth) — `source`, `wiki`, `publish-contract`, `agent-surface` 중심

## 관련 페이지

- [[concepts/pr-summary]]
- [[concepts/agentic-workflow]]
- [[projects/cross-repo-ai-automation-lab]]
