---
title: "임베딩 (Embedding)"
created: "2026-04-14"
updated: "2026-04-14"
type: concept
sources: ["[[sources/2026-04-14-system-design-interview-v1]]"]
tags: ["embedding", "vector", "llm", "rag", "machine-learning"]
status: active
published: false
slug: ""
description: ""
---

# 임베딩 (Embedding)

텍스트(또는 데이터)를 고차원 숫자 벡터로 변환하는 과정.
같은 "임베딩"이라는 단어가 맥락에 따라 3가지 다른 의미로 쓰인다.

## 3가지 맥락의 임베딩

### 1. 추론 시 임베딩 (Inference-time Embedding)

> 질문이 들어왔을 때 파라미터 관련 지식을 끌어내기 위한 과정

```
질문 텍스트
  ↓ 임베딩 변환
고차원 벡터
  ↓
Transformer 어텐션 메커니즘
  ↓
파라미터에서 관련 패턴 활성화
  ↓
답변 생성
```

### 2. 학습 단계 임베딩 (Training-time Embedding)

> 모델이 "벡터 변환 방법 자체"를 학습하는 과정

- 학습 전에는 임베딩 방법이 없음
- 수천억 번의 "다음 단어 맞추기" 반복으로 **어떻게 변환하면 좋은지** 파라미터가 학습
- 학습 완료 후 임베딩 방법이 파라미터에 내재화됨

### 3. Vector DB 임베딩 (Retrieval Embedding)

> 완성된 모델에 외부 데이터를 추가할 때, 문서를 모델이 읽기 쉽게 변환하는 과정

```
외부 문서 (PDF, DB, 최신 자료)
  ↓ 임베딩 모델로 벡터 변환
Vector DB 저장
  ↓ 질문 시 유사도 검색
관련 문서 추출 → 컨텍스트에 주입 (RAG)
```

## 핵심 차이

| 맥락 | 목적 | 주체 |
|------|------|------|
| 추론 시 | 파라미터 활성화 | 모델 내부 |
| 학습 단계 | 변환 방법 학습 | 학습 과정 |
| Vector DB | 외부 문서 검색 가능하게 저장 | 서비스 설계자 |

## 온톨로지와의 관계

임베딩은 **암묵적 온톨로지**로 볼 수 있음.
- 온톨로지: 개념 간 관계를 명시적으로 정의 ("개 IS-A 동물")
- 임베딩: 의미적으로 가까운 개념이 벡터 공간에서 가까이 위치 (이유는 블랙박스)

→ 목적은 같지만 온톨로지는 해석 가능, 임베딩은 블랙박스

## 관련 페이지

- [[concepts/rag]]
- [[concepts/knowledge-graph]]
- [[concepts/context-graph]]
- [[projects/study-system-design-interview]]
