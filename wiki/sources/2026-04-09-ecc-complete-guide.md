---
title: "ECC 완전 가이드 — 소스 요약"
created: "2026-04-12"
updated: "2026-04-12"
type: source
sources: []
tags: [ecc, claude-code, ai-tool, plugin]
status: active
published: false
slug: ""
description: ""
---

# ECC 완전 가이드 — 소스 요약

**원본:** `ai-survival-log-site/content/posts/2026-04-09-ecc-complete-guide.mdx`
**작성일:** 2026-04-09

## 핵심 요약

Everything Claude Code(ECC)의 설치, 구성 요소, 에이전트 목록, 스킬, 커맨드, Hook 시스템, MCP 서버를 종합적으로 다룬 실전 가이드. ECC v1.10.0 기준. Anthropic 해커톤 수상작.

## 주요 포인트

- **6가지 핵심 구성 요소:** Agent, Skill, Command, Rule, Hook, MCP Server
- **47개 에이전트** — 기획/설계, 코드 리뷰, 빌드 오류 해결, 테스트/유지보수/운영, 특수 파이프라인으로 분류
- **GAN 하네스:** gan-planner → gan-generator → gan-evaluator 루프
- **지속적 학습 시스템:** 인스팅트(Instinct) 기반 — pending → confirmed → 스킬로 진화
- **AgentShield:** 14가지 패턴으로 시크릿/취약점 탐지
- **Hook 프로필:** minimal | standard | strict
- **설치 방식:** 플러그인(`/plugin marketplace add`) 또는 수동(`install.sh --profile full`)

## 인사이트

- Rules 파일은 플러그인 설치로 자동 배포되지 않음 — 수동 `install.sh` 필요
- 토큰 최적화: MCP 서버 수 줄이기, Sonnet 우선 사용, `MAX_THINKING_TOKENS` 제한
- `/ecc:plan`(플러그인) vs `/plan`(수동 설치) 차이 주의

## 관련 페이지

- [[entities/ecc]] — ECC 엔티티 페이지 (상세)
- [[entities/claude-code]] — Claude Code 도구
- [[topics/ai-era-survival]] — AI 시대 생존 전략
