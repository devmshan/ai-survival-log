---
title: "Wiki RAG 확장 로드맵"
created: "2026-04-18"
updated: "2026-04-18"
type: project
sources: []
tags: [project, wiki, rag, vector-db, roadmap]
status: draft
published: false
slug: ""
description: ""
---

# Wiki RAG 확장 로드맵

이 프로젝트는 현재 위키 구조 변경 이후에 진행할 RAG/vector DB 확장을 위한 예정 작업이다. 지금 단계에서는 구현하지 않으며, human-first markdown wiki 구조를 유지한 채 추후 별도 작업으로 다룬다.

## 목적

- 현재 `wiki/` 전체를 RAG가 소비할 수 있는 형태로 인덱싱하는 장기 방향 정리
- Obsidian 친화 구조를 해치지 않고 retrieval 품질을 높이는 원칙 수립
- `ai-survival-log-site`와 분리된 upstream 지식 검색 계층 설계

## 현재 합의

- RAG는 `wiki/`를 소비하는 파생 계층이다.
- 위키 본체를 RAG 저장소처럼 재편하지 않는다.
- `indexes/`만 인덱싱하는 방식이 아니라, 전체 md를 타입별 정책으로 다르게 다룬다.
- 생성물 분리(`tags -> _generated`) 여부는 이 프로젝트에서 재검토한다.

## 추후 검토 범위

- 문서 타입별 chunking 전략
- frontmatter 확장 여부
- vector DB 스키마
- retrieval weighting
- `projects/`, `sources/`, `syntheses/`의 우선순위 정책
- Graphify/Obsidian과 충돌 없는 generated artifact 분리

## 선행 조건

- `repo-structure-refactor` 완료
- `raw/wiki/assets/output` 경계 안정화
- `ai-survival-log-site` publish 계약 재검증 완료
- 현재 wiki 문서 규칙이 충분히 안정화됨

## 완료 조건

- RAG 인덱싱 대상과 제외 대상이 명시됨
- human-first wiki 원칙을 유지하는 인덱싱 파이프라인 설계가 문서화됨
- 운영 규칙과 검증 계획이 정리됨

## 관련 페이지

- [[projects/repo-structure-refactor]]
- [[concepts/llm-wiki-pattern]]
- [[topics/wiki-markdown-vs-graph-db]]
