---
title: "Context Graph"
created: "2026-04-13"
updated: "2026-04-13"
type: concept
sources: ["[[sources/2026-04-13-context-graph-vs-knowledge-graph]]", "[[sources/2026-04-13-arxiv-2406-11160-context-graph]]", "[[sources/2026-04-13-medium-modelmind-context-graphs]]"]
tags: [context-graph, knowledge-graph, ai, data-governance, rag, llm, cgr3]
status: active
published: false
slug: ""
description: ""
---

# Context Graph

Knowledge Graph에 운영 메타데이터를 추가하여 AI가 "어떻게 작동하고 왜 결정이 내려졌는지"를 이해할 수 있게 만드는 확장 구조.

## 정의

Context Graph는 [[concepts/knowledge-graph]]의 의미론적 관계에 다음을 추가한 개념이다:

- **의사결정 추적 (Decision Lineage)**: 승인, 예외, 워크플로우 이력
- **시간적 맥락 (Temporal Context)**: 유효기간, 거래 타임스탬프, 시간 역행 쿼리
- **출처 및 신뢰도 (Provenance & Confidence)**: 소스 귀속, 품질 신호
- **거버넌스 노드 (Policy as Graph)**: 접근 제어·규정 준수를 그래프 요소로 표현

## Knowledge Graph와의 비교

| 구분 | Knowledge Graph | Context Graph |
|------|-----------------|---------------|
| 핵심 질문 | "무엇인가?" | "어떻게? 왜?" |
| 시간 인식 | 정적 관계 | 시간 역행 쿼리 지원 |
| 메타데이터 | 기본 속성 | 정책·결정·출처 포함 |
| AI 통합 | 의미 이해 제공 | LLM 토큰 효율 + 할루시네이션 감소 |
| 쿼리 방식 | SPARQL/Cypher | 그래프 탐색 + 운영 필터 |

## AI에서의 역할

Context Graph는 AI 에이전트가 자율적으로 운영할 때 필수적인 인프라다:

1. **할루시네이션 감소**: 그래프 기반 RAG는 벡터 검색 대비 40% 이상 감소
2. **추적 가능한 추론**: 벡터 유사성과 달리 명시적 관계를 따라 응답 경로가 완전히 추적 가능
3. **선례 기반 의사결정**: AI 에이전트가 엣지 케이스를 만날 때 과거 결정 이력을 참조

## 학술적 정의 (Xu et al., 2024)

arXiv:2406.11160 논문은 Context Graph를 triple 확장으로 형식화:

```
기존 KG:      (h, r, t)
Context Graph: (h, r, t, rc)
                          └── relation context
                              (시간, 위치, 출처, 신뢰도, 사건 상세)
```

### 맥락 차원 분류 (논문 기준)

**엔티티 맥락**: 속성, 타입, 설명, 별칭, 참조 링크, 이미지, 음성, 영상

**관계 맥락**: 시간 정보, 지리적 위치, 정량 데이터, 출처, 신뢰도, 사건 상세

### 추론 패러다임: [[concepts/cgr3]]

논문에서 제안한 CGR³(Retrieve-Rank-Reason)은 Context Graph를 활용하여 KGC와 KGQA에서 SOTA를 달성:
- KGC (FB15k-237): 베이스라인 대비 Hits@1 최대 +66%
- KGQA (QALD10-en): 이전 SOTA 대비 +43.6%

## 아키텍처 패턴

```
의미층 (Knowledge Graph)
  └── 비즈니스 정의, 온톨로지, 엔티티 관계
운영층 (Context Graph Extension)
  └── 품질 지표, 데이터 라인리지, 정책, 사용 패턴
```

## 활용 사례

- **금융 규정 준수**: 규정·승인·결정 선례를 인코딩하여 감시 가능한 의사결정
- **AI 고객 지원**: 제품 지식 + 티켓 이력 + 정책 변경 + 예외 처리
- **데이터 거버넌스 플랫폼**: Atlan의 MCP 서버를 통한 조직 공유 언어 구현

## 이 위키와의 연결

흥미롭게도 이 위키([[concepts/llm-wiki-pattern]])는 작은 Context Graph다:
- **Knowledge**: 각 개념/엔티티 페이지
- **Context**: `wiki/log.md`(결정 이력), frontmatter의 `sources`(출처 추적), `\[\[wikilink\]\]`(관계망)

## 관련 페이지

- [[concepts/knowledge-graph]]
- [[concepts/cgr3]]
- [[concepts/knowledge-graph-completion]]
- [[concepts/llm-wiki-pattern]]
- [[sources/2026-04-13-context-graph-vs-knowledge-graph]]
- [[sources/2026-04-13-arxiv-2406-11160-context-graph]]
- [[sources/2026-04-13-velog-context-graph-review]]
- [[sources/2026-04-13-medium-modelmind-context-graphs]]
