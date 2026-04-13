---
title: "Knowledge Graph Completion (KGC)"
created: "2026-04-13"
updated: "2026-04-13"
type: concept
sources: ["[[sources/2026-04-13-arxiv-2406-11160-context-graph]]"]
tags: [knowledge-graph, kgc, link-prediction, embedding, ai]
status: active
published: false
slug: ""
description: ""
---

# Knowledge Graph Completion (KGC)

지식그래프에서 **누락된 관계나 엔티티를 예측**하는 태스크. `(h, r, ?)` 또는 `(?, r, t)` 형태의 불완전한 삼중항을 완성하는 것이 목표.

## 정의

실세계 지식그래프는 불완전하다. "Steve Jobs -foundedBy-> ?" 같은 누락된 링크를 자동으로 채우는 것이 KGC(Knowledge Graph Completion) 또는 링크 예측(Link Prediction)이다.

## 대표 벤치마크

| 데이터셋 | 엔티티 수 | 관계 수 | 학습 삼중항 수 |
|----------|----------|--------|--------------|
| **FB15k-237** | 14,541 | 237 | 272,115 |
| **YAGO3-10** | 123,182 | 37 | 1,079,040 |
| Wikidata5M | 4,818,679 | 828 | 20,614,279 |

## 전통적 접근법 (임베딩 모델)

| 모델 | 특징 |
|------|------|
| **ComplEx** | 복소수 임베딩, 비대칭 관계 처리 |
| **RotatE** | 회전 변환 기반, 다양한 관계 패턴 |
| **GIE** | 쌍곡 공간 + 유클리드/구면 혼합 |

이들은 구조적 패턴을 잘 학습하지만 **맥락 정보 부재**로 한계.

## LLM 기반 접근법의 등장

[[concepts/cgr3]]는 기존 임베딩 모델의 한계를 LLM과 맥락 정보로 보완:
- 임베딩: 후보 사전 필터링 (효율)
- LLM + Context: 최종 순위 결정 (정확도)

CGR³ 결과: ComplEx 대비 FB15k-237 Hits@1 +66%, YAGO3-10 +31%

## 평가 지표

- **Hits@K**: 상위 K개 예측 안에 정답이 있는 비율
- **MRR**: Mean Reciprocal Rank — 정답 순위의 역수 평균

## 관련 페이지

- [[concepts/knowledge-graph]]
- [[concepts/context-graph]]
- [[concepts/cgr3]]
- [[sources/2026-04-13-arxiv-2406-11160-context-graph]]
