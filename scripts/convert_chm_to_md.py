from __future__ import annotations

import argparse
import json
import re
import shutil
from collections import Counter
from dataclasses import dataclass, field
from html import unescape
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlsplit, urlunsplit

from bs4 import BeautifulSoup
from markdownify import MarkdownConverter


HTML_EXTENSIONS = {".htm", ".html"}
ASSET_EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif", ".rar"}


@dataclass
class TocEntry:
    title: str
    local: str | None = None
    children: list["TocEntry"] = field(default_factory=list)
    source_order: int = 0
    output_path: str | None = None


def read_text(path: Path) -> str:
    data = path.read_bytes()
    for encoding in ("gb18030", "gbk", "utf-8-sig", "utf-8"):
        try:
            return data.decode(encoding)
        except UnicodeDecodeError:
            continue
    return data.decode("gb18030", errors="replace")


def decode_html(data: bytes) -> str:
    head = data[:4096].decode("ascii", errors="ignore").lower()
    match = re.search(r"charset\s*=\s*['\"]?([a-z0-9_\-]+)", head)
    candidates = []
    if match:
        candidates.append(match.group(1))
    candidates.extend(["gb18030", "gbk", "utf-8-sig", "utf-8"])

    seen = set()
    for encoding in candidates:
        if encoding in seen:
            continue
        seen.add(encoding)
        try:
            return data.decode(encoding)
        except LookupError:
            continue
        except UnicodeDecodeError:
            continue
    return data.decode("gb18030", errors="replace")


def normalize_ref(ref: str) -> str:
    value = unquote(ref or "").replace("\\", "/").strip()
    while value.startswith("./"):
        value = value[2:]
    return value


def make_slug(title: str, fallback: str = "chapter") -> str:
    value = unescape(title or "").strip()
    value = re.sub(r"[<>:\"/\\|?*\[\]!！【】（）()，,。；;：:、]+", " ", value)
    value = re.sub(r"\s+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-._ ")
    return value or fallback


def unique_path(directory: Path, stem: str, suffix: str, used: set[str]) -> Path:
    candidate = directory / f"{stem}{suffix}"
    index = 2
    while candidate.as_posix().lower() in used:
        candidate = directory / f"{stem}-{index}{suffix}"
        index += 1
    used.add(candidate.as_posix().lower())
    return candidate


def extract_object_params(obj) -> dict[str, str]:
    params = {}
    for param in obj.find_all("param", recursive=False):
        name = param.get("name")
        value = param.get("value")
        if name and value is not None:
            params[name.lower()] = value
    return params


def parse_hhc(path: Path) -> list[TocEntry]:
    soup = BeautifulSoup(read_text(path), "html5lib")
    order = 0

    def parse_ul(ul) -> list[TocEntry]:
        nonlocal order
        entries: list[TocEntry] = []
        for li in ul.find_all("li", recursive=False):
            obj = li.find("object", recursive=False)
            if not obj:
                continue
            params = extract_object_params(obj)
            title = params.get("name", "").strip()
            local = params.get("local")
            order += 1
            entry = TocEntry(
                title=title or local or f"未命名章节-{order}",
                local=normalize_ref(local) if local else None,
                source_order=order,
            )
            child_ul = li.find("ul", recursive=False)
            if child_ul:
                entry.children = parse_ul(child_ul)
            entries.append(entry)
        return entries

    root_ul = soup.find("ul")
    return parse_ul(root_ul) if root_ul else []


def flatten_toc(entries: list[TocEntry], depth: int = 0) -> list[tuple[TocEntry, int]]:
    flattened: list[tuple[TocEntry, int]] = []
    for entry in entries:
        flattened.append((entry, depth))
        flattened.extend(flatten_toc(entry.children, depth + 1))
    return flattened


def collect_html_pages(source: Path, toc_entries: list[TocEntry]) -> list[Path]:
    toc_pages: list[Path] = []
    seen = set()
    for entry, _depth in flatten_toc(toc_entries):
        if not entry.local:
            continue
        rel = normalize_ref(urlsplit(entry.local).path)
        if Path(rel).suffix.lower() not in HTML_EXTENSIONS:
            continue
        page = source / rel
        key = page.resolve().as_posix().lower()
        if page.exists() and key not in seen:
            seen.add(key)
            toc_pages.append(page)

    for page in sorted(source.rglob("*"), key=lambda p: normalize_ref(p.relative_to(source).as_posix()).lower()):
        if page.suffix.lower() in HTML_EXTENSIONS:
            key = page.resolve().as_posix().lower()
            if key not in seen:
                seen.add(key)
                toc_pages.append(page)
    return toc_pages


def build_output_maps(source: Path, output: Path, pages: list[Path], toc_entries: list[TocEntry]) -> tuple[dict[str, str], dict[str, str]]:
    chapters_dir = output / "chapters"
    used: set[str] = set()
    html_map: dict[str, str] = {}
    title_by_local = {
        normalize_ref(urlsplit(entry.local).path).lower(): entry.title
        for entry, _depth in flatten_toc(toc_entries)
        if entry.local
    }

    for index, page in enumerate(pages, 1):
        rel = normalize_ref(page.relative_to(source).as_posix())
        title = title_by_local.get(rel.lower()) or page.stem
        slug = make_slug(title, page.stem)
        out_path = unique_path(chapters_dir, f"{index:03d}-{slug}", ".md", used)
        html_map[rel.lower()] = normalize_ref(out_path.relative_to(output).as_posix())

    for entry, _depth in flatten_toc(toc_entries):
        if not entry.local:
            continue
        rel = normalize_ref(urlsplit(entry.local).path).lower()
        entry.output_path = html_map.get(rel)

    asset_map: dict[str, str] = {}
    for asset in sorted(source.rglob("*")):
        if asset.is_file() and asset.suffix.lower() in ASSET_EXTENSIONS:
            rel = normalize_ref(asset.relative_to(source).as_posix())
            asset_map[rel.lower()] = normalize_ref((Path("assets") / rel).as_posix())
    return html_map, asset_map


def relative_link(from_output_file: str, target_output: str) -> str:
    source_dir = Path(from_output_file).parent
    return normalize_ref(Path(target_output).relative_to(source_dir).as_posix()) if source_dir == Path(".") else normalize_ref(Path("../") / target_output)


def make_relative(from_output_file: str, target_output: str) -> str:
    from_parts = Path(from_output_file).parts[:-1]
    target_parts = Path(target_output).parts
    i = 0
    while i < len(from_parts) and i < len(target_parts) and from_parts[i].lower() == target_parts[i].lower():
        i += 1
    rel_parts = [".."] * (len(from_parts) - i) + list(target_parts[i:])
    return "/".join(rel_parts) if rel_parts else Path(target_output).name


def source_relative_key(source_rel: str | None, ref_path: str) -> str | None:
    if not source_rel:
        return None
    parent = PurePosixPath(normalize_ref(source_rel)).parent
    return normalize_ref((parent / ref_path).as_posix()).lower()


def lookup_mapped_target(keys: list[str], *maps: dict[str, str]) -> str | None:
    for key in keys:
        for mapping in maps:
            target = mapping.get(key)
            if target:
                return target
            normalized_key = normalize_ref(key).lower()
            target = next((value for map_key, value in mapping.items() if normalize_ref(map_key).lower() == normalized_key), None)
            if target:
                return target
    return None


def rewrite_asset_links(
    ref: str,
    from_output_file: str,
    html_map: dict[str, str],
    asset_map: dict[str, str],
    source_rel: str | None = None,
) -> str:
    if not ref:
        return ref
    split = urlsplit(ref)
    if split.scheme or split.netloc or ref.startswith("#"):
        return ref

    path = normalize_ref(split.path)
    keys = [path.lower()]
    rel_key = source_relative_key(source_rel, path)
    if rel_key and rel_key not in keys:
        keys.append(rel_key)

    target = lookup_mapped_target(keys, html_map, asset_map)
    if not target:
        return ref

    rel = make_relative(from_output_file, target)
    return urlunsplit(("", "", rel, split.query, split.fragment))


class ChmMarkdownConverter(MarkdownConverter):
    def __init__(
        self,
        *args,
        from_output_file: str,
        html_map: dict[str, str],
        asset_map: dict[str, str],
        source_rel: str | None,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.from_output_file = from_output_file
        self.html_map = html_map
        self.asset_map = asset_map
        self.source_rel = source_rel

    def convert_a(self, el, text, parent_tags):
        href = el.get("href")
        if href:
            rewritten = rewrite_asset_links(href, self.from_output_file, self.html_map, self.asset_map, self.source_rel)
            if rewritten == href and is_missing_local_reference(href):
                return text
            el["href"] = rewritten
        return super().convert_a(el, text, parent_tags)

    def convert_img(self, el, text, parent_tags):
        src = el.get("src")
        if src:
            rewritten = rewrite_asset_links(src, self.from_output_file, self.html_map, self.asset_map, self.source_rel)
            if rewritten == src and is_missing_local_reference(src):
                return el.get("alt", "")
            el["src"] = rewritten
        return super().convert_img(el, text, parent_tags)


def is_missing_local_reference(ref: str) -> bool:
    split = urlsplit(ref)
    if split.scheme or split.netloc or ref.startswith("#"):
        return False
    return PurePosixPath(normalize_ref(split.path)).suffix.lower() in HTML_EXTENSIONS | ASSET_EXTENSIONS


def clean_soup(soup: BeautifulSoup) -> BeautifulSoup:
    for tag in soup(["script", "style", "meta", "link"]):
        tag.decompose()
    for tag in soup.find_all(True):
        for attr in list(tag.attrs):
            if attr.lower().startswith("on"):
                del tag.attrs[attr]
    return soup


def html_to_markdown(
    data: bytes,
    from_output_file: str,
    asset_map: dict[str, str],
    html_map: dict[str, str] | None = None,
    source_rel: str | None = None,
) -> str:
    soup = BeautifulSoup(decode_html(data), "html5lib")
    clean_soup(soup)
    body = soup.body or soup
    converter = ChmMarkdownConverter(
        heading_style="ATX",
        bullets="-",
        strip=["font", "span"],
        from_output_file=from_output_file,
        html_map=html_map or {},
        asset_map=asset_map,
        source_rel=source_rel,
    )
    markdown = converter.convert_soup(body)
    markdown = re.sub(r"\n{3,}", "\n\n", markdown)
    markdown = "\n".join(line.rstrip() for line in markdown.splitlines()).strip()
    return markdown + "\n"


def find_title(page: Path, fallback: str) -> str:
    soup = BeautifulSoup(decode_html(page.read_bytes()), "html5lib")
    for selector in ("h1", "title"):
        tag = soup.find(selector)
        if tag and tag.get_text(strip=True):
            return tag.get_text(" ", strip=True)
    return fallback


def write_index(output: Path, toc_entries: list[TocEntry], all_pages: list[Path], html_map: dict[str, str], source: Path) -> None:
    lines = [
        "# 翎风引擎帮助文档知识库",
        "",
        "> 本知识库由原始 CHM 文档转换生成，按章节拆分为 Markdown 文件。",
        "",
        "## 目录",
        "",
    ]

    def has_indexable_content(entry: TocEntry) -> bool:
        return bool(entry.output_path or any(has_indexable_content(child) for child in entry.children))

    def append_entries(entries: list[TocEntry], depth: int = 0) -> None:
        for entry in entries:
            if not has_indexable_content(entry):
                continue
            indent = "  " * depth
            if entry.output_path:
                lines.append(f"{indent}- [{entry.title}]({entry.output_path})")
            elif entry.local:
                lines.append(f"{indent}- {entry.title}")
            else:
                lines.append(f"{indent}- {entry.title}")
            append_entries(entry.children, depth + 1)

    append_entries(toc_entries)

    mapped = set(html_map.values())
    extra_pages = []
    for page in all_pages:
        rel = normalize_ref(page.relative_to(source).as_posix())
        out = html_map.get(rel.lower())
        if out and out not in mapped:
            extra_pages.append((rel, out))

    lines.extend(["", "## 未在原目录中列出的页面", ""])
    extras = [
        (normalize_ref(page.relative_to(source).as_posix()), html_map.get(normalize_ref(page.relative_to(source).as_posix()).lower()))
        for page in all_pages
        if html_map.get(normalize_ref(page.relative_to(source).as_posix()).lower())
        and not any(entry.output_path == html_map.get(normalize_ref(page.relative_to(source).as_posix()).lower()) for entry, _ in flatten_toc(toc_entries))
    ]
    if extras:
        for rel, out in extras:
            lines.append(f"- [{rel}]({out})")
    else:
        lines.append("- 无")

    (output / "index.md").write_text("\n".join(lines).strip() + "\n", encoding="utf-8")


def copy_assets(source: Path, output: Path, asset_map: dict[str, str]) -> None:
    for source_rel_lower, target_rel in asset_map.items():
        source_path = source / source_rel_lower
        if not source_path.exists():
            matches = [p for p in source.rglob("*") if normalize_ref(p.relative_to(source).as_posix()).lower() == source_rel_lower]
            if not matches:
                continue
            source_path = matches[0]
        target = output / target_rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source_path, target)


def convert(source: Path, output: Path) -> dict[str, object]:
    hhc_files = sorted(source.glob("*.HHC")) + sorted(source.glob("*.hhc"))
    if not hhc_files:
        raise FileNotFoundError(f"No .HHC table-of-contents file found in {source}")

    toc_entries = parse_hhc(hhc_files[0])
    pages = collect_html_pages(source, toc_entries)
    html_map, asset_map = build_output_maps(source, output, pages, toc_entries)

    if output.exists():
        shutil.rmtree(output)
    (output / "chapters").mkdir(parents=True)
    (output / "assets").mkdir(parents=True)

    copy_assets(source, output, asset_map)

    converted = 0
    for page in pages:
        rel = normalize_ref(page.relative_to(source).as_posix())
        out_rel = html_map[rel.lower()]
        title = find_title(page, page.stem)
        body = html_to_markdown(page.read_bytes(), out_rel, asset_map, html_map, rel)
        if not body.lstrip().startswith("# "):
            body = f"# {title}\n\n{body}"
        out_path = output / out_rel
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(body, encoding="utf-8")
        converted += 1

    write_index(output, toc_entries, pages, html_map, source)

    local_counter = Counter()
    for entry, _depth in flatten_toc(toc_entries):
        if entry.local:
            local_counter[normalize_ref(urlsplit(entry.local).path).lower()] += 1

    manifest = {
        "source": str(source),
        "toc_file": str(hhc_files[0].relative_to(source)),
        "chapter_count": converted,
        "asset_count": len(asset_map),
        "toc_entry_count": len(flatten_toc(toc_entries)),
        "duplicate_toc_targets": {k: v for k, v in local_counter.items() if v > 1},
    }
    (output / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert extracted CHM HTML files to a Markdown knowledge base.")
    parser.add_argument("--source", default="chm_extracted", help="Directory produced by hh.exe -decompile.")
    parser.add_argument("--output", default="knowledge_base", help="Markdown knowledge base output directory.")
    args = parser.parse_args()

    manifest = convert(Path(args.source), Path(args.output))
    print(json.dumps(manifest, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
