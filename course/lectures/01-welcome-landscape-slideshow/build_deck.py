#!/usr/bin/env python3
"""Build the Session 01 welcome/landscape deck (PPTX, then convert to ODP).

Content follows course/lectures/01-welcome-landscape-lecture.md and the deep-dive
notes in course/lectures/01-welcome-landscape-deep-dives/. Slide titles are the
lecture block titles.

Design: text slides are white text on black; image slides are full-screen, placed
only where an image carries the beat (Sebastian's edits of 9 and 11 Nov 2026 set
the order). No rules, underlines or shadows.
"**...**" in a line or title marks a bold run; "\\v" inside a line is a line break.
Each image slide carries one small credit line at the bottom (short form); the full
credit is in the speaker notes and in images/ATTRIBUTION.md. Course charts print
their source inside the image and get no extra line. One exception to the
image-only rule: the hype-cycle slide shows the curve next to its explanation.

Usage: python build_deck.py [output.pptx]   (default: 01-welcome-landscape.pptx)
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

from PIL import Image
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Inches, Pt

ROOT = Path(__file__).resolve().parent
IMG = ROOT / "images"
OUT_PPTX = ROOT / "01-welcome-landscape.pptx"

W, H = Inches(13.333), Inches(7.5)
BLACK = RGBColor(0x00, 0x00, 0x00)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
FONT_TITLE = "Calibri Light"
FONT_BODY = "Calibri"
LEFT = Inches(0.95)
TEXT_W = Inches(11.4)
CREDIT_STRIP = Inches(0.42)

BLOCKS = {
    1: "Scope of the class",
    2: "What LLMs and agents are",
    3: "Drivers, visions, fears, regulation",
    4: "Economy and the AI bubble",
    5: "Ecology",
    6: "Labour",
    7: "Media-art workflows",
    8: "Default setup",
}

LECTURE = "course/lectures/01-welcome-landscape-lecture.md"
DD = "course/lectures/01-welcome-landscape-deep-dives/"

# key: (file, fit mode, on-slide credit or None, full credit for the speaker notes)
# "cover" fills the slide above the credit line; "contain" shows the whole image on black.
# None as on-slide credit: the image prints its own source (course charts).
IMAGES = {
    "13": ("13-meta-el-paso-contentstack.jpg", "cover",
           "Rendering: Meta's planned AI data centre, El Paso, Texas. Image: Meta, via industry press.",
           "Rendering, not a photo: Meta's planned AI data-centre campus in northeast El Paso, Texas (announced Oct 2025, "
           "scalable to 1 GW). Press image via the Contentstack CDN used by industry press; teaching citation."),
    "15": ("15-anatomy-of-an-ai-system-joler.jpg", "contain",
           "Kate Crawford and Vladan Joler, Anatomy of an AI System, 2018. anatomyof.ai",
           "Kate Crawford and Vladan Joler, Anatomy of an AI System (2018). anatomyof.ai"),
    "32": ("32-agentic-ai-loop-bw.png", "contain",
           "Agentic AI loop: reason, act, observe, evaluate. Source to be confirmed.",
           "Agentic AI loop graphic added by Sebastian on 11 Nov 2026. Source not yet identified: confirm before sharing."),
    "27": ("27-standard-vs-course-setup.png", "contain",
           "Diagram for this course, 2026. Sources: Cursor data-use page, OpenAI data-controls help.",
           "Standard setup or course setup. Diagram for this course, 2026. Sources: https://cursor.com/data-use, "
           "https://help.openai.com/en/articles/7730893-data-controls-faq"),
    "16": ("16-bruegel-tower-of-babel.jpg", "cover",
           "Pieter Bruegel the Elder, The Tower of Babel, 1563. Kunsthistorisches Museum Wien. Public domain.",
           "Pieter Bruegel the Elder, The Tower of Babel (1563), Kunsthistorisches Museum Wien. Public domain."),
    "28": ("28-bigtech-capex-chart.png", "contain", None,
           "Chart for this course. Data: SEC 10-K filings (via 500metrics.com, chartedfacts.com); 2026 company guidance."),
    "35": ("35-us-gdp-tech-capex-chart.png", "contain", None,
           "Chart for this course, redrawn after Bridgewater Associates (Aug 2025) as shown by J.P. Morgan Asset Management "
           "and Richard Campbell. Values read from the chart, approximate."),
    "36": ("36-mag7-sp500-gains-2024.png", "contain", None,
           "Chart for this course. Data: Voronoi (Visual Capitalist), 2 Jan 2025, contribution to the S&P 500's 2024 "
           "market-cap growth."),
    "20": ("20-nyse-crowd-1929.jpg", "cover",
           "Photo: crowds outside the New York Stock Exchange, 24 October 1929. Associated Press. Public domain.",
           "Associated Press, crowds outside the New York Stock Exchange, 24 October 1929. Public domain, Wikimedia Commons."),
    "31": ("31-us-railroad-map-1884.jpg", "contain",
           "US railroads, 1884. In 1893 to 1894 a quarter of the network went bankrupt. "
           "Map: S. A. Mitchell Jr., David Rumsey Map Collection.",
           "Samuel Augustus Mitchell Jr., Railroad map of the United States, showing the through lines of communication "
           "from the Atlantic to the Pacific, Wm. M. Bradley & Bro., Philadelphia, 1884. David Rumsey Map Collection, "
           "Stanford Libraries; public domain via Wikimedia Commons. Cropped to the map."),
    "33": ("33-bloomberg-circular-ai-deals.png", "contain",
           "Bloomberg News, \"OpenAI, Nvidia Fuel $1 Trillion AI Market With Web of Circular Deals\", 7 Oct 2025.",
           "Bloomberg graphic \"How Nvidia and OpenAI Fuel the AI Money Machine\", in Emily Forgash and Agnee Ghosh, "
           "\"OpenAI, Nvidia Fuel $1 Trillion AI Market With Web of Circular Deals\", Bloomberg, 7 Oct 2025. "
           "Source line: Bloomberg News reporting. Press graphic; teaching citation. Also shown by Richard Campbell, NDC 2026."),
    "29": ("29-shiller-cape-chart.png", "contain", None,
           "Chart for this course. Data: Robert Shiller, Yale (to Sep 2023), multpl.com (to Nov 2026)."),
    "30": ("30-bis-labour-share-scenario.png", "contain", None,
           "Chart for this course, redrawn after Bank for International Settlements, Annual Economic Report 2026, "
           "Box C, Graph C1.B."),
    "11": ("11-gw-ranch-heise.jpg", "cover",
           "Rendering: GW Ranch, Pecos County, West Texas, AI campus with its own gas plant. "
           "Image: Pacifico Energy, via heise online.",
           "Rendering, not a photo: GW Ranch, Pecos County, West Texas, about 17 miles north of Fort Stockton. "
           "Pacifico Energy's private-grid gas plant for an Amazon AI campus. Published by heise online. "
           "Press image; teaching citation."),
    "06": ("06-datacenter-cooling-tower.jpg", "cover",
           "Photo: data-centre cooling tower, Mesa, Arizona, Nov 2025. Rsparks3, CC0, Wikimedia Commons.",
           "Photo: Rsparks3, cooling tower on a data centre, Mesa, Arizona, 23 Nov 2025. CC0, Wikimedia Commons."),
    "25": ("25-ashburn-data-centers.jpg", "cover",
           "Photo: data centres, Ashburn, Loudoun County, Virginia, Nov 2025. Theodore Christopher, CC0, Wikimedia Commons.",
           "Photo: Theodore Christopher, aerial view of data centres among commercial buildings, Ashburn, Loudoun County, "
           "Virginia, 26 Nov 2025. CC0, Wikimedia Commons."),
    "05": ("05-quarto-stato-pellizza.jpg", "cover",
           "Giuseppe Pellizza da Volpedo, Il Quarto Stato, 1901. Museo del Novecento, Milan. Public domain.",
           "Giuseppe Pellizza da Volpedo, Il Quarto Stato (1901). Public domain."),
    "21": ("21-koehler-der-streik.jpg", "cover",
           "Robert Koehler, Der Streik, 1886. Deutsches Historisches Museum, Berlin. Public domain.",
           "Robert Koehler, Der Streik (1886), Deutsches Historisches Museum. Public domain."),
    "22": ("22-luddite-leader-1812.jpg", "contain",
           "The Leader of the Luddites, print, Walker and Knight, May 1812. Public domain.",
           "The Leader of the Luddites, print published by Walker and Knight, May 1812. Public domain, Wikimedia Commons."),
    "23": ("23-quadrature-cosmology-of-capital.jpg", "cover",
           "Quadrature, Cosmology of Capital, The Mass of Money, Schaufler Lab TU Dresden, 2026. "
           "Photo: Victoria Gentsch / materialmatters.online",
           "Quadrature, Cosmology of Capital, in The Mass of Money, Schaufler Lab TU Dresden, 2026. "
           "Photo: Victoria Gentsch / materialmatters.online."),
    "14": ("14-llm-wiki-annotated.png", "contain",
           "LLM Wiki diagram after Andrej Karpathy's LLM Wiki gist, published on Medium. Notes and white labels added for this course.",
           "LLM Wiki: Karpathy's knowledge compilation pattern. Diagram published on Medium (miro.medium.com), after "
           "Andrej Karpathy's LLM Wiki gist (2026). Edited for this course: section labels repainted white, "
           "a plain-language note next to each part."),
    "04": ("04-messy-desk.jpg", "cover",
           "Sugar Pond, Mess. CC BY-SA 2.0, Wikimedia Commons.",
           "Sugar Pond, Mess. CC BY-SA 2.0, Wikimedia Commons."),
}
HYPE_CYCLE = IMG / "34-hype-cycle.png"

BOLD = re.compile(r"(\*\*.+?\*\*)")


def black_slide(prs):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    fill = slide.background.fill
    fill.solid()
    fill.fore_color.rgb = BLACK
    return slide


def add_runs(p, text, size, font=FONT_BODY, italic=False):
    for k, segment in enumerate(text.split("\v")):
        if k:
            p.add_line_break()
        for part in BOLD.split(segment):
            if not part:
                continue
            bold = part.startswith("**") and part.endswith("**")
            run = p.add_run()
            run.text = part[2:-2] if bold else part
            run.font.size = Pt(size)
            run.font.name = font
            run.font.italic = italic
            run.font.bold = bold
            run.font.color.rgb = WHITE


def textbox(slide, top, height, text, size, font=FONT_BODY, italic=False, left=LEFT, width=TEXT_W):
    box = slide.shapes.add_textbox(left, top, width, height)
    tf = box.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = MSO_ANCHOR.TOP
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.LEFT
    add_runs(p, text, size, font, italic)
    return box


def lines_box(slide, top, height, lines, size=20, space_after=10, left=LEFT, width=TEXT_W):
    box = slide.shapes.add_textbox(left, top, width, height)
    tf = box.text_frame
    tf.word_wrap = True
    for i, line in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = PP_ALIGN.LEFT
        p.space_after = Pt(space_after)
        add_runs(p, line, size)
    return box


def notes(slide, text):
    tf = slide.notes_slide.notes_text_frame
    tf.text = text.strip()


def text_slide(prs, block, beat, lines, *, question=None, source=None, note="", title=None, size=20):
    """block=None and title="" give a slide with only the beat and its lines."""
    s = black_slide(prs)
    if block is not None:
        textbox(s, Inches(0.6), Inches(0.4), f"{block:02d}", 14)
    if title != "":
        textbox(s, Inches(0.95), Inches(0.9), title or BLOCKS[block], 40, font=FONT_TITLE)
    textbox(s, Inches(1.85), Inches(0.6), beat, 24)
    lines_box(s, Inches(2.75), Inches(3.3), lines, size=size)
    if question:
        textbox(s, Inches(6.05), Inches(0.5), question, 18, italic=True)
    if source:
        textbox(s, Inches(6.8), Inches(0.35), source, 11)
    notes(s, note)
    return s


def add_fitted(slide, path, mode, top, area_w, area_h):
    with Image.open(path) as im:
        iw, ih = im.size
    img_ratio, area_ratio = iw / ih, area_w / area_h
    if mode == "cover":
        pic = slide.shapes.add_picture(str(path), 0, top, width=area_w, height=area_h)
        if img_ratio > area_ratio:
            excess = 1 - area_ratio / img_ratio
            pic.crop_left = pic.crop_right = excess / 2
        else:
            excess = 1 - img_ratio / area_ratio
            pic.crop_top = pic.crop_bottom = excess / 2
    else:
        scale = min(area_w / iw, area_h / ih)
        pw, ph = int(iw * scale), int(ih * scale)
        slide.shapes.add_picture(str(path), int((area_w - pw) / 2), int(top + (area_h - ph) / 2), width=pw, height=ph)


def image_slide(prs, key, note=""):
    fname, mode, short, credit = IMAGES[key]
    s = black_slide(prs)
    area_h = H - CREDIT_STRIP if short else H
    add_fitted(s, IMG / fname, mode, 0, W, area_h)
    if short:
        textbox(s, H - CREDIT_STRIP + Inches(0.06), Inches(0.3), short, 11, left=Inches(0.35), width=W - Inches(0.7))
    notes(s, f"{note.strip()}\n\nImage: {credit}".strip())
    return s


def hype_cycle_slide(prs, beat, lines, *, source, note):
    """The one text slide with an image on it: the curve needs its explanation beside it."""
    s = black_slide(prs)
    textbox(s, Inches(0.6), Inches(0.4), "04", 14)
    textbox(s, Inches(0.95), Inches(0.9), BLOCKS[4], 40, font=FONT_TITLE)
    textbox(s, Inches(1.85), Inches(0.6), beat, 24)
    lines_box(s, Inches(2.65), Inches(4.0), lines, size=17, space_after=8, width=Inches(5.9))
    with Image.open(HYPE_CYCLE) as im:
        iw, ih = im.size
    ph = Inches(4.85)
    pw = int(ph * iw / ih)
    s.shapes.add_picture(str(HYPE_CYCLE), W - pw - Inches(0.35), Inches(1.75), width=pw, height=ph)
    textbox(s, Inches(6.8), Inches(0.35), source, 11)
    notes(s, note)
    return s


def build(out: Path = OUT_PPTX):
    prs = Presentation()
    prs.slide_width = W
    prs.slide_height = H
    img = lambda key, note="": image_slide(prs, key, note)

    img("13", "A real campus before any talk about models: concrete, power lines, cooling. "
              "This is a rendering of a planned campus, not a photo.")

    # Title
    s = black_slide(prs)
    textbox(s, Inches(2.6), Inches(1.0), "Critical Vibe Coding", 54, font=FONT_TITLE)
    textbox(s, Inches(3.6), Inches(0.6), "Session 01. Welcome and landscape", 24)
    textbox(s, Inches(6.6), Inches(0.4), "Interface Cultures, Kunstuniversität Linz", 14)
    notes(s, f"Part B, about 11:00 to 11:55, after the outdoor check-in.\n"
             f"Priority: Blocks 3 to 6 (drivers and visions, economy, ecology, labour). Shorten 2 and 7 first.\n"
             f"Q&A after each block. Lecture notes: {LECTURE}")

    # Block 1
    text_slide(prs, 1, "Two tracks, every week", [
        "**Technical:** you build a working personal agent setup. Or not….",
        "**Critical:** what this technology does to society, our planet, work, money, energy and art.",
        "A third thread: explore the agent as interface. → The setup itself as material and/or canvas.",
        "\v- Midpoint, Session 4: demo and proposal. \v- Final, Session 8: **Final presentation:** architecture, one use, "
        "reflection or ...",
    ], title="**Critical Vibe Coding** - Scope of the class",
       question="Who came for the setup, and who for the politics?",
       note="Both tracks every week; neither is optional.\n"
            "Agent as interface: tools, memory and rules are artistic material, not only a production machine.\n"
            "No polished exhibition expected by default. Eight sessions: course/course-outline.md")

    # Block 2
    text_slide(prs, 2, "The chat window is the visible tip", [
        "Behind every answer: mines, factories, data centres, energy, and people labelling data.",
        "Kate Crawford and Vladan Joler mapped one voice assistant from the mine to the dump.",
        "Today: we focus on the visible part. The rest returns in every block.",
    ], source="Crawford and Joler, Anatomy of an AI System, 2018",
       note="Medium priority block, about 8 minutes.\n"
            "Entry image next: Anatomy of an AI System. Let it stand for 20 seconds. Point to the three arcs: "
            "material extraction (left), the user and the cloud (centre), disposal (right).")
    img("15", "Crawford and Joler trace the Amazon Echo: minerals, smelters, component factories, shipping, AWS, "
              "data labelling, and finally e-waste. Each step has its own labour and income scale. anatomyof.ai")
    text_slide(prs, 2, "Basic vocabulary", [
        "**Model:** a large file of numbers trained on text. It continues text; it does not look things up.",
        "**Chat product:** the app around a model. Interface, filters, memory, payment.",
        "**Agent:** a model in a loop that can act: read and write files, search, run code.",
        "**Context:** what the model can see right now. Anything else does not exist for it.",
        "**Harness:** the tools, files, skills and rules you set up. Your material.",
        "**MCP:** Model Context Protocol. A standard plug between an agent and other apps.",
        "**Sandbox:** a closed-off space where the agent can run code and change files without touching the rest of your computer.",
        "**Lint:** an automatic check for mistakes. In code: errors and bad style. In a wiki: broken links, contradictions, forgotten pages.",
    ], size=18, note="Examples. Model: Llama, Qwen, the model inside Claude or ChatGPT. Chat product: ChatGPT, Claude.ai, Gemini. "
            "Agent: Hermes, Cursor Agent, Claude Code.\n"
            "One sentence: a chat answers; an agent acts, with the tools you allow it.\n"
            "Context explains why agents work with files and an index: the notes folder is memory the model can open when needed.\n"
            "MCP: an open standard (Anthropic, 2024) so one agent can use many apps the same way: calendar, browser, Blender, "
            "a database. Each MCP server is one plug. Session 05. course/what-is-mcp.md\n"
            "Sandbox: a container, a virtual machine or a locked folder. If the agent makes a mistake, the damage stays inside. "
            "Cloud agents run in the provider's sandbox; Hermes can run commands in Docker. Case in Session 05: the Hugging Face "
            "incident, where agents escaped their sandbox.\n"
            "Lint: the name comes from a 1978 tool that found errors in C code. In the LLM Wiki it is the third operation next "
            "to ingest and query: the agent audits the wiki and reports orphan pages, broken links, contradictions. "
            "course/what-is-lint.md\n"
            "Harness in depth: course/what-is-harness.md, Session 02.")
    img("32", "The agent loop: reason, act, observe, evaluate, then round again. Reason: make a plan from what is in context. "
              "Act: call a tool, for example write a file, search, run code. Observe: read what came back. Evaluate: compare "
              "with the goal and decide the next step. The loop runs until the task is done or a limit stops it. "
              "In this course the results land in your notes folder, and the next pass reads them from there.")
    text_slide(prs, 2, "How a model writes", [
        "It learned which words tend to follow which, from huge amounts of text.",
        "It writes the most plausible continuation, piece by piece.",
        "**Plausible is not true.** Confident mistakes are normal behavior.",
        "Good at drafts, summaries, changing formats, proposing structure.",
        "Weak at facts it never saw, your intentions, and taking responsibility.",
    ], note="Simplified teaching model. Training: next-word prediction on very large text collections. "
            "Use: your text goes in, the model samples a continuation.\n"
            "Agents raise the stakes: a confident mistake written into files without checking spreads.")
    text_slide(prs, 2, "Local or cloud", [
        "**Cloud:** the strongest models, no hardware. Your data leaves; prices and terms can change.",
        "**Local:** private, offline, your own rules. Expensive hardware, smaller models, your own upkeep.",
        "→ The choice is technical, economic and political at once.",
    ], question="Has anyone used an agent that edits files, not only a chat?",
       note="Session 03 goes deeper. Research: research/local-gpu-hardware-for-llms.md.\n"
            "Second question if time: where is authorship if the agent writes half the patch?")
    img("27", "Two rows. Standard setup: ChatGPT, or Cursor with default settings. Only the window is on your side. "
              "ChatGPT keeps chats and memory on OpenAI's servers, and for personal accounts \"Improve the model for everyone\" "
              "is on by default. Cursor sends every request through its own servers, even with your own model key, "
              "keeps a code index there, and runs the agent loop of cloud agents in its cloud. "
              "Course setup: the agent (Hermes), its skills and memory, and the notes folder stay on your computer. "
              "Only the model call leaves, and with a local model not even that. "
              f"Explained in {DD}default-setup.md section 3.")
    text_slide(prs, 2, "Why the course setup", [
        "**Your data stays with you:** notes, memory and skills are files on your own disk.",
        "**You set the limits:** which folders the agent may read, which it may write, which stay human-only.",
        "**Easy to switch:** skills, rules and memory are local, so you can change the agent or the model and keep them.",
        "**No lock-in:** plain markdown opens in any editor, with or without AI.",
        "**You can check it:** every page the agent wrote is a file you can open, compare and undo.",
        "**Model by choice:** a paid cloud model, a free tier, or a local model for private notes.",
    ], source="Course guides: default-setup.md, what-is-harness.md, knowledge-store-options.md",
       note="Limits, said aloud: the model call still leaves your computer unless you run a local model. "
            "Free tiers (OpenRouter) can log prompts. Local agents need upkeep: updates, keys, backups.\n"
            "Read and write rights: the schema file (AGENTS.md) and the Hermes tool settings; raw sources are read-only, "
            "human-only pages are off limits for the agent.\n"
            "Switching: the same folder works with Hermes, Claude Code, Cursor or a plain editor. "
            f"Details: {DD}default-setup.md section 3.")

    # Block 3
    text_slide(prs, 3, "What drives the build", [
        "Tech firms needed a next growth platform after PC, internet, smartphone, social networks...",
        "They already held the data and the computing power. → LLMs is what they have, they have no other idea.",
        "It is a race: no single company can pause alone.",
        "Society did not ask for it. The growth logic and the race did.",
    ], source="Course script: visions, fears, regulation. Coxon, The Daily Show",
       note="High priority, about 10 minutes for the four beats. Script: course/visions-fears-regulation.md.\n"
            "Coxon (ex-OpenAI, Anthropic): day to day, the motive is getting there first. Utopia is mixed with ambition. (claim, interview)\n"
            "Technical scaling is real and runs in parallel to the money story.")
    img("16", "Bruegel: a tower built higher than anyone needs, by a ruler who cannot stop. Kunsthistorisches Museum Wien.")
    text_slide(prs, 3, "Two industry stories", [
        "Abundance: AI makes work optional; everyone gets a \"universal high income\".",
        "Catastrophe: models escape control or are misused; the race underfunds safety.",
        "Often the same people tell both stories while raising hundreds of billions.",
        "Both are real rhetoric. Neither is a delivered policy.",
    ], source="Musk, Altman (abundance). Coxon, Stewart (risk and credibility)",
       note="Musk: \"age of abundance\", universal high income. Altman: Moore's Law for Everything (2021), later \"shared upside\".\n"
            "Stewart: you cannot sell Star Trek and extinction odds at once. Pick a lane.\n"
            "Two fear stacks: frontier and existential versus social and institutional (deskilling, lock-in, ecology). "
            "This course spends more time on the second.")
    text_slide(prs, 3, "Amplifier or power", [
        "**Salim Ismail:** “AI is an amplifier. Fire heats the house or burns it down.” (the tool argument)",
        "**Social science:** “it amplifies those who already hold power.” (+ a loooot of other issues...)",
    ], note="Ismail response to Stewart: regulate outcomes, not mathematics.\n"
            "Counter: systems arrive already tilted by whose data, capital and goals built them (Crawford, Joler; Zajko 2022).\n"
            "\"Depends how you use it\" is true for a chisel and incomplete for a platform that reorganises labour markets and grids.")
    text_slide(prs, 3, "What regulation can do", [
        "Rules can limit uses, protect personal data, assign liability, shape markets.",
        "They cannot put the technology back into the box.",
        "Calls for regulation can also be marketing: \"we are so powerful we need rules\". "
        "+ regulations would slow down the race which benefits current leaders (Anthropic, OpenAI).",
        "The EU AI Act and the GDPR set rules for AI uses and personal data, also in your projects.",
    ], question="What would your rule for AI usage be?",
       note="Law orientation for students: course/eu-ai-act-and-datenschutz.md (privacy input, Session 07).\n"
            "Compliance costs can favour incumbents. Distrust both self-regulation and hype-regulation.")

    # Block 4
    spending_note = (f"High priority, about 12 minutes. Deep dive: {DD}bubble-economy.md\n"
                     "Per company 2026: Amazon about $220B, Alphabet $195 to 205B, Microsoft about $170B, Meta $135 to 145B.\n"
                     "With SpaceX/xAI: $803 to 828B (Business Insider, claim). Tooze: AI is about 36% of US business investment (claim).\n"
                     "Check the Austrian GDP figure (roughly $550B) before class.")
    text_slide(prs, 4, "https://www.youtube.com/shorts/5tOuZ6ngJsk", [], note=spending_note)
    hype_cycle_slide(prs, "Where are we in the hype cycle?", [
        "**Peak:** a new technology brings in \"stupid money\". Promises grow to keep investors in.",
        "**Trough:** the promises cannot be met. Money flows out, many firms fail.",
        "**Slope and plateau:** what is useful stays and becomes ordinary.",
        "**Richard Campbell:** AI is \"headed down the trough of disillusionment\", \"far from bottomed out\".",
        "Mobile and cloud had no such cycle. Dot-com and AI did: in both, the hype paid for a huge build-out "
        "of infrastructure.",
    ], source="Gartner Hype Cycle (Jackie Fenn, 1995): a model, not data. Richard Campbell, After the AI Hype, "
              "NDC Copenhagen 2026, about 18:40 and 29:40 (claim)",
       note="Campbell: \"stupid money makes stupid decisions\". He dates the dot-com cycle 1997 to 2001, triggered by the "
            "Netscape IPO. "
            "\"Doesn't happen every time\": mobile and cloud were revolutions without a hype cycle (claim).\n"
            "His parallel: the dot-com hype funded data centres and undersea cables; most of those companies went broke, "
            "and the cables were bought for 10 cents on the dollar. Today the build-out is data centres.\n"
            "Read the curve as a story investors and analysts tell, not as a measured law. Gartner publishes new curves "
            "every year; many technologies never reach the plateau.\n"
            "Video: https://www.youtube.com/watch?v=uWnUnMphmPM\n"
            f"Deep dive: {DD}bubble-economy.md section 6.")
    text_slide(prs, 4, "The spending", [
        "2026: Amazon, Alphabet, Microsoft and Meta plan $720 to 740 billion of capital spending.",
        "About three times 2024. More than Austria's whole economy produces in a year.",
        "In one quarter, July to September 2026: about $209 billion.",
        "Most of it buys data centres and chips. Chips are about 65% of the cost.",
    ], source="Company guidance, Oct 2026 (verified fact). Azhar, Ezra Klein Show (claim)",
       note=spending_note)
    img("28", "Ten years of big-tech capex from the annual reports. Flat until 2020, then a doubling in two years, "
              "and the 2026 plans double again. Filings do not separate AI from other spending.\n"
              "Campbell shows the same series as \"Hyperscaler Capex By Year\" (about 32:20; company reports, "
              "2025 with analyst projections).")
    img("35", "Tech investment carried US growth. Bridgewater (Aug 2025), as shown by J.P. Morgan Asset Management: "
              "tech capex made 35 to 45% of US real GDP growth in the three quarters to mid-2025. "
              "Grey is the rest of the economy, which slowed from about 3% to about 1%.\n"
              "Jason Furman (Harvard) went further: information-processing equipment and software were about 4% of GDP "
              "but about 92% of growth in the first half of 2025 (claim, Oct 2025).\n"
              "Campbell shows the Bridgewater chart at about 32:30. Values here are read from that chart, approximate.")
    img("36", "Voronoi (Visual Capitalist), 2 Jan 2025: seven companies made 55% of the S&P 500's gain in market value in 2024; "
              "Nvidia alone 20%. Campbell (about 32:46): \"In 2024, more than half of the increase in value in the S&P 500 "
              "came from seven companies.\"\n"
              "Index funds and pensions hold these shares, so ordinary savers carry the concentration.")
    text_slide(prs, 4, "Building ahead of demand", [
        "Stargate Abilene, Texas: eight buildings, 1.2 GW, about $31 billion, in under 2.5 years.",
        "267 more US hyperscale campuses are approved or planned.",
        "Land, power and chips are ordered before customers exist.",
        "Planned gigawatts are not working gigawatts.",
    ], source="Oracle, Epoch AI (verified fact). Be Smart / PBS, Richard Campbell (claim)",
       note="Abilene: about 1,000 acres, 824 MW IT capacity, construction from June 2024, six of eight buildings delivered by Sep 2026, "
            "about 9,000 construction workers a day in March 2026.\n"
            "Campbell: developers over-order \"like Taylor Swift tickets\"; a single girder lets a project count as underway.\n"
            "IEA: about 20% of planned projects could be delayed by the grid.")
    text_slide(prs, 4, "Spending ahead of revenue", [
        "OpenAI lost about $21 billion in 2025.",
        "About 2.5% of Americans pay for an AI subscription.",
        "Acemoglu: about 1% more GDP over ten years.",
        "More of the build is borrowed: bonds, private credit, off-balance-sheet vehicles.",
        "More than half the money AI firms raise comes from other AI firms.",
    ], source="Zitron to DW; Klein, Azhar (claim). Acemoglu, NBER; Bank for International Settlements (BIS), "
              "Bulletin 137 (verified fact)",
       note="Zitron says the OpenAI figure comes from financials he obtained; label it a claim.\n"
            "Kedrosky: tech is now the largest US issuer of investment-grade bonds; AI-related credit may reach $10 trillion, held by insurers, "
            "private credit, sovereign funds (claim).\n"
            "BIS Bulletin 137: 55.2% of incoming AI-firm investment 2021 to 2025 came from other AI firms.\n"
            "Bank of England warned of a sharp fall in asset prices if AI is reassessed.")
    img("20", "Wall Street, 1929.")
    text_slide(prs, 4, "Every build-out overbuilt", [
        "Canals, railways, electrification, fibre: each ended in oversupply and crisis.",
        "About half of all US railroad track turned out useless.",
        "After 2000, internet fibre sold for about 10 cents on the dollar.",
        "Rails lasted a century. AI chips are written off in five to six years.",
    ], question="Your subscription costs about €20 a month. Who pays the rest?",
       source="Kedrosky, Campbell (claim). Company 10-K filings",
       note="Kedrosky: no major capex episode in Western history ended without vast oversupply.\n"
            "Zitron: AI data centres are good for one thing; unlike dark fibre they leave little for other uses.\n"
            "\"Half of all track useless\" is Kedrosky's and Campbell's phrase (claim); the receivership numbers on the next "
            "slide are the documented part.")
    img("31", "The whole US network in 1884: many companies laid parallel lines between the same cities, each betting on the "
              "same traffic. Then the Panic of 1893. By 30 June 1894, 192 railroads with more than 42,000 miles of line, "
              "about a quarter of all US railway capital, were in receivership (Interstate Commerce Commission). "
              "Northern Pacific, Union Pacific and the Santa Fe all failed in 1893. The tracks stayed; banks such as "
              "J. P. Morgan bought and merged the lines cheaply.\n"
              "Point to the dense web in the northeast and the competing transcontinental lines. "
              f"Deep dive: {DD}bubble-economy.md section 6.")
    img("33", "Bloomberg's map of circular deals, Oct 2025. Nvidia agrees to invest up to $100 billion in OpenAI, which buys "
              "Nvidia chips. OpenAI signs a $300 billion cloud deal with Oracle, which spends tens of billions on Nvidia chips. "
              "AMD gives OpenAI an option on up to 160 million AMD shares while OpenAI deploys 6 GW of AMD GPUs.\n"
              "Revenue in one firm is investment from another: money moves in a circle. Bank for International Settlements, "
              "Bulletin 137: 55.2% of the money flowing into AI firms 2021 to 2025 came from other AI firms.\n"
              "Campbell shows this graphic at about 33:45.")
    text_slide(prs, 4, "Will it burst? Arguments for", [
        "Every big build-out so far ended in oversupply. A race makes everyone overbuild.",
        "Revenue is a fraction of spending. Few customers, falling prices per token.",
        "More of it is debt, partly off the balance sheet. AI firms fund each other. (Circle investment)",
        "Ordinary savers carry it: the ten largest stocks are about 40% of the S&P 500.",
        "Shares cost about 40 years of average profit: more than in 1929 (33), less only than in 2000 (44).",
        "Chinese models are much cheaper almost as good.",
        "Almost all of current growth is based on AI investments in the US.",
    ], source="Kedrosky, Ezra Klein Show, Oct 2026; Campbell, NDC 2026 (claim). Shiller CAPE, "
              "Bank for International Settlements (BIS) Bulletin 137 (fact)",
       note="Definition first (Azhar): a burst means investment falls by half and the market by half or more. Low returns alone are not a burst.\n"
            "Kedrosky: \"you're guaranteed overcapacity\". About eight customers are 80% of a frontier lab's revenue; coders about 80% of tokens.\n"
            "Campbell: \"None of these companies are profitable, not even close.\" Memory makers refuse to double output.\n"
            "The OpenAI, Anthropic and SpaceX listings would be larger than all post-war US IPOs combined: exit events for insiders (Kedrosky).\n"
            "Growth line: Bridgewater and J.P. Morgan put tech capex at 35 to 45% of US growth; Furman at about 92% "
            "for the first half of 2025 (claim). \"Almost all\" fits Furman's figure, not the others.\n"
            f"Full list with timestamps: {DD}bubble-economy.md section 7.")
    img("29", "How to read it. CAPE = the price of the S&P 500 divided by the average yearly profit of its companies over the "
              "past ten years, both adjusted for inflation. The ten years are only the averaging window, so one boom or one "
              "recession does not distort the profit figure. There is no threshold at 10.\n"
              "In 2000 the value was 44: buyers paid 44 years of average profit. If profits stayed at that level, it would "
              "take 44 years of profit to add up to the price. Today about 40. The long-run average since 1881 is about 18; "
              "lows were about 5 (1920) and about 7 (1982).\n"
              "It does not say whether firms make a profit: the ratio is positive whenever they do. It says how expensive "
              "the shares are. 1/CAPE is the earnings yield: 2.5% at 40, about 5.5% at the average. Historically a high CAPE "
              "was followed by low returns over the next ten years. It does not time a crash.")
    text_slide(prs, 4, "Will it burst? Arguments against", [
        "Compute is scarce: demand still exceeds supply.",
        "A GPU pays for itself in 18 to 24 months at today's rental prices.",
        "More customers pay every quarter. Anthropic's Q1 2026 beat its whole 2025.",
        "If the labs fail, the data centres still get used.",
        "Debt is still limited. Big investors trim; they do not flee.",
    ], source="Azhar, Klein, Ezra Klein Show, Oct 2026; Campbell, NDC 2026 (claim)",
       note="Azhar: \"There is vast vast undersupply of the compute.\" OpenAI and Anthropic's share of GPU rental revenue is falling: demand broadens.\n"
            "Klein: \"Anthropic might collapse, but Nvidia will be fine.\" Hyperscalers can absorb losses from other businesses.\n"
            "Azhar's warning signs: external finance above 30% of capex; enterprise AI spending growth halving two quarters in a row.\n"
            "Kedrosky's test: the customer list in the coming S-1 filings.\n"
            "Both sides agree the money is real and the build-out is enormous.")
    text_slide(prs, 4, "Who gets the income", [
        "**Adam Tooze:** \"a two-way bet on disaster either way\".",
        "If the investment fails: losses, somewhere in the chain.",
        "If it pays off: the labour market shaken to its foundations.",
        "A scenario by the Bank for International Settlements (BIS): labour's share of income falls from about 60% to 20%.",
        "→ Today about 60% goes to wages. Then 20% to wages, 80% to owners.",
        "**Demand bottleneck:** replaced workers stop buying, so more automation stops paying. The fall stops near 47%.",
    ], source="Adam Tooze, Ones and Tooze Ep. 250, Foreign Policy, July 2026 (claim). "
              "Bank for International Settlements (BIS), Annual Economic Report 2026, Box C (verified fact, scenario)",
       note="Tooze (about 33:30): \"that 20% share which is a third of the 60% average which is currently prevailing in advanced economies "
            "... will not necessarily mean that the wages of those employed goes down but it'll mean that the share in the total pie collapses\". "
            "Check the wording against the audio; the transcript is automatic.\n"
            "The Bank for International Settlements in Basel is the central bank of central banks. The scenario is a model, not a forecast.\n"
            "Demand bottleneck in plain words: machines take over tasks, so wages go to the owners of the machines. But every "
            "worker who loses income is also a customer who buys less. If spending falls, it no longer pays to automate the "
            "next task, so automation stalls. Growth stays below the boom path and the labour share levels off higher than in "
            "the transformative case.\n"
            "https://www.youtube.com/watch?v=QevC7OrdJP8")
    img("30", "The Bank for International Settlements model: if AI delivers what its investors promise, the share of income paid "
              "as wages keeps falling, towards about 20%. With a demand bottleneck it levels off near 47%: replaced workers "
              "buy less, so further automation stops paying. Business as usual stays at 60%.")
    text_slide(prs, 4, "An alternative: AI as a commons", [
        "A few firms own what AI needs: data, computing power, talent.",
        "**Pieter Verdegem:** dismantle AI capitalism, build commons instead.",
        "Data trusts, public computing, cooperatives, democratic rules.",
        "Workers and communities decide what should be automated.",
    ], question="If the bubble bursts, who should own what is left?",
       source="Verdegem, Dismantling AI capitalism, AI & Society, 2022",
       note="Essay: https://pmc.ncbi.nlm.nih.gov/articles/PMC8994059/ (open access).\n"
            "AI start-up acquisitions since 2010: Apple 29, Google 15, Microsoft 13, Facebook 12, Amazon 7 (CB Insights, in Verdegem).\n"
            "Commons after Elinor Ostrom. \"Communities and workers should be involved in determining what sort of work should or should not be automated.\"\n"
            "Bridge to labour.")

    # Block 5
    text_slide(prs, 5, "Small globally, large locally", [
        "Data centres used about 1.5% of world electricity in 2024. The US used 45% of that.",
        "Half of US capacity sits in five regional clusters.",
        "To 2030, data centres drive almost half of US electricity-demand growth.",
    ], source="IEA, Energy and AI, 2025 (verified fact)",
       note=f"High priority, about 7 minutes. Deep dive: {DD}ecology.md. Student input on ecology: Session 06.\n"
            "IEA base case: about 945 TWh by 2030, still under 3% of world use; US and China are 80% of the growth.\n"
            "Be Smart (claim): 4.7% of US electricity in 2024, maybe 7 to 12% by 2028.")
    img("11", "GW Ranch, Pecos County, West Texas: a planned AI campus with its own gas power plant. "
              "A rendering by the developer, not a photo.")
    text_slide(prs, 5, "Gas, water, neighbours", [
        "New campuses build their own gas turbines to skip the queue for the grid. (sometimes illegal)",
        "GW Ranch, Texas: 35 turbines, more than 7 GW. The largest power plant in the US.",
        "Memphis: xAI ran up to 35 turbines with a permit for 15.",
        "Phoenix cools servers with water from a shrinking Colorado River.",
        "A multi-billion-dollar campus employs only a handful of permanent staff. ",
        "**→ generally there is not enough data available to know the actual ecological impact of AI.**",
    ], source="US CRS R49326 (verified fact). Be Smart / PBS, 2026 (claim)",
       note="CRS: on-site generation is mostly gas because it is dispatchable and buildable in one to three years.\n"
            "Memphis: Colossus sits in a historically Black neighbourhood; local reporting linked it to 30 to 60% more smog (claim).\n"
            "Water: the \"bottle per prompt\" meme comes from one 2023 GPT-3 study, mostly indirect water. Do not generalise it.\n"
            "Shell companies and NDAs; 38 US states offer tax incentives.")
    img("06", "A data-centre cooling tower in Mesa, Arizona. Photo.")
    text_slide(prs, 5, "Your prompt, their campus", [
        "Training a model is rare and huge. Daily use is small per request and adds up.",
        "Images, video and long agent runs cost far more than short text.",
        "The carbon is global. The water, noise and smog stay local.",
        "Three questions for any tool: where is the rack, what powers it, who lives next door?",
    ], question="Would you accept a data centre in your own district?",
       source="Luccioni, Jernite, Strubell, FAccT 2024 (verified fact)",
       note="Efficiency doubles about every 1.6 years (Koomey), and cheaper use invites more use (Jevons).\n"
            "From Linz: most of our use is served from US clusters. Local and open models move part of the load onto hardware you can see.")
    img("25", "Loudoun County, Virginia: data centres among offices and homes. Aerial photo.")

    # Block 6
    text_slide(prs, 6, "The work inside the model", [
        "Models are trained on human texts, images and code, mostly unpaid.",
        "Then people clean them. Kenyan workers labelled toxic text for OpenAI for under $2 an hour.",
        "Rating model answers was outsourced to low-wage countries.",
        "Every answer you rate is more training work.",
    ], source="TIME, 2023 (verified fact). Richard Campbell, 2026 (claim)",
       note=f"High priority, about 8 minutes. Deep dive: {DD}labour.md.\n"
            "Sama, Kenya: content warning, the TIME piece describes graphic material.\n"
            "Data Workers' Inquiry: annotators and moderators describe their own work.\n"
            "Verdegem: a small, highly paid ML elite and a large hidden workforce.")
    img("05", "Pellizza's Fourth Estate. Ask: who trains, who clicks, who owns the model?")
    text_slide(prs, 6, "Almost 40% of jobs", [
        "**IMF:** almost 40% of jobs worldwide are exposed to AI, about 60% in rich countries.",
        "Half may gain. Half may see lower demand, lower wages, fewer hires.",
        "Exposed is not replaced. **Brian Merchant:** the question is what management does with it.",
        "**Daron Acemoglu:** only about 5% of tasks can be automated profitably within ten years.",
        "Gains go to capital first. The IMF itself expects more inequality.",
    ], source="Georgieva, IMF blog, Jan 2024; Acemoglu, Economic Policy 2025 (verified fact). Merchant, Carnegie, July 2026 (claim)",
       note="IMF: \"In most scenarios, AI will likely worsen overall inequality.\" Emerging markets 40%, low-income countries 26%.\n"
            "Merchant: \"The question hasn't really been is this technology powerful... it's what can management do with it?\" "
            "AI as a threat disciplines workers; some layoffs blamed on AI are AI washing.\n"
            "Acemoglu: about 20% of US tasks exposed, a quarter of those profitable; productivity at most +0.66% in ten years, GDP about +1.1%. "
            "Negative effects fall particularly on women with low levels of education.\n"
            f"Details: {DD}labour.md section 2.")
    text_slide(prs, 6, "Creative work and first jobs", [
        "Illustrators, translators and copywriters were hit first.",
        "Translators now check machine output, for lower rates. → **deskilling.**",
        "Ages 22 to 25 in AI-exposed jobs: about 19% lower employment than comparable peers.",
        "Mostly through less hiring, not firing.",
        "Juniors gain most from AI tools, but are hired least. → might change since this is not profitable.",
    ], source="Merchant (claim). Stanford Canaries; call-centre and Copilot studies (verified fact)",
       note="Stanford (Brynjolfsson, Chandar, Chen, June 2026): no economy-wide displacement yet; the gap grows over time.\n"
            "Call centre: about +14% average, +30% for novices. Copilot field studies: juniors +21 to 40%, seniors +7 to 16%.\n"
            "METR: experienced maintainers were 19% slower with AI on their own large codebases.")
    img("21", "Robert Koehler, The Strike, 1886.")
    text_slide(prs, 6, "What the Luddites wanted", [
        "Skilled weavers who fought cheaper, worse goods and the loss of control over their work.",
        "They asked Parliament for a minimum wage. Parliament refused; organising was illegal.",
        "2023: Hollywood writers won contract rules on AI after a 148-day strike.",
        "→ The question is how much say workers have over the technology.",
    ], question="If your first job is the one being automated, how do you learn the craft?",
       source="Merchant, Blood in the Machine (claim). WGA 2023 contract (verified fact)",
       note="Luddites, 1811 to 1816. Machine breaking became a capital crime in 1812.\n"
            "WGA 2023: AI output is not literary or source material; studios cannot require writers to use AI.\n"
            "Merchant: \"It comes down to the level of democracy that the worker has over the technology.\"")
    img("22", "The Leader of the Luddites, 1812.")
    img("23", "Cosmology of Capital: an N-body simulation in which about 3,400 billionaire fortunes act as gravitational sinks. "
              "The software pipeline is the work.")

    # Block 7
    text_slide(prs, 7, "Pressures", [
        "Speed: more iterations, less time with engineering, more time for thinking… also more at the same time. "
        "(value of specialization and hesitation degrades)",
        "Democratization of what is possible for whom. → more competition.",
        "Flattening: the same generated look, the same generated concepts.",
        "Authorship: how to credit? How to value?",
        "Refusal: knowing when not to use AI is a skill and takes a lot of self discipline.",
    ], note=f"Medium priority, about 5 minutes. Deep dive: {DD}media-art-workflows.md\n"
            "Bring back the fears and hopes from the outdoor check-in.\n"
            "Flattening goes beyond style: a statistical model reproduces what is shown most online, not what exists. "
            "That average becomes a norm. Thesis for the Session 02 input: AI kills the underground and it kills diversity. "
            f"{DD}flattening-and-the-norm.md\n"
            "OpenAI rolled back a GPT-4o update in April 2025 for being \"overly flattering\": the helpful voice is a product decision.")

    # Block 8
    text_slide(prs, 8, "Notes, agent, structure, model", [
        "**Obsidian:** a folder of plain notes, synced to your phone. (or alternatives… future lecture...)",
        "**Hermes Agent:** reads and writes that folder, with the tools you allow. (or alternatives…)",
        "**LLM Wiki:** sources, wiki pages and a schema that the agent keeps in order.",
        "**A model:** whatever access you prefer, can afford makes sense for you",
    ], note=f"Deep dive with the diagram explained part by part: {DD}default-setup.md\n"
            "Free model to start Hermes with: Nemotron 3 Ultra through OpenRouter's free tier (default-setup.md section 4).\n"
            "Guides: course/howto-obsidian-setup-and-sync.md, course/howto-hermes-setup.md, course/llm-wiki-standard-files.md, "
            "course/knowledge-store-options.md.")
    img("14", "Three rows, each part labelled in the margin. Architecture: raw sources (read only), the wiki (written by the "
              "agent), the schema (the rules). Operations: ingest (a source comes in), query (you ask), lint (the health "
              "check). Actors: the human curates and asks; the agent summarises, links and maintains.")
    text_slide(prs, 8, "Homework", [
        "Bookmark or clone the course GitHub.",
        "Install a knowledge store with phone sync. Obsidian by default; alternatives allowed.",
        "Write down which AI access you already have.",
        "Read Karpathy's LLM Wiki note. → If you do not want to use AI: You can do research, investigative work on AI and input lectures.",
        "Next week: Setup guide - Karpathy & the harness, after a student humanities input.",
    ], note="Say the homework aloud. Point students at the course GitHub pack (START-HERE).")
    text_slide(prs, 8, "Student inputs: choose a topic", [
        "**02** Flattening: AI kills the underground and it kills diversity – how, why?",
        "**03** Closed or open weights: who holds the power?",
        "**05** How dangerous is AI really? See the Hugging Face incident.",
        "**06** The ecology of AI.",
        "**07** Privacy: what happens with your data?",
    ], question="Groups of four: pick a session by next week.",
       note="About 15 minutes per input, at the start of the session. Session 04 is project presentations, Session 08 the finals.\n"
            "Starting points: 02 flattening-and-the-norm.md; 03 research/local-gpu-hardware-for-llms.md and prompting-and-model-choice.md; "
            "05 Hugging Face and OpenAI incident reports, July 2026; 06 ecology.md; 07 course/eu-ai-act-and-datenschutz.md.\n"
            "List and sources: course/sessions/01-welcome-and-landscape.md and course/course-rhythm.md.")
    text_slide(prs, None, "Practices for this semester", [
        "A provenance note per project: which model, which tools, who decided (how), where it ran (local, cloud...). "
        "→ a protocol for me :)",
        "Personal ethics: what the agent may touch, remember – what to refuse. Your own manifesto on AI.",
        "Practical + theoretical work: Use this class to work on your projects with an agent or use it for research.",
    ], title="", question="Which part of your practice would you never hand to an agent?",
       note="Sessions: provenance note with the project plan (04), personal ethics and the agent's limits (05, 06).\n"
            "Examples: Holly Herndon's Holly+, Glaze and Nightshade, HM Munich Our Br00d, SFPC Handmade Datasets.")
    img("04", "Every vault starts like this.")

    prs.save(out)
    print(f"Wrote {out} with {len(prs.slides)} slides")
    return len(prs.slides)


if __name__ == "__main__":
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else OUT_PPTX
    sys.exit(0 if build(target) else 1)
