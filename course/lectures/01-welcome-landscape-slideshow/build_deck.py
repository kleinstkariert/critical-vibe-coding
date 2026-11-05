#!/usr/bin/env python3
"""Build Session 01 welcome/landscape lecture deck (PPTX → LibreOffice ODP)."""
from __future__ import annotations

import sys
from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches, Pt

ROOT = Path(__file__).resolve().parent
IMG = ROOT / "images"
OUT_PPTX = ROOT / "01-welcome-landscape.pptx"

# Widescreen 16:9
W, H = Inches(13.333), Inches(7.5)

BG = RGBColor(0x12, 0x12, 0x12)
FG = RGBColor(0xF2, 0xF0, 0xEB)
MUTED = RGBColor(0xB8, 0xB4, 0xAC)
ACCENT = RGBColor(0xC4, 0x5C, 0x26)  # warm earth, not purple
CLAIM = RGBColor(0xD9, 0xA4, 0x41)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
SOFT = RGBColor(0x2A, 0x2A, 0x28)


def set_run(run, size=28, bold=False, color=FG, font="Georgia"):
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.color.rgb = color
    run.font.name = font


def add_notes(slide, text: str):
    notes = slide.notes_slide.notes_text_frame
    notes.clear()
    notes.text = text.strip()


def blank_slide(prs):
    layout = prs.slide_layouts[6]  # blank
    slide = prs.slides.add_slide(layout)
    shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, W, H)
    shape.fill.solid()
    shape.fill.fore_color.rgb = BG
    shape.line.fill.background()
    return slide


def add_textbox(slide, left, top, width, height, text, *, size=28, bold=False, color=FG, align=PP_ALIGN.LEFT, font="Georgia"):
    box = slide.shapes.add_textbox(left, top, width, height)
    tf = box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.alignment = align
    run = p.add_run()
    run.text = text
    set_run(run, size=size, bold=bold, color=color, font=font)
    return box


def add_multiline(slide, left, top, width, height, lines, *, size=22, color=FG, font="Georgia", spacing=True):
    box = slide.shapes.add_textbox(left, top, width, height)
    tf = box.text_frame
    tf.word_wrap = True
    for i, line in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = PP_ALIGN.LEFT
        if spacing:
            p.space_after = Pt(10)
        run = p.add_run()
        run.text = line
        set_run(run, size=size, bold=False, color=color, font=font)
    return box


def picture_cover(slide, path: Path, credit: str | None = None):
    """Full-bleed cover image + bottom scrim for title/credit."""
    from PIL import Image

    with Image.open(path) as im:
        iw, ih = im.size
    slide_w, slide_h = int(W), int(H)
    scale = max(slide_w / iw, slide_h / ih)
    pw, ph = int(iw * scale), int(ih * scale)
    left = int((slide_w - pw) / 2)
    top = int((slide_h - ph) / 2)
    pic = slide.shapes.add_picture(str(path), left, top, width=pw, height=ph)

    bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, Inches(5.4), W, Inches(2.1))
    bar.fill.solid()
    bar.fill.fore_color.rgb = RGBColor(0x0A, 0x0A, 0x0A)
    bar.line.fill.background()
    if credit:
        add_textbox(
            slide,
            Inches(0.5),
            Inches(6.95),
            Inches(12.3),
            Inches(0.4),
            credit,
            size=11,
            color=MUTED,
            font="Calibri",
        )
    return pic


def title_on_image(slide, title: str, subtitle: str | None = None):
    add_textbox(slide, Inches(0.5), Inches(5.55), Inches(12.3), Inches(0.9), title, size=36, bold=True, color=WHITE)
    if subtitle:
        add_textbox(slide, Inches(0.5), Inches(6.35), Inches(12.3), Inches(0.5), subtitle, size=18, color=MUTED, font="Calibri")


def typographic_slide(slide, kicker: str, title: str, body_lines: list[str] | None = None, tag: str | None = None):
    if kicker:
        add_textbox(slide, Inches(0.7), Inches(0.55), Inches(11.5), Inches(0.4), kicker, size=14, color=ACCENT, font="Calibri")
    add_textbox(slide, Inches(0.7), Inches(1.2), Inches(11.8), Inches(1.4), title, size=40, bold=True, color=FG)
    if tag:
        add_textbox(slide, Inches(0.7), Inches(2.6), Inches(4), Inches(0.35), tag, size=12, bold=True, color=CLAIM, font="Calibri")
    if body_lines:
        add_multiline(slide, Inches(0.7), Inches(3.1), Inches(11.5), Inches(3.5), body_lines, size=22, color=MUTED, font="Calibri")


def build():
    prs = Presentation()
    prs.slide_width = W
    prs.slide_height = H

    # 1 Title
    s = blank_slide(prs)
    picture_cover(
        s,
        IMG / "01-datacenter-aisle-cyrusone.jpg",
        "CyrusOne Carrollton interior — CyrusOne Inc. / CC BY-SA 3.0",
    )
    title_on_image(s, "Critical Vibe Coding", "Session 01 — Welcome & landscape")
    add_notes(
        s,
        "Part B classroom input after outdoor check-in.\n"
        "Open with optional video snip (session file). Then Q&A after each block.\n"
        "Priority airtime: technical layers (#2), visions/fears (#3), bubble (#4).",
    )

    # 2 Twin tracks
    s = blank_slide(prs)
    typographic_slide(
        s,
        "Block 1 — Scope",
        "Two tracks. Neither optional.",
        [
            "Technical — leave with a working personal agent setup",
            "Critical / shared space — fears, hopes, authorship, labour, ecology",
            "Third thread: the agent as interface (skills, tools, knowledge as material)",
        ],
    )
    add_notes(
        s,
        "Ask: Who came mostly for the install, who mostly for the politics?\n"
        "Midpoint (s9): demo + short proposal. Final (s13): architecture + one use + reflection.",
    )

    # 3 Layers
    s = blank_slide(prs)
    typographic_slide(
        s,
        "Block 2 — Vocabulary",
        "Model ⊂ Product ⊂ Agent",
        [
            "Model — trained network, tokens → tokens (weights)",
            "Product / chat — UI + safety + memory + billing around a model",
            "Agent — loop that calls tools, reads/writes files, follows skills",
            "One-liner: chat answers; an agent acts (with permission and tools).",
        ],
        tag="keep this vocabulary all semester",
    )
    add_notes(
        s,
        "Examples: Llama/Qwen/Claude model; ChatGPT/Claude.ai product; Hermes/Cursor Agent/Claude Code as agents.\n"
        "Q: Where is authorship if the agent writes half the patch?",
    )

    # 4 Training / inference / hallucination
    s = blank_slide(prs)
    picture_cover(
        s,
        IMG / "08-hpc-datacenter-energy-gov.jpg",
        "HPC data center — U.S. Department of Energy / public domain",
    )
    title_on_image(s, "Training → inference", "Fluent continuation ≠ truth")
    add_notes(
        s,
        "verified fact / teaching model (simplified):\n"
        "1 Training — next-token prediction; parameters store regularities, not a fact DB.\n"
        "2 Inference — prompt tokenized; model samples a continuation.\n"
        "3 Context window — working memory of this call.\n"
        "4 Hallucination — fluency ≠ truth; agents worsen this if they write files without verify.\n"
        "Good at: draft, translate formalisms, summarize, structure, boilerplate.\n"
        "Bad alone: ground truth, long-horizon accountability, unstated artistic intent.",
    )

    # 5 Context + why files
    s = blank_slide(prs)
    picture_cover(
        s,
        IMG / "03-sticky-notes-wall.jpg",
        "Sticky notes — ProjectManhattan / CC BY-SA 3.0",
    )
    title_on_image(s, "Context is finite", "Why agents need files (and a wiki habit)")
    add_notes(
        s,
        "English ≈ 0.75 words/token; longer context = more € and watts.\n"
        "A 200-page vault does not fit every call → small schema + index + pull relevant pages (LLM Wiki / Karpathy gist).",
    )

    # 6 Tools / skills / MCP
    s = blank_slide(prs)
    typographic_slide(
        s,
        "Block 2 — Preview (architecture = Session 02)",
        "Tools · Skills · MCP · Harness",
        [
            "Filesystem tools — read/write a vault (enough for a wiki)",
            "Skills — written procedures the agent should follow",
            "MCP — protocol to call other apps as tool kitchens",
            "Harness — everything that isn’t the model",
            "Metaphor: waiter (host) / kitchen (MCP server) / dish (result)",
        ],
    )
    add_notes(
        s,
        "Point to what-is-mcp / what-is-harness. Deep architecture next class.\n"
        "Q: Has anyone used an agent that edits files, not only chat?",
    )

    # 7 Local vs cloud
    s = blank_slide(prs)
    picture_cover(
        s,
        IMG / "02-gpu-cluster-nvidia-tesla.jpg",
        "Tesla / NVIDIA GPU cluster — ChrisDag / CC BY 2.0",
    )
    title_on_image(s, "Local vs cloud", "Privacy, lock-in, hardware € — one slide")
    add_notes(
        s,
        "Cloud API: strong models, little hardware — lock-in, logging, price, jurisdiction.\n"
        "Local weights: privacy, offline, cost control, political choice — hardware €, ops, weaker unless you invest.\n"
        "Deep dive: research/local-gpu-hardware-for-llms · sessions 3 + 10.",
    )

    # 8 Why now — CLAIM
    s = blank_slide(prs)
    typographic_slide(
        s,
        "Block 3 — Drivers / visions / fears",
        "Why now?",
        [
            "CLAIM — next growth platform after PC → internet → mobile",
            "Data + compute were already ready; race incentives matter",
            "Two industry stories: abundance talk AND x-risk talk — often same scene",
            "Amplifier ≠ neutral tool — who owns the knob?",
        ],
        tag="CLAIM · see visions-fears-regulation handout",
    )
    add_notes(
        s,
        "Primary script: course/visions-fears-regulation — four beats only.\n"
        "Drivers (Coxon). Double message (Stewart). Amplifier (Ismail / Zajko / Crawford).\n"
        "Regulation: uses & data & liability — not a global off-switch; watch regulation-as-marketing.\n"
        "Do not teach EU AI Act here — point to eu-ai-act-and-datenschutz.",
    )

    # 9 Double message typographic
    s = blank_slide(prs)
    add_textbox(s, Inches(0.7), Inches(0.55), Inches(11), Inches(0.4), "Block 3 — Two industry stories", size=14, color=ACCENT, font="Calibri")
    add_textbox(s, Inches(0.7), Inches(2.2), Inches(5.5), Inches(1.2), "Star Trek", size=44, bold=True, color=FG, align=PP_ALIGN.CENTER)
    add_textbox(s, Inches(7.0), Inches(2.2), Inches(5.5), Inches(1.2), "% extinction", size=44, bold=True, color=FG, align=PP_ALIGN.CENTER)
    add_textbox(
        s,
        Inches(0.7),
        Inches(4.5),
        Inches(12),
        Inches(1.2),
        "Pick a lane — or name the contradiction.",
        size=24,
        color=MUTED,
        align=PP_ALIGN.CENTER,
        font="Calibri",
    )
    add_notes(
        s,
        "Utopia rhetoric (UBI/UHI, abundance) is real discourse, not delivered policy.\n"
        "Same industry also sells existential risk. Stewart: credibility problem.\n"
        "Keep social/institutional fear stack for this course (labour, lock-in, ecology).",
    )

    # 10 Bubble thesis — three boxes
    s = blank_slide(prs)
    typographic_slide(
        s,
        "Block 4 — Economy",
        "Bubble ≠ useless technology",
        [
            "1 Financial bubble — investors overpay / lose money",
            "2 Productive investment boom — overbuild can leave usable infra (Perez…)",
            "3 Technological dead end — infra ages into scrap",
            "Open question: end-user demand once circular loops are stripped out?",
        ],
        tag="THESIS",
    )
    add_notes(
        s,
        "Core sentence from lecture draft: speculative finance, circular investment, and REAL infrastructure can coexist.\n"
        "Research: research/ai-bubble-productivity-datacenter.\n"
        "Q: If investors lose money but GPUs remain, who benefited?",
    )

    # 11 BIS numbers
    s = blank_slide(prs)
    add_textbox(s, Inches(0.7), Inches(0.5), Inches(12), Inches(0.4), "Block 4 — Circularity · verified fact · BIS Bulletin 137 (1 Oct 2026)", size=14, color=ACCENT, font="Calibri")
    add_textbox(s, Inches(0.7), Inches(1.6), Inches(12), Inches(1.0), "28.7%", size=72, bold=True, color=FG)
    add_textbox(s, Inches(0.7), Inches(2.7), Inches(12), Inches(0.5), "of AI firms’ investment deal value (2021–25) targeted other AI firms", size=18, color=MUTED, font="Calibri")
    add_textbox(s, Inches(0.7), Inches(3.5), Inches(12), Inches(0.7), "55.2%  incoming from other AI firms", size=28, bold=True, color=FG)
    add_textbox(s, Inches(0.7), Inches(4.3), Inches(12), Inches(0.7), "46.4%  of AI-to-AI deal value also had supplier–customer links", size=28, bold=True, color=FG)
    add_textbox(s, Inches(0.7), Inches(5.5), Inches(12), Inches(0.8), "Interdependence ≠ all demand is fake. (Interpretation from research note.)", size=18, color=CLAIM, font="Calibri")
    add_notes(
        s,
        "Quote three BIS bullets; source in footnote aloud.\n"
        "Tooze (Chartbook / Ones and Tooze Ep. 250): skeptical political-economy reading — concentrated capex, codependent hyperscalers.\n"
        "Q: Where does your ChatGPT subscription sit in that circular diagram?",
    )

    # 12 Acemoglu + US/CN
    s = blank_slide(prs)
    typographic_slide(
        s,
        "Block 4 — Productivity & ecosystems",
        "~1% GDP order of magnitude?",
        [
            "Acemoglu: nontrivial but modest macro effect over ~10 years — vs 7%+ consultancy headlines",
            "Serious economists disagree on magnitude and timing — not “AI does nothing”",
            "US hyperscalers — capex race, closed APIs, CUDA, private credit into DCs",
            "Chinese open-ish weights — fast release, exportable weights",
            "EU / academic — hosting jurisdiction; say clearly if students cannot use campus AI",
        ],
        tag="CLAIM vs bank/consultancy headlines",
    )
    add_notes(
        s,
        "Update Austrian academic AI access sentence before class (academic-ai-austria).\n"
        "Optional productive-bubble historical image next slide.",
    )

    # 13 Productive bubble / railway
    s = blank_slide(prs)
    picture_cover(
        s,
        IMG / "07-metropolitan-railway-map-1867.jpg",
        "Metropolitan Railway map, c. 1867 — public domain",
    )
    title_on_image(s, "Productive bubbles leave tracks", "Installation phases outlive the speculation")
    add_notes(
        s,
        "Perez / DeLong / Takshashila frame: overbuild can still leave usable infrastructure.\n"
        "Contrast with technological dead end. Capex photo bridge to ecology.",
    )

    # 14 Ecology
    s = blank_slide(prs)
    picture_cover(
        s,
        IMG / "06-datacenter-cooling-tower.jpg",
        "Data-center cooling tower, Mesa AZ — Rsparks3 / CC0",
    )
    title_on_image(s, "Ecology seed", "Local grids, water, neighbours — deep dive Session 11")
    add_notes(
        s,
        "Training vs inference: students mostly inference; still scales with tokens / video.\n"
        "US ~45% of global DC electricity (IEA 2024). Name water/land/grid/who lives next door — no scopes 1–3 lecture here.\n"
        "Space data centres: hype contrast only.",
    )

    # 15 Labour
    s = blank_slide(prs)
    picture_cover(
        s,
        IMG / "05-quarto-stato-pellizza.jpg",
        "Pellizza da Volpedo, Il Quarto Stato (1901) — public domain",
    )
    title_on_image(s, "Who trains / who clicks / who owns?", "Labour question — not a GDP headline")
    add_notes(
        s,
        "Separate macro claims (IMF/McKinsey) from observed creative freelance shifts and student anxiety.\n"
        "Ghost work: annotation, moderation, eval farms — Session 10.\n"
        "Acemoglu: inequality/welfare can move differently from GDP.\n"
        "Empty follow-up: student anxiety slide is a question only if needed.",
    )

    # 16 Regulation as marketing
    s = blank_slide(prs)
    typographic_slide(
        s,
        "Block 3 / 6 — Regulation",
        "Uses & data — not maths",
        [
            "Regulation can constrain uses, liability, data, markets",
            "It cannot put the maths back in the bottle",
            "Watch credibility marketing: utopia slides + safety theatre + fundraising",
            "Law orientation later: EU AI Act & Datenschutz note",
        ],
        tag="OPEN QUESTION for the room",
    )
    add_notes(
        s,
        "Folded from Block 6 into Block 3 per lecture draft.\n"
        "Ask: what would a credible local rule look like for your studio practice?",
    )

    # 17 Media-art stakes
    s = blank_slide(prs)
    picture_cover(
        s,
        IMG / "09-eqiad-server-aisle.jpg",
        "Wikimedia EQIAD cluster — Rob Halsell / CC BY-SA 3.0",
    )
    title_on_image(s, "Media-art stakes", "Speed · flattening · authorship · interface · refusal")
    add_notes(
        s,
        "Pressures: more iterations / less sitting with a bad idea; Midjourney sameness; who signed the patch;\n"
        "agent+wiki+MCP as the piece (session 5); knowing when NOT to use AI (Session 11).\n"
        "Prefer own installation photos when available. Link outdoor Part A themes back.",
    )

    # 18 Default stack + homework
    s = blank_slide(prs)
    typographic_slide(
        s,
        "Block 8 — Default setup (preview)",
        "Obsidian · Hermes · Wiki habits",
        [
            "1 Knowledge store with phone sync (default Obsidian; alternatives OK)",
            "2 Hermes Agent pointed at that vault",
            "3 Harness + LLM Wiki habits — next class",
            "4 Models: whatever you already pay for / can access",
            "Homework: course GitHub · note LLM access · optional Karpathy gist",
        ],
    )
    add_notes(
        s,
        "Repeat homework aloud. Student share pack, not whole vault.\n"
        "Next: harness after a student humanities input.",
    )

    # 19 Closing Q
    s = blank_slide(prs)
    picture_cover(
        s,
        IMG / "04-messy-desk.jpg",
        "Messy desk — Sugar Pond / CC BY-SA 2.0",
    )
    title_on_image(s, "What stays with you from Part A?", "Bring one fear and one hope into the stack")
    add_notes(
        s,
        "Close: collect open questions for later input nodes. 11:55–12:00 homework + close.",
    )

    prs.save(OUT_PPTX)
    print(f"Wrote {OUT_PPTX} with {len(prs.slides)} slides")
    return len(prs.slides)


if __name__ == "__main__":
    n = build()
    sys.exit(0 if n else 1)
