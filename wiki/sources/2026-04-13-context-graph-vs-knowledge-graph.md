---
title: "Context Graph vs Knowledge Graph (Atlan)"
created: "2026-04-13"
updated: "2026-04-13"
type: source
sources: []
tags: [context-graph, knowledge-graph, ai, data-governance, rag]
status: active
published: false
slug: ""
description: ""
---

# Context Graph vs Knowledge Graph (Atlan)

> 원본: https://atlan.com/know/context-graph-vs-knowledge-graph/
> 수집일: 2026-04-13

## 핵심 요약

Knowledge Graph는 엔티티 간 의미론적 관계("무엇인가")를 정의하는 반면, Context Graph는 운영 메타데이터를 추가하여 AI가 "어떻게 작동하고 왜 결정이 내려졌는지"를 이해하게 합니다. Context Graph는 Knowledge Graph의 확장으로, AI 에이전트의 신뢰할 수 있는 자율 운영을 가능하게 합니다.

## 주요 포인트

- **Knowledge Graph**: RDF/프로퍼티 그래프 기반, 정적 의미 관계, SPARQL/Cypher 쿼리
- **Context Graph**: Knowledge Graph + 의사결정 추적 + 시간적 맥락 + 출처/신뢰도 + 거버넌스 정책
- 그래프 기반 RAG는 기존 벡터 검색 대비 **40% 이상 할루시네이션 감소**
- 현대 플랫폼은 두 계층을 결합: 의미층(Knowledge Graph) + 운영층(Context Graph)

## 인사이트

- Context Graph는 AI 에이전트가 엣지 케이스를 처리할 때 참조할 "선례 데이터베이스" 역할을 한다
- 정책(Policy)을 외부 문서가 아닌 그래프 노드로 표현함으로써 구조적으로 집행 가능하게 만드는 아이디어가 흥미롭다
- [[concepts/llm-wiki-pattern]]과 연결: 이 위키 자체도 일종의 Context Graph — 지식(Knowledge)에 맥락(인제스트 로그, 출처, 크로스레퍼런스)을 추가한 구조

## 관련 페이지

- [[concepts/context-graph]]
- [[concepts/knowledge-graph]]
- [[concepts/llm-wiki-pattern]]
