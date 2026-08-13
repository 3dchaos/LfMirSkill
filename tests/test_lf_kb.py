import json
import tempfile
import unittest
from pathlib import Path

import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "codex-skills" / "lf-mir200-knowledge" / "scripts"))

from lf_kb import (
    analyze_script_learning,
    build_docs_index,
    build_mapinfo_link_index,
    build_sample_index,
    build_thought_summary,
    build_training_course,
    parse_mapinfo_link_line,
    read_text,
    search_records,
    validate_root,
)


class LfKnowledgeBaseTests(unittest.TestCase):
    def test_read_text_decodes_gbk_sample_scripts(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "npc.txt"
            path.write_bytes("[@main]\n#SAY\n你好".encode("gbk"))

            self.assertIn("你好", read_text(path))

    def test_build_docs_index_extracts_title_and_content(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            chapter = root / "knowledge_base" / "chapters" / "001-test.md"
            chapter.parent.mkdir(parents=True)
            chapter.write_text("# 测试标题\n\nCHECKITEM 命令说明", encoding="utf-8")

            records = build_docs_index(root)

        self.assertEqual(records[0]["title"], "测试标题")
        self.assertEqual(records[0]["relative_path"], "knowledge_base/chapters/001-test.md")
        self.assertIn("CHECKITEM", records[0]["text"])

    def test_build_sample_index_classifies_mir200_script_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            npc = root / "样本Mir200" / "Envir" / "Market_def" / "比奇" / "老兵-0.txt"
            npc.parent.mkdir(parents=True)
            npc.write_text("[@main]\n#ACT\nMAPMOVE 3 330 330", encoding="utf-8")

            records = build_sample_index(root)

        self.assertEqual(records[0]["category"], "Market_def")
        self.assertIn("MAPMOVE", records[0]["text"])

    def test_parse_mapinfo_link_accepts_comma_and_space_coordinates(self):
        comma = parse_mapinfo_link_line("0\t308,264\t->\t0102\t3,7", line_number=10)
        spaced = parse_mapinfo_link_line("0108 4 15 -> 0109 7 6", line_number=11)

        self.assertEqual(
            comma,
            {
                "kind": "map_link",
                "line_number": 10,
                "source_map": "0",
                "source_x": 308,
                "source_y": 264,
                "target_map": "0102",
                "target_x": 3,
                "target_y": 7,
                "raw": "0\t308,264\t->\t0102\t3,7",
            },
        )
        self.assertEqual(spaced["source_map"], "0108")
        self.assertEqual((spaced["source_x"], spaced["source_y"]), (4, 15))
        self.assertEqual(spaced["target_map"], "0109")
        self.assertEqual((spaced["target_x"], spaced["target_y"]), (7, 6))

    def test_build_mapinfo_link_index_ignores_map_definitions_and_comments(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            mapinfo = root / "样本Mir200" / "Envir" / "MapInfo.txt"
            mapinfo.parent.mkdir(parents=True)
            mapinfo.write_text(
                "; comment\n"
                "[0 比奇省] DARK\n"
                "0 308,264 -> 0102 3,7\n"
                "0102 3 8 -> 0 308 265\n",
                encoding="utf-8",
            )

            records = build_mapinfo_link_index(root)

        self.assertEqual(len(records), 2)
        self.assertEqual(records[0]["source_map"], "0")
        self.assertEqual(records[0]["target_map"], "0102")
        self.assertEqual(records[1]["source_x"], 3)
        self.assertEqual(records[1]["target_y"], 265)
        self.assertIn("MapInfo.txt:3", records[0]["relative_path"])

    def test_search_records_scores_title_path_and_text(self):
        records = [
            {"title": "装备回收", "relative_path": "a.md", "text": "GAMEGOLD GIVE"},
            {"title": "地图传送", "relative_path": "b.md", "text": "MAPMOVE"},
        ]

        results = search_records(records, "地图 MAPMOVE", limit=1)

        self.assertEqual(results[0]["relative_path"], "b.md")

    def test_validate_root_reports_required_directories_and_indexes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "knowledge_base" / "chapters").mkdir(parents=True)
            (root / "knowledge_base" / "index.md").write_text("# index", encoding="utf-8")
            (root / "样本Mir200" / "Envir").mkdir(parents=True)
            index_dir = root / ".codex-kb" / "indexes"
            index_dir.mkdir(parents=True)
            (index_dir / "docs.json").write_text(json.dumps([{"title": "a"}]), encoding="utf-8")
            (index_dir / "sample.json").write_text(json.dumps([{"title": "b"}]), encoding="utf-8")
            (index_dir / "mapinfo-links.json").write_text(json.dumps([{"title": "0(308,264) -> 0102(3,7)"}]), encoding="utf-8")
            (index_dir / "thoughts.json").write_text(json.dumps({"principles": [], "patterns": []}), encoding="utf-8")
            (index_dir / "training-course.json").write_text(json.dumps({"lessons": []}), encoding="utf-8")

            report = validate_root(root)

        self.assertTrue(report["ok"])
        self.assertEqual(report["docs_index_records"], 1)
        self.assertEqual(report["sample_index_records"], 1)
        self.assertEqual(report["mapinfo_link_records"], 1)

    def test_build_thought_summary_extracts_script_thinking_patterns(self):
        records = [
            {
                "kind": "sample",
                "category": "QuestDiary",
                "title": "装备转移",
                "relative_path": "样本Mir200/Envir/QuestDiary/系统功能/装备转移.txt",
                "text": "@@bigdlg #IF #ACT ITEMBOX CHECKITEM GIVE TAKE ReturnBoxItem UpdateItem MESSAGEBOX",
            },
            {
                "kind": "sample",
                "category": "Market_def",
                "title": "老兵",
                "relative_path": "样本Mir200/Envir/Market_def/比奇城/老兵-0.txt",
                "text": "@main #SAY #IF #ACT MAPMOVE GAMEGIRD MESSAGEBOX",
            },
        ]

        summary = build_thought_summary(records)

        self.assertIn("入口", summary["patterns"][0]["name"])
        self.assertIn("@main", summary["patterns"][0]["signals"])
        self.assertIn("状态", summary["principles"][0])
        ui_pattern = next(pattern for pattern in summary["patterns"] if pattern["name"] == "UI与交互")
        self.assertEqual(ui_pattern["examples"][0]["relative_path"], "样本Mir200/Envir/QuestDiary/系统功能/装备转移.txt")

    def test_build_thought_summary_ignores_non_script_logs_for_dominant_categories(self):
        records = [
            {
                "kind": "sample",
                "category": "ConLog",
                "title": "runtime-log",
                "relative_path": "样本Mir200/ConLog/2026-07-01/C-0-10H20M.txt",
                "text": "server started ok",
            },
            {
                "kind": "sample",
                "category": "Robot_def",
                "title": "RobotManage",
                "relative_path": "样本Mir200/Envir/Robot_def/RobotManage.txt",
                "text": "[@每日清理]\n#IF\n#ACT\nAutoRunRobot\nGmexecute Mission",
            },
            {
                "kind": "sample",
                "category": "MonItems",
                "title": "爆率数据",
                "relative_path": "样本Mir200/Envir/MonItems/鹿.txt",
                "text": "金币 1/10\n太阳水 1/50",
            },
        ]

        summary = build_thought_summary(records)

        self.assertEqual(summary["dominant_categories"][0][0], "Robot_def")
        self.assertNotIn("ConLog", [category for category, _count in summary["dominant_categories"]])
        self.assertNotIn("MonItems", [category for category, _count in summary["dominant_categories"]])

    def test_thinking_records_skips_non_script_categories(self):
        from lf_kb import thinking_records

        records = [
            {"kind": "sample", "category": "MonItems", "relative_path": "a", "text": "foo"},
            {"kind": "sample", "category": "Market_def", "relative_path": "b", "text": "[@main]"},
            {"kind": "sample", "category": "QuestDiary", "relative_path": "c", "text": "#IF"},
        ]

        filtered = thinking_records(records)

        self.assertEqual([item["category"] for item in filtered], ["Market_def", "QuestDiary"])

    def test_build_training_course_groups_progressive_lessons_with_examples(self):
        records = [
            {
                "kind": "sample",
                "category": "Market_def",
                "title": "老兵",
                "relative_path": "样本Mir200/Envir/Market_def/比奇城/老兵-0.txt",
                "text": "[@main]\n#SAY\n<传送/@move>\n[@move]\n#IF\nCHECKGOLD 2000\n#ACT\nTAKE 金币 2000\nMAPMOVE 3 330 330",
            },
            {
                "kind": "sample",
                "category": "QuestDiary",
                "title": "装备转移",
                "relative_path": "样本Mir200/Envir/QuestDiary/系统功能/装备转移.txt",
                "text": "[@装备转移]\nOPENMERCHANTBIGDLG\n#SAY\nITEMBOX\n#IF\nCOMPARETEXT <$BOXITEM[4].STDMODE> <$BOXITEM[5].STDMODE>\n#ACT\nUpdateItem boxitem4\nReturnBoxItem 4",
            },
            {
                "kind": "sample",
                "category": "MapQuest_def",
                "title": "QManage",
                "relative_path": "样本Mir200/Envir/MapQuest_def/QManage.txt",
                "text": "[@Startup]\n#ACT\nSetOnTimer 5 2\n[@OnTimer5]\n#IF\nCHECKMAPNAME 3\n#ACT\nGOTO @归队",
            },
            {
                "kind": "sample",
                "category": "MapQuest_def",
                "title": "复杂入口",
                "relative_path": "样本Mir200/Envir/MapQuest_def/Complex.txt",
                "text": "[@main]\n@Startup\n@Login\n#CALL @other\nGOTO @timer",
            },
        ]

        course = build_training_course(records)

        lesson_ids = [lesson["id"] for lesson in course["lessons"]]
        self.assertIn("lesson-01-entry-dispatch", lesson_ids)
        self.assertIn("lesson-02-dialog-ui", lesson_ids)
        self.assertIn("lesson-06-timers-automation", lesson_ids)
        entry_lesson = next(lesson for lesson in course["lessons"] if lesson["id"] == "lesson-01-entry-dispatch")
        self.assertEqual(entry_lesson["examples"][0]["relative_path"], "样本Mir200/Envir/Market_def/比奇城/老兵-0.txt")
        self.assertIn("入口", entry_lesson["thinking_focus"][0])

    def test_update_writes_thought_summary_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "knowledge_base" / "chapters").mkdir(parents=True)
            (root / "knowledge_base" / "index.md").write_text("# index", encoding="utf-8")
            (root / "样本Mir200" / "Envir" / "QuestDiary").mkdir(parents=True)
            (root / "样本Mir200" / "Envir" / "QuestDiary" / "demo.txt").write_text("@main #IF #ACT", encoding="utf-8")
            (root / "样本Mir200" / "Envir" / "MapInfo.txt").write_text(
                "0 308,264 -> 0102 3,7\n",
                encoding="utf-8",
            )

            from lf_kb import write_indexes

            write_indexes(root, skill_dir=root / "skill-out")
            thought_path = root / ".codex-kb" / "indexes" / "thoughts.json"
            course_path = root / ".codex-kb" / "indexes" / "training-course.json"
            mapinfo_path = root / ".codex-kb" / "indexes" / "mapinfo-links.json"
            data = thought_path.read_text(encoding="utf-8")
            course_exists = course_path.exists()
            mapinfo_exists = mapinfo_path.exists()
        self.assertIn("principles", data)
        self.assertIn("patterns", data)
        self.assertTrue(course_exists)
        self.assertTrue(mapinfo_exists)

    def test_analyze_script_learning_extracts_calls_flags_inputs_and_manual_topics(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            script = root / "样本Mir200" / "Envir" / "QuestDiary" / "系统功能" / "老登辅助" / "辅助.txt"
            script.parent.mkdir(parents=True)
            script.write_text(
                "[@辅助功能]\n"
                "#IF\n"
                "ISADMIN\n"
                "#ACT\n"
                "MOV N$边框色值1 255\n"
                "MOV A687 <$USERNAME>\n"
                "MOV G3 1\n"
                "OPENMERCHANTBIGDLG 0 19 1 0 0 0 1 575 24\n"
                "#SAY\n"
                "<Img:#L04~:8<$flag(68)>:0:50:48|7#勾选自动召唤/@自动召唤>\n"
                "<INPUTNUM:3:0:2:80:15:0:249:255:1:100:必须输入1-100之间的数字:输入血量百分比:160>\n"
                "<text:关闭/@召唤配置(骷髅,0)>\n"
                "[@召唤配置]\n"
                "#IF\n"
                "EQUAL <$SCRIPTPARAM1> 骷髅\n"
                "#ACT\n"
                "MOV N13 <$SCRIPTPARAM2>\n"
                "GOTO @挂机自动召唤\n"
                "[@自动召唤]\n"
                "#IF\n"
                "CHECKJOB taoist\n"
                "#ELSEACT\n"
                "SET [68] 0\n"
                "BREAK\n"
                "[@存储仆从]\n"
                "#IF\n"
                "#CALL [系统功能\\老登辅助\\存储仆从.txt] @存储仆从1\n"
                "[@装备锁定]\n"
                "#SAY\n"
                "<ITEMBOX:0:1:730:250:160:45:45:*,11:254#请放入道具>\n"
                "[@开始锁定]\n"
                "#IF\n"
                "NOT Equal <$BOXITEM[0].NAME>\n"
                "#ACT\n"
                "SetUpgradeItem 0\n"
                "UpdateItem boxitem0\n"
                "ReturnBoxItem 0\n"
                "[@定时维修]\n"
                "#ACT\n"
                "SetOnTimer 10 600\n"
                "SetOffTimer 10\n",
                encoding="utf-8",
            )

            report = analyze_script_learning(root, "样本Mir200/Envir/QuestDiary/系统功能/老登辅助/辅助.txt")

        self.assertEqual(report["relative_path"], "样本Mir200/Envir/QuestDiary/系统功能/老登辅助/辅助.txt")
        self.assertIn("辅助功能", report["labels"])
        self.assertEqual(report["calls"][0]["path"], "系统功能\\老登辅助\\存储仆从.txt")
        self.assertIn("68", report["flags"])
        self.assertIn("3", report["npc_inputs"])
        self.assertIn("N$边框色值1", report["variables"]["N$"])
        self.assertIn("N13", report["variables"]["N"])
        self.assertIn("A687", report["variables"]["A"])
        self.assertIn("G3", report["variables"]["G"])
        self.assertEqual(report["timers"][0]["id"], "10")
        self.assertEqual(report["item_boxes"][0]["id"], "0")
        self.assertIn("knowledge_base/chapters/787-扩展NPC脚本点击触发带参数-NPC标签带参数.md", report["manual_topics"])
        self.assertTrue(any("入口" in note for note in report["learning_notes"]))

    def test_cmd_learn_script_prints_static_learning_report(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            script = root / "样本Mir200" / "Envir" / "QuestDiary" / "系统功能" / "老登辅助" / "辅助.txt"
            script.parent.mkdir(parents=True)
            script.write_text(
                "[@辅助功能]\n"
                "#CALL [系统功能\\老登辅助\\存储仆从.txt] @存储仆从1\n"
                "SetOnTimer 10 600\n",
                encoding="utf-8",
            )

            from io import StringIO
            import contextlib
            from lf_kb import cmd_learn_script

            buffer = StringIO()
            with contextlib.redirect_stdout(buffer):
                cmd_learn_script(root, "样本Mir200/Envir/QuestDiary/系统功能/老登辅助/辅助.txt")
            data = json.loads(buffer.getvalue())

        self.assertEqual(data["calls"][0]["label"], "@存储仆从1")
        self.assertEqual(data["timers"][0]["id"], "10")
        self.assertIn("knowledge_base/chapters/028-CallEx支持多个同样的@地址.md", data["manual_topics"])


if __name__ == "__main__":
    unittest.main()
