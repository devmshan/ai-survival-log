---
title: "2026-04-24 — AAR, Claude Design, AI for Science, Attention Business, 하네스 설계 대화"
created: "2026-04-24"
updated: "2026-04-24"
type: source
sources: []
tags: ["managed-agents", "claude-design", "ai-for-science", "attention-business", "dual-domain", "agent-harness", "study"]
status: active
published: false
slug: ""
description: ""
---

# 2026-04-24 — AAR, Claude Design, AI for Science, Attention Business, 하네스 설계 대화

- **원본 저널**: `raw/journals/2026-04-24-managed-agent-harness-and-dual-domain-planning-conversation-backup.md` (+ part2)
- **성격**: 학습 + 설계 대화 백업 2부 구성
- **날짜**: 2026-04-24

## 주요 내용 (backup)

1. **Scaling Managed Agents** 개념 이해: agent 수보다 경계와 검증 분리가 핵심.
2. **brain-hand decoupling**: 판단하는 뇌(모델)와 실행하는 손(하네스) 분리 원칙.
3. **role/lane is shared, data/surface is isolated**: 개인/회사 이중 도메인 하네스 핵심 원칙 도출.
4. **workspace-security-boundary**: 폴더 분리만으로는 격리 불완전, 4축(File/Git/Credentials/Harness) 동시 관리 필요.

## 주요 내용 (part2)

1. **AAR/verifier/weak-to-strong**: Jan Leike의 Automated Alignment Researcher 개념과 루프 검증 조건.
2. **Claude Design**: 프론트엔드 생성-검토-수정 루프를 닫는 도구. 외부 wrapper 서비스의 value prop 흡수.
3. **AI for Science / personalized precision medicine**: 데이터→해석→표적 설계→피드백 루프를 AI가 닫는 구조.
4. **두 갈래 도망길 프레임** (외부 출처): 번역의 길 / 도메인 침투의 길. 팟캐스트와 외부 아티클 기반.
5. **attention business / 취향 / fine-tuning**: 정보 과잉 시대에 attention 배치의 총합이 개인의 가치가 된다는 논의.

## 블로그 활용

- `[[topics/professors-brain-03-closing-the-loop]]` — part2 L34-94 소재 (루프 닫기 구조)
- `[[topics/agent-harness-notes-01-dual-domain]]` — backup L14-193 소재 (하네스 설계)
- `[[topics/learning-my-own-taste-on-frontier]]` — part2 L68-145 소재 (도망길 + attention business)

## 관련 페이지

- [[topics/professors-brain-03-closing-the-loop]]
- [[topics/agent-harness-notes-01-dual-domain]]
- [[topics/learning-my-own-taste-on-frontier]]
- [[projects/managed-agent-harness-draft]]
- [[projects/dual-domain-agent-operating-model]]
