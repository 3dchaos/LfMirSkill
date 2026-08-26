import json
import tempfile
import unittest
from pathlib import Path

import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from install_codex_skill import InstallError, install, validate_source


class InstallCodexSkillTests(unittest.TestCase):
    def make_source(self, root: Path, include_knowledge: bool = True, legacy_layout: bool = False) -> None:
        skill = root / "codex-skills" / "lf-mir200-knowledge"
        skill.mkdir(parents=True)
        (skill / "SKILL.md").write_text("---\nname: lf-mir200-knowledge\n---\n", encoding="utf-8")
        if include_knowledge:
            knowledge = root / "knowledge_base" if legacy_layout else skill / "knowledge_base"
            (knowledge / "chapters").mkdir(parents=True)
            (knowledge / "assets").mkdir()
            (knowledge / "index.md").write_text("# index\n", encoding="utf-8")
            (knowledge / "manifest.json").write_text(
                json.dumps({"chapter_count": 1}), encoding="utf-8"
            )
            (knowledge / "chapters" / "001-test.md").write_text(
                "# test\n", encoding="utf-8"
            )

    def test_install_copies_skill_and_packaged_knowledge_base(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "source"
            dest = root / "installed"
            self.make_source(source)

            result = install(source, dest)

            self.assertTrue(result["skill"])
            self.assertTrue(result["knowledge_base"])
            self.assertTrue((dest / "SKILL.md").is_file())
            self.assertTrue((dest / "knowledge_base" / "index.md").is_file())
            self.assertTrue((dest / "knowledge_base" / "chapters" / "001-test.md").is_file())

    def test_install_supports_legacy_root_knowledge_base_layout(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "source"
            dest = root / "installed"
            self.make_source(source, legacy_layout=True)

            install(source, dest)

            self.assertTrue((dest / "knowledge_base" / "index.md").is_file())

    def test_install_rejects_skill_without_companion_knowledge_base(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / "source"
            self.make_source(source, include_knowledge=False)

            with self.assertRaises(InstallError):
                validate_source(source)

    def test_install_does_not_overwrite_without_force(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "source"
            dest = root / "installed"
            self.make_source(source)
            dest.mkdir()

            with self.assertRaises(InstallError):
                install(source, dest)


if __name__ == "__main__":
    unittest.main()
