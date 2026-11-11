#!/usr/bin/env python3
"""Make the generated image slides for the Session 01 deck.

Writes into images/:
  14-llm-wiki-annotated.png            LLM Wiki diagram with a plain-language note next to each part
  26-agent-loop-actian-bw.png          Actian agent-loop diagram, converted to black and white (not in the deck now)
  27-standard-vs-course-setup.png      where things live: standard cloud setup versus the course setup
  28-bigtech-capex-chart.png           capital spending of Amazon, Alphabet, Microsoft, Meta
  29-shiller-cape-chart.png            Shiller CAPE ratio since 1881 (needs xlrd)
  30-bis-labour-share-scenario.png     labour share of income, Bank for International Settlements scenarios (redrawn)
  31-us-railroad-map-1884.jpg          Mitchell's railroad map of the United States, 1884, cropped from the atlas page
  34-hype-cycle.png                    hype cycle curve, for the slide that carries its explanation as text
  35-us-gdp-tech-capex-chart.png       US real GDP growth: tech capex versus the rest (redrawn after Bridgewater)
  36-mag7-sp500-gains-2024.png         share of the S&P 500's 2024 gain by company (redrawn after Voronoi)

All images are white on black to match the deck. Sources are printed on each chart
and listed in images/ATTRIBUTION.md.
"""
from __future__ import annotations

import io
import urllib.request
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parent
IMG = ROOT / "images"
UA = {"User-Agent": "Mozilla/5.0 (CVC course deck builder)"}
FONTS = Path("C:/Windows/Fonts")
W, H = 1920, 1080

ACTIAN_URL = "https://www.actian.com/wp-content/uploads/2026/09/actian-vector-ai-db-hero.png"
SHILLER_URL = "http://www.econ.yale.edu/~shiller/data/ie_data.xls"
MULTPL_URL = "https://www.multpl.com/shiller-pe/table/by-month"
RAILROAD_MAP_PAGE = ("File:Railroad map of the United States, showing the through lines of communication from the "
                     "Atlantic to the Pacific (IA dr railroad-map-of-the-united-states-showing-the-through-lines-of-"
                     "communicati-0592010).jpg")


def fetch(url: str) -> bytes:
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60).read()


def commons_thumb(title: str, width: int) -> bytes:
    import json
    import urllib.parse
    api = ("https://commons.wikimedia.org/w/api.php?action=query&prop=imageinfo&iiprop=url&format=json"
           f"&iiurlwidth={width}&titles=" + urllib.parse.quote(title))
    page = next(iter(json.loads(fetch(api))["query"]["pages"].values()))
    return fetch(page["imageinfo"][0]["thumburl"])


def font(size: int, light: bool = True):
    for name in (("calibril.ttf", "calibri.ttf") if light else ("calibri.ttf",)):
        p = FONTS / name
        if p.exists():
            return ImageFont.truetype(str(p), size)
    return ImageFont.load_default()


# --- 26: agent loop -------------------------------------------------------

def agent_loop():
    im = Image.open(io.BytesIO(fetch(ACTIAN_URL))).convert("L")
    im = ImageOps.autocontrast(im, cutoff=1)
    im = im.point(lambda v: 0 if v < 40 else v)
    canvas = Image.new("L", (W, H), 0)
    scale = min((H - 80) / im.height, (W - 80) / im.width)
    im = im.resize((int(im.width * scale), int(im.height * scale)), Image.LANCZOS)
    canvas.paste(im, ((W - im.width) // 2, (H - im.height) // 2))
    canvas.save(IMG / "26-agent-loop-actian-bw.png", optimize=True)


# --- 27: standard setup versus course setup ---------------------------------

def arrow(d, a, b, width=3, head=16, both=False):
    import math
    d.line([a, b], fill=255, width=width)
    for p, q in ((a, b), (b, a)) if both else ((a, b),):
        ang = math.atan2(q[1] - p[1], q[0] - p[0])
        for s in (+1, -1):
            d.line([q, (q[0] - head * math.cos(ang + s * 0.45), q[1] - head * math.sin(ang + s * 0.45))],
                   fill=255, width=width)


def box(d, x, y, w, h, lines, f):
    d.rectangle([x, y, x + w, y + h], outline=255, width=3)
    lh = f.size + 8
    ty = y + (h - lh * len(lines)) / 2 + 2
    for ln in lines:
        tw = d.textlength(ln, font=f)
        d.text((x + (w - tw) / 2, ty), ln, font=f, fill=255)
        ty += lh


def dashed_v(d, x, y0, y1, dash=18, gap=14):
    y = y0
    while y < y1:
        d.line([(x, y), (x, min(y + dash, y1))], fill=170, width=2)
        y += dash + gap


def dashed_box(d, x, y, w, h, lines, f, dash=14, gap=10):
    for x0, y0, x1, y1 in ((x, y, x + w, y), (x, y + h, x + w, y + h), (x, y, x, y + h), (x + w, y, x + w, y + h)):
        horizontal = y0 == y1
        length = (x1 - x0) if horizontal else (y1 - y0)
        t = 0
        while t < length:
            e = min(t + dash, length)
            d.line([(x0 + t, y0), (x0 + e, y0)] if horizontal else [(x0, y0 + t), (x0, y0 + e)], fill=200, width=3)
            t += dash + gap
    lh = f.size + 8
    ty = y + (h - lh * len(lines)) / 2 + 2
    for ln in lines:
        d.text((x + (w - d.textlength(ln, font=f)) / 2, ty), ln, font=f, fill=230)
        ty += lh


def label_between(d, a_x, b_x, y, text, f):
    d.text(((a_x + b_x) / 2 - d.textlength(text, font=f) / 2, y), text, font=f, fill=210)


def setup_comparison():
    """Standard cloud setups (ChatGPT, Cursor with defaults) against the course setup."""
    im = Image.new("L", (W, H), 0)
    d = ImageDraw.Draw(im)
    fb, fs, fl, ft = font(31), font(24), font(27, light=False), font(40)
    d.text((110, 45), "Standard setup or course setup: where your things live", font=ft, fill=255)

    split = 1110
    dashed_v(d, split, 130, 1040)
    d.text((split - 250, 128), "your computer", font=fs, fill=170)
    d.text((split + 30, 128), "company servers", font=fs, fill=170)

    # Standard setup
    y0, bh = 235, 104
    d.text((110, 180), "STANDARD SETUP: ChatGPT, or Cursor with default settings", font=fl, fill=255)
    box(d, 110, y0, 170, bh, ["You"], fb)
    box(d, 380, y0, 300, bh, ["App window", "on your screen"], fb)
    arrow(d, (280, y0 + bh / 2), (380, y0 + bh / 2), both=True)
    box(d, 1170, y0, 300, bh, ["Model"], fb)
    box(d, 1520, y0, 330, bh, ["Agent loop,", "prompt building"], fb)
    box(d, 1170, y0 + 140, 300, bh, ["Chats and memory", "(ChatGPT)"], fb)
    box(d, 1520, y0 + 140, 330, bh, ["Code index (Cursor),", "uploads (ChatGPT)"], fb)
    arrow(d, (680, y0 + bh / 2 - 16), (1170, y0 + bh / 2 - 16))
    arrow(d, (1170, y0 + bh / 2 + 16), (680, y0 + bh / 2 + 16))
    label_between(d, 680, 1170, y0 + bh / 2 - 58, "everything you type and share", fs)
    label_between(d, 680, 1170, y0 + bh / 2 + 28, "answer", fs)
    for i, ln in enumerate(["On your side: the window, and in Cursor your files.",
                            "The agent's work happens on company servers."]):
        d.text((110, y0 + 150 + i * 34), ln, font=fs, fill=255)
    for i, ln in enumerate(["ChatGPT: chats can train the next model",
                            "unless you switch it off.",
                            "Cursor: every request goes through Cursor's",
                            "servers, even with your own model key."]):
        d.text((1170, y0 + 262 + i * 30), ln, font=fs, fill=255)

    # Course setup
    y1 = 690
    d.text((110, 635), "COURSE SETUP: Hermes + Obsidian + LLM Wiki", font=fl, fill=255)
    box(d, 110, y1, 170, bh, ["You"], fb)
    box(d, 380, y1, 330, bh, ["Hermes agent", "skills, rules, memory"], fb)
    box(d, 380, y1 + 200, 330, bh, ["Notes folder", "sources, wiki, schema"], fb)
    dashed_box(d, 780, y1 + 200, 280, bh, ["or a local model", "(optional)"], fs)
    box(d, 1170, y1, 300, bh, ["Model", "any provider"], fb)
    arrow(d, (280, y1 + bh / 2), (380, y1 + bh / 2), both=True)
    arrow(d, (545, y1 + bh), (545, y1 + 200), both=True)
    d.text((565, y1 + bh + 34), "reads, writes", font=fs, fill=210)
    arrow(d, (710, y1 + bh / 2 - 16), (1170, y1 + bh / 2 - 16))
    arrow(d, (1170, y1 + bh / 2 + 16), (710, y1 + bh / 2 + 16))
    label_between(d, 710, 1170, y1 + bh / 2 - 58, "prompt + selected notes", fs)
    label_between(d, 710, 1170, y1 + bh / 2 + 28, "answer", fs)
    arrow(d, (700, y1 + bh), (880, y1 + 200), both=True)
    for i, ln in enumerate(["Only the model call leaves your computer.",
                            "Change the model or the agent: your files stay.",
                            "With a local model, nothing leaves."]):
        d.text((1170, y1 + 150 + i * 34), ln, font=fs, fill=255)

    im.save(IMG / "27-standard-vs-course-setup.png", optimize=True)


# --- 14: LLM Wiki diagram with notes ---------------------------------------

WIKI_SRC = "14-agent-setup-flowchart-medium.jpg"
# Section labels in the source image (1200 x 1011): text, search window (x0, y0, x1, y1)
WIKI_LABELS = (("ARCHITECTURE", (510, 260, 695, 282)),
               ("OPERATIONS", (525, 473, 672, 495)),
               ("ACTORS", (545, 831, 660, 851)))
# (side, y on the 1080 canvas, heading, note)
WIKI_NOTES = (
    ("L", 250, "Raw sources", "Your PDFs, clippings, transcripts. The agent reads them and never changes them."),
    ("L", 415, "The wiki", "Markdown pages the agent writes and links. This is your notes folder."),
    ("R", 290, "Schema", "The rules file (AGENTS.md): how pages look, what the agent may touch."),
    ("L", 585, "Ingest", "A new source comes in: the agent summarises it, updates the index, adds links."),
    ("R", 465, "Query", "You ask. The agent searches the index, answers, can save the answer as a page."),
    ("R", 650, "Lint", "A health check of the wiki: broken links, contradictions, forgotten pages. Then fix."),
    ("L", 870, "Human", "You: choose sources, ask, think, decide."),
    ("R", 870, "LLM agent", "Hermes: summarises, cross-links, keeps the wiki in order."),
)


def wrap(d, text, f, width):
    words, lines, cur = text.split(), [], ""
    for w_ in words:
        trial = (cur + " " + w_).strip()
        if d.textlength(trial, font=f) <= width:
            cur = trial
        else:
            lines.append(cur)
            cur = w_
    return lines + [cur]


def whiten_label(src: Image.Image, text: str, window):
    """Repaint a dim, letter-spaced section label in pure white at the same place and size."""
    region = src.crop(window)
    pts = [(x, y) for x in range(region.width) for y in range(region.height)
           if (lambda p: min(p) > 45 and max(p) - min(p) < 20)(region.getpixel((x, y)))]
    if not pts:
        return
    x0, x1 = window[0] + min(p[0] for p in pts), window[0] + max(p[0] for p in pts)
    y0, y1 = window[1] + min(p[1] for p in pts), window[1] + max(p[1] for p in pts)
    d = ImageDraw.Draw(src)
    bg = src.getpixel((x0 - 12, (y0 + y1) // 2))
    d.rectangle([x0 - 3, y0 - 3, x1 + 3, y1 + 3], fill=bg)
    probe = ImageFont.truetype(str(FONTS / "consolab.ttf"), 100)
    cap = probe.getbbox("H")
    f = ImageFont.truetype(str(FONTS / "consolab.ttf"), round(100 * (y1 - y0 + 1) / (cap[3] - cap[1])))
    widths = [d.textlength(c, font=f) for c in text]
    gap = ((x1 - x0 + 1) - sum(widths)) / max(1, len(text) - 1)
    x, top = x0, y0 - f.getbbox("H")[1]
    for c, cw in zip(text, widths):
        d.text((x, top), c, font=f, fill=(255, 255, 255))
        x += cw + gap


def wiki_annotated():
    src = Image.open(IMG / WIKI_SRC).convert("RGB")
    for text, window in WIKI_LABELS:
        whiten_label(src, text, window)
    target_h = 980
    src = src.resize((int(src.width * target_h / src.height), target_h), Image.LANCZOS)
    canvas = Image.new("RGB", (W, H), (0, 0, 0))
    left = (W - src.width) // 2
    canvas.paste(src, (left, (H - target_h) // 2))
    d = ImageDraw.Draw(canvas)
    fh, fn = font(27, light=False), font(24)
    col_w = left - 50
    for side, y, head, note in WIKI_NOTES:
        x = 25 if side == "L" else left + src.width + 25
        d.text((x, y), head, font=fh, fill=(255, 255, 255))
        for i, ln in enumerate(wrap(d, note, fn, col_w)):
            d.text((x, y + 36 + i * 30), ln, font=fn, fill=(255, 255, 255))
    canvas.save(IMG / "14-llm-wiki-annotated.png", optimize=True)


# --- 31: railroad map -------------------------------------------------------

def us_railroad_map():
    im = Image.open(io.BytesIO(commons_thumb(RAILROAD_MAP_PAGE, 3840))).convert("RGB")
    w, h = im.size
    im = im.crop((int(w * 0.072), int(h * 0.03), int(w * 0.947), int(h * 0.962)))
    im.thumbnail((2600, 2600), Image.LANCZOS)
    im.save(IMG / "31-us-railroad-map-1884.jpg", quality=88)


# --- charts ----------------------------------------------------------------

def chart_style():
    plt.rcParams.update({
        "figure.facecolor": "black", "axes.facecolor": "black", "savefig.facecolor": "black",
        "text.color": "white", "axes.labelcolor": "white", "xtick.color": "white", "ytick.color": "white",
        "axes.edgecolor": "white", "font.family": "Calibri", "font.size": 22,
        "axes.spines.top": False, "axes.spines.right": False,
    })


def finish(fig, ax, title, source, out):
    fig.text(0.06, 0.93, title, fontsize=34, fontweight="light", ha="left")
    fig.text(0.06, 0.035, source, fontsize=15, color="#bbbbbb", ha="left")
    fig.subplots_adjust(left=0.08, right=0.95, top=0.82, bottom=0.14)
    fig.savefig(IMG / out, dpi=100)
    plt.close(fig)


# SEC 10-K filings, cash purchases of property and equipment, each company's fiscal year
# (Microsoft's ends 30 June). Compiled from EDGAR XBRL by 500metrics.com/capex and
# chartedfacts.com, checked against each other, Nov 2026. $ billion.
CAPEX = {2016: 30.9, 2017: 40.0, 2018: 64.1, 2019: 69.4, 2020: 93.0, 2021: 125.0,
         2022: 150.2, 2023: 140.1, 2024: 217.3, 2025: 357.5}
CAPEX_2026_GUIDANCE = (720, 740)


def capex_chart():
    fig, ax = plt.subplots(figsize=(19.2, 10.8))
    years = list(CAPEX)
    ax.bar(years, [CAPEX[y] for y in years], color="white", width=0.62)
    mid = sum(CAPEX_2026_GUIDANCE) / 2
    ax.bar([2026], [mid], color="black", edgecolor="white", linewidth=3, width=0.62, hatch="//")
    for y in years:
        ax.text(y, CAPEX[y] + 12, f"{CAPEX[y]:.0f}", ha="center", fontsize=19)
    ax.text(2026, mid + 12, "720 to 740\nplanned", ha="center", fontsize=19)
    ax.set_xticks(years + [2026])
    ax.set_ylim(0, 820)
    ax.set_ylabel("$ billion")
    ax.tick_params(length=0)
    finish(fig, ax, "Hyperscaler capex by year: Amazon, Alphabet, Microsoft, Meta",
           "Source: SEC 10-K filings, cash purchases of property and equipment, fiscal years (Microsoft ends in June). "
           "2026: company guidance, Oct 2026, not strictly comparable.",
           "28-bigtech-capex-chart.png")


def shiller_series():
    """Yale data as far as it goes, then multpl.com's monthly table (same method) for later months."""
    import re
    from datetime import datetime

    import xlrd
    sh = xlrd.open_workbook(file_contents=fetch(SHILLER_URL)).sheet_by_name("Data")
    header_row = next(r for r in range(20) if str(sh.cell_value(r, 0)).strip() == "Date")
    cape_col = next(c for c in range(sh.ncols) if str(sh.cell_value(header_row, c)).strip() == "CAPE")
    series = {}
    for r in range(header_row + 1, sh.nrows):
        date, cape = sh.cell_value(r, 0), sh.cell_value(r, cape_col)
        if isinstance(date, float) and isinstance(cape, float) and cape > 0:
            year = int(date)
            month = round((date - year) * 100)
            series[(year, month)] = cape
    yale_end = max(series)
    page = fetch(MULTPL_URL).decode("utf-8", "ignore")
    for d, v in re.findall(r"<tr[^>]*>\s*<td[^>]*>([^<]+)</td>\s*<td[^>]*>(.*?)</td>", page, re.S):
        dt = datetime.strptime(d.strip(), "%b %d, %Y")
        key = (dt.year, dt.month)
        if key > yale_end and key not in series:
            series[key] = float(re.findall(r"[\d.]+", v.replace("&#x2002;", ""))[0])
    keys = sorted(series)
    return [y + (m - 1) / 12 for y, m in keys], [series[k] for k in keys], yale_end


def shiller_cape_chart():
    xs, ys, yale_end = shiller_series()
    fig, ax = plt.subplots(figsize=(19.2, 10.8))
    ax.plot(xs, ys, color="white", linewidth=2.2)
    for label, lo, hi in (("1929", 1929, 1930), ("2000", 1999.5, 2001)):
        pts = [(x, y) for x, y in zip(xs, ys) if lo <= x < hi]
        if pts:
            x, y = max(pts, key=lambda p: p[1])
            ax.annotate(f"{label}: {y:.0f}", (x, y), xytext=(x - 9, y + 3), fontsize=21,
                        arrowprops=dict(arrowstyle="-", color="white", lw=1))
    ax.annotate(f"latest: {ys[-1]:.0f}", (xs[-1], ys[-1]), xytext=(xs[-1] - 14, ys[-1] + 4), fontsize=21,
                arrowprops=dict(arrowstyle="-", color="white", lw=1))
    mean = sum(ys) / len(ys)
    ax.plot([xs[0], xs[-1]], [mean, mean], color="#bbbbbb", linewidth=2, linestyle=(0, (6, 4)))
    ax.text(xs[-1] + 2, mean, f"long-run\naverage: {mean:.0f}", va="center", fontsize=20, color="#bbbbbb")
    ax.set_xlim(xs[0] - 3, xs[-1] + 17)
    ax.set_ylim(0, max(ys) * 1.18)
    ax.set_ylabel("years of average profit you pay for")
    ax.tick_params(length=0)
    fig.text(0.06, 0.865, "Price of the shares divided by their average yearly profit over the past 10 years "
             "(both adjusted for inflation). 40 means: the price equals 40 years of that profit.",
             fontsize=19, color="#dddddd", ha="left")
    finish(fig, ax, "US stocks: price compared with ten years of profit (Shiller CAPE)",
           f"Source: Robert Shiller, online data (Yale), S&P composite, monthly, to {yale_end[1]}/{yale_end[0]}; "
           f"later months from multpl.com (same method), to {int(xs[-1])}.",
           "29-shiller-cape-chart.png")
    return ys[-1], xs[-1], mean


def bis_labour_share_chart():
    # Values read from BIS Annual Economic Report 2026, Box C, Graph C1.B (Rungcharoenkitkul 2026a).
    years = [2025, 2030, 2033, 2036, 2040, 2045, 2050, 2055, 2060]
    transformative = [60, 60, 55, 49, 41, 32, 26, 21, 18]
    bottleneck = [60, 60, 57, 52, 48, 47, 47, 47, 47]
    fig, ax = plt.subplots(figsize=(19.2, 10.8))
    ax.plot([2025, 2060], [60, 60], color="white", linewidth=2.5, linestyle=(0, (6, 4)))
    ax.plot(years, bottleneck, color="#bbbbbb", linewidth=3)
    ax.plot(years, transformative, color="white", linewidth=4)
    ax.text(2060.5, 61, "business as usual,\nAI only a modest boost", va="center", fontsize=20)
    ax.text(2060.5, 46, "demand bottleneck:\nreplaced workers buy less,\nso automation stalls", va="center",
            fontsize=20, color="#bbbbbb")
    ax.text(2060.5, 18, "transformative AI:\nmachines take most tasks", va="center", fontsize=20)
    ax.set_xlim(2025, 2074)
    ax.set_xticks([2030, 2040, 2050, 2060])
    ax.set_ylim(0, 70)
    ax.set_ylabel("share of income paid as wages, %")
    ax.tick_params(length=0)
    finish(fig, ax, "If AI delivers on the hype: workers' share of income",
           "Redrawn after Bank for International Settlements (BIS), Annual Economic Report 2026, Box C, Graph C1.B "
           "(model scenarios, Rungcharoenkitkul 2026). Values read from the chart, approximate.",
           "30-bis-labour-share-scenario.png")


def hype_cycle_chart():
    """Gartner-style hype cycle: a qualitative model, drawn smooth, no data behind it."""
    import numpy as np
    x = np.linspace(0, 6, 600)
    y = 0.15 + 3.3 * np.exp(-((x - 1.05) / 0.45) ** 2) + 1.75 / (1 + np.exp(-(x - 3.1) / 0.42))
    fig, ax = plt.subplots(figsize=(12, 9.5))
    ax.plot(x, y, color="white", linewidth=4)
    phases = ((0.15, "technology\ntrigger"), (1.05, "peak of inflated\nexpectations"),
              (2.15, "trough of\ndisillusionment"), (3.3, "slope of\nenlightenment"), (5.0, "plateau of\nproductivity"))
    for px, label in phases:
        py = float(np.interp(px, x, y))
        ax.plot([px, px], [-0.05, py], color="#777777", linewidth=1.2, linestyle=(0, (4, 4)))
        ax.text(px, -0.2, label, ha="center", va="top", fontsize=19)
    ax_ = 1.62
    ay_ = float(np.interp(ax_, x, y))
    ax.plot([ax_], [ay_], "o", color="white", markersize=20)
    ax.annotate("AI, 2026\n(Campbell)", (ax_, ay_), xytext=(ax_ + 0.45, ay_ + 0.35), fontsize=21,
                arrowprops=dict(arrowstyle="-", color="white", lw=1.2))
    ax.set_xlim(-0.35, 6.0)
    ax.set_ylim(-1.35, 4.0)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines["bottom"].set_position(("data", -0.05))
    ax.set_ylabel("expectations")
    ax.text(5.95, -0.0, "time", ha="right", va="bottom", fontsize=20)
    fig.text(0.04, 0.035, "After Gartner's Hype Cycle (Jackie Fenn, 1995). A model, not measured data. "
             "Redrawn for this course.", fontsize=15, color="#bbbbbb", ha="left")
    fig.subplots_adjust(left=0.07, right=0.98, top=0.97, bottom=0.08)
    fig.savefig(IMG / "34-hype-cycle.png", dpi=100)
    plt.close(fig)


# Read from Bridgewater's chart (Aug 2025) as shown by J.P. Morgan Asset Management and in Campbell's talk.
# Real GDP growth, year on year, two-quarter rolling average, percent. Approximate.
GDP_QUARTERS = ["1Q23", "2Q23", "3Q23", "4Q23", "1Q24", "2Q24", "3Q24", "4Q24", "1Q25", "2Q25"]
GDP_TOTAL = [2.3, 2.9, 3.3, 3.15, 2.9, 3.0, 2.7, 2.55, 2.0, 2.0]
GDP_REST = [2.3, 2.8, 3.2, 3.1, 2.6, 2.45, 2.1, 1.7, 1.2, 1.1]


def gdp_tech_capex_chart():
    fig, ax = plt.subplots(figsize=(19.2, 10.8))
    xs = range(len(GDP_QUARTERS))
    tech = [t - r for t, r in zip(GDP_TOTAL, GDP_REST)]
    ax.bar(xs, GDP_REST, color="#777777", width=0.62, label="rest of the economy")
    ax.bar(xs, tech, bottom=GDP_REST, color="white", width=0.62, label="tech investment (AI data centres, chips, software)")
    for i, (t, total) in enumerate(zip(tech, GDP_TOTAL)):
        if t >= 0.25:
            ax.text(i, total + 0.08, f"{100 * t / total:.0f}%", ha="center", fontsize=20)
    ax.set_xticks(list(xs))
    ax.set_xticklabels(GDP_QUARTERS)
    ax.set_ylim(0, 3.9)
    ax.set_ylabel("US real GDP growth, %")
    ax.tick_params(length=0)
    ax.legend(loc="upper right", frameon=False, fontsize=21)
    ax.text(len(GDP_QUARTERS) - 0.6, 2.75, "% = share of growth\nfrom tech investment", ha="right", fontsize=19,
            color="#dddddd")
    finish(fig, ax, "US growth: how much came from tech investment",
           "Redrawn after Bridgewater Associates (Aug 2025), as shown by J.P. Morgan Asset Management (Eye on the Market) "
           "and Richard Campbell (NDC 2026).\nTwo-quarter rolling average. Values read from the chart, approximate.",
           "35-us-gdp-tech-capex-chart.png")


# Voronoi (Visual Capitalist), 2 Jan 2025: contribution to the S&P 500's 2024 market-cap growth, percent.
MAG7_2024 = [("Nvidia", 20.4), ("Apple", 7.8), ("Amazon", 7.3), ("Alphabet", 5.7), ("Meta", 5.6),
             ("Tesla", 5.0), ("Microsoft", 3.3)]


def mag7_chart():
    fig, ax = plt.subplots(figsize=(19.2, 10.8))
    rest = 100 - sum(v for _, v in MAG7_2024)
    names = [n for n, _ in MAG7_2024] + ["the other 493 companies"]
    vals = [v for _, v in MAG7_2024] + [rest]
    ys = list(range(len(names)))[::-1]
    ax.barh(ys, vals, color=["white"] * 7 + ["#777777"], height=0.62)
    for y, v in zip(ys, vals):
        ax.text(v + 0.6, y, f"{v:.1f}%", va="center", fontsize=21)
    ax.set_yticks(ys)
    ax.set_yticklabels(names, fontsize=23)
    ax.set_xlim(0, 52)
    ax.set_xlabel("share of the total gain in market value, 2024")
    ax.tick_params(length=0)
    ax.spines["left"].set_visible(False)
    fig.text(0.06, 0.865, f"Seven companies made {sum(v for _, v in MAG7_2024):.0f}% of the gain. "
             f"The other 493 together: {rest:.0f}%.", fontsize=21, color="#dddddd", ha="left")
    fig.text(0.06, 0.93, "Who made the S&P 500's gain in 2024", fontsize=34, fontweight="light", ha="left")
    fig.text(0.06, 0.035, "Source: Voronoi (Visual Capitalist), 2 Jan 2025, \"The Magnificent Seven Propel 55% of "
             "S&P 500's 2024 Gains\", contribution to market-cap growth. Shown by Richard Campbell, NDC 2026.",
             fontsize=15, color="#bbbbbb", ha="left")
    fig.subplots_adjust(left=0.2, right=0.95, top=0.82, bottom=0.14)
    fig.savefig(IMG / "36-mag7-sp500-gains-2024.png", dpi=100)
    plt.close(fig)


if __name__ == "__main__":
    import sys
    chart_style()
    jobs = {"agent_loop": agent_loop, "setup_comparison": setup_comparison, "wiki_annotated": wiki_annotated,
            "us_railroad_map": us_railroad_map, "capex_chart": capex_chart, "shiller_cape_chart": shiller_cape_chart,
            "bis_labour_share_chart": bis_labour_share_chart, "hype_cycle_chart": hype_cycle_chart,
            "gdp_tech_capex_chart": gdp_tech_capex_chart, "mag7_chart": mag7_chart}
    for name in sys.argv[1:] or list(jobs):
        result = jobs[name]()
        print(name, "done", result if result is not None else "")
