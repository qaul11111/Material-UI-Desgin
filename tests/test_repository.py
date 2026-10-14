from pathlib import Path
import re
import unittest
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]


class RepositoryTests(unittest.TestCase):
    def test_relative_markdown_links_resolve(self):
        for source in ROOT.rglob("*.md"):
            if ".git" in source.parts:
                continue
            for value in re.findall(r"\]\(([^)\s]+)\)", source.read_text(encoding="utf-8")):
                if "://" in value or value.startswith("#"):
                    continue
                target = unquote(value.split("#")[0])
                with self.subTest(file=source, target=target):
                    self.assertTrue((source.parent / target).exists())

    def test_release_boundary(self):
        self.assertEqual({p.name for p in (ROOT / "skills").iterdir() if p.is_dir()},
                         {"material-android-ui-design", "material-android-ui-refine", "_material-android-ui-shared"})

    def test_entrypoint_relative_references(self):
        for source in (ROOT / "skills").glob("*/SKILL.md"):
            for value in re.findall(r"\x60(\.\.?/[^\x60\n]+)\x60", source.read_text()):
                with self.subTest(file=source, value=value):
                    self.assertTrue((source.parent / value).exists())


if __name__ == "__main__":
    unittest.main()
