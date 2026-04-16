# PR Summary Standard

## 목적

이 문서는 `ai-survival-log`와 `ai-survival-log-site`에서 공통으로 사용할 `PR 요약 + 리뷰 포인트 생성기`의 기준 문서다.

이 자동화의 목표는 PR 설명을 예쁘게 꾸미는 것이 아니라:
- 무엇이 바뀌었는지 빠르게 파악하고
- 어디를 먼저 봐야 하는지 알려주고
- 어떤 검증이 필요한지 드러내는 것이다

## PR 요약이 반드시 포함해야 하는 것

모든 PR 요약은 아래 4개 블록을 가져야 한다.

1. 변경 요약
2. 변경 범주
3. 테스트 영향
4. 리뷰 포인트

## 변경 요약 형식

짧고 구체적으로 쓴다.

예:
- 포스트 렌더링 경로와 시리즈 네비게이션을 함께 수정
- newsletter API 응답 처리와 폼 검증 로직 수정
- wiki publish contract 문서와 검증 스크립트 동시 수정

피해야 할 형태:
- 여러 파일 수정
- 리팩터링
- 버그 수정

## 변경 범주 taxonomy

PR은 가능한 한 아래 범주로 분류한다.

- `content` — `content/posts`, 발행 글, MDX, frontmatter
- `wiki-contract` — publish contract, wiki/source-of-truth 계약, 문서 규칙
- `ui` — 컴포넌트, 스타일, 페이지 렌더링
- `data-loading` — post parsing, search, content loading, static params
- `api` — route handlers, request/response, validation
- `test` — unit/integration/e2e test
- `build-ci` — workflow, scripts, lint, build, release checks
- `docs` — 운영 문서, 가이드, 설계 문서

하나의 PR이 여러 범주를 가질 수 있다.

## 테스트 영향 판단 기준

PR 요약은 아래를 명시해야 한다.

- 테스트 파일이 같이 바뀌었는가
- 런타임 코드만 바뀌고 테스트는 안 바뀌었는가
- `content/posts`만 수정된 것인가
- lint/test/build 중 무엇이 필수 확인 대상인가

기본 규칙:
- `src/` 변경이 있으면 최소 `test`와 `build` 확인이 필요하다
- `api` 변경이 있으면 응답 계약과 실패 케이스를 본다
- `content/posts` 변경이면 frontmatter와 content contract를 본다
- workflow/scripts 변경이면 CI 경로와 실패 처리 방식을 본다

## 리뷰 포인트 작성 규칙

리뷰 포인트는 "이상적으로 뭘 봐야 하나"가 아니라, "이 PR에서 먼저 봐야 하는 리스크"를 적는다.

좋은 예:
- `src/lib/posts.ts` 변경이 있어서 series/frontmatter 파싱 회귀 여부 우선 확인
- API route 수정인데 테스트가 함께 안 바뀌어 실패 케이스 누락 가능성 확인 필요
- content contract 스크립트 변경이 있어 잘못된 frontmatter 통과 가능성 검토 필요

나쁜 예:
- 코드 확인 부탁드립니다
- 테스트가 중요합니다

## 리뷰어 질문 5개 템플릿

자동화는 가능하면 아래 질문 중 해당되는 것을 선택해 포함한다.

1. 이 변경이 기존 contract를 깨는 경로가 있는가
2. 런타임 코드가 바뀌었는데 테스트 커버리지가 따라왔는가
3. 데이터/파싱/정렬 로직 변경으로 숨은 회귀가 생길 수 있는가
4. 문서와 실제 동작이 어긋나는 부분이 있는가
5. 배포 전에 추가로 확인해야 할 수동 검증이 있는가

## 위험도 판단 기준

### `low`

- docs만 변경
- content만 변경
- 테스트만 변경

### `medium`

- UI 변경
- data-loading 변경

### `high`

- API 변경
- build/release 경로 변경
- contract 검증 로직 변경
- 여러 범주의 핵심 파일 동시 변경

## repo별 해석

### `ai-survival-log`

중점:
- wiki contract
- publish compatibility
- slug/description/frontmatter 안정성
- docs consistency

### `ai-survival-log-site`

중점:
- runtime rendering
- content contract
- API behavior
- CI/build/release safety

## 최소 출력 예시

```md
## PR Summary

- 요약: 포스트 파싱과 시리즈 네비게이션 로직을 함께 수정
- 범주: data-loading, ui, test
- 위험도: medium

## Test Impact

- 런타임 코드 변경 있음
- 테스트 파일도 함께 수정됨
- 확인 권장: npm test, npm run build

## Review Points

- series/frontmatter 파싱 회귀 여부 확인
- 시리즈가 아닌 일반 포스트의 prev/next 계산 영향 확인

## Reviewer Questions

- 이 변경이 기존 contract를 깨는 경로가 있는가
- 데이터/파싱/정렬 로직 변경으로 숨은 회귀가 생길 수 있는가
```
