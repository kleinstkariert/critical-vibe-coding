"""Regression tests for check-course-links.py.

Run: python course/scripts/test_check_course_links.py
All fixtures are built in a temporary folder. No generated binary is committed.
"""

import ast
import importlib.util
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

SCRIPT = Path(__file__).with_name("check-course-links.py")
sys.path.insert(0, str(SCRIPT.parent))
import deck_note_paths as helper  # noqa: E402

spec = importlib.util.spec_from_file_location("check_course_links", SCRIPT)
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)

REPO = SCRIPT.resolve().parents[2]
SLIDESHOW = REPO / "course/SESSIONS/lectures/01-welcome-landscape-slideshow"

MAINZ = "research/externalReferences/UnlearGestaltungAI_Mainz/unlearn-gestaltung"
DECK_DIR = "course/SESSIONS/lectures/01-demo-slideshow"

PPTX_NS = (
    'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
    'xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" '
    'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"'
)
REL_HEAD = '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
SLIDE_TYPE = "http://schemas.openxmlformats.org/officeDocument/2006/relationships/slide"
ODF_NS = (
    'xmlns:office="urn:oasis:names:tc:opendocument:xmlns:office:1.0" '
    'xmlns:draw="urn:oasis:names:tc:opendocument:xmlns:drawing:1.0" '
    'xmlns:presentation="urn:oasis:names:tc:opendocument:xmlns:presentation:1.0" '
    'xmlns:text="urn:oasis:names:tc:opendocument:xmlns:text:1.0"'
)


def write(path, text=""):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def make_pptx(path, paragraphs):
    """paragraphs: list of paragraphs, each a list of text runs (slide 1 notes)."""
    runs = "".join(
        "<a:p>" + "".join(f"<a:r><a:t>{run}</a:t></a:r>" for run in para) + "</a:p>" for para in paragraphs
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(path, "w") as z:
        z.writestr(
            "ppt/presentation.xml",
            f'<p:presentation {PPTX_NS}><p:sldIdLst><p:sldId id="256" r:id="rId1"/></p:sldIdLst></p:presentation>',
        )
        z.writestr(
            "ppt/_rels/presentation.xml.rels",
            f'{REL_HEAD}<Relationship Id="rId1" Type="{SLIDE_TYPE}" Target="slides/slide1.xml"/></Relationships>',
        )
        z.writestr("ppt/slides/slide1.xml", f"<p:sld {PPTX_NS}/>")
        z.writestr("ppt/notesSlides/notesSlide1.xml", f"<p:notes {PPTX_NS}><p:txBody>{runs}</p:txBody></p:notes>")
        z.writestr(
            "ppt/notesSlides/_rels/notesSlide1.xml.rels",
            f'{REL_HEAD}<Relationship Id="rId1" Type="{SLIDE_TYPE}" Target="../slides/slide1.xml"/></Relationships>',
        )


def make_odp(path, paragraph_xml):
    path.parent.mkdir(parents=True, exist_ok=True)
    body = (
        f"<office:document-content {ODF_NS}><office:body><office:presentation>"
        f'<draw:page draw:name="page1"><presentation:notes><draw:frame><draw:text-box>{paragraph_xml}'
        "</draw:text-box></draw:frame></presentation:notes></draw:page>"
        "</office:presentation></office:body></office:document-content>"
    )
    with zipfile.ZipFile(path, "w") as z:
        z.writestr("mimetype", "application/vnd.oasis.opendocument.presentation", compress_type=zipfile.ZIP_STORED)
        z.writestr("content.xml", body)


class TempRepo(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name).resolve()
        self._saved = (checker.ROOT, checker.SCAN, checker.EXTRA_FILES)
        checker.ROOT = self.root
        checker.SCAN = [self.root / name for name in ("course", "research", "archive", "documentation")]
        checker.EXTRA_FILES = []

    def tearDown(self):
        checker.ROOT, checker.SCAN, checker.EXTRA_FILES = self._saved
        self._tmp.cleanup()


class WikilinkFilterTests(TempRepo):
    def setUp(self):
        super().setUp()
        write(self.root / MAINZ / "vol1-approaching.md", "# Vol 1\n")
        write(self.root / MAINZ / "shared-name.md", "# Mainz copy\n")
        write(self.root / "course/PRACTICE/shared-name.md", "# Course copy\n")
        write(self.root / "course/PRACTICE/plain-note.md", "# Plain\n")

    def check(self, link, strict):
        note = self.root / "course/SESSIONS/source.md"
        write(note, f"See [[{link}]].\n")
        return checker.check_file(note, strict)

    def test_bare_name_into_external_tree_fails(self):
        for strict in (False, True):
            broken, notices = self.check("vol1-approaching", strict)
            self.assertEqual(broken, ["wikilink not found: [[vol1-approaching]]"], strict)
            self.assertEqual(notices, [])

    def test_explicit_path_into_external_tree_resolves(self):
        link = f"{MAINZ}/vol1-approaching"
        for strict in (False, True):
            broken, notices = self.check(link, strict)
            self.assertEqual(broken, [], strict)
            self.assertEqual(len(notices), 1)

    def test_markdown_link_with_wrong_case_fails(self):
        note = self.root / "course/SESSIONS/source.md"
        write(note, "See [good](../PRACTICE/plain-note.md) and [bad](../practice/plain-note.md).\n")
        broken, _ = checker.check_file(note, True)
        self.assertEqual(broken, ["markdown link not found (case must match): ../practice/plain-note.md"])

    def test_same_name_prefers_course_note(self):
        broken, notices = self.check("shared-name", False)
        self.assertEqual(broken, [])
        self.assertEqual(len(notices), 1)

    def test_bare_name_in_course_stays_a_notice(self):
        broken, notices = self.check("plain-note", False)
        self.assertEqual(broken, [])
        self.assertEqual(notices, ["wikilink works in Obsidian only: [[plain-note]]"])


class DeckNoteTests(TempRepo):
    def setUp(self):
        super().setUp()
        write(self.root / "course/THEORY/04-bias-flattening/flattening-and-the-norm.md", "# F\n")
        write(self.root / "research/software&DataManagement/gpu.md", "# G\n")
        write(self.root / "AGENTS.md", "# A\n")
        self.pptx = self.root / DECK_DIR / "demo.pptx"
        self.odp = self.root / DECK_DIR / "demo.odp"

    def run_check(self):
        return checker.check_decks()

    def test_exact_paths_pass(self):
        make_pptx(
            self.pptx,
            [["Read course/THEORY/04-bias-flattening/flattening-and-the-norm.md and AGENTS.md."],
             ["Also research/software&amp;DataManagement/gpu.md."]],
        )
        problems, decks, strings = self.run_check()
        self.assertEqual((problems, decks, strings), ([], 1, 3))

    def test_short_form_and_bare_name_fail_with_hint(self):
        make_pptx(self.pptx, [["Use course/flattening-and-the-norm.md or flattening-and-the-norm.md."]])
        problems, _, strings = self.run_check()
        self.assertEqual(strings, 2)
        self.assertEqual(len(problems), 2)
        for _, where, text in problems:
            self.assertEqual(where, "slide 1")
            self.assertIn("no such file", text)
            self.assertIn("course/THEORY/04-bias-flattening/flattening-and-the-norm.md", text)

    def test_missing_target_fails(self):
        make_pptx(self.pptx, [["See course/gone.md."]])
        problems, _, _ = self.run_check()
        self.assertEqual(len(problems), 1)
        self.assertIn("course/gone.md: no such file", problems[0][2])

    def test_case_wrong_path_fails(self):
        make_pptx(self.pptx, [["See course/theory/04-bias-flattening/flattening-and-the-norm.md."]])
        problems, _, _ = self.run_check()
        self.assertEqual(len(problems), 1)

    def test_prose_is_not_a_path(self):
        make_pptx(
            self.pptx,
            [["All *.md files, a .md suffix, https://example.org/docs/README.md and notes.txt are prose."],
             ["Write Markdown (md) and say amd or the.mdx extension."]],
        )
        problems, _, strings = self.run_check()
        self.assertEqual((problems, strings), ([], 0))

    def test_path_split_over_runs_is_found(self):
        make_pptx(self.pptx, [["See course/THEORY/04-bias-fl", "attening/missing-note.md"]])
        problems, _, strings = self.run_check()
        self.assertEqual(strings, 1)
        self.assertEqual(len(problems), 1)

    def test_odp_notes_are_checked(self):
        make_odp(
            self.odp,
            "<text:p>Read<text:s/>course/gone.md<text:line-break/>and AGENTS.md</text:p>",
        )
        problems, decks, strings = self.run_check()
        self.assertEqual((decks, strings), (1, 2))
        self.assertEqual(len(problems), 1)
        self.assertEqual(problems[0][1], "page 1")

    def test_archive_and_old_decks_are_skipped(self):
        make_pptx(self.root / DECK_DIR / "archive/demo.pptx", [["course/gone.md"]])
        make_pptx(self.root / DECK_DIR / "demo_Old.pptx", [["course/gone.md"]])
        problems, decks, _ = self.run_check()
        self.assertEqual((problems, decks), ([], 0))


def string_constants(node):
    return [sub.value for sub in ast.walk(node) if isinstance(sub, ast.Constant) and isinstance(sub.value, str)]


def note_literals(tree):
    """Collect the string constants that feed speaker notes in a generator script."""
    found = []
    for node in ast.walk(tree):
        if isinstance(node, ast.keyword) and node.arg == "note":
            found += string_constants(node.value)
        elif isinstance(node, ast.Call) and getattr(node.func, "id", "") == "notes":
            for arg in node.args[1:]:
                found += string_constants(arg)
        elif isinstance(node, ast.Assign):
            if any(getattr(target, "id", "").endswith("note") for target in node.targets):
                found += string_constants(node.value)
    return found


def calls_name(tree, name):
    return any(
        isinstance(node, ast.Call) and getattr(node.func, "id", "") == name for node in ast.walk(tree)
    )


class DeckNoteHelperTests(unittest.TestCase):
    def test_sixteen_mappings_point_to_exact_files(self):
        self.assertEqual(len(helper.NOTE_PATH_FIXES), 16)
        for old, new in helper.NOTE_PATH_FIXES.items():
            self.assertEqual(helper.fix_note_paths(old), new)
            self.assertTrue(checker.is_file_exact(REPO / new), new)
            self.assertEqual(helper.note_path_strings(old), [old], "the checker must see the old form")

    def test_fix_is_idempotent_and_keeps_exact_paths(self):
        for new in helper.NOTE_PATH_FIXES.values():
            self.assertEqual(helper.fix_note_paths(new), new)
        text = "Deep dive: course/THEORY/03-ecology-infrastructure/ecology.md, then ecology.md."
        once = helper.fix_note_paths(text)
        self.assertEqual(
            once,
            "Deep dive: course/THEORY/03-ecology-infrastructure/ecology.md, then "
            "course/THEORY/03-ecology-infrastructure/ecology.md.",
        )
        self.assertEqual(helper.fix_note_paths(once), once)

    def test_prose_and_urls_stay_as_written(self):
        text = "All *.md files, https://example.org/ecology.md and ecology.mdx are not note paths."
        self.assertEqual(helper.fix_note_paths(text), text)


class GeneratorSourceTests(unittest.TestCase):
    def parse(self, name):
        return ast.parse((SLIDESHOW / name).read_text(encoding="utf-8"))

    def test_note_literals_in_generators_are_exact_paths(self):
        for name in ("build_deck.py", "patch_lecturer_edit.py"):
            literals = note_literals(self.parse(name))
            if name == "build_deck.py":
                self.assertGreater(len(literals), 20, "the scan found too few notes")
            for text in literals:
                for token in helper.note_path_strings(text):
                    self.assertTrue(
                        checker.is_file_exact(REPO / token), f"{name}: note names {token}, which is not an exact repo path"
                    )

    def test_lecture_constant_is_an_exact_path(self):
        tree = self.parse("build_deck.py")
        values = [
            node.value.value
            for node in tree.body
            if isinstance(node, ast.Assign)
            and any(getattr(target, "id", "") == "LECTURE" for target in node.targets)
        ]
        self.assertEqual(len(values), 1)
        self.assertTrue(checker.is_file_exact(REPO / values[0]))

    def test_generators_use_the_shared_helper(self):
        build = self.parse("build_deck.py")
        self.assertTrue(calls_name(build, "fix_note_paths"))
        patch = self.parse("patch_lecturer_edit.py")
        self.assertTrue(calls_name(patch, "normalize_presentation_notes"))


try:
    from pptx import Presentation
except ImportError:
    Presentation = None


@unittest.skipIf(Presentation is None, "python-pptx is not installed")
class GeneratorOutputTests(unittest.TestCase):
    def blank_deck(self, count):
        prs = Presentation()
        return prs, [prs.slides.add_slide(prs.slide_layouts[6]) for _ in range(count)]

    def test_build_deck_notes_helper_writes_exact_paths(self):
        build_spec = importlib.util.spec_from_file_location("build_deck_under_test", SLIDESHOW / "build_deck.py")
        try:
            build = importlib.util.module_from_spec(build_spec)
            build_spec.loader.exec_module(build)
        except ImportError:
            self.skipTest("build_deck.py needs Pillow")
        _, (slide,) = self.blank_deck(1)
        build.notes(slide, "Guides: course/howto-hermes-setup.md and ecology.md.")
        self.assertEqual(
            slide.notes_slide.notes_text_frame.text,
            "Guides: course/PRACTICE/01-harness-and-agents/howto-hermes-setup.md and "
            "course/THEORY/03-ecology-infrastructure/ecology.md.",
        )

    def test_normalize_presentation_notes(self):
        prs, (first, second, third) = self.blank_deck(3)
        first.notes_slide.notes_text_frame.text = "Read course/what-is-mcp.md.\nThen default-setup.md."
        second.notes_slide.notes_text_frame.text = "Nothing to fix: AGENTS.md."
        run_paragraph = third.notes_slide.notes_text_frame.paragraphs[0]
        run_paragraph.add_run().text = "Split run: course/what-is-"
        run_paragraph.add_run().text = "lint.md."
        self.assertEqual(helper.normalize_presentation_notes(prs), 3)
        self.assertEqual(
            first.notes_slide.notes_text_frame.text,
            "Read course/PRACTICE/06-mcp-and-tools/what-is-mcp.md.\n"
            "Then course/PRACTICE/01-harness-and-agents/default-setup.md.",
        )
        self.assertEqual(second.notes_slide.notes_text_frame.text, "Nothing to fix: AGENTS.md.")
        self.assertEqual(
            third.notes_slide.notes_text_frame.text,
            "Split run: course/PRACTICE/02-knowledge-bases/what-is-lint.md.",
        )
        self.assertEqual(helper.normalize_presentation_notes(prs), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
