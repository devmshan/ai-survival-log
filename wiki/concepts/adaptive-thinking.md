---
title: "Adaptive Thinking"
created: "2026-04-24"
updated: "2026-04-24"
type: concept
sources: ["[[sources/2026-04-23-ep94-anthropic-low-hanging-fruits]]", "[[sources/2026-04-23-claude-codex-choice-and-anthropic-direction]]"]
tags: ["adaptive-thinking", "anthropic", "opus-4-7", "llm", "reasoning"]
status: active
published: false
slug: ""
description: ""
---

# Adaptive Thinking

Anthropic이 Opus 4.7에서 도입한 추론 예산 조정 방식. 쉬운 질문에는 짧게 생각하고 바로 답하며, 어려운 문제에는 더 오래·깊게 추론한다. 항상 동일한 계산량을 쓰지 않고 문제의 난이도에 맞게 적응적으로(adaptive) 사고한다.

## 동작 방식

- 단순 질문 → 추론 스텝 최소화 → 빠른 응답
- 복잡한 문제 → 더 많은 추론 예산 투입 → 정확도 우선

비슷한 개념: test-time compute, reasoning budget, dynamic compute, adaptive inference.

사람에 비유하면 쉬운 암산은 바로 하고, 어려운 증명 문제는 오래 붙잡고 푸는 것과 비슷하다.

## Claude Code vs 웹 인터페이스 차이

- **Claude Code**: thinking 레벨을 사용자가 직접 고정 가능 (예: extended thinking default)
- **웹 인터페이스**: 모델이 알아서 결정. Ultrathink 같은 프롬프트 힌트로 유도 가능하나 항상 적용되지 않음.

Opus 4.6까지는 thinking을 항상 고정해 놓을 수 있었으나, 4.7부터는 웹에서 사용자 제어가 제한됨. 이는 트래픽 및 compute 자원 배분과 관련된 결정으로 추정됨.

## 토큰 소모와의 관계

Adaptive Thinking 때문에 4.7에서 토큰 소모가 늘어난 것처럼 체감될 수 있다. 단, EP 94 분석에 따르면 실제 주요 원인은 tokenizer 변경(vocab 감소 → 더 잘게 쪼개는 토크나이징)이다.

둘이 합쳐져 Claude Code 사용자 입장에서는 동일한 작업에 1.3~1.4x 더 많은 토큰을 소비하는 것처럼 체감됨.

상세 파이프라인: [[topics/professors-brain-02-relearning-llm]]

## 관련 페이지

- [[concepts/opus-4-7]] — Adaptive Thinking이 도입된 모델
- [[entities/anthropic]] — 개발사
- [[topics/professors-brain-02-relearning-llm]] — tokenizer·LM head 내부 구조 설명
- [[sources/2026-04-23-ep94-anthropic-low-hanging-fruits]] — EP 94 source
