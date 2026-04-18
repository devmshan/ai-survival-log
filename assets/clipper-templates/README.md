# Obsidian Web Clipper Templates

이 폴더는 `ai-survival-log`의 `raw/wiki/assets/output` 흐름에 맞춘 Obsidian Web Clipper 템플릿 모음이다.

기본 원칙:

- 웹에서 수집한 텍스트 소스는 `raw/*`로 보낸다.
- 이미지나 첨부파일처럼 바로 wiki source가 되기 어려운 자료는 `assets/intake/`에 먼저 남긴다.
- 각 템플릿은 `/wiki:ingest`가 읽기 쉬운 섹션 구조와 힌트 문구를 포함한다.
- `book-study` 계열은 `/content:book-study-blog`로 이어질 수 있게 설계한다.
- 파일명은 Obsidian Web Clipper에서 `{{date}}-{{title}}` 형식으로 생성되므로, 필요하면 나중에 수동 정리한다.

자산 경계 원칙:

- 수집 시점에 채널이 미정이면 `assets/intake/`를 사용한다.
- 블로그, 유튜브, 인스타그램, 웹툰 중 어느 채널로 갈지 결정된 뒤에만 `assets/blog/`, `assets/youtube/`, `assets/instagram/`, `assets/webtoon/`로 옮긴다.
- publishable 블로그 글에서 실제로 쓰는 upstream 이미지만 `assets/blog/`에 둔다.

추천 분류:

- `articles/`: 웹 클리핑, 아티클, 기술 글, 리서치 포스트
- `videos/`: 영상 스크립트, 강의/인터뷰 메모, 전사 초안
- `podcasts/`: 팟캐스트 에피소드 노트
- `books/`: 책 노트, 챕터별 정리, 인용 정리
- `journals/`: 일기, 생각 메모, 대화 백업, 인사이트
- `other-assets/`: 이미지, 첨부파일, 참조 자산의 메타 노트
- `generic/`: 분류가 애매할 때 임시 수집

템플릿 선택 가이드:

- 깊게 읽을 글: `articles/article-deep-research.json`
- 일단 보존할 글: `articles/article-quick-capture.json`
- 유튜브/강의/인터뷰: `videos/video-transcript-notes.json`
- 팟캐스트: `podcasts/podcast-episode-notes.json`
- 책 챕터 정리: `books/book-chapter-notes.json`
- 책 인용/발췌: `books/book-quote-capture.json`
- 개인 인사이트: `journals/journal-insight-capture.json`
- 긴 대화 백업: `journals/conversation-backup.json`
- 이미지/첨부파일 수집 기록: `other-assets/asset-reference-note.json`
- 분류가 애매함: `generic/generic-source-capture.json`

Harness 연결 의도:

- `raw/articles`, `raw/videos`, `raw/podcasts`, `raw/books`, `raw/journals`
  - 다음 단계 기본값: `/wiki:ingest`
- `raw/books`
  - 다음 단계 후보: `/wiki:ingest` 후 `/content:book-study-blog`
- `assets/intake/reference-notes`
  - 다음 단계 후보: wiki publishable 페이지나 채널 자산 제작 시 참조

운영 제안:

- 현재 `assets/`는 수집 inbox와 채널 자산 원본을 분리해 가져가는 편이 자연스럽다.
- Web Clipper 템플릿은 `assets/clipper-templates/`로 분리해 두는 편이 의미가 명확하다.
- 채널 미정 자산 intake는 `assets/intake/reference-notes/`, `assets/intake/reference-images/`, `assets/intake/attachments/`로 관리한다.
