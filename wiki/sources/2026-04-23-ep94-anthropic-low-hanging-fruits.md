---
title: "EP 94: Anthropic과 낮게 열린 과실들 — AI Frontier 팟캐스트"
created: "2026-04-24"
updated: "2026-04-24"
type: source
sources: []
tags: ["anthropic", "ai-frontier", "opus-4-7", "mythos", "adaptive-thinking", "claude-design", "managed-agents", "capability-overhang", "podcast"]
status: active
published: false
slug: ""
description: ""
---

# EP 94: Anthropic과 낮게 열린 과실들 — AI Frontier 팟캐스트

원본: `raw/articles/2026-04-23T160522+0900-EP 94 Anthropic과 낮게 열린 과실들.md`
출처: AI Frontier (aifrontier.kr) EP 94, 2026-04-21 녹화
진행: 노정석, 최승준

## 주요 주제 요약

### 70일 주기 모델 릴리스

Opus 라인 기준 대략 70일 간격으로 새 모델 출시. Opus 4 → 4.1 → 4.5 → 4.6 → 4.7. 릴리스 간격 통계상 Sonnet·Haiku 라인은 점점 늦어지는 반면 Opus는 더 빨라지는 추세. 사용자 수요가 Opus에 집중됨을 반영.

70일마다 새 모델 적응 작업이 필요해지는 구조. 현재 모델 사이클이 실질적으로 반년 분량의 임팩트를 만들어내는 속도감.

### Anthropic의 "안으로 들이기" 전략

외부 wrapper 서비스들을 공식 제품으로 내재화하는 방향. "딸깍딸깍하면서 밖에 있는 것들을 안으로 들인다"는 표현이 인상적.

- **Claude Design**: Figma 기반 외부 wrapper 서비스들의 역할을 공식 제품으로 통합
- **Managed Agents**: 뇌(brain, 모델)와 손(hand, 도구·실행)을 디커플링하는 서비스화. 세션·스토리지·샌드박스·시크릿 분리. S3 연동 포함.

상세: [[topics/professors-brain-03-closing-the-loop]], [[topics/agent-harness-notes-01-dual-domain]]

### Anthropic 집중 전략

텍스트·코딩에만 집중, B2B 유스케이스 심화. Claude Code가 대표 진입점. OpenAI는 "살짝 뒤늦게" 따라오고 있고, Google은 DeepMind/AI for Science 쪽에 무게를 두고 있다는 대비.

### Opus 4.7 — Adaptive Thinking과 Tokenizer

- Adaptive Thinking: 질문 난이도에 따라 추론 예산을 동적으로 조정. 웹 인터페이스에서는 사용자 제어 제한, Claude Code에서는 고정 가능.
- Tokenizer vocabulary 감소 → 같은 텍스트가 더 많은 토큰으로 분해 → 사용자 체감 1.3~1.4x 비용 증가. CJK 언어는 거의 변화 없음.
- Training cutoff: 2026년 1월

### Mythos

- 10T 파라미터 루머 (공식 미확인)
- 사이버보안 능력(zero-day 자동 발견, 도구 조합 공격 자동화) 우려로 프로덕션 미출시 → 그보다 compute shortage가 실질 원인이라는 분석도
- Anthropic 내부 사용 시작: 2026-02-24 추정
- Nicholas Carlini: "이미 있는 도구들을 잘 조합하는 능력" 맥락에서 언급
- Opus 파생 라인(Opus/Sonnet/Haiku)이 하나의 Mythos base model에서 Knowledge Distillation으로 만들어지는 구조로 전환됐을 것이라는 추정

### Capability Overhang

생명공학·화학·수학·보안 등 다양한 분야에서 일어나는 현상의 공통 본질: 모델이 이미 가지고 있는 능력을 "누가 빨리 잘 꺼내 쓰느냐"의 경쟁.

관련: [[concepts/ai-capability-overhang]]

### "낮게 열린 과실" 표현

모델이 스스로 완전히 작동하는 수준은 아니지만, 사람이 질문을 던지면 문헌을 잘 찾는 것만으로도 수학·과학·보안 쪽에서 쉽게 성과를 낼 수 있는 상태를 표현한 말. 팟캐스트의 에피소드 제목이기도 함.

## 블로그 연결

이 source는 blog 03편에서 참조됨: [[topics/professors-brain-03-closing-the-loop]]

## 관련 페이지

- [[entities/ai-frontier]] — AI Frontier 팟캐스트 엔티티
- [[entities/anthropic]] — Anthropic 엔티티
- [[entities/claude-code]] — Claude Code 엔티티
- [[concepts/opus-4-7]] — Opus 4.7 개념
- [[concepts/mythos]] — Mythos 개념
- [[concepts/adaptive-thinking]] — Adaptive Thinking 개념
- [[concepts/ai-capability-overhang]] — Capability Overhang 개념
- [[topics/professors-brain-03-closing-the-loop]] — 이 source를 참조한 블로그
- [[topics/agent-harness-notes-01-dual-domain]] — Managed Agents 관련 분석
