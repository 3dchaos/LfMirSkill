from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit


LINK_PATTERN = re.compile(r"(?<!!)\[[^\]]*]\(([^)]+)\)|!\[[^\]]*]\(([^)]+)\)")


def iter_markdown_links(path: Path):
    text = path.read_text(encoding="utf-8")
    for match in LINK_PATTERN.finditer(text):
        target = match.group(1) or match.group(2)
        target = target.strip().strip("<>")
        if not target or target.startswith("#"):
            continue
        split = urlsplit(target)
        if split.scheme or split.netloc:
            continue
        yield unquote(split.path)


def validate(root: Path) -> dict[str, object]:
    manifest_path = root / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8")) if manifest_path.exists() else {}
    markdown_files = sorted(root.rglob("*.md"))
    chapter_files = sorted((root / "chapters").rglob("*.md")) if (root / "chapters").exists() else []
    asset_files = [p for p in (root / "assets").rglob("*") if p.is_file()] if (root / "assets").exists() else []

    missing_links = []
    for md in markdown_files:
        for link in iter_markdown_links(md):
            target = (md.parent / link).resolve()
            if not target.exists():
                missing_links.append(
                    {
                        "file": md.relative_to(root).as_posix(),
                        "target": link,
                    }
                )

    mojibake_markers = ["����", "锟斤拷"]
    mojibake_files = []
    for md in markdown_files:
        text = md.read_text(encoding="utf-8", errors="replace")
        if any(marker in text for marker in mojibake_markers):
            mojibake_files.append(md.relative_to(root).as_posix())

    return {
        "index_exists": (root / "index.md").exists(),
        "manifest_exists": manifest_path.exists(),
        "chapter_files": len(chapter_files),
        "asset_files": len(asset_files),
        "manifest_chapter_count": manifest.get("chapter_count"),
        "manifest_asset_count": manifest.get("asset_count"),
        "missing_link_count": len(missing_links),
        "missing_links_sample": missing_links[:20],
        "mojibake_file_count": len(mojibake_files),
        "mojibake_files_sample": mojibake_files[:20],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Statically validate a generated Markdown knowledge base.")
    parser.add_argument("--root", default="codex-skills/lf-mir200-knowledge/knowledge_base")
    args = parser.parse_args()
    report = validate(Path(args.root))
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if report["missing_link_count"] or not report["index_exists"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
