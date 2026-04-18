---
title: "Graphify 평가와 RAG 방향 재정리 세션"
created: "2026-04-18"
updated: "2026-04-18"
type: source
sources: []
tags: [graphify, wiki, knowledge-management, rag, graph-database, tool-evaluation]
status: active
published: false
slug: ""
description: ""
---

# Graphify 평가와 RAG 방향 재정리 세션

**원본:** `raw/journals/2026-04-18-graphify-evaluation-and-rag-direction-conversation-backup.md`
**날짜:** 2026-04-18
**성격:** Graphify를 현재 프로젝트 구조에 도입할 가치가 있는지 점검한 세션. 초기 평가에서 잘못된 서브커맨드를 테스트해 틀린 결론을 냈고, 이후 공식 문서를 통해 재평가하여 더 정확한 채택 판단을 내렸다.

## 핵심 요약

`graphifyy 0.4.23`을 설치하고 CLI를 직접 테스트했다. 초기에 `graphify update wiki`(코드 파일 증분 갱신 전용)와 `graphify wiki`(존재하지 않는 서브커맨드)만 테스트하고 "마크다운 미지원"이라는 틀린 결론을 냈다. 이후 공식 문서 재확인으로 올바른 명령이 `graphify .`임을 파악했다. Graphify는 multi-modal 도구로, 마크다운 파일을 Claude LLM 기반으로 처리한다. 재평가 결과 "못 해서가 아니라 지금 필요 없어서" 채택하지 않기로 최종 결정했다.

## CLI 테스트 결과 (1차 — 잘못된 명령)

| 명령 | 결과 | 이유 |
|------|------|------|
| `graphify update wiki` | `No code files found`, `Nothing to update` | `update`는 코드 파일 증분 갱신 전용 서브커맨드 |
| `graphify wiki` | `unknown command 'wiki'` | `wiki`는 존재하지 않는 서브커맨드 |

**올바른 명령:** `graphify .` 또는 `graphify ./wiki`

## Graphify 실제 기능 (재확인)

| 파일 유형 | 처리 방식 |
|-----------|----------|
| 코드 (.py .js .ts 등) | tree-sitter AST 파싱 (LLM 없음) |
| 문서 (.md .mdx .html .txt) | Claude LLM 기반 개념·관계 추출 |
| PDF | 인용 채굴 + 개념 추출 |
| 이미지 | Claude 비전 분석 |

출력: `graphify-out/graph.html`, `GRAPH_REPORT.md`, `graph.json`, `obsidian/`
추가 플래그: `--mcp`(MCP 서버), `--neo4j`, `--graphml`, `--svg`

## 재평가 장단점

**장점 (수정):**
- `graphify ./wiki` 한 줄로 파생 그래프 생성, wiki 구조 변경 불필요
- `GRAPH_REPORT.md`로 허브 노드, 고아 페이지, 커뮤니티 구조 파악
- `--mcp`로 Claude Code에 그래프 쿼리 인터페이스 추가 가능
- Obsidian vault 내보내기로 기존 구조와 호환

**단점 (수정):**
- Claude API 호출 비용 (LLM 기반 마크다운 추출)
- 84페이지 규모에서 `wiki lint` + `index.md`로 충분
- 추가 의존성, 빌드 스텝, 유지보수 대상 증가
- 현재 규모에서 ROI 불분명

## 핵심 결정

- Graphify는 마크다운을 처리할 수 있다 — 기존 평가의 기술적 주장은 틀렸다
- 그러나 현재 84페이지 규모에서 그래프 도구가 당장 필요하지 않다
- `wiki/` 구조를 Graphify 친화적으로 재편하지 않는다
- 200+ 페이지 또는 MCP 통합이 실질적으로 필요해질 때 파생 레이어로 재검토
- `graphifyy` 패키지 제거 완료

## 반영 항목

- `wiki/topics/graphify-evaluation.md` — 전면 재작성, 제목·결론 변경
- `wiki/projects/wiki-rag-expansion-roadmap.md` — Graphify 판단 섹션 수정

## 관련 페이지

- [[topics/graphify-evaluation]]
- [[topics/wiki-markdown-vs-graph-db]]
- [[projects/wiki-rag-expansion-roadmap]]
- [[concepts/llm-wiki-pattern]]
- [[concepts/context-graph]]
