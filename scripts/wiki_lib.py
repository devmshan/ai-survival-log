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
