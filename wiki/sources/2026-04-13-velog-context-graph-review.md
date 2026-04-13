---
title: "Context Graph 논문 리뷰 (velog@cathx618)"
created: "2026-04-13"
updated: "2026-04-13"
type: source
sources: []
tags: [context-graph, knowledge-graph, paper-review, cgr3, korean]
status: active
published: false
slug: ""
description: ""
---

# Context Graph 논문 리뷰 (velog@cathx618)

> 원본: https://velog.io/@cathx618/%EB%85%BC%EB%AC%B8%EB%A6%AC%EB%B7%B0-Context-Graph
> 작성자: JeongYun Lee | 2026-02-09

## 핵심 요약

arxiv 논문 [[sources/2026-04-13-arxiv-2406-11160-context-graph]]를 한국어로 리뷰한 글. 삼중항 기반 KG의 한계를 구체적 예시로 설명하고 CGR³ 방법론의 단계를 상세히 정리.

## 주요 포인트

### 삼중항 KG의 2가지 한계

1. **맥락 정보 상실**: `Steve Jobs -Chairman of-> Apple Inc` 삼중항은 1980년과 2011년 모두 동일 → 시간 정보 없음
2. **의미 충돌 검증 불가**: "거주", "산다", "머무른다"가 단일 관계로 축약 → 정보 왜곡

### CGR³ 단계별 설명 (저자가 이해하기 쉽게 재구성)

**KGC 흐름**: 4가지 Retrieval → SFT/LoRA 기반 Ranking → 최종 답변

**KGQA 흐름**: Triple Retrieval → Entity Ranking → Context-aware Reasoning → (필요시 반복)

## 인사이트

- LLM 등장으로 **비정형 텍스트**의 Context Graph 변환이 테이블 데이터보다 오히려 더 쉬움
- 텍스트에서는 시간/위치 엔티티 식별이 자연스럽지만, 행 데이터에서는 엔티티 개수 판단 자체가 어려움

## 참고 자료

- [[sources/2026-04-13-arxiv-2406-11160-context-graph]]
- [[sources/2026-04-13-medium-modelmind-context-graphs]]

## 관련 페이지

- [[concepts/context-graph]]
- [[concepts/cgr3]]
- [[concepts/knowledge-graph]]
