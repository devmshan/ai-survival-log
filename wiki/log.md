---
title: "Wiki Log"
---

# Wiki Log

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
