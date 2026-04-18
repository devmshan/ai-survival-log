---
title: "Graphify"
created: "2026-04-18"
updated: "2026-04-18"
type: entity
sources:
  - "[[sources/2026-04-18-graphify-evaluation]]"
tags: [graphify, knowledge-graph, tool, llm, markdown, multi-modal]
status: active
published: false
slug: ""
description: ""
---

# Graphify

마크다운, 코드, PDF, 이미지를 지식 그래프로 변환하는 multi-modal 도구. AI 코딩 어시스턴트(Claude, OpenAI 등)가 프로젝트 문맥을 더 잘 이해할 수 있도록 구조화하는 것이 주 목적.

- **개발자:** Safi Shamsi
- **GitHub:** github.com/safishamsi/graphify
- **PyPI:** `pip install graphifyy` (CLI 명령: `graphify`)
- **공식 사이트:** graphify.net

---

## 기본 사용법

```bash
graphify .           # 현재 디렉토리 전체 처리
graphify ./wiki      # 특정 폴더만 처리
graphify . --update  # 변경된 파일만 증분 갱신
```

> **주의:** `graphify update <path>`는 **코드 파일 전용** 증분 갱신 서브커맨드다.
> 마크다운을 포함한 전체 처리는 `graphify .`이다.

---

## 처리 방식 (Multi-modal)

| 파일 유형 | 확장자 | 처리 엔진 |
|-----------|--------|----------|
| 코드 | `.py .ts .js .go .rs .java .c .cpp` 등 | tree-sitter AST 파싱 (결정론적, LLM 없음) |
| 문서 | `.md .mdx .html .txt .rst` | Claude LLM 기반 개념·관계 추출 |
| PDF | `.pdf` | 인용 채굴 + 개념 추출 |
| 이미지 | `.png .jpg .webp .gif` | Claude 비전 분석 |

---

## 출력

`graphify-out/` 폴더에 생성:

```
graphify-out/
├── graph.html        ← 인터랙티브 지식 그래프 시각화
├── GRAPH_REPORT.md   ← 허브 노드, 커뮤니티, 고아 페이지 구조 리포트
├── graph.json        ← 그래프 데이터 (지속 가능한 쿼리)
├── obsidian/         ← Obsidian vault 내보내기
├── wiki/             ← 에이전트 탐색용 아티클 (--wiki 플래그)
└── cache/            ← SHA256 기반 변경 감지 캐시
```

---

## 추가 플래그

| 플래그 | 기능 |
|--------|------|
| `--mcp` | MCP 서버 실행 → Claude Code에서 그래프 쿼리 인터페이스 사용 가능 |
| `--svg` | SVG 형식 그래프 내보내기 |
| `--graphml` | GraphML 형식 내보내기 (Gephi, yEd 호환) |
| `--neo4j` | Cypher 구문 내보내기 (Neo4j 연동) |

---

## 이 위키와의 관계

`graphify ./wiki`를 실행하면 `wiki/` 구조를 변경하지 않고 파생 그래프를 생성할 수 있다. 로드맵의 "wiki를 소비하는 파생 계층" 원칙과 부합한다.

**현재 채택 여부:** 미채택
**이유:** 84페이지 규모에서 `wiki lint` + `index.md` + Claude 직접 읽기로 충분. 그래프 도구가 해결해야 할 병목 없음.
**재검토 조건:** 위키 200+ 페이지, 또는 MCP 쿼리 인터페이스가 실질적으로 필요해질 때.

→ [[topics/graphify-evaluation]]에서 전체 평가 과정과 결정 근거 확인.

---

## 관련 페이지

- [[topics/graphify-evaluation]]
- [[projects/wiki-rag-expansion-roadmap]]
- [[topics/wiki-markdown-vs-graph-db]]
- [[concepts/llm-wiki-pattern]]
