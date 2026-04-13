---
title: "Knowledge Graph"
created: "2026-04-13"
updated: "2026-04-13"
type: concept
sources: ["[[sources/2026-04-13-context-graph-vs-knowledge-graph]]"]
tags: [knowledge-graph, graph-database, semantic-web, ai, ontology]
status: active
published: false
slug: ""
description: ""
---

# Knowledge Graph

엔티티와 그 관계를 구조화된 그래프로 표현하여 "사물이 무엇인지"를 의미론적으로 정의하는 데이터 구조.

## 정의

Knowledge Graph는 노드(엔티티)와 엣지(관계)로 구성되어 실세계 개념 간의 의미론적 관계를 표현한다. RDF(Resource Description Framework) 트리플 스토어 또는 프로퍼티 그래프 기반으로 구현된다.

## 구성 요소

- **노드(Node)**: 엔티티 (사람, 제품, 개념, 장소 등)
- **엣지(Edge)**: 관계 (is-a, has-part, related-to 등)
- **속성(Property)**: 엔티티/관계의 추가 정보
- **온톨로지(Ontology)**: 도메인 어휘와 분류 체계

## 기술 스택

- **쿼리 언어**: SPARQL (RDF 기반), Cypher (Neo4j)
- **데이터 모델**: RDF 트리플 (주어-술어-목적어), 프로퍼티 그래프
- **추론**: 규칙 기반 엔진 (RDFS, OWL)

## 적합한 사용 사례

- 도메인 온톨로지 및 비즈니스 어휘 정의
- 제품 카탈로그, 의료 온톨로지
- 의미론적 검색
- 추천 시스템의 관계 모델링

## 한계

- 정적이거나 천천히 변하는 관계만 표현
- 의사결정 이력, 시간적 맥락, 거버넌스 정책 표현 어려움
- AI 에이전트의 자율 운영에 필요한 "왜"와 "어떻게"가 없음

→ 이 한계를 극복한 확장이 [[concepts/context-graph]]

## 관련 페이지

- [[concepts/context-graph]]
- [[concepts/knowledge-graph-completion]]
- [[concepts/cgr3]]
- [[sources/2026-04-13-context-graph-vs-knowledge-graph]]
- [[sources/2026-04-13-arxiv-2406-11160-context-graph]]
