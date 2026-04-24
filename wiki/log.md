---
title: "Wiki Log"
---

# Wiki Log

## 2026-04-24

### ingest: 2026-04-23 저널 + EP 94 아티클 흡수
- **source:**
  - raw/journals/2026-04-23-claude-codex-choice-and-anthropic-direction.md
  - raw/articles/2026-04-23T160522+0900-EP 94 Anthropic과 낮게 열린 과실들.md
- **created:**
  - [[entities/codex]], [[entities/anthropic]]
  - [[concepts/opus-4-7]], [[concepts/mythos]], [[concepts/adaptive-thinking]]
  - [[sources/2026-04-23-claude-codex-choice-and-anthropic-direction]]
  - [[sources/2026-04-23-ep94-anthropic-low-hanging-fruits]]
- **updated:** [[topics/claude-code-to-codex]], [[topics/claude-plan-codex-validate]] (Codex wikilink 추가)
- **summary:** Claude/Codex 구독 선택 저널과 AI Frontier EP 94 팟캐스트를 흡수. Anthropic·Codex 엔티티 신설, Opus 4.7·Mythos·Adaptive Thinking 개념 페이지 신설.

### publish: 4편 downstream 동기화
- **output:** ai-survival-log-site/content/posts/
- **published:**
  - [[topics/professors-brain-02-relearning-llm]] → 2026-04-24-professors-brain-02-relearning-llm.mdx
  - [[topics/professors-brain-03-closing-the-loop]] → 2026-04-24-professors-brain-03-closing-the-loop.mdx
  - [[topics/agent-harness-notes-01-dual-domain]] → 2026-04-24-agent-harness-notes-01-dual-domain.mdx
  - [[topics/learning-my-own-taste-on-frontier]] → 2026-04-24-learning-my-own-taste-on-frontier.mdx
- **summary:** Axis A/B 2축 리뷰 및 편집 완료 후 4편 ai-survival-log-site로 동기화. 도서관과 교수님의 뇌 시리즈(02·03편)와 Agent Harness Notes 01, 독립 에세이 1편.

### ingest: 프론티어를 따라가며 내 취향을 학습시키는 일 초안 작성
- **source:** raw/journals/2026-04-24-managed-agent-harness-and-dual-domain-planning-conversation-backup-part2.md
- **created:** [[topics/learning-my-own-taste-on-frontier]]
- **output:** output/blog/2026-04-24-learning-my-own-taste-on-frontier.mdx
- **summary:** capability overhang 시대의 두 갈래 도망길 비교에서 attention business와 취향 → 나의 LM head 은유로 이어지는 자기 해석 에세이 초안 완성. 독립 에세이(시리즈 없음).

### ingest: Agent Harness Notes 01 초안 작성
- **source:** raw/journals/2026-04-24-managed-agent-harness-and-dual-domain-planning-conversation-backup.md
- **created:** [[topics/agent-harness-notes-01-dual-domain]]
- **output:** output/blog/2026-04-24-agent-harness-notes-01-dual-domain.mdx
- **summary:** Scaling Managed Agents → brain-hand decoupling → 개인/회사 이중 도메인 → role/lane is shared, data/surface is isolated 결론까지 판단 흐름을 서사로 정리한 Agent Harness Notes 시리즈 1편 완성.

### ingest: 도서관과 교수님의 뇌 03 초안 작성
- **source:** raw/journals/2026-04-24-managed-agent-harness-and-dual-domain-planning-conversation-backup-part2.md
- **created:** [[topics/professors-brain-03-closing-the-loop]]
- **output:** output/blog/2026-04-24-professors-brain-03-closing-the-loop.mdx
- **summary:** Claude Design과 AI for Science를 "루프를 닫는다"는 공통 구조로 묶은 03편 초안 완성.

### ingest: 도서관과 교수님의 뇌 02 초안 작성
- **source:** raw/journals/2026-04-23-anthropic-gpu-shortage-and-ai-terms-conversation-backup.md (part2 포함), raw/journals/2026-04-23-claude-codex-choice-and-anthropic-direction.md
- **created:** [[topics/professors-brain-02-relearning-llm]]
- **output:** output/blog/2026-04-24-professors-brain-02-relearning-llm.mdx
- **summary:** Claude 구독비 문제로 Anthropic 방향성을 파악하다 Mythos 10T 루머에서 tokenizer → LM head → KV cache까지 내려간 학습 서사 초안 완성.

### edit: raw/journals 파일 이동
- **updated:** `2026-04-23` (루트) → `raw/journals/2026-04-23-claude-codex-choice-and-anthropic-direction.md`

### edit: 도서관과 교수님의 뇌 01편 — series 메타 역소급
- **updated:**
  - [[topics/how-llm-works]] — `series`, `seriesSlug: professors-brain`, `seriesOrder: 1` 추가. 본문 변경 없음.

### edit: workspace 폴더 구조 검수 및 보안 경계 정책 고정
- **source:** 사용자 검수 요청 — `workspace-folder-structure-review-sheet.md` 기준 5개 포인트 검토
- **created:**
  - [[projects/workspace-security-boundary]] — 4축 보안 경계 정책 (file system, git identity, credentials, harness context)
- **updated:**
  - [[projects/dual-domain-agent-operating-model]] — 폴더 이름 확정(`company-wiki`, `shared-agent-harness`), positive/negative list 추가, 이주 계획 footnote 추가
  - [[projects/workspace-folder-structure-review-sheet]] — 이름 변경 반영
- **summary:** 최상위 폴더 5개 구조 검수 결과 조건부 통과. `company-work-wiki`→`company-wiki`, `shared-engineering-harness`→`shared-agent-harness`로 이름 확정. 4축 보안 경계 정책 신규 고정. 다음 단계로 각 폴더 내부 구조 설계 진행 가능.

### edit: 작업계획 상태 정리 및 다음 단계 확정
- **source:** 사용자 요청 — 오늘까지의 설계/검수 작업을 계획 문서에 반영하고 내일 이어갈 다음 단계 정리
- **updated:**
  - [[projects/workspace-folder-structure-review-sheet]] — 검수 완료 상태, 확정된 폴더 이름, 다음 단계 우선순위 추가
  - [[projects/dual-domain-agent-operating-model]] — 현재 진행 상태와 완료/다음/보류 항목 추가
- **summary:** 오늘까지 완료된 설계/검수 작업을 계획 문서에 반영. 내일 우선순위는 `shared-agent-harness` 내부 구조 설계, 그 다음 `company-wiki` 내부 구조 설계로 정리.

### edit: shared-agent-harness 내부 구조 설계 초안 작성
- **source:** 사용자 요청 — `shared-agent-harness` 내부 구조 설계부터 진행
- **created:**
  - [[projects/shared-agent-harness-internal-structure]] — 공용 role/lane/skill/workflow 저장소의 루트 문서, roles/lanes/skills/commands/scripts/tests/examples 구조와 positive/negative list 정의
- **updated:**
  - [[projects/workspace-folder-structure-review-sheet]] — 현재 반영 항목으로 shared-agent-harness 내부 구조 문서 링크 추가
  - [[projects/dual-domain-agent-operating-model]] — 다음 단계 반영 상태 링크 추가
- **summary:** `shared-agent-harness`를 공용 role/lane/skill/workflow 저장소로 정의하고, 개인/회사 데이터 원본과 credential은 금지하는 내부 구조 초안을 고정. 다음 단계는 `company-wiki` 내부 구조 설계.

### edit: 이중 agent 교차검증을 공용 품질 게이트로 반영
- **source:** 사용자 요청 — 블로그 글 검수에 쓰던 2-agent cross-validation을 모든 검수와 구조 변경에도 적용
- **updated:**
  - [[projects/immediate-agent-operating-structure]] — Review and QA, Engineering workflow, 운영 원칙에 이중 검증 기본값 추가
  - [[projects/shared-agent-harness-internal-structure]] — cross-validation policy, template, command, comparator 책임 추가
  - [[projects/dual-domain-agent-operating-model]] — Review Lane 공통 규칙과 step 4 품질 게이트 반영
  - `docs/operating/operations.md` — formal review gate의 2-agent cross-validation 권장 규칙 추가
- **summary:** 블로그 글 교차검증 경험을 일반화해, 모든 공식 검수 게이트에서 `primary review + secondary review` 구조를 기본값으로 채택. 특히 Engineering Lane, 구조 변경, contract-sensitive 변경에 강제에 가까운 규칙으로 반영.

### edit: 교차검증의 surface/path 다양성 규칙 추가
- **source:** 사용자 요청 — 같은 모델 반복보다 서로 다른 surface 또는 review path를 써야 한다는 규칙 반영
- **updated:**
  - [[projects/shared-agent-harness-internal-structure]] — 같은 모델/같은 checklist 반복은 교차검증으로 보지 않는 규칙 추가
  - [[projects/immediate-agent-operating-structure]] — 이중 검증 원칙에 서로 다른 surface/path 사용 조건 추가
  - [[projects/dual-domain-agent-operating-model]] — Review Lane 공통 규칙 보강
  - `docs/operating/operations.md` — formal review gate guidance 보강
- **summary:** `2-agent cross-validation`을 형식적 반복 실행이 아니라, 가능하면 서로 다른 surface 또는 다른 review path를 통한 검수로 정의. 같은 모델과 같은 checklist 반복은 교차검증으로 인정하지 않도록 명시.

## 2026-04-22

### plan: Harness 세분화와 JSON 파생 상태 설계 초안
- **source:** 사용자 요청 기반 cross-repo 구조 설계
- **created:**
  - [[projects/harness-layering-and-json-derived-state]] — `ai-survival-log`/`ai-survival-log-site` Harness 문서 분리 구조와 JSON 파생 상태 경로 설계
- **updated:**
  - `wiki/index.md` — 신규 project 페이지 반영 예정
- **summary:** `AGENTS.md` 과부하를 줄이기 위한 Harness 계층 분리안과, Markdown source-of-truth를 유지하면서 lint/publish/contract 결과를 JSON 파생 상태로 분리하는 초안을 정리. upstream는 `AGENTS.md + ARCHITECTURE.md + OPERATIONS.md + docs/adr/`, site는 `AGENTS.md + ARCHITECTURE.md + UI_GUIDE.md + docs/adr/` 조합을 권장하고, 상태 JSON은 source-of-truth가 아닌 재생성 가능한 artifact로 한정했다.

### ingest: 프로젝트 상태 관리 및 Engineering Guardrails 분석
- **source:** `raw/journals/2026-04-22-project-state-management-analysis.md`, `.codex/AGENTS.md` (Engineering Guardrails 섹션 추가)
- **created:**
  - [[sources/2026-04-22-project-state-management-analysis]] — 상태 관리 구조·TDD 규칙 현황 분석 요약
  - [[concepts/wiki-automation]] — Claude Code 훅 + wiki_lib.py 자동화 패턴
  - [[concepts/engineering-guardrails]] — TDD 적용 범위·보안·코드 품질 가드레일
- **updated:**
  - [[concepts/llm-wiki-pattern]] — wiki-automation 역링크 추가
  - `wiki/index.md` — 신규 페이지 3개 반영
- **summary:** 프로젝트 상태 관리(hooks, markdown 기반, 자동 커밋 없음)와 TDD 적용 범위(자동화 스크립트만)를 위키에 문서화. Engineering Guardrails 개념 페이지 신규 생성.

## 2026-04-21

### ingest: 대규모 시스템 설계 기초 6~9장
- **source:** `raw/books/system-design-interview-ch6-01~13.png`, `ch7-01~05.png`, `ch8-01~07.png`, `ch9-01~12.png` (총 37개 이미지)
- **created:**
  - [[sources/2026-04-21-system-design-interview-ch6]] — 6장: 키-값 저장소 설계 (CAP, Quorum, 벡터 시계, 가십, SSTable)
  - [[sources/2026-04-21-system-design-interview-ch7]] — 7장: 유일 ID 생성기 설계 (UUID, 티켓서버, 스노우플레이크)
  - [[sources/2026-04-21-system-design-interview-ch8]] — 8장: URL 단축기 설계 (301/302, 해시, Base62)
  - [[sources/2026-04-21-system-design-interview-ch9]] — 9장: 웹 크롤러 설계 (BFS, Frontier, 블룸 필터)
  - [[concepts/key-value-store]] — 키-값 저장소 개념
  - [[concepts/cap-theorem]] — CAP 정리 개념
  - [[concepts/vector-clock]] — 벡터 시계 개념
  - [[concepts/gossip-protocol]] — 가십 프로토콜 개념
  - [[concepts/unique-id-generator]] — 분산 유일 ID 생성기 개념
  - [[concepts/url-shortener]] — URL 단축기 개념
  - [[concepts/web-crawler]] — 웹 크롤러 개념
  - [[concepts/bloom-filter]] — 블룸 필터 개념
  - [[topics/system-design-interview-06]] — 6장 스터디 토픽
  - [[topics/system-design-interview-07]] — 7장 스터디 토픽
  - [[topics/system-design-interview-08]] — 8장 스터디 토픽
  - [[topics/system-design-interview-09]] — 9장 스터디 토픽
- **updated:**
  - [[projects/study-system-design-interview]] — 6~9장 완료 표시, 개념 페이지 링크 추가
  - `wiki/index.md` — 총 118개 페이지로 갱신
- **summary:** Alex Xu 책 6~9장 이미지 37장 분석. 6장은 CAP·Quorum·벡터시계·가십·SSTable+LSM+블룸필터까지 분산 KV 스토어 전 스택을 정리. 7장은 스노우플레이크 64비트 구조. 8장은 URL 단축기의 301/302·Base62 핵심 결정. 9장은 BFS 기반 크롤러·Frontier 3원칙(Politeness/Priority/Freshness)·블룸필터 중복제거를 정리. 개념 8개 + 토픽 4개 + 소스 4개 신규 생성.

## 2026-04-20

### ingest: 대규모 시스템 설계 기초 5장 — 안정 해시 설계
- **source:** `raw/books/스크린샷 2026-04-20 오후 10.56.42~55.png` (7개 이미지)
- **created:**
  - [[sources/2026-04-20-system-design-interview-ch5]] — 5장 소스 요약 (해시 재배치 문제, 해시 링, 가상 노드, 활용 사례)
  - [[concepts/consistent-hashing]] — 안정 해시 개념 (해시 링 구조, 가상 노드, DynamoDB/Cassandra 활용 사례)
  - [[topics/system-design-interview-05]] — 5장 블로그 토픽 (published: true)
- **updated:**
  - [[projects/study-system-design-interview]] — 5장 완료 표시, 개념 페이지 링크 추가
  - `wiki/index.md` — 총 102개 페이지로 갱신
- **summary:** Alex Xu 책 5장 이미지 7장 분석. 나머지 연산 해시 한계 → 해시 링으로 해결 → 불균등 문제를 가상 노드로 해결하는 흐름을 concepts 1개와 topic 1개로 정리. DynamoDB·Cassandra·Discord·Akamai·Maglev 활용 사례 포함. Phase 2 5장 완료.

### ingest: 대규모 시스템 설계 기초 4장 — 처리율 제한 장치의 설계
- **source:** `raw/books/스크린샷 2026-04-20 오전 10.17.14~43.png` (13개 이미지)
- **created:**
  - [[sources/2026-04-20-system-design-interview-ch4]] — 4장 소스 요약 (Rate Limiter 배치 위치, 5가지 알고리즘, 분산 환경 설계)
  - [[concepts/rate-limiter]] — 처리율 제한 장치 개념 (알고리즘 5종 비교, Redis 구현, 분산 환경 경쟁 조건)
  - [[topics/system-design-interview-04]] — 4장 블로그 토픽 (published: true)
- **updated:**
  - [[projects/study-system-design-interview]] — 4장 완료 표시, 개념 페이지 링크 추가
  - `wiki/index.md` — 총 99개 페이지로 갱신
- **summary:** Alex Xu 책 4장 이미지 13장 분석. 토큰 버킷/누출 버킷/고정 윈도 카운터/이동 윈도 로그/이동 윈도 카운터 5가지 알고리즘, Redis 기반 구현, HTTP 429 응답 처리, 분산 환경 경쟁 조건·동기화 문제를 concepts 1개와 topic 1개로 정리. Phase 2 시작 (4장 완료).

## 2026-04-19

### ingest: 대규모 시스템 설계 기초 2장 — 개략적인 규모 추정
- **source:** `raw/books/스크린샷 2026-04-15 오후 1.40.07~17.png` (3개 이미지)
- **created:**
  - [[sources/2026-04-15-system-design-interview-ch2]] — 2장 소스 요약 (2의 제곱수, 응답지연, 가용성, 트위터 예제)
  - [[concepts/back-of-envelope-estimation]] — 개략적 추정 개념 (단위감각, QPS/저장소 공식, 실전 팁)
  - [[concepts/availability]] — 가용성 개념 (나인, SLA, SPOF, 장애 격리)
  - [[topics/system-design-interview-02]] — 2장 블로그 토픽 (published: true)
- **updated:**
  - [[projects/study-system-design-interview]] — 2장 완료 표시, 개념 페이지 링크 추가
  - `wiki/index.md` — 총 93개 페이지로 갱신
- **summary:** Alex Xu 책 2장 캡처 이미지 3장 분석. 2의 제곱수/응답지연/가용성 수치 + 트위터 QPS·저장소 추정 예제를 concepts 2개와 topic 1개로 정리. 블로그 포스트 바로 발행 가능 상태(published: true).

### ingest: 대규모 시스템 설계 기초 3장 — 시스템 설계 면접 공략법
- **source:** `raw/books/스크린샷 2026-04-19 오후 5.13.11~38.png` (6개 이미지)
- **created:**
  - [[sources/2026-04-19-system-design-interview-ch3]] — 3장 소스 요약 (4단계 프레임워크, 뉴스 피드 예제, 체크리스트)
  - [[concepts/system-design-interview-framework]] — 면접 4단계 프레임워크 개념 (시간 배분, 해야/말아야 할 것)
  - [[topics/system-design-interview-03]] — 3장 블로그 토픽 (published: true)
- **updated:**
  - [[projects/study-system-design-interview]] — 3장 완료 표시, 개념 페이지 링크 추가
  - `wiki/index.md` — 총 96개 페이지로 갱신
- **summary:** Alex Xu 책 3장 이미지 6장 분석. 4단계 프레임워크(문제이해→개략설계→상세설계→마무리), 시간 배분, 뉴스 피드 예제(팬아웃/피드 조회 흐름), 해야 할/말아야 할 체크리스트를 concepts 1개와 topic 1개로 정리. Phase 1 기초 3장 완료.

### ingest: CMDS System Files 설계 사례 심층 분석
- **source:** `raw/articles/2026-04-19T163318+0900-johnfkoo951cmds-system-files CMDS System Files - Brutalism Style Documentation Hub.md`
- **created:**
  - [[sources/2026-04-19-cmds-system-files]] — GitHub 실제 소스(CLAUDE.md, AGENTS.md, frontmatter-standard.md) 열람 후 적용 가능 패턴 3개 정리
- **updated:**
  - `wiki/index.md` — 페이지 수 88로 갱신
- **summary:** `johnfkoo951/cmds-system-files` v4.2 GitHub 소스 직접 확인. 적용 후보 3개를 추렸고, 이 중 Essential 섹션은 즉시 도입, description 규칙은 한국어 authoring 흐름에 맞게 제한적으로 흡수, STATIC/DYNAMIC 주석은 보류하기로 판단.

### edit: CMDS 사례 기준으로 핵심 규칙만 선택 적용
- **updated:**
  - `CLAUDE.md` — `Essential (Post-Compact)` 섹션 추가, description 규칙 구체화
  - `AGENTS.md` — 핵심 경계 규칙용 `Essential (Post-Compact)` 섹션 추가
  - `.codex/AGENTS.md` — Codex용 대칭 `Essential (Post-Compact)` 섹션 추가
  - `docs/content-seo-guide.md` — description이 "무엇이 들어 있고 언제 유용한지" 드러나도록 기준 강화
  - [[sources/2026-04-19-cmds-system-files]] — 즉시 적용 / 제한 적용 / 보류 판단을 명시
- **summary:** 외부 PKM 시스템 설계를 그대로 복제하지 않고, 현재 저장소에 실효성이 높은 규칙만 선별 적용. Essential 섹션은 주요 agent surface에 대칭 추가했고, description 규칙은 한국어 SEO 흐름과 양립하도록 조정했으며, STATIC/DYNAMIC 주석은 보류.

### file-answer: Post-Compact Essential 패턴을 개념 페이지로 저장
- **created:**
  - [[concepts/post-compact-essential-section]] — 긴 agent guide에서 핵심 규칙만 상단에 재선언하는 문서 패턴
- **updated:**
  - [[concepts/llm-wiki-pattern]] — 운영 문서 패턴 섹션 추가
  - [[concepts/claude-codex-collaboration]] — 대칭적 핵심 경계 배치 패턴 링크 추가
- **summary:** 이번 대화에서 나온 결론을 source note 수준에 머무르게 하지 않고, 긴 상위 규칙 문서에서 핵심만 남기는 `Essential (Post-Compact)` 패턴을 reusable concept로 분리 저장.

## 2026-04-18

### file-answer: Wiki 카테고리 설계 결정 페이지 저장
- **created:**
  - [[projects/wiki-category-design-decision]] — syntheses 폐기 근거, 확정 카테고리 구조, 새 카테고리 도입 판단 기준
- **updated:**
  - [[projects/repo-structure-refactor]] — wiki-category-design-decision 역링크 추가
- **summary:** syntheses 폐기 결정의 배경과 Wiki 카테고리 설계 원칙을 projects/ 페이지로 보존. 향후 카테고리 추가 논의 시 참조 기준.

### edit: wiki/syntheses/ 카테고리 폐기 및 전체 surface 정리
- **updated:**
  - `CLAUDE.md` — syntheses 폴더 목록, 페이지 타입 섹션, type enum, /wiki:query, /wiki:file-answer, /wiki:lint 6곳 수정
  - `.claude/commands/wiki/query.md` — syntheses 참조 제거
  - `.claude/commands/wiki/file-answer.md` — 카테고리 목록에서 syntheses 제거, 라우팅 규칙 수정
  - `.claude/commands/wiki/lint.md` — type 유효값에서 synthesis 제거
  - `.codex/skills/wiki-file-answer/SKILL.md` — description, category list, routing rule 3곳 수정
  - `.codex/skills/wiki-query-answer/SKILL.md` — syntheses 참조 제거
  - `.codex/skills/wiki-lint/SKILL.md` — type 일관성 기준 업데이트
  - `.codex/skills/wiki-ingest/SKILL.md` — syntheses 라우팅 규칙을 topics/ 통합 방식으로 변경
  - `scripts/wiki_lib.py` — _TYPE_ORDER, _TYPE_LABELS에서 synthesis 제거, type 코멘트 수정
  - `tests/test_wiki_lib.py` — test_includes_syntheses_section 테스트 메서드 제거
  - `wiki/projects/repo-structure-refactor.md` — syntheses 도입 계획 전체 철회, 미도입 결정으로 반영
  - `wiki/topics/claude-plan-codex-validate.md` — 폴더 트리 2곳에서 syntheses/ 제거
  - `output/blog/2026-04-18-claude-plan-codex-validate.mdx` — 동일 수정
- **deleted:** `wiki/syntheses/` 빈 디렉토리 제거
- **summary:** syntheses/ 카테고리는 도입 후 한 번도 사용되지 않았음. publish 구조(topics만 published: true)와 맞지 않고, 비교/판단 지식은 topics/에 통합하는 것이 더 자연스럽다는 판단으로 전체 surface에서 제거.

## 2026-04-18

### file-answer: Graphify 재평가에서 파생된 위키 페이지 2개 저장
- **created:**
  - [[entities/graphify]] — Graphify 실제 기능 엔티티 페이지 (multi-modal 처리, 올바른 CLI, 출력 형식, 재검토 조건)
  - [[concepts/tool-evaluation-methodology]] — 도구 평가 방법론 개념 (공식 문서 확인 → 올바른 명령 테스트 → 필요성 판단 순서, 흔한 실수 패턴, 결론 품질 기준)
- **updated:**
  - [[topics/graphify-evaluation]] — entities/graphify, concepts/tool-evaluation-methodology 역링크 추가
- **summary:** 이번 Graphify 재평가 과정에서 도출된 두 가지 재사용 가능한 지식을 위키에 보존. Graphify 엔티티는 올바른 기능 스펙 참조용, 도구 평가 방법론은 향후 도구 평가 시 재활용 가능한 개념.

### edit: Post 2 대대적 수정 — Graphify 재평가 기반 리라이트
- **updated:**
  - [[topics/graphify-evaluation]] — 제목·결론·서사 전면 재작성. 기존 기술적 오류 수정 (마크다운 미지원 → multi-modal 처리 가능), 새 서사: 잘못된 명령 테스트 → 재평가 → "못 해서가 아니라 지금 필요 없어서" 비채택
  - [[sources/2026-04-18-graphify-evaluation]] — CLI 테스트 결과 테이블, Graphify 실제 기능, 재평가 장단점 수정
  - [[topics/wiki-markdown-vs-graph-db]] — Graphify 파생 레이어 가능성 보충 주석 추가
  - [[projects/wiki-rag-expansion-roadmap]] — Graphify 판단 섹션 수정 (기각 이유: 마크다운 미지원 → 현재 규모 불필요)
  - `output/blog/2026-04-18-graphify-evaluation.mdx` — MDX 재생성
- **summary:** Graphify가 `graphify .` 명령으로 마크다운도 처리 가능하다는 사실 확인 후 Post 2 전면 재작성. 결론 방향은 동일(비채택)이나 이유가 정확해짐 — "도구가 할 수 있는 것과 프로젝트가 지금 필요한 것은 다른 질문"이 새로운 핵심 메시지.

### 23:30 — publish: 블로그 포스트 2편 퍼블리시
- **created:**
  - `output/blog/2026-04-18-claude-plan-codex-validate.mdx`
  - `output/blog/2026-04-18-graphify-evaluation.mdx`
  - [[sources/2026-04-18-graphify-evaluation]] — Graphify 평가 세션 소스 페이지
  - [[topics/claude-plan-codex-validate]] — Plan→Validate→Execute 패턴 블로그 포스트
  - [[topics/graphify-evaluation]] — Graphify 비채택기 블로그 포스트
- **updated:**
  - [[topics/claude-code-to-codex]] — Post 1 역링크 추가
  - [[topics/wiki-markdown-vs-graph-db]] — Post 2 역링크 추가
- **summary:** 0418 저널 자료에서 블로그 포스트 2편 작성. Post 1은 Claude-Codex Plan→Validate→Execute 패턴 실전기, Post 2는 Web Clipper 세팅 → Graphify 첫 클리핑 → 비채택 결정 서사.



### 22:00 — ingest: raw 불변 규칙 강화와 Codex wiki skill 5종 추가
- **source:** [[sources/2026-04-18-raw-immutability-codex-skills]]
- **created:**
  - [[sources/2026-04-18-raw-immutability-codex-skills]] — raw 불변 원칙 강화 + Codex skill 추가 세션 요약
- **updated:**
  - `raw/AGENTS.md`, `raw/CLAUDE.md`, `.claude/commands/wiki/ingest.md` — 불변 규칙 표현 강화
  - `.codex/skills/wiki-ingest/`, `.codex/skills/wiki-query-answer/`, `.codex/skills/wiki-file-answer/`, `.codex/skills/wiki-lint/`, `.codex/skills/wiki-publish/` — Codex용 wiki skill 5종 신규 추가
- **summary:** `raw/` 불변 원칙을 "절대 직접 수정 금지, 요약/해설은 wiki/에서" 수준으로 강화. Claude command와 Codex skill을 병행 구조로 운용하는 원칙 정립. Codex용 wiki skill 5종 추가.

### 21:00 — ingest: wiki 명령 surface와 운영 문서 정합성 보정
- **source:** [[sources/2026-04-18-wiki-surface-alignment]]
- **created:**
  - [[sources/2026-04-18-wiki-surface-alignment]] — wiki 명령과 CLAUDE.md 재정렬 세션 요약
- **updated:**
  - `.claude/commands/wiki/query.md` — `raw/{type}` 원본 확인, `syntheses/` 우선 검토 추가
  - `.claude/commands/wiki/file-answer.md` — `syntheses/` vs `projects/` 선택 기준 추가
  - `.claude/commands/wiki/lint.md` — `synthesis` 타입, generated surface 제외 기준 추가
  - `.claude/commands/wiki/publish.md` — `output/blog` 기본 경로, `assets/intake → assets/blog` 승격 원칙 추가
  - `CLAUDE.md` — 커맨드 워크플로우와 publish 파이프라인 현재 구조 기준으로 재서술
- **summary:** 구조 변경 후 wiki 명령 surface를 실제 운영 흐름에 맞게 재정렬. `syntheses/`의 핵심 저장소 지위와 이중 artifact 경계(`output/blog` vs `ai-survival-log-site/content/posts/`) 명확화.

### 20:00 — ingest: Obsidian Web Clipper 설정 마무리와 첫 클리핑 확인
- **source:** [[sources/2026-04-18-web-clipper-setup]]
- **created:**
  - [[sources/2026-04-18-web-clipper-setup]] — Web Clipper 설정 실사용 검증 세션 요약
- **updated:**
  - `assets/clipper-templates/*.json` — 번호 붙인 이름 체계(`01 Article Deep Research` 등)로 일괄 변경
- **summary:** 템플릿 10종 등록 과정에서 전역 fallback 트리거 문제 발견·해결. 수동 선택 전용 템플릿 운용 원칙 정립. 첫 실제 클리핑 파일(Graphify 아티클)로 템플릿 유효성 확인, vault 경로 설정 문제 발견.

### 18:00 — ingest: Web Clipper 템플릿 설계와 intake 구조 재정의
- **source:** [[sources/2026-04-18-clipper-template-intake]]
- **created:**
  - [[sources/2026-04-18-clipper-template-intake]] — Web Clipper 템플릿 설계 세션 요약
  - [[entities/obsidian-web-clipper]] — Obsidian Web Clipper 도구 엔티티
  - [[concepts/assets-intake-pattern]] — 이중 intake 구조 (raw/type vs assets/intake) 개념
- **updated:**
  - [[entities/obsidian]] — Web Clipper 섹션 추가
  - `assets/clipper-templates/` — 템플릿 10종 + README 신규 추가
  - `assets/intake/reference-notes/`, `assets/intake/reference-images/`, `assets/intake/attachments/` 추가
  - `README.md`, `docs/operating-playbook.md`, `.claude/commands/wiki/ingest.md` — Web Clipper 루틴 반영
  - `.claude/commands/content/recommend-clipper-template.md`, `.codex/skills/recommend-clipper-template/` 추가
- **summary:** Obsidian Web Clipper 템플릿 10종 설계. 텍스트 소스(`raw/{type}`)와 채널 미정 비텍스트 자산(`assets/intake/`)을 분리하는 이중 intake 구조 도입. URL 기반 추천 스킬을 Claude/Codex 양쪽에 추가.

### 17:00 — ingest: Codex 폴더 구조 적용 실행
- **source:** [[sources/2026-04-18-codex-folder-structure-execution]]
- **created:**
  - [[sources/2026-04-18-codex-folder-structure-execution]] — 폴더 구조 실행 세션 요약
- **updated:**
  - `sources/` → `raw/articles/`, `book/` → `raw/books/`, `docs/images/` → `assets/blog/`, `docs/webtoon/` → `assets/webtoon/` — 파일 이동 완료
  - `wiki/syntheses/`, `assets/shared/`, `assets/youtube/`, `assets/instagram/`, `output/blog/` 등 신규 디렉토리 생성
  - `scripts/wiki_lib.py`, `scripts/pr-summary.mjs` — 새 경계 반영
  - `raw/AGENTS.md`, `assets/AGENTS.md`, `output/AGENTS.md` — 대칭 구조 추가
- **summary:** 계획된 `raw/wiki/assets/output` 4계층 구조를 실제 저장소에 적용. 27개 테스트 통과, lint 오류 없음. CLAUDE.md/AGENTS.md 대칭 구조 완성.

### 16:20 — edit: 구조 변경 계획과 RAG 보류 원칙 문서화
- **source:** [[sources/2026-04-18-claude-plan-codex-validation]]
- **created:**
  - [[sources/2026-04-18-claude-plan-codex-validation]] — Claude 계획서 Codex 검증 세션 요약
  - [[concepts/claude-codex-collaboration]] — Claude 계획 + Codex 검증/실행 협업 패턴
  - [[projects/wiki-rag-expansion-roadmap]] — human-first wiki를 유지한 채 추후 RAG/vector DB 확장을 다루는 예정 프로젝트
- **updated:**
  - [[projects/repo-structure-refactor]] — `raw/wiki/assets/output` 경계, `wiki/syntheses/`, human-first wiki 원칙, downstream site 고려사항을 반영한 최종 세부 계획으로 확장
  - `AGENTS.md`, `.codex/AGENTS.md`, `README.md`, `CLAUDE.md` — 구조 변경 계획과 future-RAG-separate-project 원칙을 참조하도록 갱신
  - `docs/publishing-contract.md`, `docs/operating-playbook.md`, `docs/content-seo-guide.md` — 구조 변경 중에도 downstream 계약이 유지된다는 점을 명시
  - `.claude/commands/wiki/file-answer.md`, `.claude/commands/wiki/publish.md` — `syntheses`와 publish artifact 계획 반영
  - wiki/index.md — 프로젝트 1개 추가, 총 72개 페이지
- **summary:** Claude가 작성한 구조 변경 계획서를 Codex가 실제 저장소 상태·테스트·계약 문서와 교차 검증. `docs/images → raw/assets` 충돌 발견 후 `assets/` 채널별 구조로 해결. human-first wiki 원칙 합의, future RAG는 별도 예정 프로젝트로 분리.

### 14:00 — edit: 레포 폴더 구조 리팩토링 계획 문서화
- **created:**
  - [[projects/repo-structure-refactor]] — raw/ 타입별 분류, wiki/syntheses/ 추가, output/ 멀티채널 구조화 계획
- **updated:**
  - wiki/index.md — projects 1개 추가, 총 71개 페이지
- **summary:** sources/→raw/, wiki/syntheses/ 신규, output/ 멀티채널 구조화를 위한 리팩토링 계획을 프로젝트 페이지로 문서화. 구현 전 계획 단계.
- **note:** 이 계획서는 이후 Codex 검증 세션([[sources/2026-04-18-claude-plan-codex-validation]])을 거쳐 최종 확정됨.

### 10:20 — file-answer: canonical URL 개념 설명 위키 저장
- **created:**
  - [[concepts/canonical-url]] — 대표 URL 지정, 중복 URL 완화, 블로그 SEO 맥락 정리
- **updated:**
  - [[projects/site-seo-foundation-and-content-rewrite]] — canonical 개념 링크 추가
  - wiki/index.md — concepts 1개 추가, 총 70개 페이지
- **summary:** SEO 대화 중 나온 canonical 개념을 별도 concept 페이지로 저장. 대표 URL 의미, 중복 URL 완화 역할, 이 프로젝트의 site SEO 정비와의 연결을 함께 정리.

### 01:30 — file-answer: site SEO foundation + 전체 포스트 리라이트 작업 위키 저장
- **created:**
  - [[projects/site-seo-foundation-and-content-rewrite]] — 기술 SEO, 콘텐츠 SEO 가이드, Search Console 제출, 전체 포스트 리라이트를 한 번에 정리한 프로젝트 페이지
- **updated:**
  - [[projects/blog-ai-study-site]] — site 현재 구현/운영 상태, 기술 SEO/리라이트 반영
  - wiki/index.md — 프로젝트 1개 추가, 총 69개 페이지
- **summary:** `ai-survival-log-site`에서 진행한 SEO 기반 정비, `content/posts` 전체 1차 리라이트, content SEO writing guide 도입, Search Console 도메인 인증 및 sitemap 제출, 초기 색인 요청까지의 흐름을 upstream wiki에 durable context로 정리.

## 2026-04-17

### 18:10 — file-answer: 개발자 자동화 실습 01 PR summary 블로그 글 작성
- **created:**
  - [[topics/developer-automation-lab-01-pr-summary]] — PR summary 학습과 실제 PR 실습 기록
- **updated:**
  - [[concepts/pr-summary]] — 시리즈 글 역링크 추가
  - [[projects/cross-repo-ai-automation-lab]] — 관련 토픽 링크 추가
  - wiki/index.md — topic 1개 추가 예정
- **summary:** 오늘의 PR summary 학습 흐름과 실제 GitHub PR 코멘트 실습, LLM 확장 보류 판단까지 한 편의 발행용 글로 정리. `개발자 자동화 실습` 시리즈의 1편으로 작성.

### 16:30 — file-answer: PR summary 개념 설명 위키 저장
- **created:**
  - [[concepts/pr-summary]] — PR summary의 목적, 동작 방식, 역할별 활용 정리
- **updated:**
  - [[concepts/pull-request]] — PR summary 관련 페이지 링크 추가
  - wiki/index.md — concepts 1개 추가, 총 67개 페이지
- **summary:** 대화에서 정리한 PR summary 설명을 concepts/pr-summary.md로 저장. PR 자동 코멘트의 목적, PR 작성 전 로컬 사전 점검, 작성자/리뷰어/maintainer 관점을 함께 정리.

### 14:00 — file-answer: .mjs 파일과 Shebang 개념 위키 저장
- **created:**
  - [[concepts/es-module-mjs]] — ES Module, .mjs 파일 형식, CommonJS vs ESM 비교
  - [[concepts/shebang]] — #! 문자열, 인터프리터 지시, /usr/bin/env 패턴
- **updated:**
  - wiki/index.md — concepts 2개 추가, 총 66개 페이지
- **summary:** 대화에서 생성된 .mjs 파일과 shebang 설명을 각각 wiki/concepts/에 저장. 두 페이지 간 상호 크로스 레퍼런스 추가.

### 10:00 — file-answer: Pull Request 개념 설명 위키 저장
- **created:**
  - [[concepts/pull-request]] — PR 개념, 흐름, 리뷰 방식, CI 연동, PR summary 자동화 연결
- **updated:**
  - [[projects/cross-repo-ai-automation-lab]] — pull-request 역링크 추가
  - wiki/index.md — concepts 1개 추가, 총 64개 페이지
- **summary:** 대화에서 생성된 PR 설명 답변을 wiki/concepts/pull-request.md로 저장. PR 기본 흐름, 리뷰 유형, CI/CD 연동, PR summary 자동화와의 연결까지 포함.

## 2026-04-16

### 12:00 — file-answer: PR summary 실습 결과 학습 문서화 + wiki 등록
- **source:** `docs/2026-04-16-pr-summary-practice-review.md`
- **created:**
  - [[projects/cross-repo-ai-automation-lab]] — cross-repo AI 자동화 실습 프로젝트 페이지
- **updated:**
  - [[projects/blog-ai-study-site]] — cross-repo 자동화 실습 프로젝트 링크 추가
  - wiki/index.md — 프로젝트 1개 추가, 총 62개 페이지
- **summary:** PR summary 실습 결과를 공부용 문서로 재정리하고, 두 저장소 역할 차이와 축소 적용 개념을 포함한 학습 경로를 wiki project 페이지로 등록. 다음 단계인 Jira issue plan draft는 진행 예정 상태로 유지.

### 10:45 — edit: AI-Native 개발자 메모를 내부 참고자료로 재분류
- **updated:**
  - `docs/2026-04-16-ai-native-developer-study-reference.md` — 공부 계획 전 참고자료로 재정리
  - wiki/index.md — 잘못 추가한 위키 항목 제거
- **summary:** 해당 메모는 블로그/위키 발행 후보가 아니라 공부 계획 수립 전 참고자료 성격이므로 `docs/` 문서로 이동하고, 위키 토픽/소스 반영분은 제거.

## 2026-04-15

### 14:30 — ingest: AI Frontier EP86 원본 전사 분석 → 위키 심화 업데이트
- **source:** `sources/2026-04-15-ai-frontier-ep86-part1.md`, `sources/2026-04-15-ai-frontier-ep86-part2.md`
- **created:**
  - [[concepts/instant-app]] — 쓰고 버리는 소프트웨어 패러다임, 인스턴트 앱 개념
- **updated:**
  - [[sources/2026-04-15-ai-frontier-ep86]] — 소스 요약 페이지 대폭 확장 (원본 발언 흐름, 데모 상세, 사이버 포뮬러 줄거리 전체, CS=영문과 비유, 자동화 파이프라인 구조, 비개발직군 사례 등)
  - [[concepts/agentic-workflow]] — 방어적 AI 프레이밍 기법, sub-agent 제약 이유, self-critique 루프, context building 선문답 방식 추가
  - [[entities/backend-ai]] — Backend.AI:GO 상세 기능, 탄생 스토리, 분산 라우팅, 자동화 파이프라인 상세 추가
  - [[entities/lablup]] — AI-for-AI 인터페이스 전환 전략, 2개월 룰, CTO 돈오 에피소드, 비개발직군 적응 사례, 사업계획서 자동화 추가
  - [[concepts/code-value-convergence]] — 인스턴트 앱 생태계, 살아남는 앱의 두 가지 조건 추가
- **summary:** EP86 원본 전사 파트1/2를 세밀히 분석해 기존 위키 페이지들을 맥락 손실 없이 심화 업데이트. 특히 sources 페이지를 단순 요약에서 발언 흐름과 예시를 보존하는 풍부한 참조 문서로 확장. 인스턴트 앱 개념 신규 생성.

### 12:00 — ingest: AI Frontier EP86 에피소드 (Agentic Workflow, Backend.AI:GO)
- **source:** AI Frontier EP86 유튜브 (2026-02-18 게시)
- **created:**
  - [[sources/2026-04-15-ai-frontier-ep86]] — 에피소드 전체 요약, 핵심 인사이트 9개 섹션
  - [[entities/ai-frontier]] — AI Frontier 유튜브 채널 (노정석, 최승준 진행)
  - [[entities/lablup]] — AI infrastructure 플랫폼, Backend.AI 개발사
  - [[entities/backend-ai]] — Lablup의 GPU 클러스터 운영 체제 + Backend.AI:GO
  - [[entities/shin-junggyu]] — Lablup 대표, Agentic Workflow 실천가
- **summary:** 신정규 Lablup 대표의 40일/130억 토큰/100만 줄 코드 Backend.AI:GO 개발 경험을 소스로 인제스트. AI Frontier 채널, Lablup, Backend.AI, 신정규 엔티티 페이지 신규 생성. concepts/agentic-workflow, bio-token, code-value-convergence, startup-watermill 등 파생 개념 페이지도 동시 생성됨.

## 2026-04-14

### 18:30 — publish: 대규모 시스템 설계 스터디 01 블로그 포스트
- **source:** `wiki/topics/system-design-interview-01.md`
- **created:**
  - [[topics/system-design-interview-01]] — 1장 핵심 정리 토픽 (published: true)
  - `ai-survival-log-site/content/posts/2026-04-14-system-design-interview-01.mdx`
- **summary:** 1장 스터디 내용을 블로그 시리즈 01로 발행. 서버 1대 → 수백만 사용자 아키텍처 진화 과정 전체 정리.

### 18:00 — ingest: 스터디 1장 보충 (ack/nack, binlog, ProxySQL, Read-Your-Writes)
- **source:** 대화 (스터디 1장 심화 보충)
- **updated:**
  - [[concepts/message-queue]] — ack/nack 상세, DLQ, TCP ack vs 메시지큐 ack 비교
  - [[concepts/db-replication]] — binlog 상세 흐름, Semi-Sync, ProxySQL 상세, Read-Your-Writes
- **summary:** ack/nack DLQ, TCP와 메시지큐 ack 비교, binlog 동기화 흐름, ProxySQL 커넥션 풀링/장애감지, Read-Your-Writes 패턴 보충.

### 17:30 — ingest: 시스템 설계 스터디 1장 심화 대화
- **source:** `sources/2026-04-14-system-design-study-ch1-deep-dive.md`
- **created:**
  - [[concepts/saml]] — SAML 프로토콜, IdP/SP 세션, SLO, 전자결재 오류 사례
- **updated:**
  - [[concepts/cache-strategies]] — 캐시 계층 위치(브라우저/CDN/인메모리), Write-Through, Write-Back, 캐시 일관성 전략, Memcached API
  - [[concepts/database-sharding]] — 수평/수직 샤딩 비교, 버티컬 샤딩 상세, 샤딩 방법(범위/해시/위치), 샤드 장애 복구
  - [[concepts/message-queue]] — 소비자 개념, 경쟁 소비자 패턴, Java/RabbitMQ 예시, ack/nack 메커니즘
  - [[concepts/db-replication]] — 동기/비동기 동기화, binlog 메커니즘, 쿼리 라우팅, ProxySQL
- **summary:** 1장 심화 스터디 대화 인제스트. Memcached API, SAML 세션 관리, 캐시 전략 심화, 샤딩 종류, 메시지 큐 소비자 패턴 등 대화에서 나온 개념 위키에 추가.

### 16:30 — ingest: 시스템 설계 1장 전체 (스크린샷 16장)
- **source:** `book/` 폴더 스크린샷 16장 (가상 면접 사례로 배우는 대규모 시스템 설계 기초 1장)
- **created:**
  - [[concepts/vertical-vs-horizontal-scaling]] — Scale Up vs Scale Out 트레이드오프
  - [[concepts/load-balancer]] — 로드밸런서 동작 원리, 장애 대처
  - [[concepts/db-replication]] — 주/부 DB 복제, 장애 시나리오
  - [[concepts/cache-strategies]] — 캐시 계층, LRU/LFU/FIFO 방출 정책
  - [[concepts/cdn]] — CDN 동작 원리, 캐시 무효화 전략
  - [[concepts/stateless-architecture]] — 무상태 웹 계층, 세션 공유 저장소
  - [[concepts/message-queue]] — 생산자/소비자 모델, 느슨한 결합
  - [[concepts/database-sharding]] — 샤딩 키, 재샤딩/핫스팟/조인 문제
- **updated:**
  - [[projects/study-system-design-interview]] — 1장 ✅ 완료, 상세 단계 업데이트
  - wiki/index.md — 총 49개 페이지
- **summary:** 책 1장 스크린샷 전체 인제스트. 단일 서버 → 백만 사용자 아키텍처 진화 과정에서 등장하는 핵심 컴포넌트 8개 개념 페이지 생성.

### 스터디중 — publish: LLM 작동 방식 블로그 포스트
- **source:** `sources/2026-04-14-how-claude-thinks.md`
- **created:**
  - [[topics/how-llm-works]] — LLM 파라미터/임베딩/RAG/KG 개념 토픽 (published: true)
  - `content/posts/how-llm-works.mdx` — 블로그 포스트 출력
- **summary:** 시스템 설계 스터디 1장 대화에서 나온 LLM 내부 구조 이해 내용을 블로그 포스트로 발행. "도서관과 교수님의 뇌" 비유로 파라미터/임베딩/RAG/KG 정리.

### 스터디중 — ingest: RAG·임베딩 개념 (시스템 설계 스터디 1장)
- **source:** 대화 (시스템 설계 면접 스터디 1장 관련 질문)
- **created:**
  - [[concepts/embedding]] — 임베딩 3가지 맥락 (추론/학습/VectorDB)
  - [[concepts/rag]] — RAG 개념, 할루시네이션 감소 + 최신성 확보
- **updated:**
  - wiki/index.md — 총 39개 페이지
- **summary:** 1장 JSON 구조 설명 중 자연스럽게 LLM 내부 구조(파라미터/임베딩/RAG)로 확장. 대학교 도서관 비유로 RAG 개념 체화.

### 00:00 — ingest: 시스템 설계 면접 스터디 플랜 수립
- **source:** `sources/2026-04-14-system-design-interview-v1.md`
- **created:**
  - [[projects/study-system-design-interview]] — 시스템 설계 면접 스터디 플랜 (4 Phase, 15챕터)
- **updated:**
  - wiki/index.md — 총 37개 페이지
- **summary:** "가상 면접 사례로 배우는 대규모 시스템 설계 기초" 스터디 시작. 질문→설명→위키 저장 방식으로 진행. 4개 Phase로 챕터 구성, 핵심 키워드 사전 정리.

## 2026-04-13

### 21:00 — ingest: AI 웹툰 제작 워크플로우 탐색 세션
- **source:** `sources/2026-04-13-ai-webtoon-workflow.md` (세션 기록)
- **created:**
  - [[sources/2026-04-13-ai-webtoon-workflow]] — AI 웹툰 도구 탐색 및 프롬프트 작성 세션
  - [[topics/ai-webtoon-creation]] — AI 인스타툰 제작 워크플로우 토픽
- **updated:**
  - wiki/index.md — 총 34개 페이지
- **summary:** fal.ai 대안 탐색으로 시작. marigold.in.bloom·darongtoon·_intotheblu 3개 계정 분석. AI 웹툰 핵심 과제(캐릭터 일관성) 정리. 민성+건승 캐릭터 시트 2종 확보. ChatGPT·Midjourney Niji 6용 프롬프트 완성.

### 17:10 — file-answer: 캐릭터 프로필 초안 저장
- **source:** 대화에서 생성된 캐릭터 소개 텍스트 (이미지 첨부)
- **created:**
  - [[projects/character-intro-draft]] — devsurvivallog 콘텐츠용 캐릭터 소개 초안
- **updated:**
  - wiki/index.md — 총 32개 페이지
- **summary:** 민성·건승 캐릭터 프로필 초안을 별도 프로젝트 파일로 저장. 향후 인스타그램/블로그 포스팅 초안으로 활용 예정.

### 17:00 — file-answer: 민성 & 건승 캐릭터 프로필
- **source:** 인스타그램 @_intotheblu 포스트 분석 (대화)
- **created:**
  - [[entities/minsung]] — devsurvivallog 운영자 캐릭터 프로필
  - [[entities/gunseung]] — 민성의 치즈 태비 고양이 캐릭터 프로필
- **updated:**
  - wiki/index.md — 총 31개 페이지
- **summary:** @_intotheblu 인스타그램 포스트 분석 후 민성(Minsung) 캐릭터와 고양이 건승(치즈 태비) 프로필 저장. 외형·성격·목소리 스타일·세계관 포함.

## 2026-04-13

### 16:00 — file-answer: Wiki 정형화/자동화 vs 마크다운
- **source:** 대화 답변 (wiki:query 결과)
- **created:**
  - [[topics/wiki-markdown-vs-graph-db]] — LLM에 맞는 위키 설계 판단
- **updated:**
  - [[concepts/llm-wiki-pattern]] — 역링크 추가
  - wiki/index.md — 총 32개 페이지
- **summary:** "정형화/자동화 vs 마크다운" 설계 질문에 대한 답변 저장. 마크다운이 LLM 네이티브 포맷이며, Claude + 마크다운이 이미 Context Graph 자동화를 대체한다는 판단 기록.

### 15:30 — file-answer: Context Graph Extraction 작업
- **source:** 대화 답변 (wiki:query 결과)
- **created:**
  - [[concepts/context-graph-extraction]] — CG 구축 전처리 단계 개념
- **updated:**
  - [[concepts/cgr3]] — extraction 역링크 추가
  - wiki/index.md — 총 31개 페이지
- **summary:** "Extraction 작업이란?" 질문 답변을 저장. 기존 삼중항 KG에서 Sentence-BERT로 Wikipedia 맥락 문장을 추출하여 (h,r,t)→(h,r,t,rc)로 변환하는 CG 구축 단계 정리.

### 15:00 — ingest: Context Graph 멀티소스 (velog + arXiv + Medium × 2)
- **source:**
  - https://velog.io/@cathx618/논문리뷰-Context-Graph
  - https://arxiv.org/abs/2406.11160
  - https://medium.com/neuralnotions/... (paywall)
  - https://medium.com/modelmind/... (paywall, 참조 링크)
- **created:**
  - [[sources/2026-04-13-velog-context-graph-review]] — 한국어 논문 리뷰
  - [[sources/2026-04-13-arxiv-2406-11160-context-graph]] — 원 논문 상세
  - [[sources/2026-04-13-medium-modelmind-context-graphs]] — ModelMind 인트로
  - [[concepts/cgr3]] — CGR³ (Retrieve-Rank-Reason) 패러다임
  - [[concepts/knowledge-graph-completion]] — KGC 태스크 개념
- **updated:**
  - [[concepts/context-graph]] — 논문 기반 학술 정의, CGR³ 링크, 출처 확장
  - [[concepts/knowledge-graph]] — KGC/CGR³ 역링크 추가
  - wiki/index.md — 6개 신규 페이지 추가, 총 30개
- **summary:** arXiv 논문(Xu et al. 2024)의 Context Graph/CGR³ 개념 인제스트. triple (h,r,t) → (h,r,t,rc) 확장, KGC에서 최대 +66% Hits@1, KGQA에서 +43.6% 달성. 참조된 velog 리뷰와 Medium 글도 함께 수집.

### 14:00 — ingest: Context Graph vs Knowledge Graph (Atlan)
- **source:** https://atlan.com/know/context-graph-vs-knowledge-graph/
- **created:**
  - [[sources/2026-04-13-context-graph-vs-knowledge-graph]] — 원본 소스 요약
  - [[concepts/context-graph]] — Context Graph 개념 페이지
  - [[concepts/knowledge-graph]] — Knowledge Graph 개념 페이지
- **updated:**
  - [[concepts/llm-wiki-pattern]] — context-graph 역링크 추가
  - wiki/index.md — 3개 신규 페이지 추가, 총 24개 페이지
- **summary:** Atlan 아티클에서 Context Graph(Knowledge Graph + 운영 메타데이터)와 Knowledge Graph의 차이를 인제스트. AI 할루시네이션 40% 감소, 의사결정 추적, 시간적 맥락 등 핵심 개념 정리.

### 00:00 — file-answer: 암묵지 (Tacit Knowledge)
- **source:** 대화 답변 (wiki:query 결과)
- **created:**
  - [[concepts/tacit-knowledge]] — AI 시대 암묵지 개념 정의
- **updated:**
  - [[concepts/rlvr]] — tacit-knowledge 역링크 추가
  - [[topics/ai-era-survival]] — tacit-knowledge 역링크 추가
  - wiki/index.md — tacit-knowledge 추가, 총 21개 페이지
- **summary:** "AI 시대 암묵지란?"에 대한 답변을 concepts/tacit-knowledge.md로 저장. RLVR과의 관계, 암묵지의 4가지 유형 정리.

## 2026-04-12

### 18:10 — ingest: Obsidian 다크모드 설정 대화
- **source:** 현재 대화 (인라인 텍스트)
- **created:**
  - [[entities/obsidian]] — Obsidian 엔티티 (다크모드 설정 팁 포함)
- **updated:**
  - wiki/index.md — obsidian 엔티티 추가, 총 20개 페이지
- **summary:** Obsidian 다크모드 켜는 3가지 방법(설정 메뉴, 하단 아이콘, 명령 팔레트)을 인제스트. Obsidian 엔티티 페이지 신규 생성.

### 17:45 — ingest: ai-survival-log-site 블로그 포스트 4편

- **source:** `ai-survival-log-site/content/posts/` (4개 포스트)
- **created:**
  - [[sources/2026-04-09-ecc-complete-guide]] — ECC 완전 가이드 소스 요약
  - [[sources/2026-04-10-why-ai-survival-log]] — 항해일지 블로그 시작 소스 요약
  - [[sources/2026-04-11-devsurvivallog-philosophy]] — devsurvivallog 철학 소스 요약
  - [[sources/2026-04-12-ai-unbundle-myself]] — AI 해체 소스 요약
  - [[entities/devsurvivallog]] — devsurvivallog 블로그 엔티티
  - [[concepts/rlvr]] — RLVR 개념
  - [[concepts/ai-unbundling]] — AI Unbundling/Bundle Theory
  - [[concepts/red-queen-effect]] — 붉은 여왕 가설
  - [[concepts/ralph-loop]] — Ralph Loop (diversification → selection → amplification)
- **updated:**
  - [[topics/ai-era-survival]] — RLVR, Unbundling, Ralph Loop 섹션 추가
  - wiki/index.md — 9개 신규 페이지 반영, 총 19개 페이지
- **summary:** ai-survival-log-site의 블로그 포스트 4편을 인제스트. 소스 요약 4개, 신규 엔티티 1개, 신규 개념 4개 생성. 총 9개 페이지 추가.

## 2026-04-24

### 23:55 — project: company-wiki 내부 구조 설계

- **created:**
  - [[projects/company-wiki-internal-structure]]
- **updated:**
  - [[projects/dual-domain-agent-operating-model]]
  - [[projects/workspace-folder-structure-review-sheet]]
  - wiki/index.md
- **summary:** `company-wiki`를 회사 도메인 authoring source로 고정하고, `meetings / projects / planning / reviews / testing` 중심의 내부 구조, page type, `company-assistant-ops` handoff 규칙, 2-agent cross-validation 적용 범위를 문서화.

### 23:58 — project: company-assistant-ops 내부 구조 설계

- **created:**
  - [[projects/company-assistant-ops-internal-structure]]
- **updated:**
  - [[projects/assistant-ops-lane-execution-draft]]
  - [[projects/dual-domain-agent-operating-model]]
  - [[projects/workspace-folder-structure-review-sheet]]
  - wiki/index.md
- **summary:** `company-assistant-ops`를 회사 도메인 외부 실행 surface로 고정하고, `actions / approvals / audit / adapters / state` 중심의 내부 구조, read/suggest/write 계층, approval/audit 원칙, `company-wiki` handoff 규칙을 문서화.

### 23:59 — project: 회사 도메인 템플릿 세트 초안

- **created:**
  - [[projects/company-domain-template-set]]
- **updated:**
  - [[projects/company-wiki-internal-structure]]
  - [[projects/company-assistant-ops-internal-structure]]
  - [[projects/workspace-folder-structure-review-sheet]]
  - wiki/index.md
- **summary:** `company-wiki`용 `meeting-note / cross-review-report / test-plan`과 `company-assistant-ops`용 `approval-record / execution-report / calendar-request` 등 핵심 템플릿 구조와 handoff 최소 필드를 한 문서로 고정.

### 2026-04-24 23:59:30+09:00 — project: 회사 도메인 review/checklist 운영 규칙

- **created:**
  - [[projects/company-domain-review-checklist-operations]]
- **updated:**
  - [[projects/company-domain-template-set]]
  - [[projects/workspace-folder-structure-review-sheet]]
  - wiki/index.md
- **summary:** 회사 도메인 공식 검수 게이트를 `문서성 변경 / 구조·정책 변경 / 실행·외부 시스템 변경`으로 나누고, primary/secondary review, checklist 묶음, severity(`warn/block/escalate`)와 anti-pattern을 운영 규칙으로 고정.

### 2026-04-25 00:02:00+09:00 — project: 회사 Assistant dry-run / materialize / approval matrix

- **created:**
  - [[projects/company-assistant-dry-run-scenarios]]
  - [[projects/company-domain-template-materialization-plan]]
  - [[projects/company-assistant-approval-matrix]]
- **updated:**
  - [[projects/company-domain-review-checklist-operations]]
  - [[projects/workspace-folder-structure-review-sheet]]
  - wiki/index.md
- **summary:** 회사 assistant workflow를 실제 실행 전 검증하기 위한 dry-run 시나리오 4개를 정의하고, 템플릿 materialize 순서와 Gmail/Calendar/Sheets 승인 레벨(Level 0~3) 세부안을 고정.

### 2026-04-25 00:05:00+09:00 — project: bootstrap / migration 준비

- **created:**
  - [[projects/company-domain-repo-bootstrap-plan]]
  - [[projects/shared-agent-harness-migration-list]]
- **updated:**
  - [[projects/workspace-folder-structure-review-sheet]]
  - wiki/index.md
- **summary:** 실제 `company-wiki`, `company-assistant-ops`, `shared-agent-harness` 생성에 필요한 초기 파일 세트와 생성 순서를 bootstrap 계획으로 고정하고, `shared-agent-harness`로 옮길 공용 설계 문서 1차/2차 후보를 분리해 정리.

### 2026-04-25 00:10:00+09:00 — bootstrap: 회사/공용 저장소 실제 생성

- **created (workspace):**
  - `~/workspace/claude/company-wiki`
  - `~/workspace/claude/company-assistant-ops`
  - `~/workspace/claude/shared-agent-harness`
- **summary:** 세 저장소의 실제 폴더와 Phase 1 초기 파일 세트 생성 완료. 루트 문서, 핵심 템플릿, 공용 lane/role 문서까지 bootstrap했으며, `git init`, 회사 git identity 연결, credential/OAuth 연결은 의도적으로 보류.

### 2026-04-25 00:18:00+09:00 — policy: 회사 프로젝트 개시 전 필수 게이트 고정

- **updated:**
  - [[projects/workspace-security-boundary]]
  - [[projects/company-domain-repo-bootstrap-plan]]
  - [[projects/workspace-folder-structure-review-sheet]]
  - wiki/index.md
- **summary:** `company-wiki`, `company-assistant-ops`는 실제 업무 시작 전 반드시 `git init -> includeIf 기반 회사 git identity -> pre-commit(user.email + secret scan)` 3단계를 완료해야 한다는 필수 게이트를 고정. 현재 상태는 `bootstrapped but not operational`.

### 2026-04-25 00:15:00+09:00 — migration: shared-agent-harness 1차 시작

- **updated (workspace):**
  - `~/workspace/claude/shared-agent-harness/ARCHITECTURE.md`
  - `~/workspace/claude/shared-agent-harness/docs/operating/operations.md`
  - `~/workspace/claude/shared-agent-harness/lanes/planning-lane.md`
  - `~/workspace/claude/shared-agent-harness/roles/planning-agent.md`
- **updated (wiki):**
  - [[projects/shared-agent-harness-migration-list]]
  - [[projects/company-domain-repo-bootstrap-plan]]
  - [[projects/workspace-folder-structure-review-sheet]]
  - wiki/index.md
- **summary:** `shared-agent-harness` placeholder 문서 중 `architecture / operations / planning-lane / planning-agent`를 공용 설계 요약으로 1차 이주 시작. source-of-truth는 여전히 현재 위키 문서에 남겨 두고, shared 저장소는 실행 가능한 공용 운영 레이어로 먼저 채우는 방식으로 진행.

### 2026-04-25 00:22:00+09:00 — migration: shared-agent-harness review / engineering 확장

- **updated (workspace):**
  - `~/workspace/claude/shared-agent-harness/lanes/review-lane.md`
  - `~/workspace/claude/shared-agent-harness/roles/review-agent.md`
  - `~/workspace/claude/shared-agent-harness/lanes/engineering-lane.md`
  - `~/workspace/claude/shared-agent-harness/roles/engineering-agent.md`
- **updated (wiki):**
  - [[projects/shared-agent-harness-migration-list]]
  - [[projects/company-domain-repo-bootstrap-plan]]
  - [[projects/workspace-folder-structure-review-sheet]]
  - wiki/index.md
- **summary:** `shared-agent-harness` 1차 이주를 `review-lane / review-agent / engineering-lane / engineering-agent`까지 확장. 공식 검수 게이트, 교차검증 원칙, engineering 실행 경계가 shared 저장소 쪽에도 실제 파일로 반영됨.

### 2026-04-25 00:26:00+09:00 — migration: shared-agent-harness research 확장

- **updated (workspace):**
  - `~/workspace/claude/shared-agent-harness/lanes/research-lane.md`
  - `~/workspace/claude/shared-agent-harness/roles/research-agent.md`
- **updated (wiki):**
  - [[projects/shared-agent-harness-migration-list]]
  - [[projects/company-domain-repo-bootstrap-plan]]
  - [[projects/workspace-folder-structure-review-sheet]]
  - wiki/index.md
- **summary:** `shared-agent-harness` 1차 이주를 `research-lane / research-agent`까지 확장. 웹서핑, 1차 출처 수집, 최신 정보 검증, planning/authoring handoff를 shared 정의로 옮기고 회사 도메인에서는 더 강한 source/security 제약을 둔다는 점을 명시.

### 2026-04-25 00:31:00+09:00 — migration: shared-agent-harness cross-validation / templates / commands / skills 확장

- **updated (workspace):**
  - `~/workspace/claude/shared-agent-harness/docs/operating/cross-validation-policy.md`
  - `~/workspace/claude/shared-agent-harness/docs/templates/review-checklist.md`
  - `~/workspace/claude/shared-agent-harness/docs/templates/cross-review-report.md`
  - `~/workspace/claude/shared-agent-harness/docs/templates/assistant-action-report.md`
  - `~/workspace/claude/shared-agent-harness/commands/planning/new-brief.md`
  - `~/workspace/claude/shared-agent-harness/commands/review/run-cross-validation.md`
  - `~/workspace/claude/shared-agent-harness/commands/engineering/execute-validated-task.md`
  - `~/workspace/claude/shared-agent-harness/commands/research/collect-sources.md`
  - `~/workspace/claude/shared-agent-harness/skills/planning/README.md`
  - `~/workspace/claude/shared-agent-harness/skills/review/README.md`
  - `~/workspace/claude/shared-agent-harness/skills/engineering/README.md`
  - `~/workspace/claude/shared-agent-harness/skills/research/README.md`
- **updated (wiki):**
  - [[projects/shared-agent-harness-migration-list]]
  - [[projects/company-domain-repo-bootstrap-plan]]
  - [[projects/workspace-folder-structure-review-sheet]]
  - wiki/index.md
- **summary:** `shared-agent-harness`의 공용 운영 레이어를 `cross-validation-policy`, review 템플릿, assistant action report 템플릿, planning/review/engineering/research command reference, skill reference 수준까지 확장. 이제 placeholder를 넘어 shared 운영 레퍼런스 저장소로 기능하기 시작함.

### 2026-04-25 00:36:00+09:00 — migration: shared-agent-harness top-level / operating / ADR 보강

- **updated (workspace):**
  - `~/workspace/claude/shared-agent-harness/README.md`
  - `~/workspace/claude/shared-agent-harness/AGENTS.md`
  - `~/workspace/claude/shared-agent-harness/docs/operating/domain-context-policy.md`
  - `~/workspace/claude/shared-agent-harness/docs/operating/approval-matrix.md`
  - `~/workspace/claude/shared-agent-harness/docs/operating/validation-matrix.md`
  - `~/workspace/claude/shared-agent-harness/docs/adr/0001-shared-harness-separates-rules-from-domain-data.md`
  - `~/workspace/claude/shared-agent-harness/docs/adr/0002-cross-validation-prefers-surface-variance.md`
  - `~/workspace/claude/shared-agent-harness/docs/adr/0003-domain-context-must-be-explicit.md`
- **updated (wiki):**
  - [[projects/shared-agent-harness-migration-list]]
  - [[projects/company-domain-repo-bootstrap-plan]]
  - [[projects/workspace-folder-structure-review-sheet]]
  - wiki/index.md
- **summary:** `shared-agent-harness`의 상위 문서와 operating/ADR 레이어를 보강. 이제 shared 저장소가 역할/레이어 정의뿐 아니라 공용 경계 원칙, approval 개념, validation 기대치, ADR까지 갖춘 참조 저장소로 정리됨.

### 2026-04-25 00:41:00+09:00 — migration: shared-agent-harness remaining shared principles 분리

- **updated (workspace):**
  - `~/workspace/claude/shared-agent-harness/docs/operating/adoption-strategy.md`
  - `~/workspace/claude/shared-agent-harness/docs/operating/stop-conditions.md`
  - `~/workspace/claude/shared-agent-harness/docs/operating/workflow-gates.md`
- **updated (wiki):**
  - [[projects/shared-agent-harness-migration-list]]
  - [[projects/company-domain-repo-bootstrap-plan]]
  - [[projects/workspace-folder-structure-review-sheet]]
  - wiki/index.md
- **summary:** `managed-agent-harness-draft`에 남아 있던 공용 원칙 중 `다중 persona, 단일 런타임으로 시작`, `강한 중단 조건`, `공용 workflow gate 흐름`을 shared 저장소 operating 문서로 분리. 이로써 1차 공용 원칙 이주는 사실상 닫힌 상태가 됨.

### 2026-04-25 00:48:00+09:00 — review: shared-agent-harness 1차 설계 검토

- **created:**
  - [[projects/shared-harness-phase1-review-2026-04-25]]
- **updated:**
  - wiki/index.md
- **summary:** `shared-agent-harness` 1차 이주와 company bootstrap 상태를 디렉터/기획자/엔지니어/검수자 관점으로 검토. 핵심 이슈는 `company-wiki`, `company-assistant-ops` 로컬 문서에 `not operational` 게이트가 빠진 점(`block`), 로컬 approval matrix 상세 부족(`warn`), shared command/skill이 아직 reference임이 충분히 표시되지 않은 점(`warn`).

### 2026-04-25 01:02:00+09:00 — review: shared-agent-harness 합동 최종 검수 보강

- **updated:**
  - [[projects/shared-harness-phase1-review-2026-04-25]]
  - wiki/index.md
- **summary:** 기존 검토 문서를 `디렉터/기획자/엔지니어/검수자` 합동 회의 형식으로 보강. `usable with 1 blocking issue` 최종 판정, 단계별 회의 메모, 역할별 최종 의견, `shared-agent-harness usable / company repos bootstrapped but not operational` 상태 구분을 명시함.

### 2026-04-25 01:10:00+09:00 — fix: company 로컬 저장소 운영 금지 게이트 반영

- **updated (workspace):**
  - `~/workspace/claude/company-wiki/README.md`
  - `~/workspace/claude/company-wiki/AGENTS.md`
  - `~/workspace/claude/company-assistant-ops/README.md`
  - `~/workspace/claude/company-assistant-ops/AGENTS.md`
- **updated (wiki):**
  - [[projects/shared-harness-phase1-review-2026-04-25]]
  - wiki/index.md
- **summary:** 회사 로컬 저장소 문서에도 `bootstrapped but not operational` 게이트를 직접 반영. 이에 따라 합동 최종 검수 문서의 초기 `block` 이슈는 해소되었고, 남은 이슈는 로컬 approval matrix 상세화와 shared command/skill의 `reference-only` 표기 두 가지 `warn`으로 정리됨.

### 2026-04-25 01:18:00+09:00 — fix: 남은 review warning 2건 수리

- **updated (workspace):**
  - `~/workspace/claude/company-assistant-ops/docs/operating/approval-matrix.md`
  - `~/workspace/claude/shared-agent-harness/commands/planning/new-brief.md`
  - `~/workspace/claude/shared-agent-harness/commands/review/run-cross-validation.md`
  - `~/workspace/claude/shared-agent-harness/commands/engineering/execute-validated-task.md`
  - `~/workspace/claude/shared-agent-harness/commands/research/collect-sources.md`
  - `~/workspace/claude/shared-agent-harness/skills/planning/README.md`
  - `~/workspace/claude/shared-agent-harness/skills/review/README.md`
  - `~/workspace/claude/shared-agent-harness/skills/engineering/README.md`
  - `~/workspace/claude/shared-agent-harness/skills/research/README.md`
- **updated (wiki):**
  - [[projects/shared-harness-phase1-review-2026-04-25]]
  - wiki/index.md
- **summary:** `company-assistant-ops` 로컬 approval matrix에 Gmail/Calendar/Sheets 액션별 레벨, block/escalate 조건을 추가하고, `shared-agent-harness` command/skill 문서에 `reference-only` 상태를 명시. 이에 따라 1차 합동 최종 검수의 남은 `warn` 2건도 수리되어 review를 닫을 수 있는 상태가 됨.

### 2026-04-25 01:32:00+09:00 — phase: shared-agent-harness executable surface 1차 전환

- **created (wiki):**
  - [[projects/shared-agent-harness-executable-surface-phase1]]
- **updated (workspace):**
  - `~/workspace/claude/shared-agent-harness/README.md`
  - `~/workspace/claude/shared-agent-harness/AGENTS.md`
  - `~/workspace/claude/shared-agent-harness/ARCHITECTURE.md`
  - `~/workspace/claude/shared-agent-harness/commands/planning/new-brief.md`
  - `~/workspace/claude/shared-agent-harness/commands/review/run-cross-validation.md`
  - `~/workspace/claude/shared-agent-harness/commands/research/collect-sources.md`
  - `~/workspace/claude/shared-agent-harness/commands/engineering/execute-validated-task.md`
  - `~/workspace/claude/shared-agent-harness/docs/templates/source-bundle.md`
  - `~/workspace/claude/shared-agent-harness/docs/templates/execution-record.md`
  - `~/workspace/claude/shared-agent-harness/scripts/harness.py`
  - `~/workspace/claude/shared-agent-harness/tests/test_harness.py`
  - `~/workspace/claude/shared-agent-harness/examples/smoke-planning-brief.md`
  - `~/workspace/claude/shared-agent-harness/examples/smoke-cross-review.md`
  - `~/workspace/claude/shared-agent-harness/examples/smoke-source-bundle.md`
  - `~/workspace/claude/shared-agent-harness/examples/smoke-execution-record.md`
- **updated (wiki):**
  - [[projects/shared-agent-harness-internal-structure]]
  - [[projects/shared-agent-harness-migration-list]]
  - wiki/index.md
- **summary:** `shared-agent-harness`를 reference repository에서 최소 executable surface로 전환. 현재 실행 범위는 `scripts/harness.py`를 통한 planning brief, cross-review report, source bundle, execution record의 안전한 artifact 생성으로 제한되며, domain source-of-truth 수정과 외부 시스템 write는 여전히 열지 않음.

### 2026-04-25 01:41:00+09:00 — gate: shared-agent-harness executable review gate 고정

- **created (wiki):**
  - [[projects/shared-agent-harness-executable-review-gate]]
- **updated (workspace):**
  - `~/workspace/claude/shared-agent-harness/docs/operating/executable-surface-gate.md`
  - `~/workspace/claude/shared-agent-harness/examples/smoke-executable-gate-review.md`
- **updated (wiki):**
  - [[projects/shared-agent-harness-executable-surface-phase1]]
  - [[projects/shared-agent-harness-migration-list]]
  - wiki/index.md
- **summary:** `shared-agent-harness`의 executable surface 확장 전에 적용할 review gate를 shared repo와 upstream wiki 양쪽에 고정. 현재 허용 범위는 `safe artifact generation`으로 한정하고, domain write/credential/external action은 자동 `escalate` 대상으로 분류함.

### 2026-04-25 01:49:00+09:00 — review: shared-agent-harness executable surface 코드 검토

- **created (wiki):**
  - [[projects/shared-harness-executable-surface-review-2026-04-25]]
- **updated:**
  - wiki/index.md
- **summary:** executable surface 1차 전환 직후 `scripts/harness.py`와 테스트를 코드 기준으로 검토. 핵심 이슈는 `--output` 경로가 unrestricted라 shared harness가 여전히 domain repo를 직접 쓸 수 있다는 점(`block`), `--domain`이 기본값 `unspecified`인 점(`warn`), negative test 부재(`warn`)로 정리됨.

### 2026-04-25 02:00:00+09:00 — fix: executable surface 경계 강제와 negative test 추가

- **updated (workspace):**
  - `~/workspace/claude/shared-agent-harness/scripts/harness.py`
  - `~/workspace/claude/shared-agent-harness/tests/test_harness.py`
  - `~/workspace/claude/shared-agent-harness/commands/planning/new-brief.md`
  - `~/workspace/claude/shared-agent-harness/commands/review/run-cross-validation.md`
  - `~/workspace/claude/shared-agent-harness/commands/research/collect-sources.md`
  - `~/workspace/claude/shared-agent-harness/commands/engineering/execute-validated-task.md`
- **updated (wiki):**
  - [[projects/shared-harness-executable-surface-review-2026-04-25]]
  - [[projects/shared-agent-harness-executable-surface-phase1]]
  - wiki/index.md
- **summary:** `scripts/harness.py`에 shared 내부 artifact 루트만 허용하는 output-path guard와 required domain validation을 추가하고, domain repo write 차단 / missing domain / invalid domain negative test를 보강. executable surface 1차 전환의 문서-구현 경계가 이제 기본적으로 일치하도록 정리됨.

### 15:00 — init: 위키 초기화

- **action:** Karpathy LLM Wiki 패턴으로 프로젝트 구조 전환
- **created:**
  - `wiki/index.md`, `wiki/log.md`
  - [[entities/claude-code]], [[entities/ecc]], [[entities/superpowers]]
  - [[concepts/ax-ai-transformation]], [[concepts/ai-capability-overhang]], [[concepts/llm-wiki-pattern]]
  - [[topics/ai-era-survival]]
  - [[projects/blog-ai-study-site]]
- **migrated:** `docs/` → `wiki/` (기존 5개 문서 마이그레이션)
  - `docs/ecc-complete-guide-ko.md` → `wiki/entities/ecc.md`
  - `docs/superpowers-complete-guide-ko.md` → `wiki/entities/superpowers.md`
  - `docs/2026-04-10-writing-first.md` → `wiki/topics/ai-era-survival.md` + 개념 2개
  - `docs/superpowers/specs/` + `plans/` → `wiki/projects/blog-ai-study-site.md`
- **summary:** Phase 1 스캐폴딩(CLAUDE.md, 디렉토리, 커맨드 5종) + Phase 2 마이그레이션 완료. 총 10개 위키 페이지 생성.
