---
title: "RLVR (Reinforcement Learning by Verifiable Rewards)"
created: "2026-04-12"
updated: "2026-04-12"
type: concept
sources: ["[[sources/2026-04-12-ai-unbundle-myself]]"]
tags: [ai, rlvr, machine-learning, ai-capability]
status: active
published: false
slug: ""
description: ""
---

# RLVR (Reinforcement Learning by Verifiable Rewards)

AI가 세상을 정복하는 방식. 보상신호(verifiable reward)를 만들 수 있는 도메인이라면, 충분한 Compute를 투입했을 때 AI가 정복할 수 있다는 원리.

## 정의

**RLVR:** 검증 가능한 보상신호를 기반으로 하는 강화학습.

- 정답이 명확하게 판별 가능한 도메인 → 보상신호 설계 가능 → AI 훈련 가능 → AI가 인간 수준 또는 초월
- 핵심 질문: "이 도메인의 성과를 객관적으로 측정할 수 있는가?"

## RLVR이 작동하는 도메인 (예시)

| 도메인 | 보상신호 | 상태 |
|--------|----------|------|
| 바둑/체스 | 승패 | ✅ AI 초월 |
| 수학 증명 | 정오 판별 | ✅ AI 초월 |
| 코딩 | 테스트 통과 여부 | ✅ AI 수준 급상승 |
| 법률 자문 | 법과 판례 기반 정오 | ⚡ 진입 중 |
| 의료 진단 | 임상 결과 | ⚡ 진입 중 (앤스로픽 바이오 인수) |

## RLVR이 닿지 않는 영역

보상신호로 포착되지 않는 영역:

- **암묵적 신뢰와 맥락:** 말하지 않아도 아는 관계, 의뢰인과의 신뢰
- **미적 판단:** "좋은 글"의 기준, 브랜드 감각
- **인간적 판단:** 법정 안팎의 복합적 상황 해석
- **가치 충돌:** 어떤 목표를 추구해야 하는지 자체

변호사 예시: 법률 자문의 정오는 명확히 판별 가능하지만, Lawyer / Attorney / Esquire 각 단어가 함의하는 무게가 다르듯, 법정 안팎의 판단은 보상신호로 포착 불가.

## AI 확장의 패턴

앤스로픽의 바이오 스타트업 인수처럼, RLVR이 작동하는 도메인이 점진적으로 확장 중. 어디까지 확장될지는 아직 알 수 없다.

> *"AI가 코드를 개선하는 방식으로, 나 자신을 개선한다."*

## 관련 페이지

- [[concepts/ai-unbundling]] — RLVR 확장과 함께 일어나는 산업 재편
- [[concepts/ralph-loop]] — RLVR 원리를 자기 성장에 적용
- [[concepts/tacit-knowledge]] — RLVR이 닿지 않는 암묵지 영역
- [[topics/ai-era-survival]] — AI 시대 생존 전략 종합
- [[sources/2026-04-12-ai-unbundle-myself]] — 원본 소스
