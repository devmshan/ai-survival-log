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


def cmd_sync(wiki_dir: Path = WIKI_DIR) -> None:
    pass


def cmd_tags(wiki_dir: Path = WIKI_DIR) -> None:
    pass


def cmd_lint(wiki_dir: Path = WIKI_DIR, summary: bool = False) -> int:
    pass
