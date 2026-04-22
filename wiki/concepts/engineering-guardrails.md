---
title: "Engineering Guardrails"
created: "2026-04-22"
updated: "2026-04-22"
type: concept
sources: ["[[sources/2026-04-22-project-state-management-analysis]]"]
tags: [engineering-guardrails, tdd, security, code-quality, claude-code, agents]
status: active
published: false
slug: ""
description: ""
---

# Engineering Guardrails

`ai-survival-log` 프로젝트의 `.codex/AGENTS.md`에 정의된 엔지니어링 가드레일. 코드 품질·보안·TDD 적용 범위를 명확히 규정한다.

## 규칙 목록

### 1. 구현 전 재사용 우선

기존 코드, 문서, 재사용 가능한 라이브러리를 먼저 확인하고 나서 새 구현을 도입한다.

### 2. 변경 후 리뷰

코드를 변경한 후, 완료 전에 변경 범위에서 버그·회귀·보안 문제·계약 드리프트를 검토한다.

### 3. TDD 적용 범위

| 대상 | TDD 적용 |
|------|---------|
| 자동화 스크립트 (automation scripts) | 적용 |
| 파서 (parsers) | 적용 |
| 트랜스포머 (transformers) | 적용 |
| publish / lint / sync 로직 | 적용 |
| 위키 콘텐츠 (마크다운) | 미적용 |
| raw 소스 인제스트 | 미적용 |
| 메타데이터 편집 | 미적용 |

위키 콘텐츠·raw 소스·메타데이터 편집에는 TDD를 강제하지 않되, 변경 범위에 맞는 검증은 수행한다.

### 4. 보안 기본 원칙

- 시크릿 하드코딩 금지
- 외부 입력(user input, API 응답, 파일 내용) 검증
- 에러 메시지에 민감 정보 노출 금지

### 5. TypeScript/JavaScript 규칙

- 공개 API 또는 공유 API는 타입 유지
- `any` 사용 최소화
- 프로덕션 경로에 `console.log` 미사용

## 배경

글로벌 `~/.claude/rules/testing.md`에는 모든 프로젝트에 TDD MANDATORY가 선언되어 있으나, 이 프로젝트는 대부분의 작업이 마크다운 콘텐츠 편집이므로 TDD 적용 범위를 명확히 구분하기 위해 Engineering Guardrails를 도입했다.

## 관련 페이지

- [[concepts/wiki-automation]] — TDD 적용 대상인 자동화 스크립트 패턴
- [[sources/2026-04-22-project-state-management-analysis]] — 가드레일 도입 배경 분석
- [[entities/claude-code]] — 가드레일이 적용되는 운영 환경
