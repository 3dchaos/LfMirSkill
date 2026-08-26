#!/usr/bin/env python3
"""Install the LF Mir200 Codex skill with its required manual knowledge base."""

from __future__ import annotations

import argparse
import json
import shutil
import tempfile
from pathlib import Path


SKILL_RELATIVE = Path("codex-skills") / "lf-mir200-knowledge"
KNOWLEDGE_RELATIVE = Path("knowledge_base")
REQUIRED_SKILL_FILES = (Path("SKILL.md"),)
REQUIRED_KNOWLEDGE_FILES = (
    Path("index.md"),
    Path("manifest.json"),
)


class InstallError(RuntimeError):
    """Raised when the source does not contain a complete installable package."""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Install lf-mir200-knowledge and its required knowledge_base."
    )
    parser.add_argument(
        "--source",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Repository root containing codex-skills/lf-mir200-knowledge/knowledge_base/.",
    )
    parser.add_argument(
        "--dest",
        type=Path,
        default=Path.home() / ".codex" / "skills" / "lf-mir200-knowledge",
        help="Destination skill directory.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Replace an existing destination after validation.",
    )
    return parser.parse_args()


def require_directory(path: Path, label: str) -> None:
    if not path.is_dir():
        raise InstallError(f"Missing {label} directory: {path}")


def require_files(root: Path, files: tuple[Path, ...], label: str) -> None:
    missing = [str(path) for path in files if not (root / path).is_file()]
    if missing:
        raise InstallError(f"Missing {label} files: {', '.join(missing)}")


def validate_source(source: Path) -> tuple[Path, Path]:
    source = source.resolve()
    skill = source / SKILL_RELATIVE
    packaged_knowledge = skill / KNOWLEDGE_RELATIVE
    legacy_knowledge = source / KNOWLEDGE_RELATIVE
    require_directory(skill, "skill")
    require_files(skill, REQUIRED_SKILL_FILES, "skill")
    knowledge = packaged_knowledge if packaged_knowledge.is_dir() else legacy_knowledge
    require_directory(knowledge, "knowledge_base")
    require_files(knowledge, REQUIRED_KNOWLEDGE_FILES, "knowledge_base")

    manifest = json.loads((knowledge / "manifest.json").read_text(encoding="utf-8"))
    chapter_count = manifest.get("chapter_count")
    if not isinstance(chapter_count, int) or chapter_count <= 0:
        raise InstallError("knowledge_base/manifest.json has no positive chapter_count")
    chapters = knowledge / "chapters"
    if not chapters.is_dir() or not any(chapters.rglob("*.md")):
        raise InstallError("knowledge_base/chapters contains no Markdown chapters")
    return skill, knowledge


def install(source: Path, dest: Path, force: bool = False) -> dict[str, object]:
    skill, knowledge = validate_source(source)
    packaged_knowledge = skill / KNOWLEDGE_RELATIVE
    dest = dest.resolve()
    if dest.exists() and not force:
        raise InstallError(f"Destination already exists: {dest}; use --force to replace it")

    dest.parent.mkdir(parents=True, exist_ok=True)
    staging_parent = Path(tempfile.mkdtemp(prefix="lf-mir200-skill-", dir=dest.parent))
    staging = staging_parent / dest.name
    try:
        shutil.copytree(skill, staging)
        if knowledge != packaged_knowledge:
            shutil.copytree(knowledge, staging / KNOWLEDGE_RELATIVE)
        if dest.exists():
            shutil.rmtree(dest)
        staging.replace(dest)
    finally:
        shutil.rmtree(staging_parent, ignore_errors=True)

    chapter_count = len(list((dest / "knowledge_base" / "chapters").rglob("*.md")))
    asset_count = len(list((dest / "knowledge_base" / "assets").rglob("*")))
    return {
        "destination": str(dest),
        "skill": True,
        "knowledge_base": True,
        "chapter_files": chapter_count,
        "asset_entries": asset_count,
    }


def main() -> int:
    args = parse_args()
    try:
        result = install(args.source, args.dest, args.force)
    except (InstallError, OSError, json.JSONDecodeError) as exc:
        print(f"Error: {exc}")
        return 1
    print(json.dumps({"ok": True, **result}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
