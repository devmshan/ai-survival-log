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
