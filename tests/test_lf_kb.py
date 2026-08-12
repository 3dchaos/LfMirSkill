import json
import tempfile
import unittest
from pathlib import Path

import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "codex-skills" / "lf-mir200-knowledge" / "scripts"))

from lf_kb import (
    build_docs_index,
    build_sample_index,
    build_thought_summary,
    build_training_course,
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
            (index_dir / "thoughts.json").write_text(json.dumps({"principles": [], "patterns": []}), encoding="utf-8")
            (index_dir / "training-course.json").write_text(json.dumps({"lessons": []}), encoding="utf-8")

            report = validate_root(root)

        self.assertTrue(report["ok"])
        self.assertEqual(report["docs_index_records"], 1)
        self.assertEqual(report["sample_index_records"], 1)

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

            from lf_kb import write_indexes

            write_indexes(root, skill_dir=root / "skill-out")
            thought_path = root / ".codex-kb" / "indexes" / "thoughts.json"
            course_path = root / ".codex-kb" / "indexes" / "training-course.json"
            data = thought_path.read_text(encoding="utf-8")
            course_exists = course_path.exists()
        self.assertIn("principles", data)
        self.assertIn("patterns", data)
        self.assertTrue(course_exists)


if __name__ == "__main__":
    unittest.main()
