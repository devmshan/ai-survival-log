import json
import sys
from pathlib import Path

import frontmatter as fm

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))
import state_lib


def make_page(wiki_dir: Path, rel: str, **meta) -> Path:
    content = meta.pop("content", "본문")
    post = fm.Post(content, **meta)
    path = wiki_dir / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(fm.dumps(post), encoding="utf-8")
    return path


class TestStateExports:
    def test_export_wiki_index_writes_counts_and_entries(self, tmp_path):
        wiki = tmp_path / "wiki"
        output_state = tmp_path / "output" / "state"
        make_page(
            wiki,
            "concepts/ai.md",
            title="AI",
            type="concept",
            status="active",
            tags=["ai"],
            description="AI 개념",
        )

        output_path = state_lib.export_wiki_index(
            wiki_dir=wiki,
            output_state_dir=output_state,
        )

        payload = json.loads(output_path.read_text(encoding="utf-8"))
        assert payload["totalPages"] == 1
        assert payload["countsByType"] == {"concept": 1}
        assert payload["entries"][0]["path"] == "concepts/ai.md"

    def test_export_publish_manifest_writes_publishable_entries(self, tmp_path):
        wiki = tmp_path / "wiki"
        output_state = tmp_path / "output" / "state"
        output_blog = tmp_path / "output" / "blog"
        site = tmp_path / "site"
        assets_blog = tmp_path / "assets" / "blog"
        (site / "public" / "images" / "example").mkdir(parents=True)
        (site / "public" / "images" / "example" / "shot.png").write_text("png", encoding="utf-8")
        assets_blog.mkdir(parents=True)
        (assets_blog / "shot.png").write_text("png", encoding="utf-8")
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
            updated="2026-04-22",
            content="![img](/images/example/shot.png)",
        )

        output_path = state_lib.export_publish_manifest(
            wiki_dir=wiki,
            site_root=site,
            output_blog_dir=output_blog,
            output_state_dir=output_state,
        )

        payload = json.loads(output_path.read_text(encoding="utf-8"))
        assert payload["totalPublishedPages"] == 1
        assert payload["totalInvalidPublishedPages"] == 0
        entry = payload["entries"][0]
        assert entry["slug"] == "example-post"
        assert entry["outputPath"].endswith("2026-04-22-example-post.mdx")
        assert entry["images"] == ["/images/example/shot.png"]

    def test_export_publish_manifest_separates_invalid_entries(self, tmp_path):
        wiki = tmp_path / "wiki"
        output_state = tmp_path / "output" / "state"
        output_blog = tmp_path / "output" / "blog"
        site = tmp_path / "site"
        make_page(
            wiki,
            "topics/invalid.md",
            title="잘못된 글",
            type="topic",
            status="active",
            tags=["ai"],
            description="잘못된 설명",
            published=True,
            slug="invalid-post",
            updated="2026-04-22",
            series="시리즈",
        )

        output_path = state_lib.export_publish_manifest(
            wiki_dir=wiki,
            site_root=site,
            output_blog_dir=output_blog,
            output_state_dir=output_state,
        )

        payload = json.loads(output_path.read_text(encoding="utf-8"))
        assert payload["totalPublishedPages"] == 0
        assert payload["totalInvalidPublishedPages"] == 1
        assert payload["invalidEntries"][0]["slug"] == "invalid-post"
        assert payload["invalidEntries"][0]["errors"]

    def test_export_agent_surface_summary_checks_required_files(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        for relative in [
            "README.md",
            "AGENTS.md",
            "CLAUDE.md",
            ".codex/AGENTS.md",
            "ARCHITECTURE.md",
            "docs/operating/operations.md",
            "docs/publishing-contract.md",
            "docs/content-seo-guide.md",
        ]:
            path = tmp_path / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("ok", encoding="utf-8")

        output_path = state_lib.export_agent_surface_summary(
            output_state_dir=tmp_path / "output" / "state",
        )

        payload = json.loads(output_path.read_text(encoding="utf-8"))
        assert payload["allRequiredPresent"] is True
        assert all(item["exists"] for item in payload["requiredFiles"])
