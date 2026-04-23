---
title: "Mythos"
created: "2026-04-24"
updated: "2026-04-24"
type: concept
sources: ["[[sources/2026-04-23-ep94-anthropic-low-hanging-fruits]]", "[[sources/2026-04-23-claude-codex-choice-and-anthropic-direction]]"]
tags: ["mythos", "anthropic", "llm", "ai-safety", "compute"]
status: active
published: false
slug: ""
description: ""
---

# Mythos

Anthropic 내부 개발 중인 대형 모델 (2026년 4월 기준 비공개). 공식 사양은 공개되지 않았으며 이 페이지의 내용은 팟캐스트와 커뮤니티 루머에 기반한다.

## 알려진 사항 (루머·추정, 공식 미확인)

- **파라미터 규모**: 10T(10조) 규모라는 루머가 커뮤니티에서 회자됨. 공식 사양 아님.
- **내부 사용 시작**: 2026년 2월 24일부터 Anthropic 내부 얼리 액세스 시작이라는 이야기가 있음.
- **50개 기관 얼리 액세스**: 보안 관련 평가를 위해 한정 기관에 선공개 중이라는 보도.

## 프로덕션 미출시 이유 (두 가지 설)

### 1. 사이버보안 능력 우려

Anthropic이 공식적으로 언급한 이유. 코딩 능력이 뛰어난 모델로 발전하다 보니 zero-day 취약점 발견, 도구 조합을 통한 보안 공격 자동화 수준의 능력을 갖추게 됐다는 것. Nicholas Carlini(보안 연구자)가 이 맥락에서 언급됨.

EP 94 관련 표현: "이미 있는 도구들을 잘 조합하는 능력이 뛰어나다" — 새로운 차원의 모델이라기보다 코딩을 잘하는 모델이 자연스럽게 보안 도구 조합 능력까지 갖춘 상태.

### 2. Compute Shortage 블로킹 (커뮤니티 분석)

Google, OpenAI, Anthropic 3사 중 Anthropic의 컴퓨팅 자원이 가장 부족하다는 분석. 2025년에 GPU 확보를 충분히 하지 못한 여파가 2026년까지 이어지고 있다는 평가.

NVIDIA GPU → AWS Trainium → Google TPU 대안 탐색 중이나, 하드웨어 타임프레임(2~3년 리드타임)과 소프트웨어 주기(60~70일) 사이의 미스매치가 있음.

## 모델 아키텍처 추정

EP 94에서 한 가설: Anthropic이 기존에는 Opus/Sonnet/Haiku 각 라인이 독립적으로 pre-training됐다면, 지금은 Mythos라는 하나의 큰 base model에서 Knowledge Distillation(KD) 방식으로 각 사이즈로 파생시키는 구조로 전환됐을 것이라는 추정. Opus 4.7의 system card에서 리소스 감사(audit) 언급이 이를 간접적으로 지지한다는 해석.

## IPO 마케팅 맥락

일부 커뮤니티에서는 Mythos를 둘러싼 화제가 IPO를 앞두고 한 의도적인 "밑장 깔기"라는 시각도 있음.

## 관련 페이지

- [[entities/anthropic]] — Mythos 개발 주체
- [[concepts/opus-4-7]] — Mythos에서 KD된 파생 모델 추정
- [[concepts/adaptive-thinking]] — Opus 4.7 (Mythos 파생 추정)에서 도입된 특징
- [[concepts/ai-capability-overhang]] — 모델 능력 과잉 보유 개념
- [[sources/2026-04-23-ep94-anthropic-low-hanging-fruits]] — EP 94 source
