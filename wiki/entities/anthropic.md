---
title: "Anthropic"
created: "2026-04-24"
updated: "2026-04-24"
type: entity
sources: ["[[sources/2026-04-23-ep94-anthropic-low-hanging-fruits]]", "[[sources/2026-04-23-claude-codex-choice-and-anthropic-direction]]"]
tags: ["anthropic", "ai-company", "claude", "llm"]
status: active
published: false
slug: ""
description: ""
---

# Anthropic

Claude 모델 시리즈를 개발·운영하는 AI 회사. 이 위키에서 가장 자주 언급되는 AI 기업.

## 전략적 특징

EP 94 팟캐스트와 개인 저널 분석에서 드러난 Anthropic의 방향성 (2026년 4월 기준):

- **텍스트·코딩 집중**: 이미지 생성, 음성 등 멀티모달 확장보다 텍스트와 코딩 에이전트에 집중하는 전략. Claude Code가 대표 산물.
- **B2B 유스케이스 심화**: 코딩 에이전트를 B2B 진입점으로 삼고, 그 위에 Claude Design 등 애플리케이션을 쌓아 올림.
- **70일 주기 릴리스**: Opus 라인 기준 대략 70일 간격으로 새 모델 출시 패턴 (Opus 4, 4.1, 4.5, 4.6, 4.7). 소프트웨어 주기가 하드웨어 타임프레임(2~3년)보다 훨씬 빠름.
- **Compute shortage**: 작년(2025년) GPU 확보 부족으로 인한 compute 수급난. Google, OpenAI, Anthropic 3사 중 컴퓨팅 자원이 가장 적은 상태. Mythos 출시 지연에도 영향.
- **Opus 수요 쏠림**: 사용자 수요가 Sonnet, Haiku보다 Opus 쪽에 집중됨. 릴리스 간격 통계에서도 Opus 줄이기가 더 빠른 추세.

## Anthropic이 "안으로 들인" 것들

EP 94 표현 — "딸깍딸깍하면서 밖에 있는 것들을 다 안으로 들인다":
- Claude Design: 외부 Figma wrapper 서비스들의 기능을 공식 제품으로 내재화
- Managed Agents: 뇌(brain)와 손(hand)을 디커플링하는 아키텍처 서비스화

## 모델 라인업 (2026-04 기준)

- **Opus 4.7**: Adaptive Thinking 도입, 토큰 소비 1.3~1.4x 증가 체감
- **Mythos**: 내부 개발 중 (비공개). 10T 파라미터 루머. 보안 이슈로 프로덕션 미출시.
- **Claude Design**: UI 피드백 루프를 닫는 디자인 생성 도구

## 관련 페이지

- [[entities/claude-code]] — Anthropic의 코딩 에이전트 CLI
- [[concepts/mythos]] — Anthropic 비공개 대형 모델
- [[concepts/opus-4-7]] — 최신 Opus 릴리스
- [[concepts/adaptive-thinking]] — Opus 4.7의 핵심 기능
- [[sources/2026-04-23-ep94-anthropic-low-hanging-fruits]] — EP 94 팟캐스트 source
- [[sources/2026-04-23-claude-codex-choice-and-anthropic-direction]] — Anthropic 전략 분석 저널
