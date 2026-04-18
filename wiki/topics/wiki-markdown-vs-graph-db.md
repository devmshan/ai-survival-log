---
title: "Wiki 정형화/자동화 vs 마크다운: LLM에 맞는 방식"
created: "2026-04-13"
updated: "2026-04-13"
type: topic
sources: []
tags: [wiki, llm, markdown, knowledge-management, context-graph, design-decision]
status: active
published: false
slug: ""
description: ""
---

# Wiki 정형화/자동화 vs 마크다운: LLM에 맞는 방식

**결론: 정형화/자동화는 Claude에게 오히려 불리하다. 현재 마크다운 방식이 Claude 작업에 더 잘 맞는다.**

## Claude가 실제로 "읽는" 방식

Claude는 그래프 DB를 쿼리하지 않는다. Claude는 **파일을 텍스트로 읽는다.**

```
그래프 DB 정형화 시:
  Claude → API 호출 → JSON 응답 파싱 → 의미 해석
  (구조는 정밀하지만 Claude에게 낯선 인터페이스)

현재 마크다운:
  Claude → 파일 읽기 → 즉시 이해
  (Claude가 훈련된 그대로의 형식)
```

[[concepts/llm-wiki-pattern]]이 "The wiki is just a git repo of markdown files"라고 말하는 이유가 바로 이것이다. **마크다운이 LLM의 네이티브 포맷**이다.

## 정형화/자동화를 도입하면 생기는 문제

| 문제 | 내용 |
|------|------|
| **도구 추가** | Neo4j, SPARQL 엔진 등 외부 인프라 필요 |
| **컨텍스트 낭비** | API 응답 JSON을 파싱하는 추가 토큰 소모 |
| **유연성 저하** | 스키마 변경 시 전체 마이그레이션 필요 |
| **인간 가독성 상실** | 사용자가 직접 읽고 수정하기 어려워짐 |
| **Claude의 강점 미활용** | Claude는 자연어 이해가 강점인데, 정형 쿼리로 대체됨 |

## 현재 방식이 Claude에게 유리한 이유

[[concepts/context-graph-extraction]]에서 정형 Context Graph는 Sentence-BERT 같은 별도 모델이 자동 처리를 담당한다. 하지만 Claude는 그 역할을 더 잘 수행한다:

```
Sentence-BERT: 문장 유사도만 계산
Claude:        의미 이해 + 판단 + 요약 + 크로스레퍼런싱 동시 수행
```

Claude + 마크다운 조합이 이미 Context Graph의 자동화 부분을 대체하고 있다.

## 개선할 가치가 있는 것 (정형화 아님)

정형화 대신 **Claude가 실제로 느리거나 어려운 부분**을 개선하는 것이 낫다:

| 현재 병목 | 개선 방향 |
|-----------|-----------|
| `index.md`를 매번 수동 갱신 | 인제스트 시 자동 업데이트 스크립트 |
| 깨진 링크 발견이 늦음 | `/wiki:lint` 주기 실행 |
| 페이지 수 늘수록 `index.md` 탐색 느려짐 | 태그 기반 서브인덱스 추가 |

## 이 위키와 Context Graph의 관계 재정리

이 위키는 [[concepts/context-graph]]의 **철학적 동형체**다:
- Context Graph가 해결하는 문제(맥락 보존)를 **사람 + LLM 협업**으로 푼다
- Context Graph는 그것을 **기계가 자동으로** 처리한다
- 둘 다 "지식에 맥락을 붙인다"는 본질은 같다

정형화/자동화는 **규모(수백만 삼중항)** 가 필요할 때 의미 있다. 개인 지식 위키(50~200 페이지) 규모에서는 마크다운 + Claude 조합이 더 단순하고 강력하다.

**참고:** Graphify(`graphify .`)처럼 마크다운을 직접 처리해 지식 그래프를 생성하는 도구는 `wiki/` 구조를 바꾸지 않고 파생 레이어로 쓸 수 있다. 이 경우 "그래프 DB를 쿼리하게 만드는" 문제는 없지만, 현재 규모에서 가치 대비 비용이 아직 불분명하다. 200+ 페이지 또는 MCP 쿼리 인터페이스가 필요해질 때 검토 대상. → [[topics/graphify-evaluation]]

## 관련 페이지

- [[concepts/llm-wiki-pattern]]
- [[concepts/context-graph]]
- [[concepts/context-graph-extraction]]
- [[concepts/knowledge-graph]]
- [[topics/graphify-evaluation]]
