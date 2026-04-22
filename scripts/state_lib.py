import json
from datetime import datetime, timezone
from pathlib import Path

import frontmatter

from wiki_lib import (
    OUTPUT_BLOG_DIR,
    SITE_ROOT,
    WIKI_DIR,
    _scan_published_pages,
    _validate_publishable,
    extract_image_paths,
    scan_pages,
)


OUTPUT_STATE_DIR = Path("output/state")


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def export_wiki_index(
    wiki_dir: Path = WIKI_DIR,
    output_state_dir: Path = OUTPUT_STATE_DIR,
) -> Path:
    pages = scan_pages(wiki_dir)
    by_type: dict[str, int] = {}
    entries = []

    for page in pages:
        by_type[page.type] = by_type.get(page.type, 0) + 1
        entries.append({
            "path": str(page.path),
            "title": page.title,
            "type": page.type,
            "status": page.status,
            "tags": page.tags,
            "description": page.description,
        })

    payload = {
        "source": "wiki/",
        "totalPages": len(pages),
        "countsByType": by_type,
        "entries": entries,
    }
    output_path = output_state_dir / "wiki-index.json"
    write_json(output_path, payload)
    return output_path


def export_publish_manifest(
    wiki_dir: Path = WIKI_DIR,
    site_root: Path = SITE_ROOT,
    output_blog_dir: Path = OUTPUT_BLOG_DIR,
    output_state_dir: Path = OUTPUT_STATE_DIR,
) -> Path:
    published_pages = _scan_published_pages(wiki_dir)
    assets_blog_dir = wiki_dir.parent / "assets" / "blog"
    entries = []
    invalid_entries = []

    for stem, published in sorted(published_pages.items()):
        md_path = wiki_dir / f"{stem}.md"
        try:
            post = frontmatter.load(md_path)
        except Exception as exc:
            raise RuntimeError(f"failed to parse publishable wiki page: {md_path}") from exc

        validation_errors = _validate_publishable(
            post=post,
            rel_path=md_path.relative_to(wiki_dir),
            site_root=site_root,
            assets_blog_dir=assets_blog_dir,
        )
        date_prefix = post.get("updated") or post.get("created") or ""
        image_paths = extract_image_paths(post.content)
        output_path = output_blog_dir / f"{date_prefix}-{published.slug}.mdx"
        entry = {
            "wikiPath": str(md_path.relative_to(wiki_dir.parent)),
            "title": post.get("title", published.title),
            "slug": published.slug,
            "datePrefix": date_prefix,
            "outputPath": str(output_path),
            "series": post.get("series"),
            "seriesSlug": post.get("seriesSlug"),
            "seriesOrder": post.get("seriesOrder"),
            "images": image_paths,
        }
        if validation_errors:
            invalid_entries.append({
                **entry,
                "errors": validation_errors,
            })
            continue
        entries.append(entry)

    payload = {
        "source": "wiki/",
        "totalPublishedPages": len(entries),
        "totalInvalidPublishedPages": len(invalid_entries),
        "entries": entries,
        "invalidEntries": invalid_entries,
    }
    output_path = output_state_dir / "publish-manifest.json"
    write_json(output_path, payload)
    return output_path


def export_agent_surface_summary(
    output_state_dir: Path = OUTPUT_STATE_DIR,
) -> Path:
    expected_files = [
        "README.md",
        "AGENTS.md",
        "CLAUDE.md",
        ".codex/AGENTS.md",
        "ARCHITECTURE.md",
        "docs/operating/operations.md",
        "docs/publishing-contract.md",
        "docs/content-seo-guide.md",
    ]
    files = []

    for relative in expected_files:
        path = Path(relative)
        files.append({
            "path": relative,
            "exists": path.exists(),
        })

    payload = {
        "source": "repository-surface",
        "requiredFiles": files,
        "allRequiredPresent": all(item["exists"] for item in files),
    }
    output_path = output_state_dir / "agent-surface-summary.json"
    write_json(output_path, payload)
    return output_path
