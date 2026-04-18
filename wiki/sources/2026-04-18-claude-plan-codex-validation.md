---
title: "Claude 계획서 검증과 구조 변경 계획 재설계 세션"
created: "2026-04-18"
updated: "2026-04-18"
type: source
sources: []
tags: [repo-structure, claude-codex, validation, raw-layer, assets, wiki]
status: active
published: false
slug: ""
description: ""
---

# Claude 계획서 검증과 구조 변경 계획 재설계 세션

**원본:** `raw/journals/2026-04-18-claude-plan-codex-validation-conversation-backup.md`
**날짜:** 2026-04-18
**성격:** Claude로 작성한 구조 변경 계획서를 Codex로 검증하고, 문제를 발견 및 해결하여 최종 계획서로 재완성한 대화 세션

## 핵심 요약

Claude가 초안 작성한 `wiki/projects/repo-structure-refactor.md`를 Codex가 실제 저장소 상태, 운영 계약 문서, 테스트까지 맞춰 검증했다. 초기 계획의 문제(`docs/images → raw/assets` 충돌, lint 실패)를 발견하고, 논의를 거쳐 `raw/wiki/assets/output` 4계층으로 최종 계획을 재완성했다. Future RAG/vector DB 확장은 별도 예정 프로젝트로 분리하는 원칙도 이 세션에서 합의됐다.

## 주요 포인트

- **검증 방식**: 문서만 보는 것이 아니라 실제 디렉토리 상태 + 테스트(`pytest`) + 계약 문서까지 교차 확인
- **발견된 문제**: `docs/images → raw/assets` 전환이 publish 계약과 충돌 / 계획 문서 자체가 lint를 깨고 있었음
- **해결 방향**: `assets/`를 최상위 채널별 자산 계층으로 분리 (`assets/blog/`, `assets/youtube/`, `assets/instagram/`, `assets/webtoon/`)
- **output/blog 도입**: `raw → wiki → output/blog → ai-survival-log-site/content/posts` 흐름 확정
- **human-first 원칙 합의**: wiki 본체를 RAG 구조로 선제적으로 바꾸지 않기로 결정, RAG는 파생 계층
- **downstream 계약 유지**: `ai-survival-log-site/content/posts/`와의 계약은 변경 없이 유지

## 블로그 소재 포인트

- Claude가 만든 계획서를 Codex가 어떻게 검증했는가
- 문서 검토가 아니라 "실제 저장소 상태 + 테스트 + 계약 문서"까지 확인하는 검증 방식
- 구조 변경에서 가장 위험한 지점이 왜 이미지/출판 계약이었는가
- human-first wiki와 future RAG를 어떻게 분리해서 생각했는가

## 관련 페이지

- [[projects/repo-structure-refactor]]
- [[projects/wiki-rag-expansion-roadmap]]
- [[concepts/claude-codex-collaboration]]
- [[sources/2026-04-18-codex-folder-structure-execution]]
