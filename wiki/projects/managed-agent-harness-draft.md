---
title: "Managed Agent Harness 초안"
created: "2026-04-23"
updated: "2026-04-23"
type: project
sources: []
tags: [project, harness, workflow, agents, automation, wiki, codex, claude]
status: draft
published: false
slug: ""
description: "ai-survival-log와 ai-survival-log-site의 단일 에이전트 협업 흐름을 역할 기반 managed agent harness로 확장할 때의 최소 설계 초안."
---

# Managed Agent Harness 초안

실제 즉시 운영 구조는 다음 문서를 우선 기준으로 본다.

- [[projects/immediate-agent-operating-structure]]

이 초안은 `ai-survival-log`와 `ai-survival-log-site`의 현재 단일 에이전트 협업 환경을 무리하게 복잡하게 만들지 않으면서, 역할 분리와 검증 강화를 중심으로 `managed agent` 구조로 확장하는 방향을 정리한다.

핵심은 `에이전트 수를 늘리는 것`이 아니라 다음 세 가지다.

- 저장소 경계(`raw -> wiki -> output/blog -> site`)를 더 강하게 지키게 만들기
- 작업 종류별 책임과 검증 지점을 명확히 분리하기
- 도구나 모델이 달라져도 유지되는 하네스 구조를 먼저 설계하기

## 문제 정의

현재 구조는 실용적이지만 다음 위험이 남아 있다.

- intake, authoring, publish, review가 하나의 대화 흐름 안에 섞여 있다
- source-of-truth와 derived artifact 경계를 사람의 주의력에 많이 의존한다
- 검증 단계가 문서화되어 있어도 실행 순서와 실패 처리 규칙이 역할별로 분리되어 있지 않다
- 같은 에이전트가 작성과 검토를 모두 수행하면 품질 게이트가 약해질 수 있다

## 설계 목표

1. `wiki/`를 계속 source of truth로 유지한다.
2. `raw/`와 `output/` 경계를 자동화 수준에서 더 분명히 한다.
3. `ai-survival-log-site`를 포함한 cross-repo workflow를 기본 대상으로 잡는다.
4. 역할은 소수만 도입하고, 대형 agent catalog는 만들지 않는다.
5. 현재 저장소의 skill, command, validation 문서와 충돌하지 않게 설계한다.
6. 초기에는 병렬 멀티 에이전트보다 `역할 기반 workflow`를 우선한다.

## 비목표

- 자율적으로 무한 작업을 이어가는 fully autonomous system
- 저장소 전반을 뒤흔드는 대형 agent pack 도입
- source-of-truth를 JSON state나 외부 DB로 이동
- wiki 구조를 미래 RAG 요구에 맞춰 선제 재편

## 최소 역할 분리안

초기안은 5개 역할로 제한한다.

중요한 원칙은 `프로젝트마다 역할을 복제하지 않는다`는 점이다. 예를 들어 `Planning Agent`와 `Review Agent`는 개인/회사 도메인 모두에서 공용으로 쓸 수 있고, `Authoring Agent`는 같은 역할 이름을 써도 저장소별 surface와 policy를 다르게 받는 구조가 기본이다.

즉:

- `Planning Agent`는 upstream에서는 wiki 프로젝트 계획과 콘텐츠 기획을 다루고
- downstream에서는 site 반영 계획과 presentation 적용 계획을 다루며
- 회사 도메인에서는 회의 후속과 업무 실행 계획을 다룰 수 있고
- 같은 역할이지만 대상 시스템에 따라 입력/출력 계약이 달라진다

### 1. Research Agent

책임:

- 웹서핑 기반 자료 수집
- 공식 문서, 1차 출처, 참고 링크 수집
- 최신 정보 확인이 필요한 작업의 fact-finding
- raw intake 전 source 후보 정리

금지:

- 출처 확인 없이 사실 확정
- 수집 자료를 바로 source of truth로 승격
- 외부 시스템 write 액션 수행

성공 기준:

- 링크와 출처가 명시된다
- raw intake나 wiki authoring 전에 검증 가능한 자료 묶음이 만들어진다

### 2. Intake Agent

책임:

- `raw/` 신규 자료 intake 보조
- 적절한 intake 경로 판단
- ingest 전 메타데이터 초안 정리
- `wiki-ingest` 또는 관련 흐름의 입력 정리

금지:

- `wiki/`를 source of truth로 확정하는 판단
- publish artifact 직접 생성

성공 기준:

- raw source 위치가 명확하다
- source type과 ingest target이 맞다

### 3. Authoring Agent

책임:

- `wiki/` 페이지 생성 및 수정
- wikilink, frontmatter, human-first 설명 구조 유지
- publishable 페이지의 slug, description, SEO 기본 품질 유지

금지:

- 검증 실패를 무시한 completion 처리
- `output/` 산출물을 source처럼 수정

성공 기준:

- 위키 페이지가 source-of-truth 규칙을 지킨다
- 관련 wikilink와 설명 밀도가 충분하다

### 4. Review Agent

책임:

- 변경 범위에 대한 품질 검토
- source-of-truth, publishing contract, docs consistency 점검
- 필요한 검증 명령과 block/warn/escalate 판정

금지:

- 작성 단계의 가정 위에 검증 없이 승인
- publish contract 변경을 암묵적으로 허용

성공 기준:

- validation matrix에 맞는 최소 검증 경로가 지정된다
- 위험, 누락, 회귀 가능성이 명시된다

### 5. Publish Agent

책임:

- `wiki -> output/blog -> ai-survival-log-site/content/posts` 흐름 관리
- publish artifact 생성과 downstream 호환성 확인
- 이미지 경로와 frontmatter 계약 점검

금지:

- wiki를 우회해 output을 직접 authoring source로 취급
- downstream 호환성 없이 publish 완료 처리

성공 기준:

- publish artifact가 재생성 가능하다
- downstream 경로와 이미지 계약이 유지된다

## Harness 원칙

## 레이어와 역할의 차이

레이어는 시스템의 구조고, 역할은 그 위에서 수행하는 책임 단위다.

### 레이어

- `Brain layer` — 계획, 판단, 초안 작성, 분류
- `Memory layer` — 세션 요약, 작업 상태, wiki 참조, journal 참조
- `Tool layer` — 파일 수정, 테스트, lint, publish, 변환
- `Integration layer` — 웹 검색, 외부 문서 조회, Gmail, Calendar, Sheets 같은 외부 시스템 연결
- `Policy layer` — 권한, approval, secrets boundary, audit log

### 역할

- `Research Agent`
- `Intake Agent`
- `Authoring Agent`
- `Review Agent`
- `Publish Agent`

같은 역할도 여러 레이어를 통과한다. 예를 들어 `Authoring Agent`는 Brain layer에서 초안을 만들고 Tool layer에서 파일을 수정하지만, Policy layer의 검증과 권한 제약을 받아야 한다.

## 저장소별 적용 방식

역할은 저장소마다 복제되기보다, 저장소별 surface와 계약을 받아 다르게 동작하는 쪽이 유지보수에 유리하다.

### `ai-survival-log`

- `Research Agent` — source 후보, 참고 문서, 최신 정보 조사
- `Intake Agent` — `raw/` intake 정리
- `Authoring Agent` — `wiki/` 문서, source 요약, 프로젝트 계획 작성
- `Review Agent` — wiki contract, publishability, docs consistency 검수
- `Publish Agent` — `wiki -> output/blog` 흐름 관리

### `ai-survival-log-site`

- `Research Agent` — presentation/SEO/reference 조사
- `Authoring Agent` — downstream adaptation, presentation copy, site-facing content 조정
- `Review Agent` — runtime contract, rendering, SEO, site compatibility 검수
- `Publish Agent` — `output/blog -> ai-survival-log-site/content/posts` 소비 호환 확인

초기 단계에서는 `Planning Agent`를 별도 역할로 분리하지 않고 `Authoring Agent` 안의 planning mode로 두는 것이 현실적이다. 이후 planning 업무가 충분히 커지면 분리한다.

도메인 분리까지 포함한 현재 원칙은 다음과 같다.

- `Planning / Review / Engineering / 일부 Research`는 공용 role/lane
- `Authoring / Publish / Assistant Ops`는 도메인 전용 surface
- 분리의 기준은 role이 아니라 data, account, storage, permission

### 역할보다 계약이 우선

각 역할은 전문화되지만, 최상위 계약은 모두 공유한다.

- `wiki/` is source of truth
- `raw/` is immutable source intake
- `output/` is derived artifact
- publishable 페이지는 stable `slug`와 concrete `description` 유지
- validation matrix를 통과하지 못하면 완료로 처리하지 않음

### 초기 구현은 "다중 persona, 단일 런타임"으로 시작

초기 도입은 실제 병렬 멀티 에이전트 시스템보다 다음 방식이 현실적이다.

- 하나의 주 에이전트가 workflow를 총괄
- 단계별로 `intake`, `authoring`, `review`, `publish` 역할 모드 전환
- skill과 command로 역할 surface를 분리
- 필요 시에만 별도 sub-agent 또는 tool wrapper 확장 검토

즉 첫 단계는 `멀티 에이전트 흉내를 내는 운영 규율`이며, 이후 필요할 때만 실제 병렬화한다.

### 강한 중단 조건

다음 경우 자동 중단 또는 human handoff가 필요하다.

- publish contract 위반
- source-of-truth 경계 위반
- 검증 명령 실패
- lane 정의 없는 새 채널 workflow 요구
- 관련 문서 간 규칙 충돌

## 권장 Workflow

### Workflow A: Web Research -> Raw Source Intake

1. Research Agent가 공식 문서, 1차 출처, 참고 링크를 수집
2. Intake Agent가 source type과 intake target을 결정
3. raw source를 저장하거나 정리
4. Authoring Agent가 `wiki/sources/` 또는 관련 페이지 초안 작성
5. Review Agent가 frontmatter, wikilink, 설명 품질 점검

### Workflow B: Wiki Authoring

1. Authoring Agent가 wiki 페이지 작성 또는 개정
2. Review Agent가 validation matrix 기준으로 필요한 검증 경로 지정
3. 검증 통과 후만 완료 처리

### Workflow C: Publishable Change

1. Authoring Agent가 publishable wiki 페이지 수정
2. Review Agent가 SEO, slug, description, image path, internal links 점검
3. Publish Agent가 artifact 생성과 downstream 호환성 확인
4. 실패 시 wiki 또는 assets 단계로 되돌림

## 도입 순서 초안

### Phase 1. 역할 명세 확정

- 역할 5개를 문서 수준에서 먼저 고정
- 각 역할의 input, output, 금지 행위 정의
- skill 또는 command 매핑 후보 정리
- web research 출처 규칙 정리

### Phase 2. Workflow Gate 추가

- 작업 유형별로 `required checks` 연결
- 완료 보고 전에 어느 역할이 어떤 검증을 수행하는지 정리
- `warn/block/escalate` 판정 문구 표준화
- cross-repo 경계(`ai-survival-log`와 `ai-survival-log-site`)를 workflow gate에 연결

### Phase 3. 시범 적용

- `web research -> raw -> wiki` 1건
- `raw -> wiki` 1건
- `wiki edit` 1건
- `wiki -> publish` 1건

이 세 흐름에 역할 분리안을 수동 적용해 friction과 누락을 확인한다.

### Phase 4. Surface 보강

- 필요 시 skill, command, checklist 문서 보강
- `output/state/agent-surface-summary.json`과 연계 가능한 점검 항목 검토

### Phase 5. Lane 확장

- planning lane과 assistant ops lane을 문서 수준에서 분리
- Gmail, Calendar, Sheets 연동은 read-first, suggest-first 원칙으로 시작
- 외부 write 액션은 approval-required 정책으로 분리

## Lane 정의

lane은 `에이전트 하나`가 아니라 `업무 흐름 묶음`이다. 하나의 lane 안에서 여러 역할이 순서대로 참여한다.

### 1. Research Lane

용도:

- 웹서핑, 자료 조사, 최신 정보 확인, 참고 링크 수집

주요 역할:

- `Research Agent`
- 필요 시 `Intake Agent`

결과물:

- 링크 묶음
- source 후보
- fact-check 메모

### 2. Planning Lane

용도:

- 기획, 디렉팅, PT 구조, 실행 계획, 우선순위 정리

주요 역할:

- 초기에는 `Authoring Agent`
- `Review Agent`

결과물:

- PRD
- 실행 계획
- 발표 구조 초안

초기에는 별도 `Planning Agent`를 만들지 않고 planning 업무를 역할 모드로 운영한다.

별도 실행안:

- [[projects/planning-lane-execution-draft]]

### 3. Authoring Lane

용도:

- wiki/source 문서, 회의록, 보고서, 초안 작성

주요 역할:

- `Authoring Agent`
- `Review Agent`

결과물:

- wiki 페이지
- 회의 요약
- 보고 초안

### 4. Engineering Lane

용도:

- 코딩, 리팩토링, 테스트, 검수 대응

주요 역할:

- 초기에는 `Authoring Agent`가 execution mode로 수행
- `Review Agent`

결과물:

- 코드 변경
- 테스트 결과
- 수정 이력

### 5. Publish Lane

용도:

- `wiki -> output/blog -> ai-survival-log-site/content/posts`

주요 역할:

- `Authoring Agent`
- `Review Agent`
- `Publish Agent`

결과물:

- publish artifact
- downstream compatibility check

### 6. Assistant Ops Lane

용도:

- 일정관리, 할 일 보고, 회의 follow-up, 시트 정리

주요 역할:

- 후속 단계에서 별도 assistant ops 역할 검토

결과물:

- 일정 후보
- action item 목록
- 보고 초안

초기에는 이 lane을 문서 수준으로만 정의하고, 실제 Gmail/Calendar/Sheets write는 나중 단계에서 연다.

별도 실행안:

- [[projects/assistant-ops-lane-execution-draft]]

## 운영상 기대 효과

- 같은 저장소 규칙을 더 일관되게 적용할 수 있다
- 작성과 검토 역할이 분리되어 self-approval 성향이 줄어든다
- downstream publish 전에 upstream 계약 위반을 더 빨리 잡을 수 있다
- Claude/Codex 중 어느 도구를 쓰든 공통 workflow를 유지하기 쉬워진다

## 리스크

- 역할만 늘고 실제 검증이 자동화되지 않으면 ceremony만 증가할 수 있다
- 작성 속도보다 review gate가 과도하게 강해지면 실무 속도가 떨어질 수 있다
- 문서만 많아지고 실제 command/skill 설계가 따라오지 않으면 drift가 생긴다

그래서 초기 원칙은 `작게 시작하고, 역할보다 계약을 먼저 고정한다`이다.

## 다음 작업 후보

- 역할별 command/skill surface 초안 만들기
- `Review Agent`의 최소 체크리스트 템플릿 정의
- publishable 변경용 시범 workflow 1개를 PRD 수준으로 구체화
- `Research Lane`의 출처 수집 규칙과 clipping 경계 정의
- planning 업무를 별도 agent로 분리할 시점 판단
- `Assistant Ops Lane`의 approval/audit 기준 정의
- 필요 시 `docs/operating/operations.md`에 역할 기반 completion gate 반영 검토

## 관련 페이지

- [[projects/immediate-agent-operating-structure]]
- [[projects/harness-layering-and-json-derived-state]]
- [[projects/cross-repo-ai-automation-lab]]
- [[projects/planning-lane-execution-draft]]
- [[projects/assistant-ops-lane-execution-draft]]
- [[projects/repo-structure-refactor]]
- [[concepts/agentic-workflow]]
- [[topics/claude-code-to-codex]]
