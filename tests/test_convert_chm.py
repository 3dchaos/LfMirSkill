import tempfile
import unittest
from pathlib import Path

import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from convert_chm_to_md import (
    html_to_markdown,
    make_slug,
    parse_hhc,
    rewrite_asset_links,
    unique_path,
)


class ConvertChmTests(unittest.TestCase):
    def test_parse_hhc_reads_gbk_toc_tree(self):
        hhc = """
        <UL>
          <LI><OBJECT type="text/sitemap">
            <param name="Name" value="第一章">
            <param name="Local" value="intro.htm">
          </OBJECT>
          <UL>
            <LI><OBJECT type="text/sitemap">
              <param name="Name" value="子章节">
              <param name="Local" value="child.htm">
            </OBJECT>
          </UL>
        </UL>
        """.encode("gbk")

        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "toc.hhc"
            path.write_bytes(hhc)
            entries = parse_hhc(path)

        self.assertEqual(entries[0].title, "第一章")
        self.assertEqual(entries[0].local, "intro.htm")
        self.assertEqual(entries[0].children[0].title, "子章节")

    def test_make_slug_keeps_chinese_and_removes_unsafe_chars(self):
        self.assertEqual(make_slug("新怪物数据[!]"), "新怪物数据")
        self.assertEqual(make_slug("NPC 代码/图片"), "NPC-代码-图片")

    def test_unique_path_ignores_existing_output_for_stable_regeneration(self):
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            (directory / "001-标题.md").write_text("old", encoding="utf-8")

            path = unique_path(directory, "001-标题", ".md", set())

        self.assertEqual(path.name, "001-标题.md")

    def test_html_to_markdown_decodes_gbk_and_rewrites_image_path(self):
        html = (
            '<html><head><meta charset="gb2312"><title>标题</title></head>'
            '<body><h1>标题</h1><p>正文</p><img src="NPC代码/0.jpg"></body></html>'
        ).encode("gbk")

        md = html_to_markdown(html, "sample.htm", {"NPC代码/0.jpg": "../assets/NPC代码/0.jpg"})

        self.assertIn("# 标题", md)
        self.assertIn("正文", md)
        self.assertIn("../assets/NPC代码/0.jpg", md)

    def test_rewrite_asset_links_remaps_html_links_to_markdown(self):
        html_map = {"intro.htm": "chapters/001-intro.md"}
        asset_map = {"img/a.jpg": "assets/img/a.jpg"}

        link = rewrite_asset_links("img/a.jpg", "chapters/002-child.md", html_map, asset_map)
        page = rewrite_asset_links("intro.htm", "chapters/002-child.md", html_map, asset_map)

        self.assertEqual(link, "../assets/img/a.jpg")
        self.assertEqual(page, "001-intro.md")

    def test_rewrite_asset_links_resolves_paths_relative_to_source_page(self):
        asset_map = {"说明/功能设置.png": "assets/说明/功能设置.png"}

        link = rewrite_asset_links(
            "功能设置.png",
            "chapters/006-speed.md",
            {},
            asset_map,
            source_rel="说明/速度.htm",
        )

        self.assertEqual(link, "../assets/说明/功能设置.png")

    def test_html_to_markdown_handles_deep_legacy_paragraph_nesting(self):
        html = "<html><body>" + ("<p>" * 1200) + "更新内容" + ("</p>" * 1200) + "</body></html>"

        md = html_to_markdown(html.encode("gbk"), "chapters/001-update.md", {})

        self.assertIn("更新内容", md)


if __name__ == "__main__":
    unittest.main()
