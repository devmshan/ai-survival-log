---
title: "Assets Intake Pattern"
created: "2026-04-18"
updated: "2026-04-18"
type: concept
sources: []
tags: [assets, intake, raw-layer, knowledge-capture, workflow, wiki]
status: active
published: false
slug: ""
description: ""
---

# Assets Intake Pattern

`ai-survival-log`에서 지식/자산을 수집할 때 텍스트 소스와 비텍스트 자산을 분리해 처리하는 이중 intake 구조.

## 핵심 아이디어

자료를 수집하는 시점에는 어떤 채널(블로그, 유튜브, 인스타그램 등)로 발행할지 모르는 경우가 많다. 수집 즉시 채널을 결정하도록 강요하면 intake 경계가 어색해진다. 이 패턴은 **수집 시점**과 **채널 결정 시점**을 분리해 이 문제를 해결한다.

## 이중 Intake 구조

### Intake 1: 텍스트 지식 → `raw/{type}/`

- 아티클, 영상 트랜스크립트, 팟캐스트 노트, 책 챕터, 대화 백업 등
- 수집 즉시 `raw/{type}/`에 저장 (불변)
- 이후 `/wiki:ingest`로 위키 페이지 생성

```
Web Clipper / 직접 입력
    ↓
raw/articles/ | raw/videos/ | raw/podcasts/ | raw/books/ | raw/journals/
    ↓
/wiki:ingest
```

### Intake 2: 채널 미정 비텍스트 자산 → `assets/intake/`

- 이미지, 첨부파일, 스크린샷 등 채널이 결정되지 않은 자산
- `assets/intake/`에 임시 보관
- 채널 결정 후 해당 채널 폴더로 승격

```
스크린샷 / 이미지 / 첨부파일
    ↓
assets/intake/reference-notes/ | reference-images/ | attachments/
    ↓ (채널 결정 후)
assets/blog/ | assets/youtube/ | assets/instagram/ | assets/webtoon/
```

## `assets/` 전체 구조

```
assets/
├── clipper-templates/     # Obsidian Web Clipper 템플릿 (도구)
├── intake/                # 채널 미정 자산 inbox
│   ├── reference-notes/
│   ├── reference-images/
│   └── attachments/
├── blog/                  # 블로그 발행용 원본 이미지
├── youtube/               # 유튜브 제작 자산
├── instagram/             # 인스타그램 제작 자산
├── webtoon/               # 웹툰 제작 자산
└── shared/                # 채널 공통 자산
```

## 관련 페이지

- [[entities/obsidian-web-clipper]]
- [[projects/repo-structure-refactor]]
- [[sources/2026-04-18-clipper-template-intake]]
- [[sources/2026-04-18-codex-folder-structure-execution]]
