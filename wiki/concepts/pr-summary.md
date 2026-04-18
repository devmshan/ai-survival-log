---
title: "PR Summary"
created: "2026-04-17"
updated: "2026-04-17"
type: concept
sources: []
tags: [pull-request, automation, code-review, workflow, github]
status: active
published: false
slug: ""
description: ""
---

# PR Summary

PR summary는 Pull Request의 changed files를 기준으로 변경 범주, 위험도, 검증 포인트, 리뷰 질문을 자동 정리해 주는 리뷰 보조 레이어다.

이 저장소에서는 작성자의 PR 설명을 대체하지 않고, 리뷰어가 "어디를 먼저 봐야 하는지"를 빨리 파악하게 만드는 목적에 가깝다.

## 무엇을 하는가

- 변경 파일 목록을 읽는다
- 저장소 역할에 맞는 범주로 분류한다
- 위험도와 검증 필요 사항을 추정한다
- 리뷰어가 먼저 봐야 할 포인트와 질문을 생성한다

## 무엇을 하지 않는가

- PR을 통과/실패로 채점하지 않는다
- 커밋 메시지를 자동으로 다시 쓰지 않는다
- PR 작성 방식 자체를 강제하지 않는다

즉, 경고 봇보다는 요약 봇에 가깝다.

## 이 저장소에서의 해석

`ai-survival-log`는 앱 런타임보다 `raw -> wiki -> output/blog -> publish` 계약을 먼저 본다.

그래서 이 저장소의 PR summary는 보통 아래를 먼저 묻는다.

- wiki source-of-truth 경계를 흐리는가
- publish contract 또는 downstream 호환성을 깨는가
- `wiki/index.md`, `wiki/log.md`, tags 동기화가 필요한가
- 문서와 운영 모델 설명이 어긋나는가

## 언제 보게 되는가

PR이 열리거나 업데이트되면 GitHub Actions가 `scripts/pr-summary.mjs`를 실행해 PR 코멘트로 summary를 남긴다.

작성자는 PR을 열기 전에도 로컬에서 같은 스크립트를 실행해 사전 점검 도구로 쓸 수 있다.

```bash
node scripts/pr-summary.mjs
node scripts/pr-summary.mjs --files "wiki/topics/ai-era-survival.md,docs/publishing-contract.md,scripts/wiki"
```

## 누가 왜 쓰는가

- 작성자: PR을 열기 전에 위험도와 검증 포인트를 미리 점검
- 리뷰어: changed files를 다 읽기 전에 검토 우선순위를 빠르게 파악
- maintainer: 저장소가 중요하게 보는 기준을 PR마다 같은 형식으로 적용

## 관련 페이지

- [[concepts/pull-request]]
- [[projects/cross-repo-ai-automation-lab]]
- [[topics/developer-automation-lab-01-pr-summary]]
