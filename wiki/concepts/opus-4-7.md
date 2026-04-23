---
title: "Opus 4.7"
created: "2026-04-24"
updated: "2026-04-24"
type: concept
sources: ["[[sources/2026-04-23-ep94-anthropic-low-hanging-fruits]]", "[[sources/2026-04-23-claude-codex-choice-and-anthropic-direction]]"]
tags: ["opus-4-7", "anthropic", "llm", "adaptive-thinking", "tokenizer"]
status: active
published: false
slug: ""
description: ""
---

# Opus 4.7

Anthropic Claude Opus 시리즈의 2026년 4월 릴리스. Training cutoff가 2026년 1월.

## 주요 변화

### Adaptive Thinking

쉬운 질문에는 짧게, 어려운 문제에는 더 오래·깊게 추론하는 방식. Claude Code에서는 thinking 레벨을 고정할 수 있지만, 웹 인터페이스에서는 모델이 알아서 결정한다.

관련 표현: test-time compute, reasoning budget, dynamic compute, adaptive inference.

4.6까지는 thinking을 항상 고정해 놓을 수 있었으나 4.7부터는 adaptive 기본값. Ultrathink 같은 프롬프트 힌트로 유도 가능하나 항상 켜지지는 않음.

### Tokenizer 변경

Vocabulary 숫자가 줄어들었고, 그 결과 같은 텍스트를 더 많은 토큰으로 처리함:

- CJK 언어는 거의 변화 없음
- 영어 산문 및 코드: 약 1.3~1.4x 토큰 증가 체감
- Claude Code를 쓰는 경우 실질 토큰 비용 1.3~1.4x 상승 체감

Vocabulary 감소 → embedding table과 LM head 크기 감소 → 파라미터 비용 절감. 단, 같은 작업을 더 많은 토큰으로 처리하므로 사용자 입장에서는 비용이 올라간 것처럼 체감.

상세 파이프라인 설명: [[topics/professors-brain-02-relearning-llm]]

### Knowledge Cutoff

Training cutoff: 2026년 1월. 4.6 대비 매우 최근.

Mythos에서 Knowledge Distillation을 통한 파생 모델일 가능성이 있다는 분석도 있으나 공식 확인되지 않음.

## 사용 맥락

EP 94 팟캐스트와 개인 저널에서 "비슷한 작업에서 토큰 소모가 2배 가까이 늘었다"는 체감이 구독 선택 고민의 출발이었다. Adaptive Thinking이 Claude Code 사용량 증가의 일부 원인으로 추정됨.

## 관련 페이지

- [[concepts/adaptive-thinking]] — Opus 4.7의 핵심 특징
- [[concepts/mythos]] — Opus 4.7의 teacher model 추정 대상
- [[entities/anthropic]] — 모델 제공사, 70일 주기 릴리스 패턴
- [[topics/professors-brain-02-relearning-llm]] — tokenizer/LM head 상세 파이프라인
