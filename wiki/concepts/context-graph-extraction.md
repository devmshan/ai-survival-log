---
title: "Context Graph Extraction (구축 단계)"
created: "2026-04-13"
updated: "2026-04-13"
type: concept
sources: ["[[sources/2026-04-13-velog-context-graph-review]]", "[[sources/2026-04-13-arxiv-2406-11160-context-graph]]"]
tags: [context-graph, extraction, sentence-bert, knowledge-graph, construction]
status: active
published: false
slug: ""
description: ""
---

# Context Graph Extraction (구축 단계)

[[concepts/context-graph]]를 **만드는** 전처리 작업. [[concepts/cgr3]]의 Retrieve-Rank-Reason이 추론(inference) 단계라면, Extraction은 그 이전에 Context Graph 자체를 구축(construction)하는 단계다.

## 핵심 구분

| 단계 | 작업 | 시점 |
|------|------|------|
| **Extraction** | Context Graph 구축 | 사전 처리 (오프라인) |
| **CGR³** | 구축된 CG로 질문에 답변 | 추론 시 (온라인) |

## Extraction 흐름

```
기존 삼중항 KG (FB15k-237, YAGO3-10, Wikidata5M 등)
  ↓ 1. Wikidata ID → Wikipedia 페이지 수집
  ↓ 2. Sentence-BERT로 삼중항 설명 문장 상위 r개 추출
  ↓ 3. 형식 변환
(h, r, t)  →  (h, r, t, rc)
                         └── rc = relation context (맥락 문장)
```

### 예시

```
기존: ("Steve Jobs", "Chairman of", "Apple Inc")

Extraction 후:
("Steve Jobs", "Chairman of", "Apple Inc",
 rc = "Steve Jobs served as chairman of Apple Inc.
       from 1997 until his death in 2011.")
```

→ 이제 1980년대와 2011년의 관계를 **구별**할 수 있게 된다.

## Sentence-BERT를 쓰는 이유

삼중항 `(h, r, t)`을 자연어로 표현했을 때, Wikipedia 문서에서 그 관계를 **가장 잘 설명하는** 문장을 골라야 한다.

Sentence-BERT는 문장 전체의 의미를 하나의 벡터로 인코딩하므로, 삼중항 텍스트와 Wikipedia 문장 사이의 **의미적 유사도**를 효율적으로 계산할 수 있다.

## 입력 데이터셋

| 데이터셋 | 규모 |
|----------|------|
| FB15k-237 | 14,541 엔티티, 237 관계 |
| YAGO3-10 | 123,182 엔티티, 37 관계 |
| Wikidata5M | 4,818,679 엔티티 |

## 왜 중요한가

Extraction 없이는 `(h, r, t, rc)` 형식의 Context Graph가 존재하지 않는다. CGR³의 성능 향상(KGC Hits@1 최대 +66%)은 이 Extraction 단계에서 만들어진 맥락 정보가 핵심 원인이다.

→ "맥락 없이 순위 결정 단계를 수행하면 최대 25% 성능 하락" — [[concepts/cgr3]] 실험 결과

## 관련 페이지

- [[concepts/context-graph]]
- [[concepts/cgr3]]
- [[concepts/knowledge-graph]]
- [[concepts/knowledge-graph-completion]]
- [[sources/2026-04-13-velog-context-graph-review]]
- [[sources/2026-04-13-arxiv-2406-11160-context-graph]]
