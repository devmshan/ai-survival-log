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


class TestCmdPublish:
    def test_lists_published_pages_when_no_target(self, tmp_path, capsys):
        wiki = tmp_path / "wiki"
        make_page(
            wiki,
            "topics/example.md",
            title="예제 글",
            type="topic",
            status="active",
            tags=["ai"],
            description="예제 설명",
            published=True,
            slug="example-post",
        )
        result = wiki_lib.cmd_publish(wiki_dir=wiki, site_root=tmp_path / "site")
        captured = capsys.readouterr()
        assert result == 0
        assert "topics/example" in captured.out
        assert "/posts/example-post" in captured.out

    def test_publishes_page_with_seo_and_series_fields(self, tmp_path):
        wiki = tmp_path / "wiki"
        site = tmp_path / "site"
        output_blog = tmp_path / "output" / "blog"
        (site / "public" / "images" / "lab").mkdir(parents=True)
        (site / "public" / "images" / "lab" / "shot.png").write_text("png", encoding="utf-8")
        (tmp_path / "assets" / "blog").mkdir(parents=True)
        (tmp_path / "assets" / "blog" / "shot.png").write_text("png", encoding="utf-8")
        make_page(
            wiki,
            "topics/example.md",
            title="예제 글",
            type="topic",
            status="active",
            tags=["ai", "study"],
            description="예제 설명",
            published=True,
            slug="example-post",
            updated="2026-04-18",
            seoTitle="검색용 제목",
            seoDescription="검색용 설명",
            series="실습 시리즈",
            seriesSlug="lab",
            seriesOrder=1,
            content="# 예제 글\n\n본문 [[topics/other|다른 글]]\n\n![샷](/images/lab/shot.png)\n\n## 관련 페이지\n\n- [[topics/other]]",
        )
        make_page(
            wiki,
            "topics/other.md",
            title="다른 글",
            type="topic",
            status="active",
            tags=["ai"],
            description="다른 설명",
            published=True,
            slug="other-post",
            updated="2026-04-17",
            content="# 다른 글\n\n본문",
        )
        result = wiki_lib.cmd_publish(
            "wiki/topics/example.md",
            wiki_dir=wiki,
            site_root=site,
            output_blog_dir=output_blog,
        )

        assert result == 0
        output = output_blog / "2026-04-18-example-post.mdx"
        assert output.exists()
        content = output.read_text(encoding="utf-8")
        assert 'seoTitle: "검색용 제목"' in content
        assert 'seoDescription: "검색용 설명"' in content
        assert 'seriesSlug: "lab"' in content
        assert "seriesOrder: 1" in content
        assert "[다른 글](/posts/other-post)" in content
        assert "## 관련 페이지" not in content
        assert content.startswith("---\n")
        assert "# 예제 글" not in content

    def test_publish_fails_when_series_slug_missing(self, tmp_path):
        wiki = tmp_path / "wiki"
        site = tmp_path / "site"
        output_blog = tmp_path / "output" / "blog"
        make_page(
            wiki,
            "topics/example.md",
            title="예제 글",
            type="topic",
            status="active",
            tags=["ai"],
            description="예제 설명",
            published=True,
            slug="example-post",
            updated="2026-04-18",
            series="실습 시리즈",
            content="# 예제 글\n\n본문",
        )
        result = wiki_lib.cmd_publish(
            "wiki/topics/example.md",
            wiki_dir=wiki,
            site_root=site,
            output_blog_dir=output_blog,
        )

        assert result == 1

    def test_publish_fails_when_image_missing_in_site_public(self, tmp_path):
        wiki = tmp_path / "wiki"
        site = tmp_path / "site"
        output_blog = tmp_path / "output" / "blog"
        (tmp_path / "assets" / "blog").mkdir(parents=True)
        (tmp_path / "assets" / "blog" / "missing.png").write_text("png", encoding="utf-8")
        make_page(
            wiki,
            "topics/example.md",
            title="예제 글",
            type="topic",
            status="active",
            tags=["ai"],
            description="예제 설명",
            published=True,
            slug="example-post",
            updated="2026-04-18",
            content="# 예제 글\n\n![샷](/images/lab/missing.png)",
        )
        result = wiki_lib.cmd_publish(
            "wiki/topics/example.md",
            wiki_dir=wiki,
            site_root=site,
            output_blog_dir=output_blog,
        )

        assert result == 1

    def test_publish_fails_when_image_missing_in_assets_blog(self, tmp_path):
        wiki = tmp_path / "wiki"
        site = tmp_path / "site"
        output_blog = tmp_path / "output" / "blog"
        (site / "public" / "images" / "lab").mkdir(parents=True)
        (site / "public" / "images" / "lab" / "shot.png").write_text("png", encoding="utf-8")
        make_page(
            wiki,
            "topics/example.md",
            title="예제 글",
            type="topic",
            status="active",
            tags=["ai"],
            description="예제 설명",
            published=True,
            slug="example-post",
            updated="2026-04-18",
            content="# 예제 글\n\n![샷](/images/lab/shot.png)",
        )

        result = wiki_lib.cmd_publish(
            "wiki/topics/example.md",
            wiki_dir=wiki,
            site_root=site,
            output_blog_dir=output_blog,
        )

        assert result == 1
