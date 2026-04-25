---
title: "Agent Harness Notes 01 — Managed Agents를 공부하다가, 왜 개인/회사 이중 도메인 하네스를 설계하게 됐나"
seoTitle: "Managed Agents 하네스 설계 — 개인/회사 이중 도메인 운영 구조 만들기"
created: "2026-04-24"
updated: "2026-04-25"
type: topic
sources: []
tags: ["agent-harness", "managed-agents", "dual-domain", "workspace-structure", "security-boundary", "claude", "operations"]
series: "Agent Harness Notes"
seriesSlug: "agent-harness-notes"
seriesOrder: 1
status: active
published: true
slug: "agent-harness-notes-01-dual-domain"
description: "Scaling Managed Agents를 공부하다가 agent 수보다 경계와 계약이 먼저라는 결론에 도달한 설계 기록. 개인/회사 이중 도메인 분리와 shared-agent-harness가 나온 맥락을 정리한다."
---

# Agent Harness Notes 01 — Managed Agents를 공부하다가, 왜 개인/회사 이중 도메인 하네스를 설계하게 됐나

처음에는 이 글이 멀티 에이전트 이야기일 거라고 생각했다.

Anthropic의 `Scaling Managed Agents`를 처음 접했을 때 머릿속에 떠오른 그림은 단순했다. Research Agent 하나, Planning Agent 하나, Engineering Agent 하나. 역할을 잘게 나누고 개수를 늘리면 더 강한 시스템이 되는 것 아닌가 하는 발상이다.

그런데 실제로 내가 붙잡게 된 건 agent의 숫자가 아니라 경계였다.

LLM이 문서와 코드, 개인 작업과 회사 작업을 한 컨텍스트 안에서 동시에 건드리기 시작하면 이 문제는 갑자기 실무가 된다. 무엇이 판단이고 무엇이 실행인지, 어떤 데이터가 개인 도메인이고 어떤 데이터가 회사 도메인인지, Claude가 무엇을 먼저 읽고 무엇을 보지 말아야 하는지. 결국 하네스 설계는 agent를 더 만드는 작업이 아니라, 섞이면 안 되는 것들을 먼저 분리하는 작업이었다.

---

## 핵심은 agent를 늘리는 게 아니라 "Managed"를 이해하는 것이었다

Managed Agents에서 핵심은 agent를 "관리"한다는 데 있었다. 더 많이 쓰는 것이 아니라.

단일 agent는 혼자 똑똑할 수 있다. 질문에 답하고, 코드를 짜고, 파일을 수정하고, 검수까지 흉내 낼 수 있다. 문제는 그 모든 것이 하나의 대화 흐름 안에 섞인다는 점이다. 판단과 실행, 검증과 기록이 한 덩어리로 움직이면 시스템은 빨라 보이지만 경계는 흐려진다.

managed agent system에서 바뀌는 것은 그 섞임이다. 모델은 판단을 돕고, 실행과 권한은 하네스가 제어하고, 검증은 다시 별도 게이트를 통과한다. 중요한 것은 더 많은 agent가 아니라 그 사이의 계약이다.

이걸 내 식으로 바꾸면 결국 `brain`과 `hand`를 나누는 구조였다. 판단하는 뇌가 직접 자원에 손을 대지 않게 만드는 것. 그게 시작점이었다.

---

## 내가 먼저 부딪힌 문제도 agent 부족이 아니라 경계 붕괴였다

이걸 이해하고 나서 내 작업 환경에 바로 적용해 보려 했다.

처음 생각은 단순했다. `ai-survival-log`에 Research Agent를 추가하고, Planning Agent를 따로 두고, Engineering Agent가 코드를 짜면 되지 않을까. agent를 더 많이 두는 방향이었다.

그런데 바로 막혔다. 그것보다 먼저 있어야 했던 것이 있었다.

[[projects/managed-agent-harness-draft]]에서 정리했던 문장이 있다.

> "핵심은 에이전트 수를 늘리는 것이 아니다. 이미 있는 경계를 강하게 지키게 만들고, 책임과 검증 지점을 먼저 분리하는 것이다."

내 작업에는 이미 흐름이 있었다.

- `raw`
- `wiki`
- `output/blog`
- `ai-survival-log-site`

문제는 이 흐름이 대화 안에서 자주 섞인다는 점이었다. 인제스트, 집필, 검토, 발행을 같은 컨텍스트 안에서 처리하면, 언뜻 빠르게 돌아가는 것처럼 보여도 어느 단계에서 무엇이 바뀌었는지 추적하기 어려워진다.

그래서 결론은 의외로 단순했다. agent를 추가하기 전에, 이미 있는 경계가 실제로 지켜지고 있는지부터 확인해야 했다. agent 수보다 계약이 먼저였다.

---

## 초안이 아니라 지금 당장 돌아가는 운영 구조가 필요했다

실제 작업으로 들어가면서 처음에는 `Planning Lane`, `Assistant Ops Lane` 같은 초안부터 잡으려 했다.

각 lane의 입력, 출력, 흐름, 분리 기준을 정리하고, 나중에 독립 agent로 분리할 수 있는 조건을 적어두는 방식이었다. 그런데 이 접근은 구조를 예쁘게 설명하는 데는 도움이 돼도, 당장 운영을 시작하는 데는 애매했다.

"나중에"가 많아질수록 시스템은 실제로는 아무것도 굴러가지 않는다.

[[projects/immediate-agent-operating-structure]]에서 방향이 바뀐 이유가 바로 그 지점이었다.

> "이 문서는 나중에 독립 agent로 분리할지 검토하는 초안이 아니라, 지금부터 바로 사용할 운영 구조를 고정한다."

계획을 실행으로 넘기는 것이 아니라, 계획 자체를 처음부터 실행 가능한 형태로 써야 했다.

프로젝트는 역할이 아니라 결과물·계약·권한 경계를 기준으로 나뉜다. 블로그 집필, 회사 기획, 코드 작업은 서로 다른 저장소와 승인 구조를 가져야 한다. 대신 Planning, Review, Engineering 같은 역할은 이 경계를 가로질러 재사용된다. 블로그 글 계획도 Planning이고, 회사 보고서 계획도 Planning이다.

이때부터 `brain`과 `hand`의 분리는 추상적인 비유가 아니라 실제 운영 구조가 되기 시작했다.

---

## 같은 역할을 두 번 만들 필요는 없었고, 데이터를 나누면 됐다

구조를 더 밀어보니 더 큰 문제가 보였다.

내 업무는 크게 두 덩어리였다.

- 개인 일상업무: 공부, wiki 수집, 블로그, 콘텐츠 제작
- 회사업무: 기획, 검수, 테스트, 회의록, 일정과 보고

둘 다 같은 workspace에 있었고, 둘 다 AI 에이전트의 도움을 받을 수 있었다. 하지만 둘은 같은 데이터 위에서 움직이면 안 됐다. 회사 보안 때문에 회사 회의록이 개인 저장소에 들어가면 안 됐고, 반대로 개인 콘텐츠 흐름이 회사 실행 계정과 섞여도 안 됐다.

그런데 여기서 중요한 질문이 하나 생겼다.

> "회사에서 쓰는 Planning, Review, Engineering의 역할과 lane은 개인 도메인에서도 그대로 써도 되지 않나?"

답은 `그렇다`였다.

Planning이 회사 전용일 이유는 없다. 블로그 기획도 Planning이고, 회사 발표자료 기획도 Planning이다. Review도 마찬가지다. 역할 자체는 도메인을 가리지 않는다.

분리해야 하는 것은 역할이 아니었다. `data`, `surface`, `account`, `permission`이었다.

그래서 [[projects/dual-domain-agent-operating-model]]에서 이 문장을 고정하게 됐다.

> `role/lane is shared, data/surface is isolated`

회사와 개인은 같은 Planning lane을 쓸 수 있다. 하지만 그 lane이 닿는 저장소, 계정, 권한은 완전히 다르다. 역할을 두 번 정의하는 것이 아니라, 하나의 역할을 서로 다른 두 surface에서 실행하는 구조다.

---

## 폴더를 나누는 것만으로는 하네스가 완성되지 않았다

workspace를 실제로 나누면서 또 하나의 착각이 깨졌다.

> "폴더 분리만으로 도메인 격리가 완성되지 않는다."

폴더를 나누는 것은 출발점일 뿐이다. 디렉토리가 다르다고 해서 데이터가 자동으로 안전해지지는 않는다.

[[projects/workspace-security-boundary]]에서 정리한 보안 경계는 네 가지였다.

- **File System**: 폴더 배치와 도메인 간 이동 금지 규칙
- **Git Identity**: 도메인별 다른 커밋 identity
- **Credentials**: API key, 토큰, 계정 정보의 분리
- **Harness Context**: Claude가 실행될 때 어떤 `CLAUDE.md`와 운영 문서를 먼저 읽는지

마지막이 특히 중요했다.

폴더가 달라도 Claude가 같은 컨텍스트로 실행되면 도메인 구분은 금방 흐려진다. 실제 경계는 파일 경로만이 아니라, 하네스가 무엇을 먼저 읽게 하느냐에서 결정된다.

그래서 최종 구조는 자연스럽게 이렇게 굳었다.

- 개인 도메인: `ai-survival-log`, `ai-survival-log-site`
- 회사 도메인: `company-wiki`, `company-assistant-ops`
- 공용 운영 레이어: `shared-agent-harness`

이건 멀티 에이전트 카탈로그를 만든 결과가 아니었다. 무엇을 공유하고 무엇을 절대 공유하지 않을지 정리한 결과였다.

---

## 결국 하네스는 Claude가 무엇을 먼저 읽게 할지 정하는 일이다

구조를 어느 정도 잡고 나서 이런 질문이 나왔다.

> "지금 계획을 클로드도 전부 확인할 수 있나요?"

이 질문이 좋았던 이유는, 하네스의 핵심을 정면으로 건드렸기 때문이다.

저장소 안에 문서를 많이 쌓아두는 것만으로는 충분하지 않다. Claude가 그 문서를 `볼 수 있는가`와 `먼저 읽는가`는 전혀 다른 문제다. 하네스는 결국 그 우선순위를 고정하는 일이다.

실행이 판단보다 앞서지 않게 하고, 판단이 올바른 도메인 문서를 먼저 읽게 하고, 검수가 계약 위에서 이뤄지게 하는 것. 그게 내가 이번 설계에서 이해한 managed agent의 실제 의미였다.

그래서 이번 글의 결론은 이렇게 정리된다.

- agent 수를 늘리는 것이 먼저가 아니었다
- 역할을 공유하되 데이터와 surface를 분리하는 것이 먼저였다
- 폴더 분리만이 아니라 context 분리가 핵심이었다
- 결국 하네스는 Claude가 무엇을 먼저 읽게 할지 정하는 구조였다

이 질문은 다음 편으로 자연스럽게 이어졌다. Claude Design과 personalized medicine을 함께 보면서, 나는 점점 `AI가 루프를 닫는다`는 말이 단지 프론트엔드 도구의 편의성이 아니라, 더 큰 설계 원리라는 쪽으로 생각이 바뀌기 시작했다.

---

## 관련 페이지

- [[topics/agent-harness-notes-02-detached-workspace]] — 왜 shared-agent-harness를 떼고, 5개 프로젝트 구조로 갔는가
- [[projects/managed-agent-harness-draft]] — 하네스 설계 출발점
- [[projects/dual-domain-agent-operating-model]] — 개인/회사 이중 도메인 운영 원칙
- [[projects/immediate-agent-operating-structure]] — 즉시 운영 구조 전환 문서
- [[projects/workspace-security-boundary]] — 4축 보안 경계 정책
- [[topics/professors-brain-03-closing-the-loop]] — AI가 루프를 닫는다는 것, Claude Design에서 AI for Science까지
