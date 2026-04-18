---
description: "책 스터디 대화를 위키 토픽과 시리즈형 블로그 포스트로 정리합니다"
---

# /content:book-study-blog — 책 스터디 → 위키 → 블로그

책 스터디 대화, 역질문, 보충 설명을 upstream 위키에 정리한 뒤 `ai-survival-log-site`용 시리즈 포스트로 연결합니다.

## 역할

- `ai-survival-log`는 authoring/source-of-truth 저장소다.
- 스터디 대화는 먼저 `raw/books/` 또는 `raw/articles/`와 `wiki/`에 흡수한다.
- 최종 블로그 출력은 `ai-survival-log-site/content/posts/`에서 소비된다.

## 입력

- 책 스터디 대화 로그
- 챕터 번호 또는 주제
- 관련 위키 토픽 경로가 있으면 함께 사용

## 워크플로우

### 1단계: source 보존

- 원본 대화나 정리 노트를 `raw/books/YYYY-MM-DD-*.md` 또는 `raw/articles/YYYY-MM-DD-*.md`로 보존한다.
- 이미 저장된 source가 있으면 재사용하고, 불필요한 중복 저장은 피한다.

### 2단계: 위키 정리

- 관련 개념/토픽 페이지를 찾는다.
- 없으면 `wiki/topics/` 또는 `wiki/concepts/`에 먼저 정리한다.
- 책 요약이 아니라 학습 과정, 의문, 보충 설명, 역질문이 드러나게 정리한다.

### 3단계: publish 준비

- 블로그로 나갈 토픽 페이지는 다음을 확인한다.
  - `published: true`
  - `slug`
  - `description`
  - standalone으로 읽히는 구조

### 4단계: 시리즈형 출력 연결

- downstream 출력은 `ai-survival-log-site/content/posts/YYYY-MM-DD-{slug}.mdx` 기준으로 본다.
- 책 스터디 포스트라면 downstream series 필드를 고려한다.
  - `series`
  - `seriesSlug`
  - `seriesOrder`

### 5단계: 검증

- source, wiki topic, downstream 포스트 경로가 서로 맞는지 확인한다.
- 책 스터디 lane가 일반 블로그 lane와 충돌하지 않는지 확인한다.
- 필요하면 `/wiki:publish`와 downstream content contract를 함께 점검한다.

## 작성 원칙

- 책 내용을 단순 요약하지 않는다.
- 질문이 생긴 맥락과 해소 과정을 남긴다.
- 예시, 코드, 비유를 설명보다 앞에 둔다.
- 역질문은 체화 확인 수단으로 남긴다.

## 완료 보고

```text
book-study-blog 정리 완료:
- source: raw/books/{파일명}
- wiki: wiki/topics/{slug}.md
- artifact: output/blog/YYYY-MM-DD-{slug}.mdx
- downstream target: ai-survival-log-site/content/posts/YYYY-MM-DD-{slug}.mdx
```
