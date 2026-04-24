---
title: "shared-agent-harness executable surface 검토"
created: "2026-04-25"
updated: "2026-04-25"
type: project
sources: []
tags: [project, review, harness, executable, scripts, validation]
status: active
published: false
slug: ""
description: "shared-agent-harness executable surface 1차 전환 이후 스크립트와 문서의 경계 일치 여부를 검토한 기록."
---

# shared-agent-harness executable surface 검토

이 문서는 `shared-agent-harness`의 executable surface 1차 전환 이후, 문서에 선언한 경계와 실제 `scripts/harness.py` 동작이 일치하는지 검토한 기록이다.

## Findings

### 1. executable surface가 여전히 domain repo 직접 쓰기를 허용했다

이전 심각도: `block`
현재 상태: `fixed`

대상:

- [shared-agent-harness/scripts/harness.py](/Users/ms/workspace/claude/shared-agent-harness/scripts/harness.py:16)
- [shared-agent-harness-executable-review-gate](/Users/ms/workspace/claude/ai-survival-log/wiki/projects/shared-agent-harness-executable-review-gate.md:27)
- [shared-agent-harness-executable-surface-phase1](/Users/ms/workspace/claude/ai-survival-log/wiki/projects/shared-agent-harness-executable-surface-phase1.md:47)

문제:

- `write_output()`는 전달받은 `--output` 경로에 그대로 파일을 쓴다
- 따라서 사용자가 `company-wiki`, `company-assistant-ops`, `ai-survival-log` 같은 domain source-of-truth 경로를 넘기면 shared harness가 직접 domain repo를 수정할 수 있다
- 이는 문서에서 선언한 `domain source-of-truth 직접 수정 금지`와 정면으로 충돌한다

영향:

- shared/domain boundary가 즉시 무너진다
- 검토 게이트 문서가 있어도 실행 레이어가 그 경계를 강제하지 못한다
- 실수로 shared harness를 domain write entrypoint처럼 쓰게 될 수 있다

조치 결과:

- `--output` 경로를 shared repo 내부 허용 루트(`examples/`, `tmp/`)로 제한했다
- `company-wiki`, `company-assistant-ops`, `ai-survival-log`, `ai-survival-log-site` 경로는 명시적으로 `block`하도록 guard를 추가했다
- 이제 shared harness는 코드 수준에서도 domain source-of-truth repo에 직접 쓰지 못한다

### 2. `domain`이 기본값 `unspecified`라서 explicit domain context 원칙이 깨졌다

이전 심각도: `warn`
현재 상태: `fixed`

대상:

- [shared-agent-harness/scripts/harness.py](/Users/ms/workspace/claude/shared-agent-harness/scripts/harness.py:72)
- [shared-agent-harness/ARCHITECTURE.md](/Users/ms/workspace/claude/shared-agent-harness/ARCHITECTURE.md:43)

문제:

- `add_common()`에서 `--domain`이 required가 아니라 기본값 `unspecified`다
- 하지만 shared harness 문서들은 `explicit domain selection`, `explicit domain context injection`을 일관되게 요구한다

영향:

- artifact만 생성하더라도 어떤 domain context에서 만든 것인지 불명확해질 수 있다
- 이후 handoff나 review에서 domain boundary 판단이 약해진다

조치 결과:

- `--domain`을 required로 변경했다
- 허용값을 `shared`, `personal`, `company`로 제한했다
- 이제 artifact 생성 시에도 explicit domain context가 강제된다

### 3. 테스트가 성공 경로만 검증하고 경계 위반을 막는지 확인하지 않았다

이전 심각도: `warn`
현재 상태: `fixed`

대상:

- [shared-agent-harness/tests/test_harness.py](/Users/ms/workspace/claude/shared-agent-harness/tests/test_harness.py:12)

문제:

- 현재 테스트는 artifact가 생성되고 일부 섹션이 채워지는지만 본다
- `domain repo 경로로 쓰기 시도`, `domain 미지정`, `잘못된 command usage` 같은 경계 위반 케이스가 없다

영향:

- boundary guard를 추가해도 회귀를 잡기 어렵다
- 지금은 문서가 말하는 안전성의 핵심이 테스트로 보호되지 않는다

조치 결과:

- `domain repo path write should fail`
- `missing domain should fail`
- `invalid domain should fail`
  케이스를 negative test로 추가했다
- 현재 executable surface의 핵심 안전 가정이 테스트로 보호된다

## 결론

현재 executable surface는 `artifact generation` 자체는 동작한다.

그리고 경계 강제 로직도 코드에 반영되어, 문서상 안전 모델과 실제 구현이 더 잘 맞게 되었다.

따라서 현 상태는:

- `기능 시연 가능`
- `경계 강제 기본형 반영 완료`
- `phase 1 executable surface usable`

으로 보는 것이 맞다.

## 관련 페이지

- [[projects/shared-agent-harness-executable-surface-phase1]]
- [[projects/shared-agent-harness-executable-review-gate]]
