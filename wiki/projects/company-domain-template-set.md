---
title: "회사 도메인 템플릿 세트 초안"
created: "2026-04-24"
updated: "2026-04-24"
type: project
sources: []
tags: [project, company, templates, wiki, assistant, review, audit, workflow]
status: active
published: false
slug: ""
description: "company-wiki와 company-assistant-ops에서 바로 사용할 수 있도록 회의록, 검수, 테스트, 승인, 실행 보고 템플릿의 필드와 구조를 정의한 초안."
---

# 회사 도메인 템플릿 세트 초안

이 문서는 회사 도메인에서 바로 옮겨 쓸 템플릿 세트를 정의한다.

구성:

- `company-wiki`용 기록 템플릿
- `company-assistant-ops`용 실행 템플릿
- 두 저장소 사이 handoff에 필요한 최소 필드

핵심 원칙:

- `company-wiki`는 판단과 맥락을 남긴다
- `company-assistant-ops`는 외부 시스템 실행과 승인/audit를 남긴다
- 같은 정보를 두 저장소에 중복 적재하지 않는다

## 1. company-wiki 템플릿

### `meeting-note.md`

용도:

- 회의 agenda, note, 결정, action item 요약

권장 frontmatter:

```yaml
title: ""
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
type: meeting
status: active
confidentiality: internal|restricted
owners: []
related_projects: []
followup_required: true|false
```

본문 구조:

```md
# {회의 제목}

## Context

## Agenda

## Notes

## Decisions

## Action Items

## Follow-up for Assistant Ops

## Related
```

중요:

- `Action Items`는 실행 가능 단위로 짧게 쓴다
- `Follow-up for Assistant Ops`에는 외부 시스템 실행에 필요한 최소 요약만 둔다

### `project-brief.md`

용도:

- 회사 프로젝트 개요와 범위 정리

권장 frontmatter:

```yaml
title: ""
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
type: project
status: active|draft|archived
confidentiality: internal|restricted
owners: []
related_meetings: []
related_reviews: []
related_tests: []
```

본문 구조:

```md
# {프로젝트 이름}

## Goal

## Scope

## Non-Goals

## Milestones

## Risks

## Related Notes
```

### `planning-brief.md`

용도:

- 기획, 디렉팅, 발표 구조, 실행 계획

권장 본문 구조:

```md
# {기획 제목}

## Problem

## Goal

## Audience / Stakeholders

## Options Considered

## Chosen Direction

## Execution Plan

## Open Questions
```

### `review-report.md`

용도:

- 단일 검수 결과 기록

권장 frontmatter:

```yaml
title: ""
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
type: review
status: draft|resolved
review_path: primary|secondary
confidentiality: internal|restricted
related_projects: []
related_tests: []
```

본문 구조:

```md
# {검수 제목}

## Scope

## Checklist Used

## Findings

## Severity Summary

## Block / Warn / Escalate

## Suggested Fixes
```

### `cross-review-report.md`

용도:

- `primary review`와 `secondary review`를 비교해 공식 결론 기록

권장 본문 구조:

```md
# {교차검증 제목}

## Reviewed Scope

## Primary Review Summary

## Secondary Review Summary

## Agreements

## Conflicts

## Resolved / Unresolved

## Final Gate Decision
```

중요:

- 같은 모델 + 같은 checklist + 같은 prompt 반복은 허용하지 않는다는 문구를 template note에 포함한다

### `test-plan.md`

용도:

- 테스트 범위와 기대 결과 정의

본문 구조:

```md
# {테스트 계획 제목}

## Scope

## Environment

## Test Cases

## Expected Results

## Risks
```

### `test-result.md`

용도:

- 테스트 실행 결과 요약

본문 구조:

```md
# {테스트 결과 제목}

## Scope

## Executed Cases

## Passed

## Failed

## Regression Notes

## Next Action
```

## 2. company-assistant-ops 템플릿

### `calendar-request.md`

용도:

- 일정 생성/변경 요청

권장 frontmatter:

```yaml
title: ""
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
request_type: calendar
status: draft|awaiting-approval|approved|executed|failed
system: google-calendar
confidentiality: internal|restricted
source_wiki_page: ""
```

본문 구조:

```md
# {일정 요청 제목}

## Reason

## Proposed Event

## Participants

## Constraints

## Approval Needed

## Execution Result
```

### `followup-request.md`

용도:

- 회의 후속 메일/메시지 요청

본문 구조:

```md
# {후속 요청 제목}

## Source Summary

## Target Audience

## Requested Follow-up

## Draft Message

## Approval Needed

## Execution Result
```

### `report-request.md`

용도:

- 보고 초안 또는 시트 반영 요청

본문 구조:

```md
# {보고 요청 제목}

## Context

## Intended Output

## Draft Summary

## Approval Needed

## Execution Result
```

### `approval-record.md`

용도:

- write-with-approval 이상 단계의 승인 기록

권장 frontmatter:

```yaml
title: ""
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
type: approval
status: recorded|revoked
system: gmail|calendar|sheets
action_ref: ""
approved_by: ""
```

본문 구조:

```md
# {승인 기록 제목}

## Action Reference

## Approved Scope

## Approved By

## Approved At

## Conditions

## Notes
```

### `execution-report.md`

용도:

- 외부 write 실행 결과 기록

본문 구조:

```md
# {실행 보고 제목}

## Action Reference

## Target System

## Executed At

## Result

## Side Effects

## Follow-up Needed
```

### `failure-report.md`

용도:

- 실행 실패 또는 보류 기록

본문 구조:

```md
# {실패 보고 제목}

## Action Reference

## Failure Type

## What Happened

## Retry Decision

## Escalation Needed
```

## 3. handoff 최소 필드

### `company-wiki -> company-assistant-ops`

필수 최소 필드:

- `source_wiki_page`
- `requested_action`
- `reason`
- `target_system`
- `draft_payload_summary`
- `approval_level`

### `company-assistant-ops -> company-wiki`

필수 최소 필드:

- `action_ref`
- `target_system`
- `executed_at`
- `result_status`
- `summary`
- `followup_needed`

## 4. 교차검증 템플릿 규칙

공식 검수와 실행 정책 변경은 다음을 만족해야 한다.

- `primary review` 템플릿과 `cross-review-report`를 함께 사용 가능해야 한다
- 교차검증은 가능한 한 다른 agent surface 또는 다른 review path를 사용해야 한다
- 같은 모델 + 같은 checklist + 같은 prompt 반복은 template note에 금지 문구로 남긴다

## 5. 구현 우선순위

### Phase 1

- `meeting-note.md`
- `cross-review-report.md`
- `test-plan.md`
- `approval-record.md`
- `execution-report.md`

### Phase 2

- `project-brief.md`
- `planning-brief.md`
- `review-report.md`
- `calendar-request.md`
- `followup-request.md`
- `report-request.md`

### Phase 3

- `failure-report.md`
- handoff payload helper
- 템플릿별 checklist note

## 다음 단계

- 실제 저장소 생성 시 템플릿 파일 materialize
- 회사 도메인 review/checklist 운영 규칙 분리
- assistant workflow별 dry-run 예시 추가

현재 반영:

- [[projects/company-domain-review-checklist-operations]]
- [[projects/company-domain-template-materialization-plan]]

## 관련 페이지

- [[projects/company-wiki-internal-structure]]
- [[projects/company-assistant-ops-internal-structure]]
- [[projects/shared-agent-harness-internal-structure]]
- [[projects/assistant-ops-lane-execution-draft]]
