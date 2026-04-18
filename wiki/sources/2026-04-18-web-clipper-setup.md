---
title: "Obsidian Web Clipper 설정 마무리와 첫 클리핑 확인 세션"
created: "2026-04-18"
updated: "2026-04-18"
type: source
sources: []
tags: [obsidian-web-clipper, clipper-templates, setup, first-clip, trigger]
status: active
published: false
slug: ""
description: ""
---

# Obsidian Web Clipper 설정 마무리와 첫 클리핑 확인 세션

**원본:** `raw/journals/2026-04-18-web-clipper-setup-and-first-clip-conversation-backup.md`
**날짜:** 2026-04-18
**성격:** Web Clipper 템플릿을 실제 UI에 등록하고, 트리거 문제를 발견·해결하고, 첫 실제 클리핑 파일까지 확인한 실사용 검증 세션

## 핵심 요약

10개 템플릿을 Obsidian Web Clipper UI에 등록하는 과정에서, `10 Generic Source Capture`의 `https://*` 전역 트리거가 모든 URL을 잡아먹는 문제를 발견했다. 해결책으로 fallback 템플릿(`Article Quick Capture`, `Generic Source Capture`, `Journal Insight Capture`)의 트리거를 비워 수동 선택 전용으로 운용하는 원칙을 정립했다. 첫 실제 클리핑 파일은 `Graphify` 아티클로, 템플릿 구조는 유효했으나 vault 저장 경로가 `wiki/raw/articles/`로 들어가는 설정 문제를 발견했다.

## 주요 발견

- **fallback 트리거 문제**: `https://*` 패턴은 수동 선택용 템플릿에서 제거해야 함
- **번호 붙인 이름의 효과**: `01 Article Deep Research` 형식이 UI 정렬 안정성을 높임
- **vault 경로 이슈**: 첫 클리핑이 `wiki/raw/articles/`에 저장됨 → vault 루트 설정 점검 필요
- **수동 선택 원칙**: 트리거 없는 템플릿은 클리퍼 확장 메뉴에서 수동으로 선택

## 템플릿 이름 체계 (최종)

| 번호 | 이름 | 트리거 방식 |
|------|------|-----------|
| 01 | Article Deep Research | 자동 트리거 |
| 02 | Video Transcript Notes | 자동 트리거 |
| 03 | Podcast Episode Notes | 자동 트리거 |
| 04 | Book Chapter Notes | 자동 트리거 |
| 05 | Book Quote Capture | 자동 트리거 |
| 06 | Conversation Backup | 자동 트리거 |
| 07 | Asset Reference Note | 자동 트리거 |
| 08 | Journal Insight Capture | **수동 전용** |
| 09 | Article Quick Capture | **수동 전용** |
| 10 | Generic Source Capture | **수동 전용** |

## 첫 클리핑 파일

- 파일: `2026-04-18T193443+0900-AI 코딩 어시스턴트를 위한 지식 그래프 스킬.md`
- 소스: `https://graphify.net/kr/`
- 확인: 템플릿 구조(Why This Matters, Summary Seed 등) 잘 적용됨

## 관련 페이지

- [[entities/obsidian-web-clipper]]
- [[entities/obsidian]]
- [[sources/2026-04-18-clipper-template-intake]]
- [[sources/2026-04-18-wiki-surface-alignment]]
