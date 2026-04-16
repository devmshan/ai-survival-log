# Cross-Repo AI Automation Collaboration Plan

## 목적

`ai-survival-log`와 `ai-survival-log-site`에 공통으로 적용 가능한 자동화를, 두 프로젝트 관리자가 협업하는 방식으로 설계한다.

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

즉, 한 저장소가 다른 저장소를 대체하는 구조가 아니라:
- upstream manager가 `무엇을 자동화할지`와 `어떤 기준으로 검증할지`를 정의하고
- downstream manager가 `어디에 붙일지`와 `어떻게 실행할지`를 구현한다

## 협업 대상 자동화 10개 분류

### 두 저장소 모두 적용 가능한 항목

1. PR 요약 + 리뷰 포인트 생성기
2. Jira 이슈 구현 계획 초안 생성기
3. 회귀 테스트 실행 + 실패 원인 정리 봇
4. API 문서와 런북 자동 갱신기
5. 배포 체크리스트 자동 수행 에이전트
6. 사내 백오피스 반복 작업 자동화

### `ai-survival-log`에 특히 잘 맞는 항목

7. 반복 운영 쿼리 생성기
8. 경쟁사/기술 동향 모니터링 스크래퍼
9. 오픈소스 이슈 대응 보조 워크플로우

### `ai-survival-log-site`에 특히 잘 맞는 항목

10. 장애 1차 분석 봇

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

## 1~3번 공통 실습 로드맵

### Phase 1. 공통 규칙 고정

산출물:
- PR 요약 포맷
- 구현 계획 포맷
- 배포 체크리스트 포맷

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

## 성공 기준

이 협업 구조가 잘 작동하면:
- upstream은 기준과 문서를 더 잘 통제하게 되고
- downstream은 구현과 검증을 더 빠르게 돌리게 된다

최종적으로는:
- 사람이 규칙을 기억하는 방식에서
- 저장소가 규칙을 실행하는 방식으로 이동한다

## 관련 문서

- [docs/operating-playbook.md](/Users/ms/workspace/claude/ai-survival-log/docs/operating-playbook.md:1)
- [docs/publishing-contract.md](/Users/ms/workspace/claude/ai-survival-log/docs/publishing-contract.md:1)
- [ai-survival-log-site 협업 실행 계획](</Users/ms/workspace/claude/ai-survival-log-site/docs/superpowers/plans/2026-04-16-cross-repo-execution-plan.md:1>)
