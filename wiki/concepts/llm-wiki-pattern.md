---
title: "LLM Wiki 패턴"
created: "2026-04-12"
updated: "2026-04-12"
type: concept
sources: []
tags: [wiki, knowledge-management, llm, karpathy]
status: active
published: false
slug: ""
description: ""
---

# LLM Wiki 패턴

Andrej Karpathy가 제시한 지식 관리 패턴. RAG의 "쿼리 타임" 재발견 대신, "인제스트 타임"에 지식을 한 번 컴파일하여 지속적으로 유지하는 위키를 구축한다.

## 핵심 철학

- 위키는 **지속적이고 누적되는 결과물** — 한 번 컴파일되면 계속 현재 상태로 유지
- 인간은 **소스 큐레이션**과 **질문 방향**을 담당
- LLM은 **요약, 크로스레퍼런싱, 파일링, 북키핑**을 수행
- "The wiki is just a git repo of markdown files"

## RAG vs LLM Wiki

| 방식 | 처리 시점 | 토큰 사용 | 유지보수 |
|------|----------|----------|----------|
| RAG | 쿼리 타임마다 | 매번 소모 | 벡터 DB 필요 |
| LLM Wiki | 인제스트 타임 한 번 | 95% 절감 | 마크다운 + git |

## 3 Layer 아키텍처

1. **Raw Sources** (`sources/`) — 불변 원본 (PDF, 아티클, 노트)
2. **The Wiki** (`wiki/`) — LLM이 생성/유지하는 마크다운 페이지
3. **The Schema** (`CLAUDE.md`) — 위키 구조와 규칙 정의

## 핵심 커맨드

| 커맨드 | 역할 |
|--------|------|
| `/ingest` | 소스 분석 → 위키 페이지 생성/갱신 (10-15개 페이지 영향) |
| `/query` | 위키 검색 + 출처 인용 답변 |
| `/file-answer` | 답변을 위키 페이지로 저장 (지식 순환) |
| `/lint` | 고아 페이지, 깨진 링크, 모순 탐지 |

## 스케일 고려사항

- **50-200개 페이지:** 가장 효율적
- **200개 초과:** "false coherence" 위험 — 오류가 일관되게 번식
- 벡터 DB 대신 `index.md`가 human-readable 검색 인덱스 역할

## 출처

- Andrej Karpathy Gist: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- aboutcorelab 해설: https://aboutcorelab.com/llm-wiki-in-obsidian-for-2nd-brain/

## 관련 페이지

- [[entities/claude-code]] — 이 위키를 운영하는 도구
- [[entities/obsidian]] — 위키 Vault 시각화 도구
- [[topics/ai-era-survival]] — 위키를 활용한 지식 축적 전략
- [[concepts/context-graph]] — 이 위키는 일종의 Context Graph (지식 + 맥락 + 출처)
- [[topics/wiki-markdown-vs-graph-db]] — 정형화/자동화 vs 마크다운 설계 판단
