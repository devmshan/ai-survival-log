---
title: "Claude Code"
created: "2026-04-12"
updated: "2026-04-12"
type: entity
sources: []
tags: [claude-code, ai-tool, anthropic]
status: active
published: false
slug: ""
description: ""
---

# Claude Code

Anthropic이 개발한 AI 코딩 에이전트 CLI 도구. 터미널에서 직접 실행하여 코드 작성, 디버깅, 리팩토링, 프로젝트 관리 등을 수행한다.

## 개요

- **개발사:** Anthropic
- **유형:** CLI 기반 AI 코딩 에이전트
- **모델:** Claude Sonnet 4.6 (기본), Claude Opus 4.6, Claude Haiku 4.5
- **플랫폼:** macOS, Linux, Windows (WSL)

## 핵심 기능

### 도구 시스템

Claude Code는 다양한 빌트인 도구를 통해 개발 작업을 수행한다:

- **Read / Write / Edit** — 파일 읽기, 쓰기, 수정
- **Bash** — 셸 명령 실행
- **Grep / Glob** — 코드 검색 및 파일 탐색
- **Agent** — 서브에이전트 실행 (병렬 작업)
- **WebFetch / WebSearch** — 웹 콘텐츠 접근

### 커스터마이징

- **CLAUDE.md** — 프로젝트별 지시사항 파일 (자동 로드)
- **커맨드 (Slash Commands)** — `.claude/commands/`에 마크다운으로 정의
- **Hook** — PreToolUse, PostToolUse, Stop 등 이벤트 기반 자동화
- **MCP 서버** — 외부 도구 연결 (GitHub, Playwright 등)

### 플러그인 생태계

Claude Code는 플러그인을 통해 기능을 확장할 수 있다:

- [[entities/ecc|Everything Claude Code (ECC)]] — 47개 에이전트, 181개 스킬의 종합 하네스
- [[entities/superpowers|Superpowers]] — 14개 핵심 워크플로우 스킬 (TDD, 코드 리뷰 등)

## 작업 모드

| 모드 | 설명 |
|------|------|
| 일반 모드 | 기본 대화 + 도구 실행 |
| Plan 모드 | 읽기 전용 탐색 → 계획 수립 |
| Fast 모드 | 동일 모델, 빠른 출력 |

## 모델 선택 가이드

| 모델 | 용도 |
|------|------|
| Haiku 4.5 | 경량 에이전트, 빈번한 호출, 비용 효율 |
| Sonnet 4.6 | 메인 개발 작업, 복잡한 코딩 |
| Opus 4.6 | 아키텍처 설계, 최고 수준 추론 |

## 관련 페이지

- [[entities/ecc]] — Claude Code 종합 플러그인
- [[entities/superpowers]] — 워크플로우 스킬 라이브러리
- [[concepts/llm-wiki-pattern]] — 이 위키 자체가 Claude Code로 운영됨
