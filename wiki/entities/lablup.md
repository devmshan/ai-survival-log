---
title: "Lablup"
created: "2026-04-15"
updated: "2026-04-15"
type: entity
sources: ["[[sources/2026-04-15-ai-frontier-ep86]]"]
tags: [mlops, ai-infrastructure, startup, korea]
status: active
published: false
slug: ""
description: ""
---

# Lablup

## 개요

AI infrastructure 운영 플랫폼 기업. [[entities/backend-ai|Backend.AI]]의 개발사로, GPU 클러스터 기반 ML/AI 워크로드 관리 솔루션을 제공한다. 설립 11년차 (2026년 기준) 한국 스타트업. 대표 [[entities/shin-junggyu|신정규]].

## 주요 정보

| 항목 | 내용 |
|------|------|
| 설립 | 약 2015년 (2026년 기준 11년차) |
| 대표 | [[entities/shin-junggyu|신정규]] |
| 주력 제품 | [[entities/backend-ai|Backend.AI]] |
| 고객 규모 | GPU 100~1,000개 규모 enterprise |
| 주요 시장 | MLOps, AI infrastructure, 연구소/기업 GPU 클러스터 운영 |

## 사업 방향

- **핵심 비즈니스:** GPU 클러스터 운영 체제인 [[entities/backend-ai|Backend.AI]] 개발 및 공급
- **[[concepts/startup-watermill|물레방아론]] 적용:** IT 기술(GPU 클러스터 운영)과 AI/ML 도메인의 교차점에서 기회를 찾아 성장.

### 2026년 두 가지 전략적 전환

**1. AI를 위한 인터페이스로 전환 (상반기 목표)**

> "이거 과연 사람이 쓸 도구일까. 미래에도. AI가 가장 잘 다룰 수 있는 도구가 되게 하자."

사람이 CLI/GUI를 직접 조작하는 구조에서, 에이전트가 Backend.AI를 tool로 호출하는 구조로 전환 중:
- Skill 배포 (에이전트가 읽어가서 사용할 수 있는 형태)
- CLI 출력 포맷을 AI가 쉽게 이해하고 유추할 수 있도록 변경
- "GPU 몇 개, 메모리 얼마" 같은 수동 설정 대신 "이 모델 만들어줘"라고 하면 AI가 알아서 자원 할당

**2. Backend.AI 코어 자체를 모델로**

> "Backend.AI의 코어도 모델이 될 거다."

AI 자원 관리에 특화된 모델을 연구팀이 개발 중. 다음 메이저 버전에서 Backend.AI 스타트업 파이프라인 자체에 모델 런타임이 포함되는 구조를 테스트할 계획이다.

### 조직 내 AI 적응 사례

- **CFO:** Claude Code를 30분 배워 2시간 걸리던 문서 작업을 3분 안에 처리
- **콘텐츠 담당:** 1주일 만에 자기만의 harness 완성. GitHub을 직접 쓰진 못하지만 GitHub 작업용 커맨드를 스스로 만들었다
- **CTO:** 신정규 대표가 "2개월 룰"(지금 안 되면 그냥 미뤄라)을 전파했으나 한동안 저항. Claude 4.6 출시 후 직접 써보고 돈오. HWP 전체를 분해해 사내 HWP 문서 작성을 자동화했다

**2개월 룰:** "지금 AI가 잘 못한다면 그냥 미뤄라. 2개월 후엔 달라진다." 이 개념을 사내에 전파하는 게 제일 오래 걸렸다.

### 사업계획서 작성 자동화

2026년부터 사업 계획서를 사람이 직접 쓰지 않는다:
- 250개+ 참고 문서를 마크다운으로 변환
- 최신 뉴스 크롤링으로 방향성 검증
- AI가 정합성 검토, 예측 비교, 수정 제안
- CFO와 신정규 대표가 함께 사용. CFO는 코딩 불가능하지만 sync 커맨드로 commit을 직접 한다

## Agentic Workflow 실천

2026년 초, 신정규 대표는 Claude Code Max를 활용해 Backend.AI:GO를 **40일** 만에 개발. 130억 토큰, 100만 줄 코드를 사용한 이 프로젝트는 Lablup이 11년간 축적한 기술 자산 위에서 Agentic Workflow가 얼마나 강력한 가속 효과를 낼 수 있는지를 증명한 사례다.

자세한 내용: [[sources/2026-04-15-ai-frontier-ep86]]

## 관련 페이지

- [[entities/shin-junggyu]]
- [[entities/backend-ai]]
- [[entities/ai-frontier]]
- [[concepts/agentic-workflow]]
- [[concepts/startup-watermill]]
- [[sources/2026-04-15-ai-frontier-ep86]]
