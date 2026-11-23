"""Apply the 11 Nov 2026 review fixes on top of Sebastian's own edit of the deck.

Base: Sebastian's edit (his bullets, wording, pages and links stay as he left them).
Donor: the agent build of 11 Nov, used only for the requested new slides, images,
credit strips and notes.

    python patch_sebastian_edit.py

Do not run build_deck.py over the deck: it rebuilds every slide from scratch and
drops manual edits.
"""

import copy
import io
from pathlib import Path

from pptx import Presentation
from pptx.util import Emu, Inches

HERE = Path(__file__).parent
# Local-only inputs (not tracked). Teaching deck is OUT; keep archives off git.
BASE = HERE / "archive" / "2026-11-11-1854-sebastian-edit-52-slides-old.pptx"
DONOR = HERE / "archive" / "2026-11-11-1848-agent-build-55-slides-before-restore.pptx"
OUT = HERE / "01-welcome-landscape.pptx"

P = "{http://schemas.openxmlformats.org/presentationml/2006/main}"
A = "{http://schemas.openxmlformats.org/drawingml/2006/main}"

MEDIUM_URL = (
    "https://medium.com/online-inference/"
    "agentic-loops-in-ai-governance-feedback-and-failure-modes-at-scale-f038e32add6c"
)

if not BASE.is_file() or not DONOR.is_file():
    raise SystemExit(
        "BASE/DONOR pptx missing. Archives are not in git. "
        "Edit 01-welcome-landscape.pptx directly, or restore local archive copies."
    )

base = Presentation(str(BASE))
donor = Presentation(str(DONOR))
B = list(base.slides)
D = list(donor.slides)
blank_layout = [l for l in base.slide_layouts if l.name == "Blank"][0]


def old(n):
    return B[n - 1]


def don(n):
    return D[n - 1]


def shape(slide, name):
    return [s for s in slide.shapes if s.name == name][0]


def notes(slide):
    return slide.notes_slide.notes_text_frame.text


def set_notes(slide, text):
    slide.notes_slide.notes_text_frame.text = text


def next_id(slide):
    ids = [int(e.get("id")) for e in slide._element.iter(P + "cNvPr")]
    return max(ids + [1]) + 1


def append_shape_xml(slide, sp):
    sp = copy.deepcopy(sp)
    sp.find(".//" + P + "cNvPr").set("id", str(next_id(slide)))
    slide.shapes._spTree.append(sp)
    return sp


def remove_pictures(slide):
    for pic in [s for s in slide.shapes if s.shape_type == 13]:
        rId = pic._element.blipFill.find(A + "blip").get(
            "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed"
        )
        pic._element.getparent().remove(pic._element)
        slide.part.drop_rel(rId)


def copy_picture(src_pic, slide):
    pic = slide.shapes.add_picture(
        io.BytesIO(src_pic.image.blob), src_pic.left, src_pic.top, src_pic.width, src_pic.height
    )
    for side in ("crop_left", "crop_right", "crop_top", "crop_bottom"):
        setattr(pic, side, getattr(src_pic, side))
    return pic


def donor_image_slide(target, src):
    """Swap the picture for the donor's fitted picture and copy its credit strip."""
    remove_pictures(target)
    for s in src.shapes:
        if s.shape_type == 13:
            copy_picture(s, target)
    for s in src.shapes:
        if s.has_text_frame and s.top >= Inches(7.0):
            append_shape_xml(target, s._element)


def set_runs(par, runs):
    """Replace the runs of a paragraph, keeping its bullet and run formatting."""
    tmpl = par.runs[0]._r
    for r in list(par._p.findall(A + "r")):
        par._p.remove(r)
    end = par._p.find(A + "endParaRPr")
    for text, bold, size in runs:
        r = copy.deepcopy(tmpl)
        r.find(A + "t").text = text
        rpr = r.find(A + "rPr")
        rpr.set("b", "1" if bold else "0")
        if size:
            rpr.set("sz", str(size))
        if end is not None:
            end.addprevious(r)
        else:
            par._p.append(r)


def donor_runs(par, size=False):
    return [(r.text, bool(r.font.bold), int(r.font.size.pt * 100) if size and r.font.size else None) for r in par.runs]


def fill_body(body, donor_pars, template_par, size=False):
    """Rebuild a text box with Sebastian's bullet paragraph as the template."""
    txBody = body.text_frame._txBody
    for p in list(txBody.findall(A + "p")):
        txBody.remove(p)
    for dp in donor_pars:
        p = copy.deepcopy(template_par._p)
        txBody.append(p)
    for p, dp in zip(body.text_frame.paragraphs, donor_pars):
        set_runs(p, donor_runs(dp, size))


def append_par(body, template_par, runs):
    p = copy.deepcopy(template_par._p)
    body.text_frame._txBody.append(p)
    set_runs(body.text_frame.paragraphs[-1], runs)


def set_text(shape_, text):
    par = shape_.text_frame.paragraphs[0]
    set_runs(par, [(text, bool(par.runs[0].font.bold), None)])


def new_slide_like(src):
    """New slide with the background and text boxes of one of Sebastian's slides."""
    s = base.slides.add_slide(blank_layout)
    for ph in list(s.placeholders):
        ph._element.getparent().remove(ph._element)
    bg = src._element.cSld.find(P + "bg")
    if bg is not None:
        s._element.cSld.insert(0, copy.deepcopy(bg))
    for sh in src.shapes:
        if sh.shape_type != 13:
            append_shape_xml(s, sh._element)
    return s


# Sebastian's vocabulary bullet: bold label, plain definition.
VOCAB_TMPL = shape(old(6), "TextBox 4").text_frame.paragraphs[0]

# 1. Image slides: credits on the slide (donor credit strips), fitted pictures.
image_pairs = {
    1: 1, 5: 5, 7: 7, 12: 13, 18: 20, 21: 25, 23: 27, 24: 28, 26: 30, 29: 33,
    32: 36, 34: 38, 36: 40, 38: 42, 41: 45, 43: 47, 44: 48, 47: 51, 51: 55,
}
for o, d in image_pairs.items():
    donor_image_slide(old(o), don(d))

# Restored "Cloud or local" diagram (slide 10 of his edit) gets a credit strip too.
s10 = old(10)
pic = [s for s in s10.shapes if s.shape_type == 13][0]
h = Inches(7.08)
w = int(pic.width * h / pic.height)
pic.left, pic.top, pic.width, pic.height = int((base.slide_width - w) / 2), 0, w, h
strip = append_shape_xml(s10, [s for s in don(1).shapes if s.has_text_frame][0]._element)
strip.find(".//" + A + "t").text = "Diagram for this course, 2026."

# Agent loop source (slide 7).
strip7 = [s for s in old(7).shapes if s.has_text_frame][0]
set_text(strip7, 'Agentic AI loop. David Davies, "Agentic loops in AI", Online Inference (Medium), Aug 2026. Shown in black and white.')
loop_desc = notes(don(7)).split("\n\nImage:")[0]
set_notes(
    old(7),
    loop_desc
    + "\n\nImage: David Davies, Agentic loops in AI: Governance, feedback, and failure modes at scale, "
    "Online Inference (Medium), 5 Aug 2026. " + MEDIUM_URL + " Lead image, shown inverted in black and white. "
    "Teaching citation.",
)

# 2. Vocabulary: sandbox and lint, in his bullet format.
voc = shape(old(6), "TextBox 4")
append_par(voc, VOCAB_TMPL, [("Sandbox:", True, None), (" a closed space where the agent can run code without touching the rest of your system.", False, None)])
append_par(voc, VOCAB_TMPL, [("Lint:", True, None), (" an automatic check for mistakes, such as bugs in code or broken links in a wiki.", False, None)])

# 3. Bank for International Settlements spelled out on the slides.
set_text(shape(old(20), "TextBox 5"), shape(don(24), "TextBox 5").text_frame.text)
set_text(shape(old(25), "TextBox 16"), shape(don(29), "TextBox 5").text_frame.text)
set_text(shape(old(28), "TextBox 5"), shape(don(32), "TextBox 5").text_frame.text)
tooze = shape(old(28), "TextBox 4")
set_text_par = tooze.text_frame.paragraphs[3]
set_runs(set_text_par, [(shape(don(32), "TextBox 4").text_frame.paragraphs[3].text, False, None)])

# 4. Demand bottleneck in plain words, on the slide.
append_par(tooze, tooze.text_frame.paragraphs[0], donor_runs(shape(don(32), "TextBox 4").text_frame.paragraphs[5]))

# Notes where a requested fix adds an explanation. His notes stay; additions follow.
for o, d in {1: 1, 6: 6, 18: 20, 22: 26, 23: 27, 25: 29, 32: 36, 34: 38, 36: 40, 47: 51}.items():
    set_notes(old(o), notes(don(d)))

set_notes(old(24), notes(old(24)) + "\n\n" + notes(don(28)))

cape_old = notes(old(26)).split("\n\nImage:")[0]
set_notes(old(26), cape_old + "\n" + notes(don(30)))

n28 = notes(old(28)).split("\n")
bottleneck = [l for l in notes(don(32)).split("\n") if l.startswith("Demand bottleneck")][0]
url_i = [i for i, l in enumerate(n28) if l.startswith("https://")][0]
n28.insert(url_i, bottleneck)
set_notes(old(28), "\n".join(n28))

n29 = notes(old(29)).split("\n\nImage:")[0]
set_notes(
    old(29),
    n29
    + " Demand bottleneck: replaced workers buy less, so further automation stops paying."
    + "\n\nImage: Chart for this course, redrawn after Bank for International Settlements (BIS), "
    "Annual Economic Report 2026, Box C, Graph C1.B.",
)

# 5. New slides from the requested fixes.
def new_image_slide(d):
    s = base.slides.add_slide(blank_layout)
    for ph in list(s.placeholders):
        ph._element.getparent().remove(ph._element)
    s._element.cSld.insert(0, copy.deepcopy(old(5)._element.cSld.find(P + "bg")))
    donor_image_slide(s, don(d))
    set_notes(s, notes(don(d)))
    return s


# Why the course setup: his slide 9 header, his bullet style.
pros = new_slide_like(old(9))
set_text(shape(pros, "TextBox 3"), "Why the course setup")
fill_body(shape(pros, "TextBox 4"), shape(don(11), "TextBox 4").text_frame.paragraphs, VOCAB_TMPL)
q = shape(pros, "TextBox 5")
q._element.getparent().remove(q._element)
foot = append_shape_xml(pros, shape(old(4), "TextBox 5")._element)
foot.find(".//" + A + "t").text = shape(don(11), "TextBox 5").text_frame.text
set_notes(pros, notes(don(11)))

course_setup = new_image_slide(10)

# Hype cycle: his slide 17 header, text left, curve right.
hype = new_slide_like(old(17))
set_text(shape(hype, "TextBox 9"), shape(don(18), "TextBox 3").text_frame.text)
hb = shape(hype, "TextBox 10")
db = shape(don(18), "TextBox 4")
hb.left, hb.top, hb.width = db.left, db.top, db.width
fill_body(hb, db.text_frame.paragraphs, VOCAB_TMPL, size=True)
set_text(shape(hype, "TextBox 11"), shape(don(18), "TextBox 6").text_frame.text)
for s in don(18).shapes:
    if s.shape_type == 13:
        copy_picture(s, hype)
set_notes(hype, notes(don(18)))

gdp = new_image_slide(21)
mag7 = new_image_slide(22)

# 6. Order: his slides, new slides placed as in the requested fixes, credits page removed.
sld = base.slides._sldIdLst
ids = list(sld)
by_slide = {s.slide_id: e for s, e in zip(base.slides, ids)}


def sid(s):
    return by_slide[s.slide_id]


credits = old(52)
order = []
for n in range(1, 52):
    order.append(sid(old(n)))
    if n == 10:
        order += [sid(pros), sid(course_setup)]
    if n == 16:
        order.append(sid(hype))
    if n == 18:
        order += [sid(gdp), sid(mag7)]

credits_el = sid(credits)
for e in ids:
    sld.remove(e)
for e in order:
    sld.append(e)
base.part.drop_rel(credits_el.rId)

base.save(str(OUT))
print(f"wrote {OUT.name}: {len(order)} slides")
