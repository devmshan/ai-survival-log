---
title: "RAG (Retrieval-Augmented Generation)"
created: "2026-04-14"
updated: "2026-04-14"
type: concept
sources: ["[[sources/2026-04-14-system-design-interview-v1]]"]
tags: ["rag", "llm", "vector-db", "embedding", "ai-architecture"]
status: active
published: false
slug: ""
description: ""
---

# RAG (Retrieval-Augmented Generation)

LLM이 학습된 파라미터만으로 답변하면 발생하는 한계를 보완하기 위해,
외부 지식 베이스(Vector DB)를 실시간으로 검색해서 컨텍스트에 주입하는 기술/방법론.

## RAG가 필요한 이유

### LLM 파라미터만 사용 시 한계

| 문제 | 원인 |
|------|------|
| 할루시네이션 | 뇌처럼 패턴을 재현하므로 부정확할 수 있음 |
| 지식 컷오프 | 학습 시점 이후 정보를 모름 |
| 도메인 지식 부재 | 특정 조직 내부 자료는 학습 불가 |

## RAG 동작 방식

```
[사전 준비] 외부 문서 → 임베딩 변환 → Vector DB 저장

[질문 시]
  질문
    ↓
  질문도 임베딩 변환
    ↓
  Vector DB에서 코사인 유사도로 관련 문서 검색
    ↓
  검색된 문서를 컨텍스트에 주입
    ↓
  LLM 파라미터 + 주입된 문서 조합해서 답변
```

## 비유: 교수님 + 도서관

```
LLM 파라미터  =  교수님 뇌 (수십년 학습이 압축됨)
Vector DB     =  도서관 (최신 논문, 내부 자료 보관)
RAG           =  질문 받을 때 도서관에서 관련 자료 꺼내 참고하는 체계
```

## RAG의 두 가지 핵심 효과

1. **정확성 향상** — 명확한 출처 문서 기반 답변 → 할루시네이션 감소
2. **최신성 확보** — 학습 이후 데이터도 참조 가능

## 활용 예시

| 도메인 | Vector DB에 넣는 것 |
|--------|-------------------|
| 대학교 | 교내 논문, 강의자료, 공지사항 |
| 기업 | 사내 문서, 제품 매뉴얼, 고객 DB |
| 의료 | 최신 논문, 진료 가이드라인 |

## LLM vs RAG 비교

```
LLM만:    질문 → 파라미터 → 답변 (뇌만 사용)
RAG 추가: 질문 → Vector DB 검색 → 컨텍스트 주입
                      ↓
               파라미터 + 문서 → 답변 (뇌 + 도서관)
```

## 관련 페이지

- [[concepts/embedding]]
- [[concepts/knowledge-graph]]
- [[concepts/context-graph]]
- [[projects/study-system-design-interview]]
