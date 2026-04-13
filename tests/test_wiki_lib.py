"""wiki_lib 단위 테스트."""
import sys
from pathlib import Path

import frontmatter as fm
import pytest

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))
import wiki_lib


# ── 테스트 헬퍼 ──────────────────────────────────────────────────────────────

def make_page(wiki_dir: Path, rel: str, **meta) -> Path:
    """frontmatter가 포함된 마크다운 파일 생성."""
    content = meta.pop("content", "본문 내용")
    post = fm.Post(content, **meta)
    path = wiki_dir / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(fm.dumps(post), encoding="utf-8")
    return path


# ── extract_wikilinks 테스트 ─────────────────────────────────────────────────

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
