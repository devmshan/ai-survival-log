---
title: "Obsidian Web Clipper"
created: "2026-04-18"
updated: "2026-04-18"
type: entity
sources: []
tags: [obsidian, web-clipper, knowledge-capture, raw-layer, templates]
status: active
published: false
slug: ""
description: ""
---

# Obsidian Web Clipper

Obsidian의 공식 브라우저 확장 프로그램. 웹 페이지를 마크다운으로 변환해 Vault에 직접 저장한다. 템플릿을 통해 저장 형식, 메타데이터, 저장 경로를 커스터마이징할 수 있다.

## 주요 기능

- **웹 페이지 → 마크다운 변환**: 브라우저에서 한 번에 클리핑
- **템플릿 시스템**: JSON 형식의 템플릿으로 frontmatter, 본문 구조, 저장 경로 지정
- **자동 트리거**: URL 패턴 기반으로 템플릿 자동 선택
- **수동 선택**: 트리거 없는 템플릿은 확장 메뉴에서 수동 선택 가능

## ai-survival-log 설정

`ai-survival-log`에서는 `assets/clipper-templates/`에 10종 템플릿을 보관한다.

### 템플릿 체계

| 번호 | 이름 | 저장 위치 | 트리거 |
|------|------|---------|-------|
| 01 | Article Deep Research | `raw/articles/` | 자동 |
| 02 | Video Transcript Notes | `raw/videos/` | 자동 |
| 03 | Podcast Episode Notes | `raw/podcasts/` | 자동 |
| 04 | Book Chapter Notes | `raw/books/` | 자동 |
| 05 | Book Quote Capture | `raw/books/` | 자동 |
| 06 | Conversation Backup | `raw/journals/` | 자동 |
| 07 | Asset Reference Note | `assets/intake/reference-notes/` | 자동 |
| 08 | Journal Insight Capture | (수동) | **수동 전용** |
| 09 | Article Quick Capture | `raw/articles/` | **수동 전용** |
| 10 | Generic Source Capture | (수동 분류) | **수동 전용** |

### 운용 원칙

- 텍스트 소스는 가능한 한 `raw/{type}/`으로 바로 저장
- `https://*` 같은 전역 트리거는 fallback 템플릿에서 제거 — 수동 선택용으로 운용
- 번호 붙인 이름 체계(`01 Article Deep Research`)가 UI 정렬 안정성을 높임
- 채널 미정 비텍스트 자산은 `assets/intake/`로 먼저 받음

### 클리핑 후 흐름

```
Web Clipper 클리핑
    ↓
raw/{type}/ 또는 assets/intake/
    ↓
/wiki:ingest (Claude command) 또는 wiki-ingest (Codex skill)
    ↓
wiki/ 페이지 생성/갱신
```

## 관련 페이지

- [[entities/obsidian]]
- [[concepts/assets-intake-pattern]]
- [[sources/2026-04-18-clipper-template-intake]]
- [[sources/2026-04-18-web-clipper-setup]]
