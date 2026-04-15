---
description: "블로그 포스트를 인스타그램 캐러셀 제작 흐름으로 전개합니다"
---

# /content:blog-to-instagram — 블로그 → 인스타그램 캐러셀

블로그 포스트를 downstream 소비 관점에서 다시 읽어, 인스타그램 캐러셀 제작 흐름으로 전개합니다.

## 역할

- upstream 글의 구조와 메시지는 `ai-survival-log`에서 관리한다.
- 실제 블로그 소비 포맷은 `ai-survival-log-site`가 담당한다.
- 인스타그램 캐러셀은 블로그 포스트를 다시 압축한 downstream expansion lane다.

## 입력

- publish 가능한 wiki topic 또는 이미 발행된 블로그 포스트
- 관련 프로젝트 문서나 캡션 초안이 있으면 함께 사용

## 워크플로우

### 1단계: 기준 포스트 확정

- 기준이 되는 글을 하나 정한다.
- 가능하면 이미 publish 가능한 위키 토픽이나 downstream MDX를 기준으로 삼는다.

### 2단계: 핵심 메시지 추출

- 한 장짜리 요약이 아니라 슬라이드 흐름을 만든다.
- 기본 순서:
  - cover
  - opening hook
  - 핵심 포인트
  - 보충 사례 또는 수정 과정
  - closing message

### 3단계: downstream 경로 연결

- 블로그 원문은 `ai-survival-log-site/content/posts/` 기준으로 참조한다.
- 인스타그램 산출물은 별도 asset lane로 다루되, source post와 연결 관계를 유지한다.

### 4단계: 형식 검증

- 슬라이드가 원문 의미를 왜곡하지 않는지 본다.
- 제목, 훅, 결론이 블로그의 핵심 메시지와 맞는지 확인한다.
- 필요하면 downstream site 표현과 인스타 표현의 차이를 명시한다.

## 제작 원칙

- 블로그를 축약하되, 핵심 서사를 보존한다.
- 한 슬라이드에 너무 많은 설명을 넣지 않는다.
- 후킹 문장과 마무리 문장은 별도로 다듬는다.
- 인스타용 표현은 가능하지만 source-of-truth는 여전히 upstream wiki와 downstream post다.

## 완료 보고

```text
blog-to-instagram 준비 완료:
- source wiki topic: wiki/topics/{slug}.md
- downstream post: ai-survival-log-site/content/posts/YYYY-MM-DD-{slug}.mdx
- expansion lane: instagram/{date}/
```
