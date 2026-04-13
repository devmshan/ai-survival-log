---
title: "Wiki Log"
---

# Wiki Log

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
