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
