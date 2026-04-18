---
description: "소스 자료를 읽고 위키 페이지를 생성/갱신합니다"
---

# /wiki:ingest — 소스 자료 인제스트

소스 자료를 분석하여 위키 페이지를 자동으로 생성하고 갱신합니다.

## 입력

사용자가 제공하는 소스: 파일 경로, URL, 또는 인라인 텍스트.
인자가 없으면 사용자에게 소스를 요청합니다.

## 워크플로우

### 1단계: 소스 확보

- 파일 경로인 경우: 해당 파일을 읽습니다
- URL인 경우: WebFetch로 내용을 가져오고, `raw/articles/` 등에 `YYYY-MM-DD-제목.md` 형식으로 원본을 저장합니다
- 인라인 텍스트인 경우: 적절한 `raw/{type}/` 폴더에 저장합니다
- `raw/`의 파일은 **불변** — 한 번 저장하면 수정하지 않습니다

Obsidian Web Clipper를 쓸 때는 `assets/clipper-templates/`의 템플릿을 우선 사용합니다:

- 아티클: `articles/article-deep-research.json` 또는 `articles/article-quick-capture.json`
- 영상: `videos/video-transcript-notes.json`
- 팟캐스트: `podcasts/podcast-episode-notes.json`
- 책: `books/book-chapter-notes.json` 또는 `books/book-quote-capture.json`
- 저널/대화 기록: `journals/journal-insight-capture.json` 또는 `journals/conversation-backup.json`
- 이미지/첨부파일 참조: `other-assets/asset-reference-note.json`
- 애매한 자료: `generic/generic-source-capture.json`

클리퍼 템플릿은 다음 기준을 따릅니다:

- 텍스트 소스는 가능한 한 `raw/{type}/`로 바로 저장
- 자산 참조 노트는 `assets/intake/reference-notes/`로 저장
- 채널이 미정인 이미지/첨부파일은 `assets/intake/`에 머물고, 채널 결정 후에만 `assets/blog/` 등으로 이동
- 본문에 `Why This Matters`, `Summary Seed`, `Extraction Priorities`, `Recommended Harness` 같은 힌트 섹션을 남겨 `/wiki:ingest`가 후속 분석 방향을 빠르게 잡을 수 있게 함

### 2단계: 소스 분석

소스 자료에서 다음을 추출합니다:

- **핵심 요약**: 3-5줄 요약
- **엔티티**: 도구, 프레임워크, 인물, 제품 등 고유명사
- **개념**: 아이디어, 패턴, 정의 등 추상적 개념
- **관련 토픽**: 기존 위키 토픽과의 연결점

### 3단계: 위키 페이지 생성/갱신

1. **소스 요약 페이지** (`wiki/sources/`) — 항상 새로 생성
   - frontmatter: `type: source`
   - 핵심 요약, 주요 포인트, 인사이트

2. **엔티티 페이지** (`wiki/entities/`) — 기존 페이지가 있으면 갱신, 없으면 생성
   - 갱신 시: 기존 내용 보존 + 새 정보 추가 + 출처 표기

3. **개념 페이지** (`wiki/concepts/`) — 기존 페이지가 있으면 갱신, 없으면 생성
   - 충돌 정보가 있으면 출처와 함께 병기

4. **토픽 페이지** (`wiki/topics/`) — 관련 기존 토픽이 있으면 갱신

### 4단계: 크로스 레퍼런싱

- 모든 신규/갱신 페이지에 `[[wikilink]]` 추가
- 관련 기존 페이지의 `## 관련 페이지` 섹션에 역링크 추가

### 5단계: 인덱스 및 로그 갱신

- `wiki/index.md` — 신규 페이지 추가, 카테고리별 알파벳순
- `wiki/log.md` — 작업 기록 추가 (날짜, 시간, 생성/갱신 페이지 목록, 요약)

## 완료 보고

인제스트 완료 후 다음을 보고합니다:

```
인제스트 완료:
- 소스: [소스 제목]
- 생성: N개 페이지 (목록)
- 갱신: M개 페이지 (목록)
- 총 위키 페이지: X개
```

## 주의사항

- 하나의 소스가 10-15개 페이지에 영향을 줄 수 있음
- 기존 페이지 갱신 시 절대로 기존 내용을 삭제하지 않음
- 모든 위키 페이지는 CLAUDE.md의 frontmatter 스펙을 따름
