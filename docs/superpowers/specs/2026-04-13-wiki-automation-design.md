# Wiki 자동화 설계 문서

**날짜:** 2026-04-13
**상태:** 확정
**목표:** wiki 운영 3가지 병목 해소

---

## 문제 정의

| 병목 | 현재 상태 | 목표 |
|------|-----------|------|
| `index.md` 수동 갱신 | 인제스트 후 매번 수동 편집 | 인제스트 시 자동 재생성 |
| 깨진 링크 발견 지연 | 발견이 늦음 | pre-commit + 세션 종료 시 자동 검사 |
| 페이지 증가 시 `index.md` 탐색 저하 | 단일 파일에 모든 페이지 | 태그별 서브인덱스 (`wiki/tags/`) 추가 |

---

## 아키텍처

```
wiki/
├── index.md          ← scripts/wiki sync 로 자동 재생성
├── tags/
│   ├── ai.md         ← scripts/wiki tags 로 자동 생성 (태그당 1파일)
│   ├── context-graph.md
│   └── ...
└── ...

scripts/
└── wiki              ← Python CLI (chmod +x)

.claude/
└── settings.local.json  ← PostToolUse + Stop 훅

.git/hooks/
└── pre-commit        ← lint 실행 (wiki 파일 변경 시만)
```

### 데이터 흐름

```
wiki:ingest → Claude가 wiki/*.md Write/Edit
  → PostToolUse 훅 감지
  → ./scripts/wiki sync
  → index.md 재생성 + tags/ 재생성

세션 종료 (Stop 훅)
  → ./scripts/wiki lint --summary

git commit (wiki 파일 포함 시)
  → pre-commit 훅
  → ./scripts/wiki lint
  → 오류 시 커밋 차단 (exit 1)
```

---

## CLI 인터페이스

```bash
./scripts/wiki sync            # index.md + tags/ 재생성
./scripts/wiki lint            # 무결성 검사, 오류 시 exit 1
./scripts/wiki lint --summary  # 요약 출력, exit 0 유지 (Stop 훅용)
./scripts/wiki tags            # tags/ 만 재생성
```

### 스캔 제외 목록

```python
EXCLUDE_FILES = {"index.md", "log.md"}
EXCLUDE_DIRS  = {"tags", ".obsidian"}
```

### wikilink 파싱 정규식

```python
# [[page|alias]] 와 [[page]] 모두 처리
re.findall(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]', content)
```

---

## Python 스크립트 구조

**파일:** `scripts/wiki` (단일 파일, ~300줄, chmod +x)
**의존성:** `python-frontmatter` (pip install python-frontmatter)
**나머지:** 표준 라이브러리 (`pathlib`, `re`, `sys`, `argparse`)

```python
#!/usr/bin/env python3
# 의존성 설치: pip install python-frontmatter

WIKI_DIR      = Path("wiki")
EXCLUDE_FILES = {"index.md", "log.md"}
EXCLUDE_DIRS  = {"tags", ".obsidian"}

def scan_pages() -> list[Page]              # frontmatter 파싱, 제외 목록 적용
def extract_wikilinks(content) -> list[str] # [[link|alias]] 처리
def cmd_sync()                              # index.md + tags/ 재생성
def cmd_lint(summary=False) -> int          # 검사 후 오류 수 반환
def cmd_tags()                              # tags/ 만 재생성
```

### `cmd_lint` 검사 항목

| # | 검사 항목 | 오류 예시 |
|---|-----------|-----------|
| 1 | 깨진 wikilink | `[[concepts/없는페이지]]` 대상 파일 없음 |
| 2 | 고아 페이지 | 어디서도 링크되지 않은 파일 |
| 3 | index.md 누락 | 파일 존재하는데 index에 없음 |
| 4 | frontmatter 필수 필드 누락 | `title`, `type`, `status` 없음 |
| 5 | tags/ 파일 | 자동생성 파일 → 검사 제외 |

### `tags/ai.md` 파일 형식

```markdown
# Tag: ai

| 페이지 | 설명 | 타입 | 상태 |
|--------|------|------|------|
| [[concepts/ax-ai-transformation]] | 기업 AI 전환 전략 | concept | active |
| [[topics/ai-era-survival]] | AI 시대 생존 전략 | topic | active |
```

---

## 훅 설정

### Claude Code (`settings.local.json`)

```json
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "Write|Edit",
      "hooks": [{
        "type": "command",
        "command": "cd /Users/ms/workspace/claude/ai-survival-log && ./scripts/wiki sync"
      }]
    }],
    "Stop": [{
      "matcher": "",
      "hooks": [{
        "type": "command",
        "command": "cd /Users/ms/workspace/claude/ai-survival-log && ./scripts/wiki lint --summary || true"
      }]
    }]
  }
}
```

> `|| true` — Stop 훅 실패 시에도 세션 정상 종료 보장

### git pre-commit (`.git/hooks/pre-commit`)

```bash
#!/bin/sh
# wiki 파일 변경 시에만 실행
git diff --cached --name-only | grep -q "^wiki/" || exit 0

cd "$(git rev-parse --show-toplevel)"
./scripts/wiki lint
if [ $? -ne 0 ]; then
  echo "❌ Wiki lint 실패 — 위 오류를 수정 후 재시도하세요."
  exit 1
fi
```

---

## 구현 범위 (Out of Scope)

- `log.md` 자동 갱신 (수동 기록 파일, 변경 없음)
- 증분(incremental) 업데이트 — sync는 항상 전체 재생성 (30파일 기준 <1초)
- 태그 파일명 slugify — 태그가 이미 `kebab-case` 형식

---

## 구현 순서

1. `scripts/wiki` Python CLI 작성
2. `pip install python-frontmatter` 확인 및 문서화
3. `settings.local.json` 훅 추가
4. `.git/hooks/pre-commit` 작성 + chmod +x
5. 동작 검증 (sync → lint → tags)
