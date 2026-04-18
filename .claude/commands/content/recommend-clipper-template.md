---
description: "URL을 보고 ai-survival-log용 Obsidian Web Clipper 템플릿을 추천합니다"
---

# /content:recommend-clipper-template — URL 기반 클리퍼 템플릿 추천

사용자가 URL이나 웹 주소를 주면 `assets/clipper-templates/` 중 가장 적절한 Obsidian Web Clipper 템플릿을 추천합니다.

## 입력

- 단일 URL 또는 여러 URL
- 필요하면 간단한 맥락
  - 왜 저장하려는지
  - 공부용인지
  - 자산 참조용인지

## 워크플로우

### 1단계: URL 분류

먼저 URL의 visible cue만 보고 분류합니다.

- domain
- path
- slug
- 플랫폼 패턴

페이지 내용을 직접 열어야만 분류 가능한 경우가 아니면, browsing 없이 URL만으로 우선 분류합니다.

### 2단계: 템플릿 선택

- 아티클/블로그/문서: `articles/article-deep-research.json`
- 가벼운 저장용 아티클: `articles/article-quick-capture.json`
- 유튜브/강의/인터뷰: `videos/video-transcript-notes.json`
- 팟캐스트 에피소드: `podcasts/podcast-episode-notes.json`
- 책 챕터/읽기 정리: `books/book-chapter-notes.json`
- 책 인용/발췌: `books/book-quote-capture.json`
- 개인 메모/인사이트: `journals/journal-insight-capture.json`
- 긴 대화/세션 백업: `journals/conversation-backup.json`
- 이미지/첨부파일/갤러리/참조 자산: `other-assets/asset-reference-note.json`
- 애매한 경우: `generic/generic-source-capture.json`

### 3단계: intake 경로와 다음 단계 제안

항상 함께 알려줍니다:

- 추천 템플릿
- 이유
- 저장 경로
- 다음 harness
- 필요 시 보조 선택지

기본 경로:

- 텍스트 소스: `raw/{type}/`
- 채널 미정 자산 메모: `assets/intake/reference-notes/`

### 4단계: 출력 형식

다음 형식으로 답변합니다:

```md
추천 템플릿: `...`
이유: ...
저장 경로: `...`
다음 단계: `...`
보조 선택지: `...`
```

## 주의사항

- 수집 시점에 채널이 미정이면 `assets/blog/` 같은 채널 폴더로 바로 보내지 않습니다.
- 채널 미정 자산은 `assets/intake/`에 두고, 실제 활용 채널이 정해진 뒤 이동합니다.
- URL만으로 확신이 낮으면 기본 선택지 1개와 fallback 1개를 함께 줍니다.
