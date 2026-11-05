#!/usr/bin/env python3
"""Build Session 01 welcome/landscape lecture deck (PPTX → LibreOffice ODP).

Structure follows course/lectures/01-welcome-landscape-lecture.md blocks 1–8.
Visual direction: Scandinavian-minimal — cool neutrals, whitespace, restrained type.
Argument lives in speaker notes. No gag slides.
"""
from __future__ import annotations

import sys
from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches, Pt, Emu

ROOT = Path(__file__).resolve().parent
IMG = ROOT / "images"
OUT_PPTX = ROOT / "01-welcome-landscape.pptx"

# Widescreen 16:9
W, H = Inches(13.333), Inches(7.5)

# Scandinavian-minimal palette (cool neutrals — not purple, not cream/terracotta)
BG = RGBColor(0xF4, 0xF5, 0xF7)          # cool light grey
BG_SOFT = RGBColor(0xE8, 0xEA, 0xEE)
FG = RGBColor(0x1C, 0x1F, 0x24)           # near-black
MUTED = RGBColor(0x6B, 0x73, 0x80)        # slate
ACCENT = RGBColor(0x3D, 0x5A, 0x66)       # muted blue-grey
LINE = RGBColor(0xC5, 0xCB, 0xD3)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
SCRIM = RGBColor(0x14, 0x16, 0x1A)

FONT_DISPLAY = "Calibri Light"
FONT_BODY = "Calibri"


def set_run(run, size=28, bold=False, color=FG, font=FONT_BODY):
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.color.rgb = color
    run.font.name = font


def add_notes(slide, text: str):
    notes = slide.notes_slide.notes_text_frame
    notes.clear()
    notes.text = text.strip()


def blank_slide(prs, bg=BG):
    layout = prs.slide_layouts[6]  # blank
    slide = prs.slides.add_slide(layout)
    shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, W, H)
    shape.fill.solid()
    shape.fill.fore_color.rgb = bg
    shape.line.fill.background()
    return slide


def add_textbox(
    slide,
    left,
    top,
    width,
    height,
    text,
    *,
    size=28,
    bold=False,
    color=FG,
    align=PP_ALIGN.LEFT,
    font=FONT_BODY,
):
    box = slide.shapes.add_textbox(left, top, width, height)
    tf = box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.alignment = align
    run = p.add_run()
    run.text = text
    set_run(run, size=size, bold=bold, color=color, font=font)
    return box


def add_multiline(
    slide,
    left,
    top,
    width,
    height,
    lines,
    *,
    size=20,
    color=FG,
    font=FONT_BODY,
    spacing=True,
):
    box = slide.shapes.add_textbox(left, top, width, height)
    tf = box.text_frame
    tf.word_wrap = True
    for i, line in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = PP_ALIGN.LEFT
        if spacing:
            p.space_after = Pt(12)
        run = p.add_run()
        run.text = line
        set_run(run, size=size, bold=False, color=color, font=font)
    return box


def hairline(slide, top=Inches(1.15)):
    line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.75), top, Inches(1.4), Emu(4000))
    line.fill.solid()
    line.fill.fore_color.rgb = ACCENT
    line.line.fill.background()


def typographic_slide(
    slide,
    kicker: str,
    title: str,
    body_lines: list[str] | None = None,
    tag: str | None = None,
):
    if kicker:
        add_textbox(
            slide,
            Inches(0.75),
            Inches(0.55),
            Inches(11.5),
            Inches(0.35),
            kicker,
            size=13,
            color=ACCENT,
            font=FONT_BODY,
        )
    hairline(slide)
    add_textbox(
        slide,
        Inches(0.75),
        Inches(1.45),
        Inches(11.8),
        Inches(1.35),
        title,
        size=36,
        bold=False,
        color=FG,
        font=FONT_DISPLAY,
    )
    if tag:
        add_textbox(
            slide,
            Inches(0.75),
            Inches(2.85),
            Inches(11),
            Inches(0.35),
            tag,
            size=12,
            bold=True,
            color=MUTED,
            font=FONT_BODY,
        )
    if body_lines:
        y = Inches(3.35) if tag else Inches(3.05)
        add_multiline(
            slide,
            Inches(0.75),
            y,
            Inches(11.5),
            Inches(3.6),
            body_lines,
            size=18,
            color=MUTED,
            font=FONT_BODY,
        )


def picture_cover(slide, path: Path, credit: str | None = None, dark_scrim=True):
    """Full-bleed cover image + bottom scrim for title/credit."""
    from PIL import Image

    with Image.open(path) as im:
        iw, ih = im.size
    slide_w, slide_h = int(W), int(H)
    scale = max(slide_w / iw, slide_h / ih)
    pw, ph = int(iw * scale), int(ih * scale)
    left = int((slide_w - pw) / 2)
    top = int((slide_h - ph) / 2)
    slide.shapes.add_picture(str(path), left, top, width=pw, height=ph)

    if dark_scrim:
        bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, Inches(5.35), W, Inches(2.15))
        bar.fill.solid()
        bar.fill.fore_color.rgb = SCRIM
        bar.line.fill.background()
    if credit:
        add_textbox(
            slide,
            Inches(0.55),
            Inches(6.95),
            Inches(12.2),
            Inches(0.35),
            credit,
            size=10,
            color=MUTED,
            font=FONT_BODY,
        )


def title_on_image(slide, title: str, subtitle: str | None = None):
    add_textbox(
        slide,
        Inches(0.55),
        Inches(5.5),
        Inches(12.2),
        Inches(0.85),
        title,
        size=32,
        bold=False,
        color=WHITE,
        font=FONT_DISPLAY,
    )
    if subtitle:
        add_textbox(
            slide,
            Inches(0.55),
            Inches(6.3),
            Inches(12.2),
            Inches(0.45),
            subtitle,
            size=16,
            color=MUTED,
            font=FONT_BODY,
        )


def build():
    prs = Presentation()
    prs.slide_width = W
    prs.slide_height = H

    # ── Block 1 — Scope ──────────────────────────────────────────────
    # 1 Title
    s = blank_slide(prs)
    picture_cover(
        s,
        IMG / "13-meta-el-paso-contentstack.jpg",
        "Meta El Paso data-center campus (press / Contentstack CDN) — teaching use; see ATTRIBUTION.md",
    )
    title_on_image(s, "Critical Vibe Coding", "Session 01 — Welcome & landscape")
    add_notes(
        s,
        "Part B classroom input after outdoor check-in.\n"
        "Priority airtime: Block 2 (technical), Block 3 (visions/fears/regulation), Block 4 (bubble).\n"
        "Q&A after each block. Source: course/lectures/01-welcome-landscape-lecture.md",
    )

    # 2 Twin tracks
    s = blank_slide(prs)
    typographic_slide(
        s,
        "Block 1 — Scope · ~4 min",
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
        "Midpoint (s9): demo + short proposal. Final (s13): architecture + one use + reflection.\n"
        "Neither track is optional.",
    )

    # ── Block 2 — What LLMs / agents are ─────────────────────────────
    # 3 Layers
    s = blank_slide(prs)
    typographic_slide(
        s,
        "Block 2 — What LLMs and agents are · ~12 min · high priority",
        "Model ⊂ Product ⊂ Agent",
        [
            "Model — trained network, tokens → tokens (weights on disk / GPU)",
            "Product / chat — UI + safety + memory + billing around a model",
            "Agent — loop that calls tools, reads/writes files, follows skills",
            "Chat answers. An agent acts — with your permission and tools.",
        ],
        tag="Keep this vocabulary all semester",
    )
    add_notes(
        s,
        "Examples: Llama/Qwen/Claude model; ChatGPT/Claude.ai product; Hermes/Cursor Agent/Claude Code as agents.\n"
        "Q: Where is authorship if the agent writes half the patch?",
    )

    # 4 Training / inference
    s = blank_slide(prs)
    picture_cover(
        s,
        IMG / "08-hpc-datacenter-energy-gov.jpg",
        "HPC data center — U.S. Department of Energy / public domain",
    )
    title_on_image(s, "Training → inference", "Fluent continuation is not truth")
    add_notes(
        s,
        "verified fact / teaching model (simplified):\n"
        "1 Training — next-token prediction; parameters store regularities, not a fact database.\n"
        "2 Inference — prompt tokenized; the model samples a continuation.\n"
        "3 Context window — working memory of this call.\n"
        "4 Hallucination — fluency ≠ truth; agents worsen this if they write files without verify.\n"
        "Good at: draft, translate formalisms, summarize, structure, boilerplate.\n"
        "Bad alone: ground truth, long-horizon accountability, unstated artistic intent.",
    )

    # 5 Context + files
    s = blank_slide(prs)
    typographic_slide(
        s,
        "Block 2 — Context",
        "Context is finite",
        [
            "Longer context = more compute per turn = more € and watts",
            "A 200-page vault does not fit in every call",
            "Pattern: small schema + index + pull only relevant pages",
            "That is the LLM Wiki habit (Karpathy gist) — Session 02 deepens it",
        ],
    )
    add_notes(
        s,
        "English ≈ 0.75 words/token; code denser.\n"
        "Why agents need files: overflow forces drop or summarize.\n"
        "Image alternative if wanted: sticky-notes overflow (03) — keep typographic for calm Scandinavian beat.",
    )

    # 6 Tools / skills / MCP / harness
    s = blank_slide(prs)
    typographic_slide(
        s,
        "Block 2 — Preview (architecture = Session 02)",
        "Tools · Skills · MCP · Harness",
        [
            "Filesystem tools — read/write a vault (enough for a wiki)",
            "Skills — written procedures the agent should follow",
            "MCP — protocol so an agent can call other apps as tool kitchens",
            "Harness — everything that is not the model",
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
    title_on_image(s, "Local vs cloud", "Privacy, lock-in, hardware cost — one slide")
    add_notes(
        s,
        "Cloud API: strong models, little hardware — lock-in, logging, price, jurisdiction.\n"
        "Local weights: privacy, offline, cost control, political choice — hardware €, ops, weaker unless you invest.\n"
        "Deep dive: research/local-gpu-hardware-for-llms · sessions 3 + 10.",
    )

    # ── Block 3 — Drivers / visions / fears / regulation ─────────────
    # 8 Drivers
    s = blank_slide(prs)
    typographic_slide(
        s,
        "Block 3 — Drivers, visions, fears, regulation · 10–15 min · high priority",
        "Why now?",
        [
            "CLAIM — next growth platform after PC → internet → mobile",
            "Data and compute were already ready; race incentives matter",
            "Script: course/visions-fears-regulation — four beats only",
            "Do not teach the EU AI Act here — point to eu-ai-act-and-datenschutz",
        ],
        tag="CLAIM · political-economy frame",
    )
    add_notes(
        s,
        "Primary script: course/visions-fears-regulation.\n"
        "Beat 1 Drivers (Coxon): growth treadmill + data/compute + race — not “we asked for utopia.”\n"
        "Technical scaling is real and parallel to the money story.",
    )

    # 9 Two industry stories (serious — lecture frames sci-fi vs doom discourse)
    s = blank_slide(prs)
    add_textbox(
        s,
        Inches(0.75),
        Inches(0.55),
        Inches(11.5),
        Inches(0.35),
        "Block 3 — Two industry stories",
        size=13,
        color=ACCENT,
        font=FONT_BODY,
    )
    hairline(s)
    add_textbox(
        s,
        Inches(0.75),
        Inches(1.6),
        Inches(5.5),
        Inches(1.0),
        "Abundance rhetoric",
        size=28,
        color=FG,
        font=FONT_DISPLAY,
        align=PP_ALIGN.LEFT,
    )
    add_textbox(
        s,
        Inches(7.0),
        Inches(1.6),
        Inches(5.5),
        Inches(1.0),
        "Existential risk rhetoric",
        size=28,
        color=FG,
        font=FONT_DISPLAY,
        align=PP_ALIGN.LEFT,
    )
    # vertical divider
    div = s.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, Inches(6.55), Inches(1.55), Emu(2500), Inches(3.2)
    )
    div.fill.solid()
    div.fill.fore_color.rgb = LINE
    div.line.fill.background()
    add_multiline(
        s,
        Inches(0.75),
        Inches(2.8),
        Inches(5.4),
        Inches(2.8),
        [
            "UBI / UHI talk, “age of abundance”",
            "Real discourse — not delivered policy",
            "Musk, Altman, Ismail responses",
        ],
        size=16,
        color=MUTED,
    )
    add_multiline(
        s,
        Inches(7.0),
        Inches(2.8),
        Inches(5.4),
        Inches(2.8),
        [
            "Loss of control, misuse, race under-funds safety",
            "Same industry scene often carries both stories",
            "Credibility problem if both are sold at once",
        ],
        size=16,
        color=MUTED,
    )
    add_notes(
        s,
        "Lecture frames positive sci-fi futures vs doom futures as industry discourse — keep serious.\n"
        "Utopia rhetoric (UBI/UHI, abundance) is real discourse, not a funded social contract.\n"
        "Same scene also sells existential risk. Stewart: pick a lane / credibility problem.\n"
        "This course spends more time on the social/institutional fear stack (labour, lock-in, ecology).\n"
        "Clips (teacher): Coxon Daily Show; Stewart monologue — paths in visions-fears-regulation.",
    )

    # 10 Amplifier
    s = blank_slide(prs)
    typographic_slide(
        s,
        "Block 3 — Amplifier vs power",
        "Who owns the gain knob?",
        [
            "Ismail: AI as amplifier — useful language",
            "Social science: not neutral; amplifies hierarchy; feedback loops",
            "A tutor-bot for a student ≠ a hyperscaler with weights, cloud, and lobbying",
            "“Depends how you use it” is incomplete for platforms that reorganise labour and grids",
        ],
    )
    add_notes(
        s,
        "Ismail amplifier / fire metaphor — then complicate with Crawford / Zajko.\n"
        "Class line: Amplifier is useful if you always ask who owns the gain knob.",
    )

    # 11 Regulation (Block 6 folded here)
    s = blank_slide(prs)
    typographic_slide(
        s,
        "Block 3 (+6) — Regulation",
        "Uses and data — not mathematics",
        [
            "Regulation can constrain uses, liability, data, markets",
            "It cannot put the maths back in the bottle",
            "Watch credibility marketing: safety theatre + fundraising",
            "Law orientation: course/eu-ai-act-and-datenschutz (not taught in this hour)",
        ],
        tag="OPEN QUESTION for the room",
    )
    add_notes(
        s,
        "Beat 4 from visions-fears-regulation. Folded from Block 6 per lecture.md.\n"
        "Ask: what would a credible local rule look like for your studio practice?\n"
        "GDPR stays in parallel with the AI Act — verified fact from DSB position in the law note.",
    )

    # ── Block 4 — Bubble / economy ───────────────────────────────────
    # 12 Thesis
    s = blank_slide(prs)
    typographic_slide(
        s,
        "Block 4 — Economic background · 10–12 min · high priority",
        "Bubble does not mean useless technology",
        [
            "1 Financial bubble — investors overpay / lose money",
            "2 Productive investment boom — overbuild can leave usable infra (Perez…)",
            "3 Technological dead end — infra ages into scrap",
            "Open question: end-user demand once circular loops are stripped out?",
        ],
        tag="THESIS · research/ai-bubble-productivity-datacenter",
    )
    add_notes(
        s,
        "Core sentence: speculative finance, circular investment, and REAL infrastructure can coexist.\n"
        "Q: If investors lose money but GPUs remain, who benefited?",
    )

    # 13 BIS numbers
    s = blank_slide(prs)
    add_textbox(
        s,
        Inches(0.75),
        Inches(0.5),
        Inches(12),
        Inches(0.4),
        "Block 4 — Circularity · verified fact · BIS Bulletin 137 (1 Oct 2026)",
        size=13,
        color=ACCENT,
        font=FONT_BODY,
    )
    hairline(s, top=Inches(1.0))
    add_textbox(s, Inches(0.75), Inches(1.5), Inches(12), Inches(0.9), "28.7%", size=64, color=FG, font=FONT_DISPLAY)
    add_textbox(
        s,
        Inches(0.75),
        Inches(2.45),
        Inches(12),
        Inches(0.45),
        "of AI firms’ investment deal value (2021–25) targeted other AI firms",
        size=16,
        color=MUTED,
        font=FONT_BODY,
    )
    add_textbox(s, Inches(0.75), Inches(3.3), Inches(12), Inches(0.55), "55.2%  incoming from other AI firms", size=26, color=FG, font=FONT_DISPLAY)
    add_textbox(
        s,
        Inches(0.75),
        Inches(4.0),
        Inches(12),
        Inches(0.55),
        "46.4%  of AI-to-AI deal value also had supplier–customer links",
        size=26,
        color=FG,
        font=FONT_DISPLAY,
    )
    add_textbox(
        s,
        Inches(0.75),
        Inches(5.2),
        Inches(12),
        Inches(0.7),
        "Interdependence is not proof that all demand is fake.",
        size=18,
        color=ACCENT,
        font=FONT_BODY,
    )
    add_notes(
        s,
        "Quote three BIS bullets; source aloud.\n"
        "Tooze (Chartbook / Ones and Tooze Ep. 250 clipping): skeptical political-economy — concentrated capex, codependent hyperscalers.\n"
        "Q: Where does your ChatGPT subscription sit in that circular diagram?",
    )

    # 14 Productivity + ecosystems
    s = blank_slide(prs)
    typographic_slide(
        s,
        "Block 4 — Productivity and ecosystems",
        "Modest macro effect — contested timing",
        [
            "Acemoglu: nontrivial but modest macro GDP effect over ~10 years (~1% order) vs 7%+ consultancy headlines",
            "Serious economists disagree on magnitude and timing — not “AI does nothing”",
            "US hyperscalers — capex race, closed APIs, CUDA, private credit into data centres",
            "Chinese open-ish weights — fast release, exportable weights",
            "EU / academic — hosting jurisdiction; say clearly if students cannot use campus AI",
        ],
    )
    add_notes(
        s,
        "Update Austrian academic AI access sentence before class (academic-ai-austria).\n"
        "Vault clipping: A new look at the economics of AI (Acemoglu / MIT Sloan).",
    )

    # 15 Productive bubble / historical
    s = blank_slide(prs)
    picture_cover(
        s,
        IMG / "07-metropolitan-railway-map-1867.jpg",
        "Metropolitan Railway map, c. 1867 — public domain",
    )
    title_on_image(s, "Productive bubbles leave tracks", "Installation phases can outlive the speculation")
    add_notes(
        s,
        "Perez / DeLong / Takshashila: overbuild can still leave usable infrastructure.\n"
        "Contrast with technological dead end. Bridge to ecology / real build-out next.",
    )

    # ── Block 5 — Ecology / labour seed ──────────────────────────────
    # 16 GW Ranch — PROMINENT (Sebastian favourite)
    s = blank_slide(prs)
    picture_cover(
        s,
        IMG / "11-gw-ranch-heise.jpg",
        "GW Ranch render — via heise online (Amazon / Pacifico Energy AI campus + gas generation, Texas) · ATTRIBUTION.md",
    )
    title_on_image(
        s,
        "Real build-out at campus scale",
        "Ecology seed · local grids, water, emissions, neighbours — deep dive Session 11",
    )
    add_notes(
        s,
        "PROMINENT image (Sebastian). GW Ranch: off-grid gas generation planned for hyperscale AI — Heise reporting on Amazon/Pacifico plans in Texas.\n"
        "Use as scale + ecology bridge: training vs inference; students mostly inference; still scales with tokens/video.\n"
        "US ~45% of global DC electricity (IEA 2024). Name water/land/grid/who lives next door — no scopes 1–3 lecture here.\n"
        "Space data centres: hype contrast only.\n"
        "Research: data-centers-energy-ecology-economy · Session 11.",
    )

    # 17 Labour
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
        "Jobs seed only: rising tide + early-career canary — research/ai-jobs-rising-tide-productivity.",
    )

    # ── Block 7 — Media-art workflows ────────────────────────────────
    # 18 Media-art stakes
    s = blank_slide(prs)
    typographic_slide(
        s,
        "Block 7 — Media-art workflows · ~5 min",
        "Speed · flattening · authorship · interface · refusal",
        [
            "More iterations — less sitting with a bad idea",
            "Taste flattening — same generative look, same helpful prose voice",
            "Authorship — who signed the work if the agent wrote the patch?",
            "New interfaces — agent + wiki + MCP as the piece (Session 05)",
            "Refusal — knowing when not to use AI is a skill (Session 11)",
        ],
    )
    add_notes(
        s,
        "Link outdoor Part A themes back. Prefer own installation photos when available.\n"
        "Block 6 regulation already covered inside Block 3.",
    )

    # ── Block 8 — Default setup ──────────────────────────────────────
    # 19 Default stack
    s = blank_slide(prs)
    typographic_slide(
        s,
        "Block 8 — Default setup · ~5 min",
        "Obsidian · Hermes · Wiki habits",
        [
            "1 Knowledge store with phone sync (default Obsidian; alternatives OK)",
            "2 Hermes Agent pointed at that vault",
            "3 Harness + LLM Wiki habits — next class",
            "4 Models: whatever you already pay for / can access",
            "Homework: note LLM access · optional Karpathy gist · course materials",
        ],
    )
    add_notes(
        s,
        "Repeat homework aloud. Student share pack, not whole vault.\n"
        "howto-obsidian-setup-and-sync · howto-hermes-setup · llm-wiki-standard-files.\n"
        "Next: harness after a student humanities input.",
    )

    # 20 Close
    s = blank_slide(prs)
    typographic_slide(
        s,
        "Close",
        "What stays with you from Part A?",
        [
            "Bring one fear and one hope into the stack",
            "Open questions feed later input nodes",
            "11:55–12:00 — homework and close",
        ],
    )
    add_notes(
        s,
        "Collect open questions. Do not race leftover blocks — priorities were #2, #3, #4.",
    )

    prs.save(OUT_PPTX)
    print(f"Wrote {OUT_PPTX} with {len(prs.slides)} slides")
    return len(prs.slides)


if __name__ == "__main__":
    n = build()
    sys.exit(0 if n else 1)
