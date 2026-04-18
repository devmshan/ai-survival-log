---
title: "Wiki 카테고리 설계 결정 — syntheses 폐기"
created: "2026-04-18"
updated: "2026-04-18"
type: project
sources: []
tags: [wiki, project, structure, category-design, syntheses, decision]
status: active
published: false
slug: ""
description: ""
---

# Wiki 카테고리 설계 결정 — syntheses 폐기

## 배경

초기 저장소 구조 리팩토링([[projects/repo-structure-refactor]])에서 `wiki/syntheses/`를 신규 카테고리로 도입했다. 비교 분석, 질의 결과, 통합 판단 문서를 담는 카테고리였다.

2026-04-18 기준, 도입 후 단 한 개의 페이지도 생성되지 않은 상태에서 카테고리 전체를 폐기하는 결정을 내렸다.

---

## 폐기 결정 근거

### 1. Publish 구조와 맞지 않는다

현재 publish 파이프라인에서 `published: true`를 갖는 페이지는 실질적으로 `topics/`에 집중된다. `syntheses/`는 비교/판단 성격이라 standalone 블로그 글로 읽힐 수 있는 서사 구조가 약하다. publish 파이프라인과 단절된 카테고리를 유지하는 비용이 명확한 이득보다 크다.

### 2. 한 번도 사용되지 않았다

도입 시점부터 실제 필요가 생겼을 때 채우겠다는 계획이었는데, 그 필요가 한 번도 발생하지 않았다. 비교/판단 성격의 지식은 자연스럽게 `topics/` 안에 섹션으로 흡수됐다.

예시:
- Graphify 재평가 → [[topics/graphify-evaluation]] (topics/)
- 도구 평가 방법론 → [[concepts/tool-evaluation-methodology]] (concepts/)
- wiki markdown vs graph DB → [[topics/wiki-markdown-vs-graph-db]] (topics/)

### 3. topics/가 이미 그 역할을 하고 있다

`topics/`는 "여러 소스/엔티티/개념을 엮는 종합 페이지"로 정의되어 있다. 비교, 통합, 판단이 모두 이 정의 안에 들어온다. `syntheses/`는 `topics/`의 하위집합을 별도 카테고리로 분리하는 형태였는데, 분리의 실익이 없었다.

### 4. Surface 부담이 컸다

`syntheses/` 하나를 위해 관리해야 할 surface:
- `CLAUDE.md` (type enum, 폴더 설명, 워크플로우 3개)
- `scripts/wiki_lib.py` (`_TYPE_ORDER`, `_TYPE_LABELS`)
- `tests/test_wiki_lib.py`
- `.claude/commands/wiki/` 4개 파일
- `.codex/skills/wiki-*/SKILL.md` 4개 파일
- `wiki/projects/repo-structure-refactor.md`

실제 페이지 0개인 카테고리가 14개 파일에 흔적을 남기고 있었다.

---

## 결정

```
syntheses/ 카테고리 폐기.
비교/판단 지식은 topics/에 통합.
추상 패턴은 concepts/에 저장.
```

---

## 확정된 Wiki 카테고리 구조

| 카테고리 | 대상 | Publishable |
|----------|------|-------------|
| `entities/` | 도구, 인물, 제품, 회사 | 드물게 |
| `concepts/` | 추상 개념, 패턴, 정의 | 드물게 |
| `sources/` | raw 자료 요약과 분석 | 아니오 |
| `topics/` | 여러 소스/개념을 엮는 종합 페이지 | **주로 여기** |
| `projects/` | 설계 문서, 실행 계획, 운영 변경 | 아니오 |

**비교/통합/판단 지식의 귀속:**
- 서사로 풀 수 있으면 → `topics/`
- 재사용 가능한 패턴/원칙이면 → `concepts/`
- 특정 프로젝트 결정이면 → `projects/`

---

## 카테고리 추가 판단 기준

새 카테고리 도입을 고려할 때 확인할 항목:

1. **publish 파이프라인과 연결되는가?** 독자에게 standalone으로 읽힐 수 있는가
2. **기존 카테고리로 흡수할 수 없는가?** 실제로 맞지 않는 페이지가 존재하는가
3. **surface 부담 대비 이득이 있는가?** 관리 포인트 증가가 실익과 균형을 이루는가
4. **실제로 페이지가 생성되고 있는가?** "앞으로 필요해질 것 같아서"는 YAGNI 위반

---

## 관련 페이지

- [[projects/repo-structure-refactor]]
- [[concepts/llm-wiki-pattern]]
- [[topics/wiki-markdown-vs-graph-db]]
- [[projects/wiki-rag-expansion-roadmap]]
