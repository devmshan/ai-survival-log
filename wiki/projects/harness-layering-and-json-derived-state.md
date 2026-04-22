---
title: "Harness 세분화와 JSON 파생 상태 설계"
created: "2026-04-22"
updated: "2026-04-22"
type: project
sources: []
tags: [project, harness, repository, structure, refactor, json, state-management, codex, claude]
status: active
published: false
slug: ""
description: "ai-survival-log와 ai-survival-log-site의 Harness를 세분화하고, Markdown source-of-truth를 유지하면서 JSON 파생 상태를 어디에 둘지 정리한 설계 초안."
---

# Harness 세분화와 JSON 파생 상태 설계

`ai-survival-log`와 `ai-survival-log-site`는 둘 다 AI agent가 읽는 로컬 surface를 갖고 있지만, 현재는 `AGENTS.md`가 너무 많은 역할을 떠안고 있다. 동시에 상태 관리도 Markdown 중심이라 사람에게는 읽기 좋지만, 자동화가 소비할 파생 상태는 별도로 두지 못하고 있다.

이 설계의 목표는 두 가지다.

1. Harness 문서를 얇고 명확한 계층으로 분리한다.
2. Markdown source-of-truth는 유지하되, 자동화가 필요한 상태는 JSON 파생물로 분기한다.

## 판단 요약

- `AGENTS.md`는 계속 남긴다. 다만 역할, 핵심 경계, 작업 루프, 절대 규칙만 남기는 얇은 문서로 줄인다.
- 루트 문서는 저장소당 최대 4개까지 허용한다: `README.md`, `AGENTS.md`, `CLAUDE.md`, `ARCHITECTURE.md`.
- 세부 규칙은 루트가 아니라 `docs/operating/`과 `docs/adr/`로 분리한다.
- `CLAUDE.md`와 `.codex/AGENTS.md`는 공통 규칙의 원문 저장소가 아니라, 공통 문서에 대한 포인터와 각 agent 전용 메모만 둔다.
- `PRD.md`는 상시 고정 문서로 두지 않는다. 기능 단위 작업에서만 만든다.
- JSON은 source-of-truth가 아니라 재생성 가능한 파생 상태로만 도입한다.
- JSON 파생 상태 경로는 두 저장소 모두 `output/state/`를 기본값으로 통일한다.
- JSON 파생물은 전부 git 추적하지 않고, review 가치가 높고 비민감한 안정적 요약만 일부 추적한다.
- 상태 출력 책임은 기본적으로 `scripts/wiki`에 섞지 않고 별도 `scripts/state` 계열로 분리한다.
- `ai-survival-log`와 `ai-survival-log-site`는 같은 문서 세트를 강제하지 않는다. 저장소 역할에 따라 다르게 가져간다.

## 배경 문제

### 현재 `AGENTS.md`의 과부하

- 저장소 역할 설명
- 작업 루프
- publish/content 계약
- agent surface 정합성 요구
- engineering guardrails

이 정보가 한 파일에 모이면 compact 이후 핵심 규칙은 남기기 좋지만, 세부 운영 규칙은 길어질수록 찾기 어렵다.

### 상태 관리의 혼합

현재 상태는 사람 친화적 Markdown과 자동화용 결과물이 명확히 분리되어 있지 않다.

- 사람/설명/운영 기록: `wiki/index.md`, `wiki/log.md`, 각종 wiki page
- 자동화/검증 결과: lint 결과, publish 결과, contract 검사 결과, changed-scope 요약

앞의 집합은 Markdown으로 유지해야 하지만, 뒤의 집합은 JSON이 더 적합하다.

## 설계 원칙

- `wiki/`는 계속 source of truth다.
- `raw/`는 계속 불변 원본 계층이다.
- JSON은 파생 상태여야 하며, Markdown 규칙을 대체하지 않는다.
- Harness 문서는 "핵심 경계", "정적 설계", "운영 절차", "설계 결정"을 분리한다.
- 두 저장소는 cross-repo contract는 맞추되, 역할이 다른 부분은 의도적으로 다르게 유지한다.
- 문서 수를 늘리더라도 중복 복사는 피한다.

## 목표 Harness 구조

### `ai-survival-log`

루트 문서 4개:

- `README.md`
- `AGENTS.md`
- `CLAUDE.md`
- `ARCHITECTURE.md`
  - `raw -> wiki -> output/blog -> ai-survival-log-site/content/posts`
  - source-of-truth vs derived artifact 경계
  - assets/publish/downstream image flow

세부 문서:

- `docs/operating/operations.md`
  - ingest/sync/lint/publish 흐름
  - wiki surface consistency 규칙
  - 검증 루프와 self-review 기준
- `docs/adr/`
  - 장기 결정 기록
  - 예: Markdown source-of-truth 유지, JSON 파생 상태만 허용, harness 분리 원칙

상시 루트 문서로 만들지 않는 것:

- `PRD.md`
- `UI_GUIDE.md`

Claude/Codex 적용 방식:

- `AGENTS.md`는 공통 상위 규칙의 원문
- `CLAUDE.md`는 `@AGENTS.md` + Claude 전용 메커니즘
- `.codex/AGENTS.md`는 compact-safe 규칙 + 세부 문서 포인터
- 세부 규칙 원문은 `ARCHITECTURE.md`, `docs/operating/operations.md`, `docs/adr/`에 둔다

### `ai-survival-log-site`

루트 문서 4개:

- `README.md`
- `AGENTS.md`
- `CLAUDE.md`
- `ARCHITECTURE.md`
  - `wiki -> publish -> site/content/posts`
  - runtime/content contract/series/SEO 흐름
  - upstream와 downstream의 경계

세부 문서:

- `docs/operating/ui-guide.md`
  - typography, layout tone, MDX presentation, image rules, reusable component guidance
- `docs/operating/content-contract.md`
  - frontmatter, slug/date, series, manual post compatibility
- `docs/operating/seo-operations.md`
  - SEO operations와 runtime 연결
- `docs/adr/`
  - series rule, slug/date contract, manual-write vs published-output 같은 장기 결정

상시 루트 문서로 만들지 않는 것:

- `PRD.md`
- `OPERATIONS.md`

Claude/Codex 적용 방식:

- `AGENTS.md`는 공통 상위 규칙의 원문
- `CLAUDE.md`는 `@AGENTS.md` + Claude 전용 메모
- `.codex/AGENTS.md`는 compact-safe 요약 + 세부 문서 포인터
- 운영/표현 규칙 원문은 `ARCHITECTURE.md`, `docs/operating/*`, `docs/adr/`에 둔다

## 문서 역할 분리 표

| 문서 | 역할 | 성격 |
|------|------|------|
| `AGENTS.md` | 핵심 경계와 최상위 실행 규칙 | compact-safe, 짧음 |
| `CLAUDE.md` | `AGENTS.md` 상속 + Claude 전용 메커니즘 | agent-specific |
| `.codex/AGENTS.md` | compact-safe 요약 + Codex 전용 메모 | agent-specific |
| `ARCHITECTURE.md` | 구조와 데이터/계약 흐름 | 정적 설계 |
| `docs/operating/operations.md` | 사람이 따라야 할 운영 절차 | 실행 절차 |
| `docs/operating/ui-guide.md` | 시각/컴포넌트/콘텐츠 표현 규칙 | presentation 규칙 |
| `docs/adr/*.md` | 장기 결정과 tradeoff 기록 | 불변에 가까운 판단 |
| `docs/plans/*` 또는 project wiki page | 작업 단위 실행 계획 | 임시/변동 가능 |

## 링크/참조 통일 원칙

- 공통 규칙의 원문은 한 곳에만 둔다.
- `AGENTS.md`는 세부 내용을 반복하지 않고 `ARCHITECTURE.md`, `docs/operating/*`, `docs/adr/*`로 링크한다.
- `CLAUDE.md`는 첫 줄에 `@AGENTS.md`를 두고, 이후에는 Claude 전용 훅·권한·작업 메모만 적는다.
- `.codex/AGENTS.md`는 compact-safe 핵심 규칙을 유지하되, 세부 규칙은 공통 문서로 링크한다.
- 같은 규칙을 `AGENTS.md`, `CLAUDE.md`, `.codex/AGENTS.md`에 풀텍스트로 중복 복사하지 않는다.

## JSON 파생 상태 설계

### 왜 별도 JSON이 필요한가

다음 정보는 Markdown보다 JSON이 더 잘 맞는다.

- lint/contract/publish 결과
- changed-scope 요약
- publish 대상 manifest
- frontmatter/slug/series 메타데이터의 기계 친화 뷰
- agent가 빠르게 읽을 수 있는 현재 상태 snapshot

### 왜 source-of-truth로 쓰면 안 되는가

- 사람이 바로 읽고 수정하기 어렵다.
- Obsidian-friendly 원칙에 어긋난다.
- wiki graph와 설명 문서가 또 다른 상태 계층과 분리돼 drift가 발생한다.
- JSON을 먼저 고치고 Markdown을 나중에 맞추는 역전이 발생하기 쉽다.

### 권장 배치

#### `ai-survival-log`

트래킹 가능한 파생 상태:

- `output/state/wiki-index.json`
  - `wiki/index.md`의 기계 친화 스냅샷
- `output/state/wiki-lint-summary.json`
  - lint 결과 요약
- `output/state/publish-manifest.json`
  - publishable 페이지, slug, output path, image dependency
- `output/state/agent-surface-summary.json`
  - `README.md`, `AGENTS.md`, `CLAUDE.md`, `.codex/AGENTS.md`의 핵심 경계 체크 결과

선택적 비추적 캐시:

- `.cache/wiki/*.json`
  - 실행 속도를 위한 임시 캐시

#### `ai-survival-log-site`

트래킹 가능한 파생 상태:

- `output/state/content-contract-summary.json`
  - 현재 posts 집합이 contract를 만족하는지 요약
- `output/state/series-manifest.json`
  - seriesSlug, order, date 기반 정렬 정보
- `output/state/content-inventory.json`
  - post slug/date/tags/image/series metadata 요약

선택적 비추적 캐시:

- `.cache/site/*.json`
  - 로컬 실행용 계산 캐시

### 파생 상태 규칙

- JSON은 항상 스크립트가 생성한다.
- 사람이 직접 수정하는 문서로 취급하지 않는다.
- JSON이 없더라도 source-of-truth에서 재생성 가능해야 한다.
- JSON 내용이 Markdown과 충돌하면 Markdown을 우선한다.
- publish artifact와 혼동되지 않도록 `state` 또는 `summary` 이름을 명확히 쓴다.
- 사람용 문서인 `docs/` 아래에 JSON state를 두지 않는다.

### Git 추적 정책

git 추적 추천:

- `*-manifest.json`
- `*-inventory.json`
- `*-summary.json`
  - 단, 입력/출력 계약과 리뷰 가치가 있고 민감 정보가 없는 경우만

git 비추적 추천:

- 로컬 캐시
- 환경 의존 경로가 들어간 결과
- stack trace, raw error payload, request header, secret 유추 정보
- 변동이 심하고 리뷰 가치가 낮은 런타임 상태

보안 기준:

- JSON에는 secret, token, API key, env 값, 절대 로컬 경로, 개인 데이터, raw request metadata를 넣지 않는다.
- JSON에는 slug, date, tags, series metadata, contract pass/fail, artifact path 같은 비민감 구조 정보만 넣는다.

## ADR 제안

### `ai-survival-log`

- `docs/adr/0001-markdown-source-of-truth.md`
- `docs/adr/0002-json-derived-state-only.md`
- `docs/adr/0003-harness-layering-for-upstream-repo.md`

### `ai-survival-log-site`

- `docs/adr/0001-site-consumer-contract-boundary.md`
- `docs/adr/0002-harness-layering-for-site-repo.md`
- `docs/adr/0003-manual-posts-must-remain-contract-compatible.md`

## 상태 출력 스크립트 방침

기본 추천은 `scripts/wiki`에 상태 출력을 직접 섞지 않고 별도 스크립트로 분리하는 것이다.

이유:

- `scripts/wiki`는 source-of-truth 관리 책임이 강하다.
- state export는 derived artifact 생성 책임이다.
- 두 책임을 섞으면 실패 원인과 유지보수 경계가 흐려진다.
- `ai-survival-log-site`에서도 같은 패턴으로 맞추기 어렵다.

권장 구조:

- `scripts/wiki`
  - `sync`
  - `lint`
  - `publish`
- `scripts/state`
  - `export --target wiki`
  - `export --target site`

절충안:

- `scripts/wiki sync --emit-state`처럼 옵션을 둘 수는 있다.
- 하지만 내부 구현은 별도 state export 로직을 호출하게 해서 책임은 분리한다.

## 구현 전 합의 포인트

1. 루트 문서를 몇 개까지 허용할지
2. `output/state/`를 두 저장소 공통 파생 상태 경로로 확정할지
3. JSON 파생물을 git 추적 대상으로 둘지, 일부만 추적할지
4. `scripts/state` 계열을 별도 엔트리포인트로 둘지
5. `AGENTS.md`와 새 문서 사이의 링크/참조 방식을 어떻게 통일할지

## 세부 계획서

### Phase 0. 브랜치와 범위 고정

- `ai-survival-log`: `codex-harness-layering-json-derived-state`
- `ai-survival-log-site`: 동일 이름의 전용 브랜치 권장
- 이 단계에서는 동작 로직보다 문서 구조와 상태 계층 정의를 먼저 확정한다.

### Phase 1. 문서 분리 초안 작성

`ai-survival-log`

- 루트 문서 4개 원칙 고정
- `ARCHITECTURE.md` 초안 작성
- `docs/operating/operations.md` 초안 작성
- `docs/adr/0001~0003` 초안 작성
- `AGENTS.md`, `CLAUDE.md`, `.codex/AGENTS.md`의 역할 재분배 초안 작성

`ai-survival-log-site`

- 루트 문서 4개 원칙 고정
- `ARCHITECTURE.md` 초안 작성
- `docs/operating/ui-guide.md` 초안 작성
- `docs/operating/content-contract.md` 재배치 또는 래핑 구조 정의
- `docs/operating/seo-operations.md` 재배치 또는 래핑 구조 정의
- `docs/adr/0001~0003` 초안 작성
- `AGENTS.md`, `CLAUDE.md`, `.codex/AGENTS.md`의 역할 재분배 초안 작성

완료 기준:

- 각 문서의 책임이 1차로 겹치지 않는다.
- `AGENTS.md`에는 핵심 규칙만 남긴다.
- Claude와 Codex 모두 같은 공통 문서를 참조할 수 있다.

### Phase 2. JSON 파생 상태 경로와 스키마 확정

`ai-survival-log`

- `output/state/` 생성
- `wiki-index.json`, `wiki-lint-summary.json`, `publish-manifest.json` 스키마 설계
- 추적 대상과 비추적 대상을 분리

`ai-survival-log-site`

- `output/state/` 생성
- `content-contract-summary.json`, `series-manifest.json`, `content-inventory.json` 스키마 설계
- 추적 대상과 비추적 대상을 분리

완료 기준:

- 각 JSON 파일의 source-of-truth와 생성 스크립트 책임이 문서화된다.
- "직접 수정 금지" 규칙이 명시된다.
- 보안상 넣지 말아야 할 필드 목록이 명시된다.

### Phase 3. 생성 스크립트/검증 루프 연결

`ai-survival-log`

- `scripts/state` 또는 `scripts/export-state` 엔트리포인트 설계
- 필요 시 `scripts/wiki`에서 선택적으로 호출하는 옵션 설계

`ai-survival-log-site`

- 기존 contract verification 스크립트와 `scripts/state`의 책임 분리
- build/lint/test와 별도로 state generation을 둘지 결정

완료 기준:

- 사람이 언제 어떤 명령으로 state를 재생성하는지 명확하다.
- source-of-truth 작업과 derived artifact 작업의 경계가 명확하다.

### Phase 4. 문서 표면 정합성 정리

- `README.md`, `AGENTS.md`, `CLAUDE.md`, `.codex/AGENTS.md`, 관련 contract docs를 새 계층에 맞춰 정리
- 중복 설명은 제거하고 상위 문서에서 하위 문서로 링크한다.
- cross-repo 계약이 drift하지 않게 서로 참조한다.
- `AGENTS.md -> ARCHITECTURE.md -> docs/operating/* -> docs/adr/*` 포인터 모델을 반영한다.

완료 기준:

- 상위 문서는 얇고, 세부 문서는 역할별로 분리되어 있다.
- 같은 규칙이 여러 문서에서 다른 표현으로 충돌하지 않는다.

### Phase 5. 검증

`ai-survival-log`

- `python3 scripts/wiki sync`
- `python3 scripts/wiki lint --summary`
- 필요 시 `pytest` 범위 확인

`ai-survival-log-site`

- content contract verification
- `npm test`
- 필요 시 build/lint 확인

완료 기준:

- 새 문서 구조가 lint/contract/test 기준과 모순되지 않는다.
- JSON 파생물은 source-of-truth를 대체하지 않는다.

## 초기 파일 트리 초안

### `ai-survival-log`

```text
.
├── README.md
├── AGENTS.md
├── CLAUDE.md
├── ARCHITECTURE.md
├── docs/
│   ├── operating/
│   │   ├── operations.md
│   │   ├── publishing-contract.md
│   │   └── content-seo-guide.md
│   └── adr/
│       ├── 0001-markdown-source-of-truth.md
│       ├── 0002-json-derived-state-only.md
│       └── 0003-harness-layering-for-upstream-repo.md
├── .codex/
│   └── AGENTS.md
├── scripts/
│   ├── wiki
│   └── state
└── output/
    └── state/
```

### `ai-survival-log-site`

```text
.
├── README.md
├── AGENTS.md
├── CLAUDE.md
├── ARCHITECTURE.md
├── docs/
│   ├── operating/
│   │   ├── ui-guide.md
│   │   ├── content-contract.md
│   │   └── seo-operations.md
│   └── adr/
│       ├── 0001-site-consumer-contract-boundary.md
│       ├── 0002-harness-layering-for-site-repo.md
│       └── 0003-manual-posts-must-remain-contract-compatible.md
├── .codex/
│   └── AGENTS.md
├── scripts/
│   └── state
└── output/
    └── state/
```

## 비목표

- 위키 source-of-truth를 JSON으로 전환
- 두 저장소에 동일한 문서 세트 강제
- PRD를 상시 루트 규칙 문서로 승격
- 대형 agent catalog나 MCP 전용 메타데이터 도입
- 미래 RAG/vector DB 요구를 현재 wiki 구조에 선반영

## 추천 구현 순서

1. `ai-survival-log` 문서 분리 초안
2. `ai-survival-log` JSON 파생 상태 스키마
3. `ai-survival-log-site` 문서 분리 초안
4. `ai-survival-log-site` JSON 파생 상태 스키마
5. cross-repo contract 정렬
6. 스크립트/검증 연결

upstream source-of-truth를 먼저 정리한 다음 downstream consumer를 맞추는 순서가 더 안전하다.

## 관련 페이지

- [[projects/repo-structure-refactor]]
- [[projects/cross-repo-ai-automation-lab]]
- [[concepts/post-compact-essential-section]]
- [[concepts/engineering-guardrails]]
- [[concepts/wiki-automation]]
- [[sources/2026-04-19-cmds-system-files]]
- [[sources/2026-04-22-project-state-management-analysis]]
