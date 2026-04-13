---
title: "CGR³ (Context Graph Reasoning)"
created: "2026-04-13"
updated: "2026-04-13"
type: concept
sources: ["[[sources/2026-04-13-arxiv-2406-11160-context-graph]]"]
tags: [cgr3, context-graph, llm, knowledge-graph, reasoning, rag]
status: active
published: false
slug: ""
description: ""
---

# CGR³ (Context Graph Reasoning)

Xu et al. (2024)이 제안한 **Retrieve-Rank-Reason** 3단계 패러다임. [[concepts/context-graph]]를 활용하여 LLM 기반 지식그래프 추론 성능을 대폭 향상시킨다.

논문: [[sources/2026-04-13-arxiv-2406-11160-context-graph]] (arXiv:2406.11160)

## 핵심 아이디어

기존 triple 기반 KG `(h, r, t)` → Context Graph `(h, r, t, rc)` 로 확장한 후, LLM을 3단계 파이프라인에 통합하여 추론한다.

```
질문 입력
  ↓
[1. Retrieve] — 관련 삼중항 + 맥락 수집
  ↓
[2. Rank]    — SFT+LoRA 모델로 후보 재정렬
  ↓
[3. Reason]  — LLM으로 최종 추론 (정보 부족 시 1로 복귀)
  ↓
답변 출력
```

## 3단계 상세

### 1단계: Retrieve (검색)

4가지 검색 방식을 병렬 수행:

| 방식 | 역할 |
|------|------|
| Supporting Triple | 구조적 정보 — h, r 공유 삼중항 |
| Textual Context | 자연어 강화 — Wikidata + Wikipedia 문장 |
| KG Embedding | 임베딩 기반 후보 사전 필터링 |
| LLM Generation | 자연어 질문으로 변환 후 LLM 후보 생성 |

### 2단계: Rank (순위 결정)

- **모델**: Llama-3-8B-Instruct + LoRA(rank=16) SFT
- 질문-삼중항-맥락 정합성을 "판사" LLM이 평가
- 기존 임베딩 순위와 합성하여 최종 재정렬
- **핵심**: 맥락 없이 순위만 제거하면 최대 25% 성능 하락

### 3단계: Reason (추론)

- **모델**: GPT-3.5-turbo-0125 (5-shot)
- 검색된 삼중항 + relation context 종합 판단
- 정보 충분하면 답변, 부족하면 → 1단계 재실행
- 최대 깊이 D_max=3, 빔 너비 M=3

## 성능

### KGC (지식그래프 완성)

베이스라인 대비 Hits@1 향상:
- FB15k-237: ComplEx +66%, RotatE +22%, GIE +11%
- YAGO3-10: ComplEx +31%, RotatE +10%, GIE +3%

### KGQA (질의응답)

| 데이터셋 | CGR³ | w/o Context | SOTA 대비 |
|----------|------|-------------|-----------|
| QALD10-en | 54.7% | 38.1% | +4.5%p |
| WWQ | 78.8% | 67.3% | +6.2%p |

## 왜 중요한가?

1. **맥락의 정량적 증명**: 맥락 제거 시 최대 25% 성능 하락 → 맥락이 단순 보조가 아닌 핵심 요소임을 실험으로 입증
2. **장꼬리 강건성**: 이웃 삼중항이 적은 희귀 엔티티에서도 일관된 성능 (LLM의 의미 이해가 구조적 희소성을 보완)
3. **반복 추론**: RAG의 단일 검색과 달리 충분한 정보를 확보할 때까지 반복 — 복잡한 다중 홉 질문에 유리

## 구현 스펙

- GPU: NVIDIA A100-SXM4-40GB × 8
- Rank: Llama-3-8B-Instruct, BF16, AdamW lr=1e-4
- Reason: GPT-3.5-turbo-0125

## 관련 페이지

- [[concepts/context-graph]]
- [[concepts/context-graph-extraction]] — CG 구축 전처리 단계
- [[concepts/knowledge-graph]]
- [[concepts/knowledge-graph-completion]]
- [[sources/2026-04-13-arxiv-2406-11160-context-graph]]
- [[sources/2026-04-13-velog-context-graph-review]]
