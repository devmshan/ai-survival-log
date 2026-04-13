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
    """위키 무결성 검사: 깨진 링크, 고아 페이지, 누락된 frontmatter 검사."""
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

    # 고아 페이지 탐지: content 페이지 링크만 집계 (index.md 제외)
    all_linked_from_content: set[str] = set()
    for page in pages:
        all_linked_from_content.update(extract_wikilinks(page.content))

    for page in pages:
        stem = str(page.path.with_suffix(''))

        # 검사 1: 깨진 wikilink
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
