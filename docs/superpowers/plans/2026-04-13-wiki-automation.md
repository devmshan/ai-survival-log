# Wiki 자동화 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** wiki 파일 수정 시 index.md + tags/ 자동 갱신, 커밋/세션 종료 시 lint 자동 실행

**Architecture:** Python CLI(`scripts/wiki_lib.py` + `scripts/wiki`)가 핵심 로직 담당. Claude Code PostToolUse 훅이 wiki 파일 수정 시 sync 실행. git pre-commit과 Stop 훅이 lint 실행.

**Tech Stack:** Python 3.11+, python-frontmatter, pytest

---

## 파일 구조

| 파일 | 역할 |
|------|------|
| `scripts/wiki_lib.py` | 핵심 로직 (scan, sync, lint, tags) |
| `scripts/wiki` | CLI 진입점 shebang wrapper (chmod +x) |
| `tests/test_wiki_lib.py` | pytest 단위 테스트 |
| `.claude/settings.local.json` | PostToolUse + Stop 훅 추가 |
| `.git/hooks/pre-commit` | lint 실행 shell script |

---

## Task 1: 환경 설정

**Files:**
- Create: `scripts/wiki_lib.py`
- Create: `scripts/wiki`
- Create: `tests/test_wiki_lib.py`
- Create: `requirements-wiki.txt`

- [ ] **Step 1: python-frontmatter 설치 확인**

```bash
pip install python-frontmatter
python3 -c "import frontmatter; print('ok')"
```

Expected: `ok`

- [ ] **Step 2: requirements-wiki.txt 생성**

```
python-frontmatter
pytest
```

- [ ] **Step 3: scripts/wiki_lib.py 스켈레톤 생성**

```python
#!/usr/bin/env python3
"""Wiki 자동화 라이브러리. pip install python-frontmatter 필요."""

import re
import sys
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

import frontmatter

WIKI_DIR = Path("wiki")
EXCLUDE_FILES = {"index.md", "log.md"}
EXCLUDE_DIRS = {"tags", ".obsidian"}


@dataclass
class Page:
    path: Path          # wiki/ 기준 상대 경로 (예: Path("concepts/ai.md"))
    title: str
    type: str           # entity | concept | source | topic | project
    status: str         # draft | active | archived
    tags: list[str]
    description: str
    content: str        # frontmatter 제외 본문


def scan_pages(wiki_dir: Path = WIKI_DIR) -> list[Page]:
    pass


def extract_wikilinks(content: str) -> list[str]:
    pass


def cmd_sync(wiki_dir: Path = WIKI_DIR) -> None:
    pass


def cmd_tags(wiki_dir: Path = WIKI_DIR) -> None:
    pass


def cmd_lint(wiki_dir: Path = WIKI_DIR, summary: bool = False) -> int:
    pass
```

- [ ] **Step 4: scripts/wiki CLI 진입점 생성**

```python
#!/usr/bin/env python3
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from wiki_lib import cmd_sync, cmd_tags, cmd_lint


def main():
    parser = argparse.ArgumentParser(description="Wiki 관리 CLI")
    sub = parser.add_subparsers(dest="cmd")

    sub.add_parser("sync", help="index.md + tags/ 재생성")

    lint_p = sub.add_parser("lint", help="무결성 검사")
    lint_p.add_argument("--summary", action="store_true")

    sub.add_parser("tags", help="tags/ 재생성")

    args = parser.parse_args()

    if args.cmd == "sync":
        cmd_sync()
    elif args.cmd == "lint":
        sys.exit(cmd_lint(summary=args.summary))
    elif args.cmd == "tags":
        cmd_tags()
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
```

- [ ] **Step 5: 실행 권한 부여**

```bash
chmod +x scripts/wiki
```

- [ ] **Step 6: tests/test_wiki_lib.py 빈 파일 생성**

```python
"""wiki_lib 단위 테스트."""
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))
import wiki_lib


# ── 테스트 헬퍼 ──────────────────────────────────────────────────────────────

def make_page(wiki_dir: Path, rel: str, **meta) -> Path:
    """frontmatter가 포함된 마크다운 파일 생성."""
    import frontmatter as fm
    content = meta.pop("content", "본문 내용")
    post = fm.Post(content, **meta)
    path = wiki_dir / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(fm.dumps(post), encoding="utf-8")
    return path
```

- [ ] **Step 7: 커밋**

```bash
git add scripts/wiki scripts/wiki_lib.py tests/test_wiki_lib.py requirements-wiki.txt
git commit -m "chore: wiki 자동화 CLI 스켈레톤 추가"
```

---

## Task 2: extract_wikilinks() 구현

**Files:**
- Modify: `scripts/wiki_lib.py`
- Modify: `tests/test_wiki_lib.py`

- [ ] **Step 1: 실패하는 테스트 작성**

`tests/test_wiki_lib.py`에 추가:

```python
class TestExtractWikilinks:
    def test_simple_link(self):
        result = wiki_lib.extract_wikilinks("본문 [[concepts/ai]] 내용")
        assert result == ["concepts/ai"]

    def test_alias_link(self):
        result = wiki_lib.extract_wikilinks("[[concepts/ai|AI 개념]]")
        assert result == ["concepts/ai"]

    def test_multiple_links(self):
        result = wiki_lib.extract_wikilinks("[[a/b]] 과 [[c/d|D]]")
        assert result == ["a/b", "c/d"]

    def test_no_links(self):
        result = wiki_lib.extract_wikilinks("링크 없는 본문")
        assert result == []
```

- [ ] **Step 2: 테스트 실행 — FAIL 확인**

```bash
pytest tests/test_wiki_lib.py::TestExtractWikilinks -v
```

Expected: `FAILED` (returns None, not list)

- [ ] **Step 3: extract_wikilinks() 구현**

`scripts/wiki_lib.py`의 `extract_wikilinks` 함수:

```python
def extract_wikilinks(content: str) -> list[str]:
    """[[link]] 와 [[link|alias]] 에서 링크 경로만 추출."""
    return re.findall(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]', content)
```

- [ ] **Step 4: 테스트 실행 — PASS 확인**

```bash
pytest tests/test_wiki_lib.py::TestExtractWikilinks -v
```

Expected: 4개 모두 PASSED

- [ ] **Step 5: 커밋**

```bash
git add scripts/wiki_lib.py tests/test_wiki_lib.py
git commit -m "feat: extract_wikilinks() 구현 — [[link|alias]] 파싱"
```

---

## Task 3: scan_pages() 구현

**Files:**
- Modify: `scripts/wiki_lib.py`
- Modify: `tests/test_wiki_lib.py`

- [ ] **Step 1: 실패하는 테스트 작성**

`tests/test_wiki_lib.py`에 추가:

```python
class TestScanPages:
    def test_scans_concept_page(self, tmp_path):
        make_page(tmp_path / "wiki", "concepts/ai.md",
                  title="AI 개념", type="concept", status="active",
                  tags=["ai", "ml"], description="AI 기초 개념")
        pages = wiki_lib.scan_pages(tmp_path / "wiki")
        assert len(pages) == 1
        p = pages[0]
        assert p.title == "AI 개념"
        assert p.type == "concept"
        assert p.tags == ["ai", "ml"]

    def test_excludes_index_and_log(self, tmp_path):
        wiki = tmp_path / "wiki"
        make_page(wiki, "concepts/ai.md", title="AI", type="concept",
                  status="active", tags=[], description="")
        make_page(wiki, "index.md", title="Index", type="", status="", tags=[], description="")
        make_page(wiki, "log.md", title="Log", type="", status="", tags=[], description="")
        pages = wiki_lib.scan_pages(wiki)
        assert len(pages) == 1
        assert pages[0].path == Path("concepts/ai.md")

    def test_excludes_tags_dir(self, tmp_path):
        wiki = tmp_path / "wiki"
        make_page(wiki, "concepts/ai.md", title="AI", type="concept",
                  status="active", tags=["ai"], description="")
        make_page(wiki, "tags/ai.md", title="Tag AI", type="", status="", tags=[], description="")
        pages = wiki_lib.scan_pages(wiki)
        assert len(pages) == 1

    def test_missing_frontmatter_uses_defaults(self, tmp_path):
        wiki = tmp_path / "wiki"
        p = wiki / "concepts" / "bare.md"
        p.parent.mkdir(parents=True)
        p.write_text("# 본문만 있는 파일", encoding="utf-8")
        pages = wiki_lib.scan_pages(wiki)
        assert pages[0].title == "bare"
        assert pages[0].type == ""
        assert pages[0].tags == []
```

- [ ] **Step 2: 테스트 실행 — FAIL 확인**

```bash
pytest tests/test_wiki_lib.py::TestScanPages -v
```

Expected: FAILED (scan_pages returns None)

- [ ] **Step 3: scan_pages() 구현**

`scripts/wiki_lib.py`의 `scan_pages` 함수:

```python
def scan_pages(wiki_dir: Path = WIKI_DIR) -> list[Page]:
    """wiki_dir 하위 마크다운 파일을 스캔하여 Page 목록 반환."""
    pages = []
    for md_file in sorted(wiki_dir.rglob("*.md")):
        rel = md_file.relative_to(wiki_dir)
        if rel.name in EXCLUDE_FILES:
            continue
        if any(part in EXCLUDE_DIRS for part in rel.parts):
            continue
        try:
            post = frontmatter.load(md_file)
        except Exception:
            continue
        pages.append(Page(
            path=rel,
            title=post.get("title", rel.stem),
            type=post.get("type", ""),
            status=post.get("status", "draft"),
            tags=list(post.get("tags", [])),
            description=post.get("description", ""),
            content=post.content,
        ))
    return pages
```

- [ ] **Step 4: 테스트 실행 — PASS 확인**

```bash
pytest tests/test_wiki_lib.py::TestScanPages -v
```

Expected: 4개 모두 PASSED

- [ ] **Step 5: 커밋**

```bash
git add scripts/wiki_lib.py tests/test_wiki_lib.py
git commit -m "feat: scan_pages() 구현 — frontmatter 파싱 + 제외 목록"
```

---

## Task 4: cmd_sync() — index.md 재생성

**Files:**
- Modify: `scripts/wiki_lib.py`
- Modify: `tests/test_wiki_lib.py`

- [ ] **Step 1: 실패하는 테스트 작성**

`tests/test_wiki_lib.py`에 추가:

```python
class TestCmdSync:
    def test_creates_index_md(self, tmp_path):
        wiki = tmp_path / "wiki"
        make_page(wiki, "concepts/ai.md", title="AI 개념", type="concept",
                  status="active", tags=["ai"], description="AI 기초")
        wiki_lib.cmd_sync(wiki)
        index = wiki / "index.md"
        assert index.exists()
        content = index.read_text(encoding="utf-8")
        assert "## Concepts" in content
        assert "[[concepts/ai]]" in content
        assert "AI 기초" in content

    def test_groups_by_type(self, tmp_path):
        wiki = tmp_path / "wiki"
        make_page(wiki, "concepts/c1.md", title="C1", type="concept",
                  status="active", tags=[], description="개념1")
        make_page(wiki, "entities/e1.md", title="E1", type="entity",
                  status="active", tags=[], description="엔티티1")
        wiki_lib.cmd_sync(wiki)
        content = (wiki / "index.md").read_text(encoding="utf-8")
        assert "## Entities" in content
        assert "## Concepts" in content
        # Entities 섹션이 Concepts보다 먼저 나옴
        assert content.index("## Entities") < content.index("## Concepts")

    def test_source_type_uses_origin_column(self, tmp_path):
        wiki = tmp_path / "wiki"
        make_page(wiki, "sources/2026-04-01-test.md", title="테스트 소스",
                  type="source", status="active", tags=["ai"], description="원본 설명")
        wiki_lib.cmd_sync(wiki)
        content = (wiki / "index.md").read_text(encoding="utf-8")
        assert "## Sources" in content
        assert "| 원본 |" in content

    def test_total_count_in_header(self, tmp_path):
        wiki = tmp_path / "wiki"
        make_page(wiki, "concepts/a.md", title="A", type="concept",
                  status="active", tags=[], description="")
        make_page(wiki, "concepts/b.md", title="B", type="concept",
                  status="active", tags=[], description="")
        wiki_lib.cmd_sync(wiki)
        content = (wiki / "index.md").read_text(encoding="utf-8")
        assert "총 2개 페이지" in content
```

- [ ] **Step 2: 테스트 실행 — FAIL 확인**

```bash
pytest tests/test_wiki_lib.py::TestCmdSync -v
```

Expected: FAILED (cmd_sync returns None, index.md not created)

- [ ] **Step 3: _write_index() 구현**

`scripts/wiki_lib.py`에 추가:

```python
_TYPE_ORDER = ["entity", "concept", "source", "topic", "project"]
_TYPE_LABELS = {
    "entity": "Entities",
    "concept": "Concepts",
    "source": "Sources",
    "topic": "Topics",
    "project": "Projects",
}


def _write_index(pages: list[Page], wiki_dir: Path) -> None:
    today = date.today().isoformat()
    groups: dict[str, list[Page]] = {t: [] for t in _TYPE_ORDER}
    for page in pages:
        if page.type in groups:
            groups[page.type].append(page)

    lines = [
        '---',
        'title: "Wiki Index"',
        f'updated: "{today}"',
        '---',
        '',
        '# Wiki Index',
        '',
        f'> 마지막 업데이트: {today} | 총 {len(pages)}개 페이지',
        '',
    ]

    for t in _TYPE_ORDER:
        group = sorted(groups[t], key=lambda p: str(p.path))
        if not group:
            continue
        lines.append(f'## {_TYPE_LABELS[t]}')
        lines.append('')
        if t == "source":
            lines.append('| 페이지 | 원본 | 태그 | 상태 |')
            lines.append('|--------|------|------|------|')
        else:
            lines.append('| 페이지 | 설명 | 태그 | 상태 |')
            lines.append('|--------|------|------|------|')
        for page in group:
            stem = str(page.path.with_suffix(''))
            tags_str = ', '.join(page.tags)
            lines.append(f'| [[{stem}]] | {page.description} | {tags_str} | {page.status} |')
        lines.append('')

    (wiki_dir / "index.md").write_text('\n'.join(lines), encoding='utf-8')
```

- [ ] **Step 4: cmd_sync() 구현 (index 부분만)**

```python
def cmd_sync(wiki_dir: Path = WIKI_DIR) -> None:
    pages = scan_pages(wiki_dir)
    _write_index(pages, wiki_dir)
    _write_tags(pages, wiki_dir)
    print(f"✓ sync 완료 — {len(pages)}개 페이지, index.md + tags/ 갱신")
```

(`_write_tags`는 다음 Task에서 구현. 지금은 `pass` 함수 남겨둠)

- [ ] **Step 5: 테스트 실행 — PASS 확인**

```bash
pytest tests/test_wiki_lib.py::TestCmdSync -v
```

Expected: 4개 모두 PASSED

- [ ] **Step 6: 커밋**

```bash
git add scripts/wiki_lib.py tests/test_wiki_lib.py
git commit -m "feat: cmd_sync() index.md 재생성 구현"
```

---

## Task 5: cmd_sync() — tags/ 재생성

**Files:**
- Modify: `scripts/wiki_lib.py`
- Modify: `tests/test_wiki_lib.py`

- [ ] **Step 1: 실패하는 테스트 작성**

`tests/test_wiki_lib.py`에 추가:

```python
class TestCmdTags:
    def test_creates_tag_file(self, tmp_path):
        wiki = tmp_path / "wiki"
        make_page(wiki, "concepts/ai.md", title="AI", type="concept",
                  status="active", tags=["ai", "ml"], description="AI 개념")
        wiki_lib.cmd_sync(wiki)
        assert (wiki / "tags" / "ai.md").exists()
        assert (wiki / "tags" / "ml.md").exists()

    def test_tag_file_contains_page_link(self, tmp_path):
        wiki = tmp_path / "wiki"
        make_page(wiki, "concepts/ai.md", title="AI", type="concept",
                  status="active", tags=["ai"], description="AI 개념")
        wiki_lib.cmd_sync(wiki)
        content = (wiki / "tags" / "ai.md").read_text(encoding="utf-8")
        assert "# Tag: ai" in content
        assert "[[concepts/ai]]" in content
        assert "AI 개념" in content

    def test_old_tag_files_removed_on_sync(self, tmp_path):
        wiki = tmp_path / "wiki"
        # 첫 번째 sync — "old-tag" 생성
        make_page(wiki, "concepts/a.md", title="A", type="concept",
                  status="active", tags=["old-tag"], description="")
        wiki_lib.cmd_sync(wiki)
        assert (wiki / "tags" / "old-tag.md").exists()
        # 태그 변경 후 두 번째 sync
        import frontmatter as fm
        p = wiki / "concepts" / "a.md"
        post = fm.load(p)
        post["tags"] = ["new-tag"]
        p.write_text(fm.dumps(post), encoding="utf-8")
        wiki_lib.cmd_sync(wiki)
        assert not (wiki / "tags" / "old-tag.md").exists()
        assert (wiki / "tags" / "new-tag.md").exists()

    def test_cmd_tags_standalone(self, tmp_path):
        wiki = tmp_path / "wiki"
        make_page(wiki, "concepts/ai.md", title="AI", type="concept",
                  status="active", tags=["ai"], description="")
        wiki_lib.cmd_tags(wiki)
        assert (wiki / "tags" / "ai.md").exists()
```

- [ ] **Step 2: 테스트 실행 — FAIL 확인**

```bash
pytest tests/test_wiki_lib.py::TestCmdTags -v
```

Expected: FAILED (_write_tags is pass)

- [ ] **Step 3: _write_tags() 구현**

`scripts/wiki_lib.py`에 추가:

```python
def _write_tags(pages: list[Page], wiki_dir: Path) -> None:
    tags_dir = wiki_dir / "tags"
    tags_dir.mkdir(exist_ok=True)
    # 기존 태그 파일 제거
    for f in tags_dir.glob("*.md"):
        f.unlink()
    # 태그별 페이지 그룹
    tag_map: dict[str, list[Page]] = {}
    for page in pages:
        for tag in page.tags:
            tag_map.setdefault(tag, []).append(page)
    for tag, tagged in sorted(tag_map.items()):
        lines = [
            f'# Tag: {tag}',
            '',
            '| 페이지 | 설명 | 타입 | 상태 |',
            '|--------|------|------|------|',
        ]
        for page in sorted(tagged, key=lambda p: str(p.path)):
            stem = str(page.path.with_suffix(''))
            lines.append(
                f'| [[{stem}]] | {page.description} | {page.type} | {page.status} |'
            )
        (tags_dir / f"{tag}.md").write_text('\n'.join(lines) + '\n', encoding='utf-8')


def cmd_tags(wiki_dir: Path = WIKI_DIR) -> None:
    pages = scan_pages(wiki_dir)
    _write_tags(pages, wiki_dir)
    print("✓ tags/ 갱신 완료")
```

- [ ] **Step 4: 테스트 실행 — PASS 확인**

```bash
pytest tests/test_wiki_lib.py::TestCmdTags -v
```

Expected: 4개 모두 PASSED

- [ ] **Step 5: 커밋**

```bash
git add scripts/wiki_lib.py tests/test_wiki_lib.py
git commit -m "feat: _write_tags() 구현 — wiki/tags/ 태그별 서브인덱스"
```

---

## Task 6: cmd_lint() 구현

**Files:**
- Modify: `scripts/wiki_lib.py`
- Modify: `tests/test_wiki_lib.py`

- [ ] **Step 1: 실패하는 테스트 작성**

`tests/test_wiki_lib.py`에 추가:

```python
class TestCmdLint:
    def test_passes_clean_wiki(self, tmp_path):
        wiki = tmp_path / "wiki"
        # 두 페이지가 서로 링크 → 고아 없음, 깨진 링크 없음
        make_page(wiki, "concepts/ai.md", title="AI", type="concept",
                  status="active", tags=["ai"], description="AI 개념",
                  content="본문 [[topics/ai-era]] 링크")
        make_page(wiki, "topics/ai-era.md", title="AI 시대", type="topic",
                  status="active", tags=["ai"], description="AI 시대 개요",
                  content="본문 [[concepts/ai]] 역링크")
        # index.md 생성
        wiki_lib.cmd_sync(wiki)
        result = wiki_lib.cmd_lint(wiki)
        assert result == 0

    def test_detects_broken_wikilink(self, tmp_path):
        wiki = tmp_path / "wiki"
        # wikilink는 확장자 없는 경로 형태 사용 (예: concepts/없는페이지)
        make_page(wiki, "concepts/ai.md", title="AI", type="concept",
                  status="active", tags=["ai"], description="AI",
                  content="[[concepts/없는페이지]] 깨진링크")
        wiki_lib.cmd_sync(wiki)
        result = wiki_lib.cmd_lint(wiki)
        assert result == 1

    def test_detects_orphan_page(self, tmp_path):
        wiki = tmp_path / "wiki"
        # ai.md는 connected.md를 링크하지만 orphan.md는 아무도 링크 안 함
        make_page(wiki, "concepts/ai.md", title="AI", type="concept",
                  status="active", tags=["ai"], description="AI",
                  content="[[concepts/connected]]")
        make_page(wiki, "concepts/connected.md", title="Connected", type="concept",
                  status="active", tags=["ai"], description="연결된 페이지",
                  content="[[concepts/ai]]")
        make_page(wiki, "concepts/orphan.md", title="고아", type="concept",
                  status="active", tags=[], description="아무도 링크 안 함")
        wiki_lib.cmd_sync(wiki)
        result = wiki_lib.cmd_lint(wiki)
        assert result == 1  # orphan.md 고아 감지

    def test_detects_missing_frontmatter_field(self, tmp_path):
        wiki = tmp_path / "wiki"
        # type 필드 없음
        make_page(wiki, "concepts/ai.md", title="AI",
                  status="active", tags=["ai"], description="AI")
        wiki_lib.cmd_sync(wiki)
        result = wiki_lib.cmd_lint(wiki)
        assert result == 1

    def test_summary_always_returns_0(self, tmp_path):
        wiki = tmp_path / "wiki"
        make_page(wiki, "concepts/ai.md", title="AI", type="concept",
                  status="active", tags=["ai"], description="AI",
                  content="[[concepts/없는페이지]]")
        wiki_lib.cmd_sync(wiki)
        result = wiki_lib.cmd_lint(wiki, summary=True)
        assert result == 0  # --summary는 항상 0
```

- [ ] **Step 2: 테스트 실행 — FAIL 확인**

```bash
pytest tests/test_wiki_lib.py::TestCmdLint -v
```

Expected: FAILED (cmd_lint returns None)

- [ ] **Step 3: cmd_lint() 구현**

`scripts/wiki_lib.py`의 `cmd_lint` 함수:

```python
def cmd_lint(wiki_dir: Path = WIKI_DIR, summary: bool = False) -> int:
    pages = scan_pages(wiki_dir)
    errors: list[str] = []

    # 유효한 페이지 경로 집합 (확장자 없는 stem 형태)
    valid_stems = {str(p.path.with_suffix('')) for p in pages}
    valid_stems.update({"index", "log"})  # 제외 파일도 유효한 링크 대상

    # index.md에 등록된 링크 집합
    index_path = wiki_dir / "index.md"
    index_links: set[str] = set()
    if index_path.exists():
        index_links = set(extract_wikilinks(index_path.read_text(encoding="utf-8")))

    # 고아 페이지 탐지: index.md 제외, content 페이지 링크만 집계
    # (index.md는 sync로 항상 전체 링크 → 고아 탐지 시 제외해야 의미 있음)
    all_linked_from_content: set[str] = set()
    for page in pages:
        all_linked_from_content.update(extract_wikilinks(page.content))

    for page in pages:
        stem = str(page.path.with_suffix(''))

        # 검사 1: 깨진 wikilink (wikilink는 확장자 없는 경로 형태 사용)
        for link in extract_wikilinks(page.content):
            if link not in valid_stems:
                errors.append(f"깨진 링크: [[{link}]] in {page.path}")

        # 검사 2: 고아 페이지 (content 페이지 어디서도 링크 안 됨)
        if stem not in all_linked_from_content:
            errors.append(f"고아 페이지: {page.path}")

        # 검사 3: index.md 누락
        if stem not in index_links:
            errors.append(f"index.md 누락: {page.path}")

        # 검사 4: 필수 frontmatter 필드
        for field_name in ("title", "type", "status"):
            if not getattr(page, field_name, ""):
                errors.append(f"frontmatter 누락 '{field_name}': {page.path}")

    if summary:
        if errors:
            print(f"⚠ lint: {len(errors)}개 오류 발견")
        else:
            print("✓ lint: 오류 없음")
        return 0

    for err in errors:
        print(f"❌ {err}", file=sys.stderr)
    if errors:
        print(f"\n총 {len(errors)}개 오류", file=sys.stderr)
        return 1
    print("✓ lint 통과")
    return 0
```

- [ ] **Step 4: 테스트 실행 — PASS 확인**

```bash
pytest tests/test_wiki_lib.py::TestCmdLint -v
```

Expected: 5개 모두 PASSED

- [ ] **Step 5: 전체 테스트 통과 확인**

```bash
pytest tests/test_wiki_lib.py -v
```

Expected: 모든 테스트 PASSED

- [ ] **Step 6: 커밋**

```bash
git add scripts/wiki_lib.py tests/test_wiki_lib.py
git commit -m "feat: cmd_lint() 구현 — 깨진 링크, 고아 페이지, frontmatter 검사"
```

---

## Task 7: Claude Code 훅 설정

**Files:**
- Modify: `.claude/settings.local.json`

- [ ] **Step 1: 현재 settings.local.json 읽기**

```bash
cat .claude/settings.local.json
```

- [ ] **Step 2: hooks 섹션 추가**

`.claude/settings.local.json`을 다음과 같이 수정 (기존 `permissions` 유지):

```json
{
  "permissions": {
    "allow": [
      "WebFetch(domain:github.com)",
      "WebFetch(domain:raw.githubusercontent.com)",
      "Bash(git add:*)",
      "Bash(git commit:*)",
      "Read(//Users/ms/workspace/claude/ai-survival-log-site/**)",
      "Bash(npx shadcn@latest add badge card command input separator --yes)"
    ]
  },
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "cd /Users/ms/workspace/claude/ai-survival-log && ./scripts/wiki sync"
          }
        ]
      }
    ],
    "Stop": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "cd /Users/ms/workspace/claude/ai-survival-log && ./scripts/wiki lint --summary || true"
          }
        ]
      }
    ]
  }
}
```

- [ ] **Step 3: 훅 동작 수동 검증**

```bash
./scripts/wiki sync
```

Expected: `✓ sync 완료 — N개 페이지, index.md + tags/ 갱신`

- [ ] **Step 4: 커밋**

```bash
git add .claude/settings.local.json
git commit -m "chore: Claude Code PostToolUse + Stop 훅 추가"
```

---

## Task 8: git pre-commit 훅

**Files:**
- Create: `.git/hooks/pre-commit`

- [ ] **Step 1: pre-commit 스크립트 작성**

`.git/hooks/pre-commit` 파일 생성:

```bash
#!/bin/sh
# wiki 파일이 staged에 포함된 경우에만 lint 실행
git diff --cached --name-only | grep -q "^wiki/" || exit 0

cd "$(git rev-parse --show-toplevel)"
./scripts/wiki lint
if [ $? -ne 0 ]; then
  echo ""
  echo "❌ Wiki lint 실패 — 위 오류를 수정 후 재시도하세요."
  echo "   건너뛰려면: git commit --no-verify"
  exit 1
fi
```

- [ ] **Step 2: 실행 권한 부여**

```bash
chmod +x .git/hooks/pre-commit
```

- [ ] **Step 3: lint 통과 시 커밋 정상 진행 확인**

```bash
touch test-dummy.txt
git add test-dummy.txt
git commit -m "test: pre-commit 훅 테스트 (wiki 파일 없음)"
```

Expected: 커밋 성공 (wiki 파일 미포함이므로 lint 건너뜀)

- [ ] **Step 4: 더미 파일 제거**

```bash
git rm test-dummy.txt
git commit -m "chore: 테스트 더미 파일 제거"
```

- [ ] **Step 5: wiki 파일 포함 커밋 시 lint 실행 확인**

```bash
# 임시로 깨진 링크 추가
echo "[[concepts/존재하지않는페이지]]" >> wiki/concepts/llm-wiki-pattern.md
git add wiki/concepts/llm-wiki-pattern.md
git commit -m "test: lint 차단 확인"
```

Expected: `❌ 깨진 링크: [[concepts/존재하지않는페이지]]` 출력 후 커밋 차단

- [ ] **Step 6: 임시 변경 되돌리기**

```bash
git checkout -- wiki/concepts/llm-wiki-pattern.md
```

---

## Task 9: 통합 검증

**Files:** 없음 (기존 wiki 파일 대상)

- [ ] **Step 1: 전체 sync 실행**

```bash
./scripts/wiki sync
```

Expected:
```
✓ sync 완료 — 32개 페이지, index.md + tags/ 갱신
```

- [ ] **Step 2: index.md 내용 확인**

```bash
head -20 wiki/index.md
```

Expected: frontmatter + `# Wiki Index` + `> 마지막 업데이트: 2026-04-13 | 총 32개 페이지`

- [ ] **Step 3: tags/ 폴더 확인**

```bash
ls wiki/tags/
```

Expected: `ai.md`, `context-graph.md`, `knowledge-graph.md` 등 태그 파일 목록

- [ ] **Step 4: lint 전체 실행**

```bash
./scripts/wiki lint
```

Expected: `✓ lint 통과` 또는 실제 오류 목록 출력

- [ ] **Step 5: 최종 커밋**

```bash
git add wiki/index.md wiki/tags/ .git/hooks/pre-commit
git commit -m "feat: wiki 자동화 완성 — sync, lint, tags/ 서브인덱스"
```
