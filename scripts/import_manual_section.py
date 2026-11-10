#!/usr/bin/env python3
"""Import an extracted CHM manual into the LF knowledge base as an extra section.

The LF engine manual lives in ``knowledge_base/chapters`` with a flat numbering
scheme. Extra manuals (for example the 老GOM / PG 盘古插件 manual) are kept in
their own sub-directory so the two numbering schemes never collide:

    knowledge_base/chapters/<section>/NNN-title.md
    knowledge_base/assets/<section>/...

Chapter links are rewritten from ``../assets/...`` to
``../../assets/<section>/...`` and only assets referenced by a kept chapter are
copied, which keeps the repository small.

Usage:

    python scripts/import_manual_section.py \
        --source "<dir produced by hh.exe -decompile>" \
        --section pg-plugin \
        --title "老GOM PG插件使用说明书"
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import tempfile
from pathlib import Path

from convert_chm_to_md import convert

DEFAULT_SKILL = Path("codex-skills") / "lf-mir200-knowledge"
TOC_HEADING = "## 目录"
TOC_END_HEADING = "## 未在原目录中列出的页面"
BEGIN_MARK = "<!-- extra-section:begin -->"
END_MARK = "<!-- extra-section:end -->"
ASSET_LINK_RE = re.compile(r"\.\./assets/([^)\"\s]+)")
SKIP_TITLE_PREFIXES = ("header", "待添加")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Import an extra CHM manual section.")
    parser.add_argument("--source", type=Path, required=True, help="Extracted CHM directory (contains a .HHC).")
    parser.add_argument("--section", default="pg-plugin", help="Sub-directory name under chapters/ and assets/.")
    parser.add_argument("--title", default="老GOM PG插件使用说明书", help="Section heading written into index.md.")
    parser.add_argument("--skill", type=Path, default=DEFAULT_SKILL, help="Skill package directory.")
    parser.add_argument("--keep", action="append", default=[], help="Extra chapter stem to keep although the TOC omits it.")
    return parser.parse_args()


def chapter_title(markdown: str, fallback: str) -> str:
    for line in markdown.splitlines():
        match = re.match(r"^#\s+(.+?)\s*$", line)
        if match:
            return match.group(1).strip()
    return fallback


def should_drop(stem: str, title: str) -> bool:
    lowered = title.strip().lower()
    return any(lowered.startswith(prefix) for prefix in SKIP_TITLE_PREFIXES) or stem.endswith("-header")


def extract_toc(index_text: str) -> list[str]:
    """Return the TOC block (without the heading lines) from a generated index.md."""
    lines = index_text.splitlines()
    try:
        start = lines.index(TOC_HEADING) + 1
    except ValueError:
        return []
    end = len(lines)
    if TOC_END_HEADING in lines:
        end = lines.index(TOC_END_HEADING)
    return [line for line in lines[start:end] if line.strip()]


def normalize_heading(text: str) -> str:
    """Strip bold markers that CHM authors sometimes put inside the H1 title."""
    lines = text.splitlines()
    if lines:
        match = re.fullmatch(r"#\s+\*\*(.+?)\*\*\s*", lines[0])
        if match:
            lines[0] = f"# {match.group(1)}"
    return "\n".join(lines) + ("\n" if text.endswith("\n") else "")


def copy_chapters(staged: Path, target_dir: Path, keep: set[str]) -> tuple[list[str], list[str]]:
    if target_dir.exists():
        shutil.rmtree(target_dir)
    target_dir.mkdir(parents=True)
    kept: list[str] = []
    extras: list[str] = []
    for source in sorted(staged.glob("*.md")):
        text = normalize_heading(source.read_text(encoding="utf-8"))
        title = chapter_title(text, source.stem)
        if should_drop(source.stem, title):
            continue
        (target_dir / source.name).write_text(text, encoding="utf-8")
        kept.append(source.name)
        if source.stem in keep:
            extras.append(source.name)
    return kept, extras


def rewrite_links(target_dir: Path, section: str) -> None:
    for path in sorted(target_dir.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        rewritten = text.replace("../assets/", f"../../assets/{section}/")
        if rewritten != text:
            path.write_text(rewritten, encoding="utf-8")


def collect_assets(target_dir: Path, section: str) -> set[str]:
    """Return asset paths relative to the staged ``assets`` directory."""
    prefix = f"{section}/"
    refs: set[str] = set()
    for path in sorted(target_dir.glob("*.md")):
        for match in ASSET_LINK_RE.findall(path.read_text(encoding="utf-8")):
            refs.add(match[len(prefix):] if match.startswith(prefix) else match)
    return refs


def copy_assets(staged_assets: Path, target_dir: Path, refs: set[str]) -> tuple[int, float]:
    if target_dir.exists():
        shutil.rmtree(target_dir)
    target_dir.mkdir(parents=True)
    total = 0
    size = 0
    for rel in sorted(refs):
        source = staged_assets / Path(*rel.split("/"))
        if not source.is_file():
            continue
        target = target_dir / Path(*rel.split("/"))
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
        total += 1
        size += target.stat().st_size
    return total, size / 1048576


def render_section(title: str, section: str, toc_lines: list[str], extras: list[str], source: Path) -> str:
    body = [BEGIN_MARK, "", f"## {title}", ""]
    body.append(
        "> 由 G盾盘古插件（PG 插件）3.49 说明书 CHM 转换而来，覆盖老 GOM 引擎的 PG/盘古插件安装、"
        "功能开关、脚本命令与常见问题。章节文件位于 "
        f"`chapters/{section}/`，图片位于 `assets/{section}/`。"
    )
    body.append("")
    body.append(f"> 原始资料：`{source}`")
    body.append("")
    for line in toc_lines:
        body.append(line.replace("(chapters/", f"(chapters/{section}/"))
    if extras:
        body.extend(["", "### 补充页面", ""])
        for name in extras:
            body.append(f"- [{name.split('-', 1)[-1][:-3]}](chapters/{section}/{name})")
    body.extend(["", END_MARK])
    return "\n".join(body)


def splice_index(index_path: Path, section_markdown: str) -> None:
    text = index_path.read_text(encoding="utf-8")
    if BEGIN_MARK in text and END_MARK in text:
        head, rest = text.split(BEGIN_MARK, 1)
        _old, tail = rest.split(END_MARK, 1)
        text = head.rstrip() + "\n\n" + section_markdown + tail
    else:
        text = text.rstrip() + "\n\n" + section_markdown + "\n"
    index_path.write_text(text, encoding="utf-8")


def update_manifest(manifest_path: Path, section: str, title: str, chapters: int, assets: int, source: Path) -> None:
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    sections = data.setdefault("extra_sections", [])
    sections = [item for item in sections if item.get("id") != section]
    sections.append(
        {
            "id": section,
            "title": title,
            "source": str(source),
            "chapter_count": chapters,
            "asset_count": assets,
        }
    )
    data["extra_sections"] = sections
    manifest_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    args = parse_args()
    skill = args.skill.resolve()
    knowledge = skill / "knowledge_base"
    if not (knowledge / "index.md").is_file():
        raise SystemExit(f"Not a knowledge root: {knowledge}")

    with tempfile.TemporaryDirectory(prefix="manual-section-") as tmp:
        staged = Path(tmp) / "out"
        manifest = convert(args.source.resolve(), staged)
        toc_lines = extract_toc((staged / "index.md").read_text(encoding="utf-8"))

        chapters_dir = knowledge / "chapters" / args.section
        assets_dir = knowledge / "assets" / args.section
        keep = set(args.keep)
        kept, extras = copy_chapters(staged / "chapters", chapters_dir, keep)
        rewrite_links(chapters_dir, args.section)
        refs = collect_assets(chapters_dir, args.section)
        asset_count, asset_mb = copy_assets(staged / "assets", assets_dir, refs)

    section_markdown = render_section(args.title, args.section, toc_lines, extras, args.source.resolve())
    splice_index(knowledge / "index.md", section_markdown)
    update_manifest(knowledge / "manifest.json", args.section, args.title, len(kept), asset_count, args.source.resolve())

    print(
        json.dumps(
            {
                "ok": True,
                "section": args.section,
                "converted_chapters": manifest["chapter_count"],
                "kept_chapters": len(kept),
                "assets_copied": asset_count,
                "assets_mb": round(asset_mb, 1),
                "chapters_dir": str(chapters_dir),
                "assets_dir": str(assets_dir),
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
