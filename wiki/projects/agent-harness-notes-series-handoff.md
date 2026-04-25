---
title: "agent harness notes series handoff"
created: "2026-04-25"
updated: "2026-04-25"
type: project
sources: []
tags: [project, agent-harness, writing, series, handoff, continuation, operations]
status: active
published: false
slug: ""
description: "Agent Harness Notes 01/02의 현재 상태와 다음 작업을 한 곳에서 이어받기 위한 작업 인계 문서."
---

# Agent Harness Notes series handoff

이 문서는 `Agent Harness Notes` 시리즈의 현재 상태와 다음 작업 재개 지점을 기록한다.

## 현재 상태

- `01`은 publish 가능한 초안으로 정리됐다
- `02`는 최종 polish 1차 완료. detached workspace migration과 5개 프로젝트 구조로의 분리를 설명하는 글로 정리됐다
- 시리즈의 핵심 원칙은 `role/lane is shared, data/surface is isolated`다
- A 도메인과 B 도메인은 독립적이지만 `shared-agent-harness`를 공용 운영 레이어로 공유한다
- `02` 마지막 예고는 "Bounded Context의 시선으로 다시 읽는다"로 고정됐다

## 이번에 확보된 글감

- managed agent system을 `경계와 계약` 관점으로 읽는 서사
- `shared-agent-harness`를 detached operational source로 분리한 이유
- `operational source`와 `history source`를 다시 나누는 과정
- `Separation of Concerns`, `Bounded Context`, `Hexagonal Architecture`로 구조를 설명하는 비유

## 다음 작업

1. `Agent Harness Notes 03` 주제 확정 및 위키 초안 작성
   - 방향: **Bounded Context로 본 5개 프로젝트 구조**
   - 02 마지막 문단이 "이 구조를 Bounded Context의 시선으로 다시 읽는다"로 예고하고 있음
   - SW 엔지니어링 비유(SoC, Bounded Context, Hexagonal Architecture)를 본문 한 섹션으로 확장

## 03편 방향 (확정)

- **Bounded Context로 본 5개 프로젝트** — 02에서 만든 5개 저장소 구조를 SW 엔지니어링 프레임으로 다시 읽는 편

## 이후 편 후보 (04 또는 그 이후)

- Ports and Adapters로 본 회사 도메인 — `company-wiki`(authoring source)와 `company-assistant-ops`(execution surface)를 Ports and Adapters 비유로 풀어내는 편
- 하네스를 나눈 뒤 사람의 가치 — 하네스 분리 이후 attention/취향/판단이 더 중요해지는 이유를 다루는 에세이 편

## 관련 페이지

- [[topics/agent-harness-notes-01-dual-domain]]
- [[topics/agent-harness-notes-02-detached-workspace]]
- [[projects/detached-workspace-repo-migration-review-and-plan]]
- [[projects/shared-agent-harness-internal-structure]]
- [[projects/company-wiki-internal-structure]]
- [[projects/company-assistant-ops-internal-structure]]
