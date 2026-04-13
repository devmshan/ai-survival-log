---
title: "What Are Context Graphs? (Medium/ModelMind)"
created: "2026-04-13"
updated: "2026-04-13"
type: source
sources: []
tags: [context-graph, knowledge-graph, ai, explainer]
status: active
published: false
slug: ""
description: ""
---

# What Are Context Graphs? (Medium/ModelMind)

> 원본: https://medium.com/modelmind/what-are-context-graphs-building-the-ai-that-trulyunderstands-e7e5db39138d
> 참고: Paywall으로 인트로 섹션만 수집

## 핵심 요약

Context Graph를 비기술적 독자에게 설명하는 인트로덕션 글. 전통 DB → Knowledge Graph → Context Graph로의 진화 단계를 간결하게 도식화.

## 주요 포인트

### 데이터 구조 진화 3단계

| 단계 | 표현 | 맥락 |
|------|------|------|
| 전통 DB | Name, Email, LastPurchase 컬럼 | 없음 |
| Knowledge Graph | Customer→Purchased→Product 관계 | 메타데이터로만 |
| Context Graph | 관계 + 5차원 맥락 내장 | 1급 시민 |

### 5가지 맥락 차원

1. **Temporal** — 언제 발생했는가
2. **Spatial** — 어디서 발생했는가
3. **Confidence** — 얼마나 확실한가
4. **Provenance** — 어디서 온 정보인가
5. **Reasoning traces** — 왜 그런 결정을 했는가

## 인사이트

- "5가지 차원" 프레임은 [[sources/2026-04-13-arxiv-2406-11160-context-graph]] 논문의 맥락 분류와 일치
- Reasoning traces(추론 기록)를 맥락 차원으로 포함하는 점이 [[sources/2026-04-13-context-graph-vs-knowledge-graph]]의 "의사결정 추적"과 동일한 개념

## 관련 페이지

- [[concepts/context-graph]]
- [[concepts/knowledge-graph]]
- [[sources/2026-04-13-arxiv-2406-11160-context-graph]]
