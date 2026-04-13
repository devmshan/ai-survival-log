"""Wiki 자동화 라이브러리. pip install python-frontmatter 필요."""

import re
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path

import frontmatter

WIKI_DIR = Path("wiki")
EXCLUDE_FILES = {"index.md", "log.md"}
EXCLUDE_DIRS = {"tags", ".obsidian"}


@dataclass
class Page:
    """Wiki 페이지 메타데이터와 본문을 담는 데이터 클래스."""

    path: Path          # wiki/ 기준 상대 경로 (예: Path("concepts/ai.md"))
    title: str
    type: str           # entity | concept | source | topic | project
    status: str         # draft | active | archived
    tags: list[str]
    description: str
    content: str        # frontmatter 제외 본문


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


def extract_wikilinks(content: str) -> list[str]:
    """[[link]] 와 [[link|alias]] 에서 링크 경로만 추출."""
    return re.findall(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]', content)


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


def cmd_sync(wiki_dir: Path = WIKI_DIR) -> None:
    pages = scan_pages(wiki_dir)
    _write_index(pages, wiki_dir)
    _write_tags(pages, wiki_dir)
    print(f"✓ sync 완료 — {len(pages)}개 페이지, index.md + tags/ 갱신")


def cmd_tags(wiki_dir: Path = WIKI_DIR) -> None:
    pages = scan_pages(wiki_dir)
    _write_tags(pages, wiki_dir)
    print("✓ tags/ 갱신 완료")


def cmd_lint(wiki_dir: Path = WIKI_DIR, summary: bool = False) -> int:
    pass
