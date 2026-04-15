---
title: "Backend.AI"
created: "2026-04-15"
updated: "2026-04-15"
type: entity
sources: ["[[sources/2026-04-15-ai-frontier-ep86]]"]
tags: [mlops, ai-infrastructure, lablup, open-source]
status: active
published: false
slug: ""
description: ""
---

# Backend.AI

## 개요

[[entities/lablup|Lablup]]이 개발한 AI infrastructure 운영 체제(OS). GPU 클러스터 관리, 워크로드 스케줄링, 컨테이너 기반 실행 환경을 제공한다. 연구소 및 기업 고객이 GPU 100~1,000개 규모의 ML/AI 인프라를 효율적으로 운영할 수 있도록 돕는다.

## 주요 기능

- **GPU 클러스터 관리:** 다수의 GPU 노드를 통합 관리, 자원 할당 및 모니터링
- **워크로드 스케줄링:** ML 학습, 추론 작업의 우선순위 관리 및 큐 처리
- **컨테이너 실행 환경:** Docker/Kubernetes 기반 격리된 실행 환경 제공
- **멀티 테넌트 지원:** 여러 팀/사용자가 동일 클러스터를 안전하게 공유

## Backend.AI:GO

Backend.AI의 일반 사용자 대상 파생 제품. 기존 enterprise 중심의 Backend.AI에서 핵심 컴포넌트인 Continuum 라우터를 분리해, 일반 개발자와 팀이 쓸 수 있는 로컬 AI 라우팅 도구로 재탄생했다.

### 탄생 스토리

2025년 12월 24일(크리스마스 이브), Anthropic의 토큰 2배 이벤트를 계기로 라우터 웹 UI 개발을 시작했다. llama.cpp를 자동화해 웹 UI에 넣다 보니 기능이 계속 붙었고, DeepL 구독료가 아까워지자 번역기가, 이미지 생성 필요가 생기자 그 기능도 추가되며 완전한 도구가 됐다. 내부 공유 후 "이거는 우리 대신 우리를 홍보해 줄 수 있다"는 반응으로 Backend.AI:GO라는 이름을 붙여 제품화됐다.

### 주요 기능

- **로컬 모델 관리:** Hugging Face에서 모델 검색, 다운로드, 파라미터 시각화 (양자화, KV 캐시, transformer 블록 구조)
- **llama.cpp 자동화:** 원클릭 실행, 로컬 GPU(NVIDIA/AMD) 지원
- **클라우드 API 연결:** OpenAI, Gemini, Anthropic 등 175개+ 모델 통합 관리
- **분산 라우팅:** 사무실 여러 PC를 묶어 각자 다른 모델 담당. 내 PC에서 전체를 사용하거나, 내 모델을 팀원들이 쓸 수 있게 공유
- **Circuit Breaking:** 특정 공급자 장애 시 자동 대체 라우팅, 지연 시간 모니터링
- **번역기 내장:** DeepL 구독 대체. 파일 통째로 번역 (PDF, TXT, Docs), 이미지 번역 지원
- **벤치마킹:** 모델 간 속도/품질 비교, 결과 내보내기
- **UI 테마:** Windows XP 스타일, Mac 글래스 테마 등 — "연배가 비슷한 분들이 익숙하게 느끼는" 인터페이스가 기본값

### 개발 결과

[[entities/shin-junggyu|신정규]] 대표가 [[concepts/agentic-workflow|Agentic Workflow]]로 **40일** 만에 완성.
- 소비 토큰: 약 **130억 개**
- 생성 코드: **100만 줄**
- 개발 환경: Claude Code Max 8개 VM/PC에서 병렬 구동
- 첫 공개: 2026년 1월 6일 CES

[[entities/lablup|Lablup]]이 11년간 축적한 Backend.AI 도메인 지식(수많은 설치 환경 예외 케이스, GPU 클러스터 운영 노하우)이 있었기에 가능한 속도였다.

### 자동화 개발 파이프라인

출시 후 개발도 자동화됐다:
- GitHub 이슈 → cron(15분마다) → 검증 → 개발 → 테스트 → PR → merge
- **764개 PR** 자동 처리
- AI가 자체적으로 UI 스크린샷을 분석해 개선 이슈를 발행하고, 그 이슈를 다시 자동 개발
- 이슈 해결 후 **Tech Report** 자동 생성: 기술 결정 내용 + "이 기술은 당신이 공부해야 합니다" 항목 포함

이 프로젝트는 AI 코딩이 단순 보조가 아닌 제품 개발의 주축이 될 수 있음을 보여주는 실증 사례로, [[entities/ai-frontier|AI Frontier]] EP86에서 상세히 다뤄졌다.

## 관련 페이지

- [[entities/lablup]]
- [[entities/shin-junggyu]]
- [[entities/ai-frontier]]
- [[concepts/agentic-workflow]]
- [[sources/2026-04-15-ai-frontier-ep86]]
