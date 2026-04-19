---
title: "Obsidian"
created: "2026-04-12"
updated: "2026-04-18"
type: entity
sources: []
tags: [obsidian, note-taking, knowledge-management, tool]
status: active
published: false
slug: ""
description: ""
---

# Obsidian

마크다운 기반의 로컬 우선 지식 관리 도구. 파일 간 `\[\[wikilink\]\]`로 연결되는 그래프 구조의 개인 지식베이스(PKM)를 구축할 수 있다.

## 핵심 특징

- **로컬 파일 기반**: 모든 노트가 로컬 `.md` 파일로 저장됨 — 데이터 소유권 보장
- **Wikilink**: `\[\[페이지명\]\]` 문법으로 노트 간 양방향 연결
- **그래프 뷰**: 노트 간 연결을 시각화하는 지식 그래프
- **플러그인 생태계**: 커뮤니티 플러그인으로 기능 확장 가능
- **Vault**: 로컬 폴더를 Vault로 지정해 워크스페이스로 사용

## 설정 팁

### 다크모드 켜기

세 가지 방법:

1. **설정 메뉴**: `Cmd + ,` → **Appearance** → **Base theme** → **Dark**
2. **하단 아이콘**: 좌측 하단 ⚙️ → **Appearance** → **Base theme: Dark**
3. **명령 팔레트**: `Cmd + P` → "dark" 검색 → **Toggle dark mode**

### Wikilink 경로 설정

경로 포함 wikilink(`[[entities/claude-code]]`)를 인식하려면:

- Settings → Files & links → **New link format** → **Relative path to file**

## 이 프로젝트에서의 사용

`ai-survival-log` 위키를 Obsidian Vault로 열어 지식 그래프를 시각화할 수 있다.

**추천 플러그인:**
- **Dataview**: 위키 페이지를 쿼리/필터링
- **Tag Wrangler**: 태그 일괄 관리
- **Graph Analysis**: 노트 간 연결 분석

## Web Clipper

Obsidian 공식 브라우저 확장 프로그램. 웹 페이지를 마크다운으로 클리핑해 Vault에 직접 저장한다. → [[entities/obsidian-web-clipper]] 참조

## 관련 페이지

- [[concepts/llm-wiki-pattern]]
- [[entities/obsidian-web-clipper]]
- [[projects/blog-ai-study-site]]
- [[sources/2026-04-19-cmds-system-files]] — Obsidian 기반 PKM 설계 사례 (CMDS v4.2)
