# Context Graph 논문 리뷰 (velog@cathx618)

> 원본 URL: https://velog.io/@cathx618/%EB%85%BC%EB%AC%B8%EB%A6%AC%EB%B7%B0-Context-Graph
> 수집일: 2026-04-13
> 작성자: JeongYun Lee (2026-02-09)

## 핵심 요약

기존 삼중항(triple) 기반 지식그래프의 맥락 정보 상실 문제를 분석하고, Context Graph의 CGR³ 방법론을 리뷰한 글.

## 삼중항 KG의 한계

- "Steve Jobs-Chairman of->Apple Inc"는 1980년과 2011년 모두 동일한 삼중항 → 시간 정보 상실
- 의미적으로 유사한 속성("거주", "산다", "머무른다")이 단일 관계로 축약되어 정보 왜곡

## CGR³ 방법론

### KGC 단계
1. Supporting Triple Retrieval (구조적)
2. Textual Context Retrieval (자연어 강화)
3. Candidate Answer Retrieval from KG (임베딩)
4. Candidate Answer Retrieval from Text (LLM)
5. SFT/LoRA 기반 LLM으로 최종 순위 매김

### KGQA 단계
1. Context-aware Triple Retrieval
2. Candidate Entity Ranking
3. Context-aware Reasoning (반복 가능)

## 저자 인사이트

LLM 등장으로 비정형 데이터의 Context Graph 변환이 테이블형 정형 데이터 변환보다 더 용이함.

## 참고 자료
- https://arxiv.org/abs/2406.11160
- https://medium.com/modelmind/what-are-context-graphs-building-the-ai-that-trulyunderstands-e7e5db39138d
