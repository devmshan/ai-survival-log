---
title: "Claude/Codex 선택 기로 — Anthropic 방향성 분석 저널"
created: "2026-04-24"
updated: "2026-04-24"
type: source
sources: []
tags: ["claude-code", "codex", "anthropic", "opus-4-7", "mythos", "adaptive-thinking", "gpu", "journal"]
status: active
published: false
slug: ""
description: ""
---

# Claude/Codex 선택 기로 — Anthropic 방향성 분석 저널

원본: `raw/journals/2026-04-23-claude-codex-choice-and-anthropic-direction.md`

## 배경

- Claude Code Max 구독 시작: 2026년 3월 9일
- 4월 들어 토큰 소모량이 눈에 띄게 늘었다는 체감 (원인 불명확 — 성능 개선인지 내부 캐시 정책 변경인지)
- 2026-04-09 ~ 2026-04-23 기간 API 사용량: $83.98 (하루 평균 약 $5)
- Codex Plus 구독도 병행 사용 중

## 핵심 질문

"내가 잘못 쓰고 있는 건지, Anthropic 정책이 잘못된 건지" 판단하기 위해 자료 조사 시작.

## 주관적 도구 비교 (2026-04 기준)

- Claude Code: 빠르지만 더 자주 수정 필요. 토큰 소모가 Codex 대비 몇 배 체감.
- Codex: 같은 결과물 대비 토큰 소모가 상대적으로 적게 체감.

상세: [[topics/claude-code-to-codex]]

## Anthropic 방향성 분석

저널에서 추출한 4가지 시그널:

1. **Pro 모델 Claude Code 사용 금지 테스트**: Anthropic이 Pro 플랜에서 Claude Code 사용을 제한하는 테스트를 진행 중이라는 이야기가 있었다.
2. **Opus 4.7 토큰 1.3~1.5x 증가**: 새 모델 출시와 함께 같은 작업에 더 많은 토큰이 소비됨. Adaptive Thinking 도입 및 tokenizer 변경이 원인으로 추정.
3. **Mythos 출시 지연**: 사이버보안 능력 우려라는 공식 이유 외에, compute shortage(GPU 수급난)가 실질 원인이라는 분석이 있음.
4. **GPU 수급난 지속**: 2025년 GPU 확보 부족의 여파가 2026년까지 이어짐. Google, OpenAI, Anthropic 3사 중 컴퓨팅 자원이 가장 적은 상태.

## GPU/TPU/Trainium 비교 메모

저널에서 정리한 하드웨어 생태계 차이:

| 칩 | 특징 |
|---|---|
| NVIDIA GPU | 가장 범용적. AI·그래픽·HPC. CUDA 생태계 표준. |
| Google TPU | AI 학습/추론 전용. TensorFlow/JAX 최적화. Google Cloud 중심. |
| AWS Trainium | 학습 비용 절감 목적. AWS Neuron 생태계. |

Anthropic은 NVIDIA 의존도를 줄이는 방향 탐색 중이나, 하드웨어 타임프레임(2~3년 리드타임)과 소프트웨어 주기(60~70일) 사이의 미스매치가 진행 중.

## 결론

Anthropic의 정책 실패보다는 compute-constrained efficiency 전략으로 해석. 주어진 자원 안에서 최적 효율을 내기 위한 선택들로 보임.

## 관련 페이지

- [[entities/anthropic]] — Anthropic 엔티티 페이지
- [[entities/codex]] — Codex 엔티티 페이지
- [[entities/claude-code]] — Claude Code 엔티티 페이지
- [[concepts/opus-4-7]] — Opus 4.7 모델
- [[concepts/mythos]] — Mythos 모델
- [[concepts/adaptive-thinking]] — Adaptive Thinking 개념
- [[concepts/ai-capability-overhang]] — 능력 과잉 보유 개념
- [[topics/claude-code-to-codex]] — 도구 선택 결정 과정
