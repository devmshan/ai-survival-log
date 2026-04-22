# Cross-Repo AI Automation Collaboration Plan

## 목적

`ai-survival-log`와 `ai-survival-log-site`에 공통으로 적용 가능한 자동화를, 두 프로젝트 관리자가 협업하는 방식으로 설계한다.

이 문서는 실습 방향 메모가 아니라, cross-repo 자동화 후보를 검토하고 다음 구현 순서를 고르는 기준 문서로 사용한다.

## 현재 상태

- `1. PR 요약 + 리뷰 포인트 생성기` — 완료
  - 공통 기준 문서 작성 완료
  - `ai-survival-log-site` 구현 완료
  - `ai-survival-log` 축소 적용 완료
- `2. Jira 이슈 구현 계획 초안 생성기` — 진행 예정
- 구현은 일단 멈추고, PR summary 실습 결과를 학습 문서로 정리하는 단계

핵심 전제:
- `ai-survival-log`는 upstream authoring/source-of-truth
- `ai-survival-log-site`는 downstream presentation/consumer
- 자동화도 이 경계를 흐리지 않고 설계해야 한다

적용 범위:
- canonical authoring은 계속 `ai-survival-log/wiki/`와 관련 계약 문서에 둔다
- runtime, CI, deploy, production signal 실행은 `ai-survival-log-site` 또는 해당 consumer 저장소에서 맡는다
- `output/`과 state export는 구현 후 필요가 입증된 경우에만 추가한다

비목표:
- 새로운 canonical authoring schema를 도입하지 않는다
- lane이나 consumer가 불명확한 자동화를 바로 공식 workflow로 승격하지 않는다
- downstream 구현 세부를 upstream 문서가 대체하지 않는다

즉, 한 저장소가 다른 저장소를 대체하는 구조가 아니라:
- upstream manager가 `무엇을 자동화할지`와 `어떤 기준으로 검증할지`를 정의하고
- downstream manager가 `어디에 붙일지`와 `어떻게 실행할지`를 구현한다

## 협업 대상 자동화 10개 분류

상태 규칙:
- `completed`: 기준 문서와 최소 구현, 샘플 검증까지 끝난 항목
- `planned`: 다음 실습 후보로 선정됐지만 PRD/검증 계획 보강이 더 필요한 항목
- `exploratory`: 아이디어 수준이며 lane, consumer, contract owner가 아직 고정되지 않은 항목

### 두 저장소 모두 적용 가능한 항목

1. PR 요약 + 리뷰 포인트 생성기 (`completed`)
2. Jira 이슈 구현 계획 초안 생성기 (`planned`)
3. 회귀 테스트 실행 + 실패 원인 정리 봇 (`exploratory`)
4. API 문서와 런북 자동 갱신기 (`exploratory`)
5. 배포 체크리스트 자동 수행 에이전트 (`planned`)
6. 사내 백오피스 반복 작업 자동화 (`exploratory`)

### `ai-survival-log`에 특히 잘 맞는 항목

7. 반복 운영 쿼리 생성기 (`exploratory`)
8. 경쟁사/기술 동향 모니터링 스크래퍼 (`exploratory`)
9. 오픈소스 이슈 대응 보조 워크플로우 (`exploratory`)

### `ai-survival-log-site`에 특히 잘 맞는 항목

10. 장애 1차 분석 봇 (`exploratory`)

공식 승격 규칙:
- `planned` 이상으로 다루는 항목은 problem, goals, non-goals, surfaces, validation을 최소한 문서화한다
- 새로운 consumer나 lane을 만들면 `docs/operating/channel-lanes.md` 또는 별도 PRD에서 owner와 validation path를 정의한다
- state export나 cross-repo contract 변경이 생기면 PRD와 관련 계약 문서를 같은 change set에서 함께 갱신한다

## 공동 관리자 역할 분담

### Upstream Manager (`ai-survival-log`)

책임:
- 자동화 대상 업무를 정의
- 체크리스트와 품질 기준을 문서화
- publish contract, wiki contract, docs consistency 기준 유지
- 학습 메모, 평가 기준, 템플릿 저장
- 자동화 결과가 지식으로 축적될 수 있게 문서 경로를 관리

주요 산출물:
- 기준 문서
- 체크리스트
- 템플릿
- 입력 포맷
- 검증 기준

### Downstream Manager (`ai-survival-log-site`)

책임:
- GitHub Actions, scripts, test runners, deploy checks 구현
- 사이트 런타임과 CI에 자동화 부착
- 운영 신호, 실패 로그, 배포 정보 수집
- 실제 실행 결과를 리포트로 남김

주요 산출물:
- workflow 파일
- 실행 스크립트
- 검증 리포트
- 운영 가이드

## 협업 방식

각 자동화 항목은 같은 템플릿으로 관리한다.

1. upstream manager가 문제 정의와 완료 기준 작성
2. downstream manager가 실행 설계와 구현 범위 작성
3. 둘이 합의한 최소 수직 슬라이스부터 구현
4. 검증 결과를 다시 upstream 문서에 환류

권장 운영 리듬:
- 주 초: 우선순위 선정
- 중간: 구현/검증
- 주 말: 결과 회고 및 템플릿 개선

## repo별 역할 분담표

| 자동화 항목 | `ai-survival-log` 역할 | `ai-survival-log-site` 역할 |
|---|---|---|
| PR 요약 + 리뷰 포인트 | PR 요약 기준, 리뷰 질문 템플릿 정의 | changed files 분석, Action/코멘트 구현 |
| Jira 이슈 계획 초안 | 요구사항 템플릿, 구현계획 포맷 정의 | issue body 파싱, 계획 초안 생성기 구현 |
| 회귀 테스트 실패 분석 | 실패 분류 기준, 리뷰 포맷 정의 | test runner, 로그 수집, 코멘트 자동화 |
| 장애 1차 분석 | incident template, triage 질문 정의 | runtime/deploy/log 기반 분석 봇 구현 |
| API 문서/런북 갱신 | 문서 구조, 필수 항목 정의 | route 변경 감지, 초안 생성 구현 |
| 반복 운영 쿼리 | 운영 질문 카탈로그 정의 | 실행 가능한 query/filter 예시 연결 |
| 배포 체크리스트 | 배포 기준과 contract 확인 항목 정의 | pre-release checks, workflow 구현 |
| 오픈소스 이슈 대응 | 분석 템플릿, 재현 문서 형식 정의 | 실제 재현, patch, PR draft 구현 |
| 기술 동향 모니터링 | 수집 대상과 분류 체계 정의 | fetch/diff/요약 파이프라인 구현 |
| 백오피스 자동화 | 보고서 포맷, 회고 템플릿 정의 | activity/test/deploy 데이터 수집 자동화 |

## 같이 시작할 1차 공통 실습 3개

### 1. PR 요약 + 리뷰 포인트 생성기

이유:
- 두 저장소 모두 Git 기반 협업을 한다
- 효과가 가장 빨리 보인다
- 규칙 기반 1차 버전을 먼저 만들 수 있다

upstream manager:
- "좋은 PR 요약" 형식 정의
- 변경 유형 분류 기준 정의
- 리뷰어 질문 5개 템플릿 정의

downstream manager:
- `.github/workflows/pr-summary.yml`
- changed files 분류 스크립트
- PR 코멘트 자동 게시 구현

### 2. Jira 이슈 구현 계획 초안 생성기

이유:
- 두 저장소 모두 구현 전 정리 비용이 있다
- Jira가 없어도 local template로 먼저 실습 가능하다
- 현재 상태: `진행 예정`

upstream manager:
- intake 문서 구조 정의
- 구현 계획 템플릿 정의
- 확인 질문 규칙 정의

downstream manager:
- issue body 또는 markdown intake 파서 구현
- 초안 생성용 스크립트/Action 구현

문제:
- 구현 전에 요구사항, 변경 범위, 테스트 계획을 사람이 매번 수동으로 정리해야 한다
- upstream/downstream 저장소가 같은 이슈를 다르게 해석해 구현 전 정렬 비용이 커진다

목표:
- intake 입력만으로 구현 계획 초안을 반복 가능하게 만든다
- 변경 파일 후보, 테스트 계획, 확인 질문을 같은 형식으로 생성한다

비목표:
- Jira 자체를 source of truth로 만들지 않는다
- 이 단계에서 코드 생성이나 자동 머지를 포함하지 않는다

영향 surface:
- upstream: 요구사항 템플릿, 구현 계획 템플릿, 평가 기준 문서
- downstream: issue body parser, draft generator script, CI comment or artifact

입력과 출력:
- 입력: issue body 또는 markdown intake
- 출력: implementation plan draft, changed-file candidates, test plan, open questions

검증 계획:
- parser/generator 로직에 대한 관련 테스트
- malformed issue body, missing section, empty acceptance criteria 케이스 확인
- 생성 결과가 upstream 템플릿 필수 섹션을 빠뜨리지 않는지 샘플 검증
- cross-repo에서 같은 입력에 대해 역할별 해석 차이만 남고 기본 구조는 유지되는지 수동 리뷰

롤아웃:
- 1차는 local markdown intake로 실습
- 2차에서 필요하면 GitHub issue 템플릿과 Action으로 확장

### 3. 배포 체크리스트 자동 수행 에이전트

이유:
- upstream은 publish contract를, downstream은 runtime contract를 가진다
- 둘을 같이 다뤄야 실제 배포 안정성이 올라간다

upstream manager:
- publish 전 확인 항목
- 문서 정합성 확인 항목
- slug/description/frontmatter 안정성 기준

downstream manager:
- lint/test/build/content contract checks 연결
- release report 생성
- 배포 전 자동 점검 workflow 구현

문제:
- 배포 전 확인 항목이 문서, publish contract, runtime check로 흩어져 있다
- upstream과 downstream이 서로의 실패 조건을 늦게 발견하면 릴리즈 비용이 커진다

목표:
- 배포 전 필수 확인 항목을 자동 실행 가능한 체크리스트로 통합한다
- upstream publish contract와 downstream runtime contract를 한 번에 점검한다

비목표:
- 배포 승인 자체를 완전 무인화하지 않는다
- production incident 대응이나 rollback 자동화까지 한 번에 묶지 않는다

영향 surface:
- upstream: publish contract docs, wiki lint/publish validation 기준
- downstream: lint/test/build workflow, release report, pre-release gate

필수 체크 후보:
- `python3 scripts/wiki sync`
- `python3 scripts/wiki lint --summary`
- publishable page의 `slug`, `description`, frontmatter 안정성 확인
- downstream lint/test/build/content contract checks

검증 계획:
- 체크리스트 스크립트 또는 workflow에 대한 관련 테스트
- 성공 케이스와 대표 실패 케이스를 각각 샘플로 검증
- 실패 리포트가 어느 저장소 계약이 깨졌는지 구분해 설명하는지 확인
- 필요 시 `python3 scripts/state export` 결과 diff review

롤아웃:
- 1차는 수동 실행 가능한 checklist runner로 시작
- 2차에서 release workflow gate로 연결

## 1~3번 공통 실습 로드맵

### Phase 1. 공통 규칙 고정

산출물:
- PR 요약 포맷
- 구현 계획 포맷
- 배포 체크리스트 포맷
- automation별 problem/goals/non-goals/validation 메모

위치:
- `ai-survival-log/docs/`

### Phase 2. `ai-survival-log-site`에서 먼저 실행형 구현

이유:
- GitHub 이벤트, 테스트, 빌드, API route가 이미 존재
- 자동화 성과를 관찰하기 쉽다

산출물:
- workflow
- scripts
- 검증 리포트

위치:
- `ai-survival-log-site/.github/workflows/`
- `ai-survival-log-site/scripts/`
- `ai-survival-log-site/docs/superpowers/`

### Phase 3. `ai-survival-log`에 맞게 변형 적용

이유:
- upstream은 runtime보다 contract/document 중심 자동화가 더 중요하다

예:
- PR 요약은 문서 계약 위반 중심으로 해석
- 이슈 계획 초안은 wiki/topic/source 갱신 범위 중심으로 해석
- 배포 체크는 publish compatibility 중심으로 해석

## 추천 순서

1. `ai-survival-log`에 공통 기준 문서 만든다
2. `ai-survival-log-site`에서 1번 PR 자동화 구현한다
3. 같은 형식을 `ai-survival-log`에 축소 적용한다
4. 2번, 3번 자동화를 같은 방식으로 확장한다

다음 착수 조건:
- `2. Jira 이슈 구현 계획 초안 생성기`는 intake template, output template, validation 샘플이 준비되면 구현 시작
- `3. 배포 체크리스트 자동 수행 에이전트`는 upstream/downstream 필수 체크 목록과 owner가 합의되면 구현 시작
- `exploratory` 항목은 새 lane, consumer, state schema 여부를 먼저 판별한 뒤 승격 여부를 결정

## 성공 기준

이 협업 구조가 잘 작동하면:
- upstream은 기준과 문서를 더 잘 통제하게 되고
- downstream은 구현과 검증을 더 빠르게 돌리게 된다

최종적으로는:
- 사람이 규칙을 기억하는 방식에서
- 저장소가 규칙을 실행하는 방식으로 이동한다

완료 정의:
- 기준 문서가 있다
- 최소 실행 구현이 있다
- validation path가 문서화돼 있다
- 샘플 또는 실제 실행 검증 결과가 남아 있다

## 관련 문서

- [docs/operating-playbook.md](/Users/ms/workspace/claude/ai-survival-log/docs/operating-playbook.md:1)
- [docs/publishing-contract.md](/Users/ms/workspace/claude/ai-survival-log/docs/publishing-contract.md:1)
- [ai-survival-log-site 협업 실행 계획](</Users/ms/workspace/claude/ai-survival-log-site/docs/superpowers/plans/2026-04-16-cross-repo-execution-plan.md:1>)
