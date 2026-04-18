# PR Summary Automation for `ai-survival-log`

## 목적

이 저장소의 PR summary는 앱 런타임보다 `raw -> wiki -> output/blog -> publish` 계약을 먼저 본다.

즉, 이 자동화는 다음을 빠르게 드러내기 위한 것이다.

- wiki source-of-truth 경계를 흐리는 변경인가
- publish contract를 깨는가
- 문서와 운영 규칙 설명이 어긋나는가
- wiki lint나 downstream 호환성 검증이 필요한가

공통 기준 문서는 [PR Summary Standard](/Users/ms/workspace/claude/ai-survival-log/docs/2026-04-16-pr-summary-standard.md:1)이고, 이 문서는 `ai-survival-log`에 맞는 축소 적용 규칙을 적는다.

## 현재 구현 범위

1차 구현은 규칙 기반이다.

포함:
- changed files 수집
- `source`, `wiki`, `publish-contract`, `script`, `agent-surface`, `docs`, `test` 분류
- 위험도 추정
- 검증 영향 분석
- 리뷰 포인트 생성

## 로컬 실행

현재 워킹트리 기준:

```bash
node scripts/pr-summary.mjs
```

특정 파일 목록을 직접 넣기:

```bash
node scripts/pr-summary.mjs --files "wiki/topics/ai-era-survival.md,docs/publishing-contract.md,scripts/wiki"
```

파일로 저장:

```bash
node scripts/pr-summary.mjs --files "README.md,AGENTS.md,CLAUDE.md" --output /tmp/pr-summary.md
```

## 해석 규칙

- `raw/` 변경은 `source`
- `assets/` 변경은 `asset`
- `output/` 변경은 `output`
- `wiki/` 변경은 `wiki`
- publish 경로나 계약 문서는 `publish-contract`
- `scripts/`와 wiki command 경로는 `script`
- `AGENTS.md`, `CLAUDE.md`, `.claude/`, `.codex/`는 `agent-surface`
- `docs/`, `README.md`는 `docs`

## 검증 권장 규칙

- `wiki` 또는 `script` 변경이면 `python3 scripts/wiki lint --summary`
- `publish-contract` 변경이면 downstream 호환성 검토
- `agent-surface` 또는 `docs` 변경이면 문서 정합성 검토

## 한계

- 실제 의미까지 완전 이해하지는 못하고 파일 경로 기준으로 판단한다
- wiki/index.md, wiki/log.md 직접 수정의 적절성은 사람이 마지막 판단해야 한다
