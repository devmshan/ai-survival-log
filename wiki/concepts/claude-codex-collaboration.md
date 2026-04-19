---
title: "Claude-Codex 협업 패턴"
created: "2026-04-18"
updated: "2026-04-19"
type: concept
sources: ["[[sources/2026-04-19-cmds-system-files]]"]
tags: [claude, codex, collaboration, planning, validation, ai-agent]
status: active
published: false
slug: ""
description: ""
---

# Claude-Codex 협업 패턴

같은 저장소에서 Claude와 Codex가 서로 다른 강점을 활용해 협업하는 운영 패턴. Claude는 계획 수립과 대화형 상호작용에 강하고, Codex는 실제 저장소 상태 검증과 실행에 강하다.

## 역할 분리

### Claude의 강점

- 대화 맥락을 유지하며 계획 수립
- 사용자와 상호작용하며 요구사항 명확화
- slash command(`/wiki:ingest`, `/wiki:publish` 등) 중심 실행
- 글쓰기, 요약, 분석

### Codex의 강점

- 실제 저장소 상태와 계획 문서 교차 검증
- 파일 이동, 스크립트 수정, 테스트 실행 등 구현 중심 작업
- skill + 문서 + 스크립트 중심 위키 운영

## 대표 협업 플로우

### 1. Plan(Claude) → Validate(Codex) → Execute(Codex)

```
Claude: 계획 문서 초안 작성
    ↓
Codex: 실제 저장소 상태, 테스트, 계약 문서와 교차 검증
    ↓
Codex: 검증된 계획을 실제 저장소에 적용
```

**실제 사례 (2026-04-18):** `repo-structure-refactor.md` 계획을 Claude가 작성하고 Codex가 검증 후 실행

### 2. Command(Claude) ↔ Skill(Codex) 병행

- 같은 기능을 Claude command와 Codex skill로 양쪽에 구현
- 대체 관계가 아니라 상호 보완 구조
- 예시: `/wiki:ingest` (Claude command) ↔ `wiki-ingest` (Codex skill)

## Command vs Skill 선택 기준

| 기준 | Claude Command | Codex Skill |
|------|---------------|-------------|
| 적합한 작업 | 실행 절차형 | 판단형/재사용형 |
| UX | slash command | skill + 문서 + 스크립트 |
| 예시 | `/wiki:ingest`, `/wiki:lint` | `wiki-ingest`, `recommend-clipper-template` |

## 외부 설계 사례와의 비교

`[[sources/2026-04-19-cmds-system-files]]`는 agent별 시스템 파일과 shared rules를 분리한 PKM 운영 사례다. 이 프로젝트 기준으로는 다음 판단이 유효하다.

- `CLAUDE.md`와 `AGENTS.md`를 분리하는 현재 구조는 유지 가치가 있다.
- Claude command와 Codex skill을 병행 surface로 두는 방식은 재사용 가능한 패턴이다.
- 핵심 경계를 각 surface에 대칭 배치할 때는 `[[concepts/post-compact-essential-section]]` 같은 경량 패턴이 효과적이다.
- 반면 우선순위 메타데이터, 과도한 frontmatter, 대형 명령 분류 체계까지 그대로 들여올 필요는 없다.

## 검증 방식의 중요성

Codex로 계획을 검증할 때 "문서만 읽기"는 불충분하다. 실제 검증에는 다음이 포함돼야 한다:

1. 실제 디렉토리 상태 확인
2. 테스트(`pytest`) 실행
3. 계약 문서(publishing-contract.md 등)와 교차 검토
4. lint 검증

## 관련 페이지

- [[entities/claude-code]]
- [[entities/ecc]]
- [[concepts/post-compact-essential-section]]
- [[sources/2026-04-19-cmds-system-files]]
- [[sources/2026-04-18-claude-plan-codex-validation]]
- [[sources/2026-04-18-raw-immutability-codex-skills]]
