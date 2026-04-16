# PR Summary 실습 정리

## 문서 목적

이 문서는 지금까지 진행한 `PR 요약 + 리뷰 포인트 생성기` 실습을 다시 공부하기 위한 학습용 정리 문서다.

이번 턴에서의 원칙:
- 구현은 여기서 일단 멈춘다
- 현재까지 만든 결과물을 다시 이해할 수 있게 정리한다
- 다음 실습인 `2. Jira 이슈 구현 계획 초안 생성기`는 `진행 예정` 상태로만 남긴다

## 현재 상태

### 완료

- 공통 기준 문서 작성
- `ai-survival-log-site`용 PR summary 1차 구현
- `ai-survival-log`용 PR summary 축소 적용
- 두 저장소 모두 GitHub Actions workflow 초안 추가
- 두 저장소 모두 로컬 샘플 실행으로 출력 검증

### 진행 예정

- `2. Jira 이슈 구현 계획 초안 생성기`

## 이번 실습에서 실제로 만든 것

### 1. 공통 기준 문서

파일:
- [docs/2026-04-16-pr-summary-standard.md](/Users/ms/workspace/claude/ai-survival-log/docs/2026-04-16-pr-summary-standard.md:1)

역할:
- PR 요약이 반드시 포함해야 할 블록 정의
- 변경 범주 taxonomy 정의
- 테스트 영향 판단 기준 정의
- 리뷰 포인트와 리뷰어 질문 형식 정의

### 2. `ai-survival-log-site` 구현

파일:
- [scripts/pr-summary.mjs](/Users/ms/workspace/claude/ai-survival-log-site/scripts/pr-summary.mjs:1)
- [docs/automation/pr-summary.md](/Users/ms/workspace/claude/ai-survival-log-site/docs/automation/pr-summary.md:1)
- [.github/workflows/pr-summary.yml](/Users/ms/workspace/claude/ai-survival-log-site/.github/workflows/pr-summary.yml:1)

역할:
- changed files 수집
- `content`, `ui`, `api`, `data-loading`, `build-ci`, `docs`, `test` 분류
- 위험도 추정
- 테스트 영향과 리뷰 포인트 생성
- PR 코멘트 자동 게시 workflow

### 3. `ai-survival-log` 축소 적용

파일:
- [scripts/pr-summary.mjs](/Users/ms/workspace/claude/ai-survival-log/scripts/pr-summary.mjs:1)
- [docs/automation/pr-summary.md](/Users/ms/workspace/claude/ai-survival-log/docs/automation/pr-summary.md:1)
- [.github/workflows/pr-summary.yml](/Users/ms/workspace/claude/ai-survival-log/.github/workflows/pr-summary.yml:1)

역할:
- changed files 수집
- `source`, `wiki`, `publish-contract`, `script`, `agent-surface`, `docs`, `test` 분류
- 위험도 추정
- `wiki lint`, publish compatibility, docs consistency 중심 검증 포인트 생성
- PR 코멘트 자동 게시 workflow

## "축소 적용"이란 무엇이었나

대화에서 말한 `ai-survival-log에도 축소 적용`은 같은 자동화를 그대로 복사하는 뜻이 아니었다.

의미는 이렇다.
- `ai-survival-log-site`는 런타임, API, 렌더링, 테스트, 빌드가 중요한 저장소다
- `ai-survival-log`는 source-of-truth, wiki 구조, publish contract, 문서 정합성이 중요한 저장소다

그래서 같은 PR summary라도 질문이 달라져야 했다.

`site` 쪽 질문:
- 이 변경이 화면이나 API를 깨뜨릴 수 있는가
- 테스트가 충분한가
- build/release 경로에 영향이 있는가

`upstream` 쪽 질문:
- 이 변경이 wiki source-of-truth 경계를 흐리는가
- publish contract를 깨는가
- `wiki/index.md`, `wiki/log.md`, 역링크 정리가 필요한가
- 문서와 운영 모델 설명이 어긋나는가

즉, 축소 적용이란:
- 같은 자동화 아이디어를 유지하되
- 저장소 역할에 맞는 범주와 검증 기준으로 다시 설계한 것이다

## 1장짜리 비교표

| 항목 | `ai-survival-log-site` PR summary | `ai-survival-log` PR summary |
|---|---|---|
| 저장소 역할 | downstream presentation / runtime consumer | upstream authoring / source-of-truth |
| 핵심 관심사 | UI, API, data loading, test, build | source, wiki, publish contract, docs consistency |
| 주요 분류 | `content`, `ui`, `api`, `data-loading`, `build-ci`, `docs`, `test` | `source`, `wiki`, `publish-contract`, `script`, `agent-surface`, `docs`, `test` |
| 대표 질문 | 화면/API/빌드가 깨질 수 있는가 | wiki/publish contract가 깨질 수 있는가 |
| 대표 검증 | `npm run lint`, `npm test`, `npm run build`, content contract 확인 | `python3 scripts/wiki lint --summary`, publish compatibility 확인, 문서 정합성 확인 |
| 위험도 높음 기준 | API 변경, CI/build 경로 변경, 여러 핵심 범주 동시 변경 | publish contract 변경, wiki와 script 동시 변경 |
| 리뷰 포인트 예시 | 테스트 누락, API 실패 케이스, 렌더링 회귀 | `wiki/index.md`/`wiki/log.md` 반영, downstream 경로 호환성, 운영 문서 정합성 |
| 자동화 목표 | 리뷰어가 앱 변경 리스크를 빨리 파악 | 리뷰어가 지식 구조/발행 계약 리스크를 빨리 파악 |

## 샘플 검증 결과

### `ai-survival-log-site`

실행 예:

```bash
node scripts/pr-summary.mjs --files "src/lib/posts.ts,src/app/posts/[slug]/page.tsx,src/lib/__tests__/posts.test.ts"
```

확인한 점:
- `data-loading, ui, test`로 분류됨
- 위험도 `medium`
- `npm run lint`, `npm test`, `npm run build` 권장
- posts 파싱/렌더링 회귀 중심 리뷰 포인트 생성

### `ai-survival-log`

실행 예:

```bash
node scripts/pr-summary.mjs --files "wiki/topics/ai-era-survival.md,docs/publishing-contract.md,scripts/wiki"
```

확인한 점:
- `wiki, publish-contract, docs, script`로 분류됨
- 위험도 `high`
- `python3 scripts/wiki lint --summary` 권장
- publish compatibility, wiki 반영, 운영 규칙 충돌 여부 중심 리뷰 포인트 생성

## 이번 실습에서 배운 점

1. 같은 자동화라도 저장소 역할이 다르면 분류와 검증 기준이 달라져야 한다.
2. `site`는 runtime 중심, `upstream`은 contract 중심 자동화가 더 맞다.
3. 처음부터 LLM을 붙이지 않아도, 규칙 기반 1차 버전만으로도 리뷰 품질을 꽤 끌어올릴 수 있다.
4. 자동화의 핵심은 "멋진 요약"보다 "리뷰어가 어디를 먼저 봐야 하는지"를 드러내는 것이다.

## 다음 단계

다음 실습은 `2. Jira 이슈 구현 계획 초안 생성기`다.

현재 상태:
- `진행 예정`
- 아직 구현 시작하지 않음
- 이번 문서를 기준으로 PR summary 실습을 먼저 복기한 뒤 진행

## 관련 문서

- [docs/2026-04-16-cross-repo-ai-automation-collaboration-plan.md](/Users/ms/workspace/claude/ai-survival-log/docs/2026-04-16-cross-repo-ai-automation-collaboration-plan.md:1)
- [docs/2026-04-16-pr-summary-standard.md](/Users/ms/workspace/claude/ai-survival-log/docs/2026-04-16-pr-summary-standard.md:1)
- [site 실행 계획](</Users/ms/workspace/claude/ai-survival-log-site/docs/superpowers/plans/2026-04-16-cross-repo-execution-plan.md:1>)
- [site automation lab plan](</Users/ms/workspace/claude/ai-survival-log-site/docs/superpowers/plans/2026-04-16-ai-automation-lab-plan.md:1>)
