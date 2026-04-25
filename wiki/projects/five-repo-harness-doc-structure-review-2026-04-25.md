---
title: "Five Repo Harness Doc Structure Review"
created: "2026-04-25"
updated: "2026-04-25"
type: project
sources: []
tags: [project, review, harness, docs, agents, claude, operations]
status: active
published: false
slug: ""
description: "5개 저장소의 AGENTS.md, CLAUDE.md, 상위 운영 문서가 과밀한지와 분리 필요성을 엔지니어, 선임 엔지니어, 검수자 관점에서 검토한 문서."
---

# Five Repo Harness Doc Structure Review

## Review Scope

검토 대상 저장소:

- `ai-survival-log`
- `ai-survival-log-site`
- `shared-agent-harness`
- `company-wiki`
- `company-assistant-ops`

검토 대상 문서:

- `AGENTS.md`
- `CLAUDE.md`
- `ARCHITECTURE.md`
- 각 저장소의 `docs/operating/*` 상위 운영 문서

검토 질문:

1. 각 저장소의 상위 문서에 정보가 너무 많이 몰려 있는가
2. 역할이 다른 정보가 한 파일에 과하게 섞여 있는가
3. 지금 당장 분리해야 하는가, 아니면 현재 수준이 적절한가

## Engineer Review

엔지니어 관점에서 보면 저장소별 상태는 다릅니다.

### 1. `ai-survival-log`

판단:

- `AGENTS.md`는 길지만 역할이 비교적 명확하다
- 문제는 `CLAUDE.md`가 너무 많은 층위를 동시에 담고 있다는 점이다

현재 `CLAUDE.md`가 동시에 담는 것:

- adapter surface 메모
- 위키 스키마
- frontmatter 스펙
- index/log 규칙
- command surface
- ingest/publish workflow 설명
- 프로젝트 소개와 layer 모델

즉 하나의 파일이:
- Claude adapter notes
- wiki schema reference
- operating quickstart
- local command catalog
를 동시에 맡고 있습니다.

엔지니어 판단:

- `ai-survival-log/CLAUDE.md`는 현재 5개 저장소 중 가장 과밀하다
- 이 파일은 향후 분리 우선순위 1순위다

### 2. `ai-survival-log-site`

판단:

- `AGENTS.md`는 길지만 상위 규칙 선언과 상세 문서 링크로 나뉘어 있어 관리 가능 범위다
- `CLAUDE.md`는 adapter 메모로 얇게 유지되고 있어 적절하다

엔지니어 판단:

- 지금 당장 추가 분리 필요는 크지 않다

### 3. `shared-agent-harness`

판단:

- `AGENTS.md`, `CLAUDE.md`는 오히려 적절하게 얇다
- 상세 운영 정보는 `docs/operating/*`, `lanes/*`, `roles/*`로 이미 잘 분산돼 있다

엔지니어 판단:

- 현재 구조가 가장 모범적이다
- 추가 분리보다 현 상태 유지가 낫다

### 4. `company-wiki`

판단:

- 상위 문서는 짧고, 실제 운영 규칙은 `docs/operating/*`로 분리돼 있다
- authoring source라는 역할도 분명하다

엔지니어 판단:

- 과밀 문제 없음
- 지금 수준이 적절하다

### 5. `company-assistant-ops`

판단:

- `AGENTS.md`, `CLAUDE.md`는 얇고 명확하다
- `approval / audit / credential / handoff` 문서가 분리돼 있어 책임 경계도 분명하다

엔지니어 판단:

- 과밀 문제 없음
- 지금 수준이 적절하다

## Senior Engineer Review

선임 엔지니어 관점에서는 `문서 길이`보다 `drift risk`를 더 봅니다.

### 핵심 관찰

1. `shared-agent-harness`, `company-wiki`, `company-assistant-ops`는 이미 좋은 분리 상태다  
   - 상위 문서는 얇다  
   - 실제 운영 규칙은 operating docs로 빠져 있다  
   - 이 셋은 지금 더 쪼개기보다 유지가 낫다

2. `ai-survival-log-site`도 구조적으로는 안정적이다  
   - AGENTS는 선언적  
   - CLAUDE는 adapter 성격  
   - detailed references가 따로 있다

3. `ai-survival-log`만 예외다  
   - `AGENTS.md`는 rule hub 역할이라 길어도 괜찮다  
   - 하지만 `CLAUDE.md`는 adapter surface를 넘어 사실상 repository manual처럼 커졌다  
   - 이 상태가 계속되면 `AGENTS.md`, `CLAUDE.md`, `docs/operating/*` 사이 drift 가능성이 가장 높다

### 선임 엔지니어 결론

- `전부 분리해야 한다`는 판단은 아님
- `ai-survival-log/CLAUDE.md`만 선택적으로 정리 대상이다

권장 분리 축:

1. `docs/reference/wiki-schema.md`
   - page types
   - frontmatter spec
   - wikilink rules
   - index/log rules

2. `docs/reference/local-command-surface.md`
   - `/wiki:*`
   - `/content:*`
   - local command surface

이렇게 두 축으로 빼면 `CLAUDE.md`는 adapter notes + reference links만 남길 수 있다.

## Reviewer Review

검수자 관점에서 중요한 것은:

1. 어떤 문서를 먼저 읽어야 하는지 헷갈리지 않는가
2. 상위 문서가 세부 문서를 압도하지 않는가
3. 문서 분리가 실제로 유지보수 리스크를 줄이는가

판단:

- 현재 5개 저장소 중 4개는 문제 없다
- 오히려 무리하게 분리하면 문서가 더 흩어져 온보딩 비용이 올라갈 수 있다
- 따라서 `일괄 분리`는 오버엔지니어링이다
- 다만 `ai-survival-log/CLAUDE.md`는 이미 찾기 어려운 정보가 한 파일에 몰려 있어, selective split이 맞다

검수자 결론:

- `block 없음`
- `warn 없음`

## Findings

초기 리뷰 시 경고 1개가 있었지만 수리됐다.

### fixed 1. `warn` — `ai-survival-log/CLAUDE.md`가 adapter surface를 넘어 repository manual처럼 커졌다

조치:

- `docs/reference/wiki-schema.md` 추가
- `docs/reference/local-command-surface.md` 추가
- `CLAUDE.md`를 adapter surface + reference link hub로 축소

현재 상태:

- `CLAUDE.md`는 top-level Claude adapter 역할로 돌아갔다
- schema와 local command surface는 dedicated reference 문서로 분리됐다

## Final Decision

- `block`: 0
- `warn`: 0
- `overall`: `selective split completed`

## Director Recommendation

디렉터에게 올릴 권고는 단순합니다.

- 5개 프로젝트 문서를 전부 쪼개지 말 것
- `ai-survival-log/CLAUDE.md`만 선택적으로 정리할 것
- 나머지 4개 저장소는 현재 수준 유지

즉:

`full split`이 아니라 `targeted split`이 맞았고, 필요한 범위는 이번 변경으로 닫혔다.

## Related

- [[projects/detached-workspace-repo-migration-review-and-plan]]
- [[projects/detached-workspace-phase4-review-2026-04-25]]
