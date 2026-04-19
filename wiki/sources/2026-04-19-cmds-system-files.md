---
title: "CMDS System Files (johnfkoo951/cmds-system-files)"
created: "2026-04-19"
updated: "2026-04-19"
type: source
sources: []
tags: [pkm, obsidian, claude-code, ai-agent, knowledge-management, system-design]
status: active
published: false
slug: ""
description: "Source analysis of CMDS System Files by Yohan Koo (CMDSPACE). Documents architecture patterns applicable to ai-survival-log wiki system, including Essential section, STATIC/DYNAMIC annotation, and LLM-readable description fields."
---

# CMDS System Files (johnfkoo951/cmds-system-files)

> 원본: https://github.com/johnfkoo951/cmds-system-files
> 버전: v4.2 (2026-04-15)
> 작성자: 구요한 (Yohan Koo / CMDSPACE)
> 캡처: 2026-04-19

## 시스템 개요

Obsidian 기반 PKM 시스템. 10,000+ 노트 규모의 `CMDSPACE` 볼트를 운영하기 위한 AI 에이전트용 시스템 파일 세트.
Claude Code, Gemini CLI, Codex 등 다양한 AI 에이전트가 동일한 볼트에서 일관되게 동작하도록 설계되었다.

### 핵심 구성

| 파일 | 대상 | 역할 | precedence |
|------|------|------|-----------|
| CLAUDE.md | Claude Code | 기술 구현 (HOW) | 1 |
| AGENTS.md | Gemini, Codex, Cursor | 이식 가능한 기술 규칙 | 2 |
| CMDS.md | 모든 LLM | 철학·맥락 (WHY/WHAT) | 3 |
| CMDS Guide | User + AI | 운영 표준 | 4 |
| CMDS Head Quarter | User | 탐색 허브 | 5 |

### CMDS 프로세스

```
Connect → Merge → Develop → Share
```

8개 슬래시 커맨드가 이 4단계에 정렬되어 있음: `/connect`, `/merge`, `/develop`, `/share`, `/inbox`, `/lint`, `/query`, `/status`

---

## 우리 위키에 적용 가능한 패턴

### 1. Essential (Post-Compact) 섹션 ★★★

**무엇인가:** CLAUDE.md / AGENTS.md 안에 `## Essential (Post-Compact)` 헤딩 + blockquote 형식으로 핵심 규칙을 별도 명시하는 패턴.

**실제 형식 (AGENTS.md에서 발췌):**
```markdown
## Essential (Post-Compact)

> 컨텍스트 압축 후에도 반드시 기억해야 할 핵심 규칙:
> 1. **YAML frontmatter: 2 SPACES** / **Markdown body: TAB**
> 2. **Wikilinks in YAML: 반드시 큰따옴표** `"[wikilink]"` 형태
> 3. **코드 출력 경로**: `00. Inbox/03. AI Agent/{환경 하위폴더}/`
> 4. **필수 프로퍼티 7개**: type, aliases, description, author, date created, date modified, tags
> 5. **날짜 포맷**: ISO 8601 (YYYY-MM-DD)
```

**왜 유용한가:** compaction이 발생하면 CLAUDE.md 전체가 요약되어 세부 규칙이 희석된다. Essential 섹션은 "컴팩션 후에도 살아남아야 할 규칙"을 한 곳에 모아 AI가 우선 보존하도록 신호를 준다.

**우리 CLAUDE.md에 넣을 내용 후보:**
- raw → wiki → output → site 파이프라인
- frontmatter 필수 필드 (title, created, updated, type, status, published, slug, description)
- published: true일 때 slug/description 필수
- 슬래시 커맨드 목록 (/wiki:ingest, /wiki:query, /wiki:publish 등)
- wikilink 형식 `\[\[entities/...]\]`

**적용 판단:** 즉시 도입 가치가 가장 높다. 현재 `CLAUDE.md`가 길고 규칙 밀도가 높아 핵심 규칙만 상단에 다시 선언해 두는 편이 안전하다.

---

### 2. STATIC / DYNAMIC 섹션 주석 ★★

**무엇인가:** CLAUDE.md 본문을 HTML 주석으로 두 영역으로 구분하는 패턴.

**실제 형식 (CLAUDE.md에서 발췌):**
```markdown
<!-- STATIC: 아래 내용은 거의 변경되지 않는 규칙입니다. AI는 높은 신뢰도로 캐시할 수 있습니다. -->

## ⚠️ CRITICAL RULES — READ FIRST
...

<!-- DYNAMIC: 아래 내용은 주기적으로 갱신됩니다. 검증이 필요할 수 있습니다. -->

## Critical Workflow Rules
...
```

**STATIC vs DYNAMIC 구분 기준:**

| 섹션 | 분류 |
|------|------|
| 파일명 컨벤션, frontmatter 스펙 | STATIC |
| 슬래시 커맨드 워크플로우 규칙 | STATIC |
| 현재 페이지 수 (index.md) | DYNAMIC |
| 최근 로그, 진행 중인 작업 | DYNAMIC |
| 위키 카테고리 구조 | STATIC |

**왜 유용한가:** AI가 어느 부분을 신뢰하고 캐시할 수 있는지, 어느 부분을 재검증해야 하는지 명시적으로 알 수 있다.

**적용 판단:** 지금 당장 도입할 정도로 우선순위가 높지는 않다. 문서가 더 커지거나 동적 운영 상태가 많이 섞일 때 재검토하는 편이 낫다.

---

### 3. description 필드 LLM 힌트 강화 ★★

**무엇인가:** frontmatter의 `description` 필드를 **영어**로, **AI가 연관성을 판단하기 위한 힌트**로 작성하는 규칙.

**CMDS frontmatter-standard.md의 규칙:**
> description: 1-2 sentences describing what the note contains and when an LLM should reference it.
> Write it as a skill/tool description — specific, action-oriented, no fluff.

**예시 비교:**
```yaml
# ❌ 현재 방식 (막연, 한국어)
description: "Claude Code에 대한 정리"

# ✅ CMDS 방식 (영어, LLM 힌트)
description: "Entity page for Claude Code CLI. Reference when querying about agentic workflows, Claude features, or ECC plugin usage."
```

**적용 범위:** 새 페이지 작성 및 `/wiki:publish` 전 검토 시 적용. 기존 페이지는 일괄 수정 불필요.

**적용 판단:** 부분 채택이 적절하다. 다만 이 저장소는 한국어 authoring과 downstream SEO 흐름이 있으므로 "영문 설명 강제"보다는 "무엇이 들어 있고 언제 참고할지 드러나는 구체적 description" 규칙으로 흡수하는 편이 맞다.

---

### 4. 적용하지 않는 패턴

| 패턴 | 이유 |
|------|------|
| `precedence` 필드 | CLAUDE.md + AGENTS.md 2개 파일만 존재, 충돌 가능성 낮음 |
| `token-estimate` 필드 | 현재 컨텍스트 관리 문제 없음 |
| `memory-type`, `required-for` | CMDS 생태계 전용, 과잉 |
| Connect→Merge→Develop→Share 프로세스 | 우리 raw→wiki→output→site 파이프라인이 이미 확립 |
| camelCase frontmatter 신규 필드 10개 | CMDS 커맨드 전용 메타데이터, 불필요 |

---

## 최종 판단

- 즉시 적용: `Essential (Post-Compact)` 섹션
- 제한적으로 적용: `description`을 더 구체적인 참조 힌트로 쓰는 규칙
- 보류: `STATIC/DYNAMIC` 주석, `precedence`, `token-estimate`, CMDS 전용 frontmatter

## 관련 페이지

- [[entities/obsidian]]
- [[projects/repo-structure-refactor]]
