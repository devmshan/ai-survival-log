---
title: "Wiki Log"
---

# Wiki Log

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
  - [[wiki/index]] — 프로젝트 1개 추가, 총 72개 페이지
- **summary:** Claude가 작성한 구조 변경 계획서를 Codex가 실제 저장소 상태·테스트·계약 문서와 교차 검증. `docs/images → raw/assets` 충돌 발견 후 `assets/` 채널별 구조로 해결. human-first wiki 원칙 합의, future RAG는 별도 예정 프로젝트로 분리.

### 14:00 — edit: 레포 폴더 구조 리팩토링 계획 문서화
- **created:**
  - [[projects/repo-structure-refactor]] — raw/ 타입별 분류, wiki/syntheses/ 추가, output/ 멀티채널 구조화 계획
- **updated:**
  - [[wiki/index.md]] — projects 1개 추가, 총 71개 페이지
- **summary:** sources/→raw/, wiki/syntheses/ 신규, output/ 멀티채널 구조화를 위한 리팩토링 계획을 프로젝트 페이지로 문서화. 구현 전 계획 단계.
- **note:** 이 계획서는 이후 Codex 검증 세션([[sources/2026-04-18-claude-plan-codex-validation]])을 거쳐 최종 확정됨.

### 10:20 — file-answer: canonical URL 개념 설명 위키 저장
- **created:**
  - [[concepts/canonical-url]] — 대표 URL 지정, 중복 URL 완화, 블로그 SEO 맥락 정리
- **updated:**
  - [[projects/site-seo-foundation-and-content-rewrite]] — canonical 개념 링크 추가
  - [[wiki/index.md]] — concepts 1개 추가, 총 70개 페이지
- **summary:** SEO 대화 중 나온 canonical 개념을 별도 concept 페이지로 저장. 대표 URL 의미, 중복 URL 완화 역할, 이 프로젝트의 site SEO 정비와의 연결을 함께 정리.

### 01:30 — file-answer: site SEO foundation + 전체 포스트 리라이트 작업 위키 저장
- **created:**
  - [[projects/site-seo-foundation-and-content-rewrite]] — 기술 SEO, 콘텐츠 SEO 가이드, Search Console 제출, 전체 포스트 리라이트를 한 번에 정리한 프로젝트 페이지
- **updated:**
  - [[projects/blog-ai-study-site]] — site 현재 구현/운영 상태, 기술 SEO/리라이트 반영
  - [[wiki/index.md]] — 프로젝트 1개 추가, 총 69개 페이지
- **summary:** `ai-survival-log-site`에서 진행한 SEO 기반 정비, `content/posts` 전체 1차 리라이트, content SEO writing guide 도입, Search Console 도메인 인증 및 sitemap 제출, 초기 색인 요청까지의 흐름을 upstream wiki에 durable context로 정리.

## 2026-04-17

### 18:10 — file-answer: 개발자 자동화 실습 01 PR summary 블로그 글 작성
- **created:**
  - [[topics/developer-automation-lab-01-pr-summary]] — PR summary 학습과 실제 PR 실습 기록
- **updated:**
  - [[concepts/pr-summary]] — 시리즈 글 역링크 추가
  - [[projects/cross-repo-ai-automation-lab]] — 관련 토픽 링크 추가
  - [[wiki/index.md]] — topic 1개 추가 예정
- **summary:** 오늘의 PR summary 학습 흐름과 실제 GitHub PR 코멘트 실습, LLM 확장 보류 판단까지 한 편의 발행용 글로 정리. `개발자 자동화 실습` 시리즈의 1편으로 작성.

### 16:30 — file-answer: PR summary 개념 설명 위키 저장
- **created:**
  - [[concepts/pr-summary]] — PR summary의 목적, 동작 방식, 역할별 활용 정리
- **updated:**
  - [[concepts/pull-request]] — PR summary 관련 페이지 링크 추가
  - [[wiki/index.md]] — concepts 1개 추가, 총 67개 페이지
- **summary:** 대화에서 정리한 PR summary 설명을 concepts/pr-summary.md로 저장. PR 자동 코멘트의 목적, PR 작성 전 로컬 사전 점검, 작성자/리뷰어/maintainer 관점을 함께 정리.

### 14:00 — file-answer: .mjs 파일과 Shebang 개념 위키 저장
- **created:**
  - [[concepts/es-module-mjs]] — ES Module, .mjs 파일 형식, CommonJS vs ESM 비교
  - [[concepts/shebang]] — #! 문자열, 인터프리터 지시, /usr/bin/env 패턴
- **updated:**
  - [[wiki/index.md]] — concepts 2개 추가, 총 66개 페이지
- **summary:** 대화에서 생성된 .mjs 파일과 shebang 설명을 각각 wiki/concepts/에 저장. 두 페이지 간 상호 크로스 레퍼런스 추가.

### 10:00 — file-answer: Pull Request 개념 설명 위키 저장
- **created:**
  - [[concepts/pull-request]] — PR 개념, 흐름, 리뷰 방식, CI 연동, PR summary 자동화 연결
- **updated:**
  - [[projects/cross-repo-ai-automation-lab]] — pull-request 역링크 추가
  - [[wiki/index.md]] — concepts 1개 추가, 총 64개 페이지
- **summary:** 대화에서 생성된 PR 설명 답변을 wiki/concepts/pull-request.md로 저장. PR 기본 흐름, 리뷰 유형, CI/CD 연동, PR summary 자동화와의 연결까지 포함.

## 2026-04-16

### 12:00 — file-answer: PR summary 실습 결과 학습 문서화 + wiki 등록
- **source:** `docs/2026-04-16-pr-summary-practice-review.md`
- **created:**
  - [[projects/cross-repo-ai-automation-lab]] — cross-repo AI 자동화 실습 프로젝트 페이지
- **updated:**
  - [[projects/blog-ai-study-site]] — cross-repo 자동화 실습 프로젝트 링크 추가
  - [[wiki/index.md]] — 프로젝트 1개 추가, 총 62개 페이지
- **summary:** PR summary 실습 결과를 공부용 문서로 재정리하고, 두 저장소 역할 차이와 축소 적용 개념을 포함한 학습 경로를 wiki project 페이지로 등록. 다음 단계인 Jira issue plan draft는 진행 예정 상태로 유지.

### 10:45 — edit: AI-Native 개발자 메모를 내부 참고자료로 재분류
- **updated:**
  - `docs/2026-04-16-ai-native-developer-study-reference.md` — 공부 계획 전 참고자료로 재정리
  - [[wiki/index.md]] — 잘못 추가한 위키 항목 제거
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
  - [[wiki/index.md]] — 총 49개 페이지
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
  - [[wiki/index.md]] — 총 39개 페이지
- **summary:** 1장 JSON 구조 설명 중 자연스럽게 LLM 내부 구조(파라미터/임베딩/RAG)로 확장. 대학교 도서관 비유로 RAG 개념 체화.

### 00:00 — ingest: 시스템 설계 면접 스터디 플랜 수립
- **source:** `sources/2026-04-14-system-design-interview-v1.md`
- **created:**
  - [[projects/study-system-design-interview]] — 시스템 설계 면접 스터디 플랜 (4 Phase, 15챕터)
- **updated:**
  - [[wiki/index.md]] — 총 37개 페이지
- **summary:** "가상 면접 사례로 배우는 대규모 시스템 설계 기초" 스터디 시작. 질문→설명→위키 저장 방식으로 진행. 4개 Phase로 챕터 구성, 핵심 키워드 사전 정리.

## 2026-04-13

### 21:00 — ingest: AI 웹툰 제작 워크플로우 탐색 세션
- **source:** `sources/2026-04-13-ai-webtoon-workflow.md` (세션 기록)
- **created:**
  - [[sources/2026-04-13-ai-webtoon-workflow]] — AI 웹툰 도구 탐색 및 프롬프트 작성 세션
  - [[topics/ai-webtoon-creation]] — AI 인스타툰 제작 워크플로우 토픽
- **updated:**
  - [[wiki/index.md]] — 총 34개 페이지
- **summary:** fal.ai 대안 탐색으로 시작. marigold.in.bloom·darongtoon·_intotheblu 3개 계정 분석. AI 웹툰 핵심 과제(캐릭터 일관성) 정리. 민성+건승 캐릭터 시트 2종 확보. ChatGPT·Midjourney Niji 6용 프롬프트 완성.

### 17:10 — file-answer: 캐릭터 프로필 초안 저장
- **source:** 대화에서 생성된 캐릭터 소개 텍스트 (이미지 첨부)
- **created:**
  - [[projects/character-intro-draft]] — devsurvivallog 콘텐츠용 캐릭터 소개 초안
- **updated:**
  - [[wiki/index.md]] — 총 32개 페이지
- **summary:** 민성·건승 캐릭터 프로필 초안을 별도 프로젝트 파일로 저장. 향후 인스타그램/블로그 포스팅 초안으로 활용 예정.

### 17:00 — file-answer: 민성 & 건승 캐릭터 프로필
- **source:** 인스타그램 @_intotheblu 포스트 분석 (대화)
- **created:**
  - [[entities/minsung]] — devsurvivallog 운영자 캐릭터 프로필
  - [[entities/gunseung]] — 민성의 치즈 태비 고양이 캐릭터 프로필
- **updated:**
  - [[wiki/index.md]] — 총 31개 페이지
- **summary:** @_intotheblu 인스타그램 포스트 분석 후 민성(Minsung) 캐릭터와 고양이 건승(치즈 태비) 프로필 저장. 외형·성격·목소리 스타일·세계관 포함.

## 2026-04-13

### 16:00 — file-answer: Wiki 정형화/자동화 vs 마크다운
- **source:** 대화 답변 (wiki:query 결과)
- **created:**
  - [[topics/wiki-markdown-vs-graph-db]] — LLM에 맞는 위키 설계 판단
- **updated:**
  - [[concepts/llm-wiki-pattern]] — 역링크 추가
  - [[wiki/index.md]] — 총 32개 페이지
- **summary:** "정형화/자동화 vs 마크다운" 설계 질문에 대한 답변 저장. 마크다운이 LLM 네이티브 포맷이며, Claude + 마크다운이 이미 Context Graph 자동화를 대체한다는 판단 기록.

### 15:30 — file-answer: Context Graph Extraction 작업
- **source:** 대화 답변 (wiki:query 결과)
- **created:**
  - [[concepts/context-graph-extraction]] — CG 구축 전처리 단계 개념
- **updated:**
  - [[concepts/cgr3]] — extraction 역링크 추가
  - [[wiki/index.md]] — 총 31개 페이지
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
  - [[wiki/index.md]] — 6개 신규 페이지 추가, 총 30개
- **summary:** arXiv 논문(Xu et al. 2024)의 Context Graph/CGR³ 개념 인제스트. triple (h,r,t) → (h,r,t,rc) 확장, KGC에서 최대 +66% Hits@1, KGQA에서 +43.6% 달성. 참조된 velog 리뷰와 Medium 글도 함께 수집.

### 14:00 — ingest: Context Graph vs Knowledge Graph (Atlan)
- **source:** https://atlan.com/know/context-graph-vs-knowledge-graph/
- **created:**
  - [[sources/2026-04-13-context-graph-vs-knowledge-graph]] — 원본 소스 요약
  - [[concepts/context-graph]] — Context Graph 개념 페이지
  - [[concepts/knowledge-graph]] — Knowledge Graph 개념 페이지
- **updated:**
  - [[concepts/llm-wiki-pattern]] — context-graph 역링크 추가
  - [[wiki/index.md]] — 3개 신규 페이지 추가, 총 24개 페이지
- **summary:** Atlan 아티클에서 Context Graph(Knowledge Graph + 운영 메타데이터)와 Knowledge Graph의 차이를 인제스트. AI 할루시네이션 40% 감소, 의사결정 추적, 시간적 맥락 등 핵심 개념 정리.

### 00:00 — file-answer: 암묵지 (Tacit Knowledge)
- **source:** 대화 답변 (wiki:query 결과)
- **created:**
  - [[concepts/tacit-knowledge]] — AI 시대 암묵지 개념 정의
- **updated:**
  - [[concepts/rlvr]] — tacit-knowledge 역링크 추가
  - [[topics/ai-era-survival]] — tacit-knowledge 역링크 추가
  - [[wiki/index.md]] — tacit-knowledge 추가, 총 21개 페이지
- **summary:** "AI 시대 암묵지란?"에 대한 답변을 concepts/tacit-knowledge.md로 저장. RLVR과의 관계, 암묵지의 4가지 유형 정리.

## 2026-04-12

### 18:10 — ingest: Obsidian 다크모드 설정 대화
- **source:** 현재 대화 (인라인 텍스트)
- **created:**
  - [[entities/obsidian]] — Obsidian 엔티티 (다크모드 설정 팁 포함)
- **updated:**
  - [[wiki/index.md]] — obsidian 엔티티 추가, 총 20개 페이지
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
  - [[wiki/index.md]] — 9개 신규 페이지 반영, 총 19개 페이지
- **summary:** ai-survival-log-site의 블로그 포스트 4편을 인제스트. 소스 요약 4개, 신규 엔티티 1개, 신규 개념 4개 생성. 총 9개 페이지 추가.

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
