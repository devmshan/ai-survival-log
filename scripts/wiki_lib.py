"""Wiki 자동화 라이브러리. pip install python-frontmatter 필요."""

import re
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any

import frontmatter

WIKI_DIR = Path("wiki")
EXCLUDE_FILES = {"index.md", "log.md"}
EXCLUDE_DIRS = {"tags", ".obsidian"}
SITE_ROOT = Path("../ai-survival-log-site")
OUTPUT_BLOG_DIR = Path("output/blog")


@dataclass
class Page:
    """Wiki 페이지 메타데이터와 본문을 담는 데이터 클래스."""

    path: Path          # wiki/ 기준 상대 경로 (예: Path("concepts/ai.md"))
    title: str
    type: str           # entity | concept | source | topic | project | synthesis
    status: str         # draft | active | archived
    tags: list[str]
    description: str
    content: str        # frontmatter 제외 본문


@dataclass
class PublishedPage:
    """Publish 가능한 페이지의 최소 메타데이터."""

    stem: str
    title: str
    slug: str


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


def extract_image_paths(content: str) -> list[str]:
    """마크다운 이미지 경로 추출."""
    return re.findall(r'!\[[^\]]*\]\(([^)]+)\)', content)


_TYPE_ORDER = ["entity", "concept", "source", "topic", "project", "synthesis"]
_TYPE_LABELS = {
    "entity": "Entities",
    "concept": "Concepts",
    "source": "Sources",
    "topic": "Topics",
    "project": "Projects",
    "synthesis": "Syntheses",
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


def _scan_published_pages(wiki_dir: Path) -> dict[str, PublishedPage]:
    published_pages: dict[str, PublishedPage] = {}
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
        if not post.get("published") or not post.get("slug"):
            continue
        stem = str(rel.with_suffix(""))
        published_pages[stem] = PublishedPage(
            stem=stem,
            title=post.get("title", rel.stem),
            slug=post["slug"],
        )
    return published_pages


def _strip_leading_h1(content: str) -> str:
    lines = content.splitlines()
    start = 0
    while start < len(lines) and lines[start].strip() == "":
        start += 1
    if start < len(lines) and lines[start].startswith("# "):
        start += 1
        while start < len(lines) and lines[start].strip() == "":
            start += 1
    return "\n".join(lines[start:]).strip() + "\n"


def _remove_related_pages_section(content: str) -> str:
    return re.sub(r"\n## 관련 페이지[\s\S]*$", "\n", content).strip() + "\n"


def _convert_wikilinks(content: str, published_pages: dict[str, PublishedPage]) -> str:
    def replace(match: re.Match[str]) -> str:
        target = match.group(1)
        alias = match.group(2)
        page = published_pages.get(target)
        label = alias or (page.title if page else target.split("/")[-1].replace("-", " "))
        if page:
            return f"[{label}](/posts/{page.slug})"
        return label

    return re.sub(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]", replace, content)


def _validate_publishable(
    post: frontmatter.Post,
    rel_path: Path,
    site_root: Path,
    assets_blog_dir: Path,
) -> list[str]:
    errors: list[str] = []

    if not post.get("published"):
        errors.append(f"published: true 아님: {rel_path}")
    if not post.get("slug"):
        errors.append(f"slug 누락: {rel_path}")
    if not post.get("description"):
        errors.append(f"description 누락: {rel_path}")
    if post.get("status") != "active":
        errors.append(f"status가 active 아님: {rel_path}")

    if post.get("series") and not post.get("seriesSlug"):
        errors.append(f"seriesSlug 누락: {rel_path}")
    if post.get("series") and post.get("seriesOrder") is None:
        errors.append(f"seriesOrder 누락: {rel_path}")

    for field_name in ("seoTitle", "seoDescription"):
        value = post.get(field_name)
        if value is not None and not isinstance(value, str):
            errors.append(f"{field_name} 형식 오류: {rel_path}")

    for image_path in extract_image_paths(post.content):
        if not image_path.startswith("/images/"):
            errors.append(f"이미지 경로 형식 오류: {rel_path} -> {image_path}")
            continue
        if any(ord(ch) > 127 for ch in Path(image_path).name):
            errors.append(f"이미지 파일명은 ASCII kebab-case 권장: {rel_path} -> {image_path}")
        upstream_image = assets_blog_dir / Path(image_path).name
        if not upstream_image.exists():
            errors.append(f"upstream 이미지 누락: {rel_path} -> {upstream_image}")
        served_image = site_root / "public" / image_path.lstrip("/")
        if not served_image.exists():
            errors.append(f"downstream 이미지 누락: {rel_path} -> {image_path}")

    return errors


def _format_frontmatter_list(values: list[str]) -> str:
    return "[" + ", ".join(f'"{value}"' for value in values) + "]"


def _build_mdx_frontmatter(post: frontmatter.Post) -> str:
    lines = [
        "---",
        f'title: "{post["title"]}"',
    ]
    if post.get("seoTitle"):
        lines.append(f'seoTitle: "{post["seoTitle"]}"')
    lines.extend([
        f'date: "{post.get("updated") or post.get("created")}"',
        f"tags: {_format_frontmatter_list(list(post.get('tags', [])))}",
        f'description: "{post["description"]}"',
    ])
    if post.get("seoDescription"):
        lines.append(f'seoDescription: "{post["seoDescription"]}"')
    if post.get("thumbnail"):
        lines.append(f'thumbnail: "{post["thumbnail"]}"')
    lines.append("draft: false")
    if post.get("series"):
        lines.append(f'series: "{post["series"]}"')
        lines.append(f'seriesSlug: "{post["seriesSlug"]}"')
        lines.append(f"seriesOrder: {post['seriesOrder']}")
    lines.append("---")
    return "\n".join(lines) + "\n\n"


def _target_post_path(post: frontmatter.Post, output_blog_dir: Path) -> Path:
    output_dir = output_blog_dir
    output_dir.mkdir(parents=True, exist_ok=True)
    date_prefix = post.get("updated") or post.get("created")
    return output_dir / f"{date_prefix}-{post['slug']}.mdx"


def _render_mdx(post: frontmatter.Post, published_pages: dict[str, PublishedPage]) -> str:
    content = post.content
    content = _strip_leading_h1(content)
    content = _remove_related_pages_section(content)
    content = _convert_wikilinks(content, published_pages)
    return _build_mdx_frontmatter(post) + content.rstrip() + "\n"


def cmd_publish(
    target: str | None = None,
    wiki_dir: Path = WIKI_DIR,
    site_root: Path = SITE_ROOT,
    output_blog_dir: Path = OUTPUT_BLOG_DIR,
    publish_all: bool = False,
) -> int:
    published_pages = _scan_published_pages(wiki_dir)
    assets_blog_dir = wiki_dir.parent / "assets" / "blog"
    if not published_pages:
        print("발행 가능한 페이지가 없습니다.")
        return 0

    if target is None and not publish_all:
        print("published: true 페이지 목록:")
        for page in published_pages.values():
            print(f"- {page.stem} -> /posts/{page.slug}")
        return 0

    targets: list[Path] = []
    if publish_all:
        targets = [wiki_dir / f"{page.stem}.md" for page in published_pages.values()]
    else:
        normalized = target.removeprefix("wiki/")
        path = Path(normalized)
        if path.suffix != ".md":
            path = path.with_suffix(".md")
        targets = [wiki_dir / path]

    errors: list[str] = []
    written: list[tuple[Path, Path]] = []

    for md_path in targets:
        rel_path = md_path.relative_to(wiki_dir)
        post = frontmatter.load(md_path)
        errors.extend(_validate_publishable(post, rel_path, site_root, assets_blog_dir))
        if errors:
            continue
        output_path = _target_post_path(post, output_blog_dir)
        output_path.write_text(_render_mdx(post, published_pages), encoding="utf-8")
        written.append((rel_path, output_path))

    if errors:
        for error in errors:
            print(f"❌ {error}", file=sys.stderr)
        return 1

    for rel_path, output_path in written:
        print(f"✓ publish 완료: {rel_path} -> {output_path}")
    return 0


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
