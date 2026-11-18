from pathlib import Path

out = Path(__file__).resolve().parent
BG = "#000000"
FG = "#f2f2f2"
MUTED = "#b0b0b0"
LINE = "#e8e8e8"
BOX = "#141414"


def svg(w, h, body, title=""):
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{title}">
  <rect width="{w}" height="{h}" fill="{BG}"/>
{body}
</svg>
"""


def box(x, y, w, h, label, fs=40):
    tx = x + w / 2
    ty = y + h / 2 + fs * 0.35
    return (
        f'  <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{BOX}" '
        f'stroke="{LINE}" stroke-width="6"/>\n'
        f'  <text x="{tx}" y="{ty}" fill="{FG}" '
        f'font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="{fs}" '
        f'font-weight="700" text-anchor="middle">{label}</text>'
    )


def caption(text, y=820, fs=32):
    return (
        f'  <text x="800" y="{y}" fill="{MUTED}" '
        f'font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="{fs}" '
        f'text-anchor="middle">{text}</text>'
    )


def hflow(labels, y=360, box_w=280, box_h=120, gap=50, fs=36, mid="m"):
    n = len(labels)
    total = n * box_w + (n - 1) * gap
    x = (1600 - total) / 2
    parts = [
        f'  <defs><marker id="{mid}" markerWidth="14" markerHeight="14" '
        f'refX="12" refY="7" orient="auto">'
        f'<path d="M0,0 L14,7 L0,14 Z" fill="{LINE}"/></marker></defs>'
    ]
    for i, lab in enumerate(labels):
        parts.append(box(x, y, box_w, box_h, lab, fs=fs))
        if i < n - 1:
            x1 = x + box_w + 8
            x2 = x + box_w + gap - 8
            cy = y + box_h / 2
            parts.append(
                f'  <line x1="{x1}" y1="{cy}" x2="{x2}" y2="{cy}" '
                f'stroke="{LINE}" stroke-width="6" marker-end="url(#{mid})"/>'
            )
        x += box_w + gap
    return "\n".join(parts)


files = {}

files["01-hermes-terminal-banner.svg"] = svg(
    1600,
    900,
    f"""
  <rect x="120" y="180" width="1360" height="540" rx="16" fill="{BOX}" stroke="{LINE}" stroke-width="8"/>
  <text x="800" y="340" fill="{FG}" font-family="Consolas, Menlo, monospace" font-size="92" font-weight="700" text-anchor="middle">HERMES AGENT</text>
  <text x="800" y="430" fill="{MUTED}" font-family="Consolas, Menlo, monospace" font-size="40" text-anchor="middle">$ hermes</text>
  <text x="800" y="520" fill="{MUTED}" font-family="Consolas, Menlo, monospace" font-size="34" text-anchor="middle">terminal banner · teaching redraw</text>
  <text x="800" y="620" fill="{MUTED}" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="28" text-anchor="middle">Inspired by NousResearch/hermes-agent banner.py (MIT)</text>
""",
    "Hermes terminal banner",
)

files["02-user-agent-tools-result.svg"] = svg(
    1600,
    900,
    hflow(["User", "Agent", "Tools", "Result"], box_w=260, gap=40, fs=40, mid="m2")
    + "\n"
    + caption("One path from ask to change"),
    "User Agent Tools Result",
)

parts = [
    box(560, 80, 480, 140, "Model", 48),
    f'  <defs><marker id="md" markerWidth="14" markerHeight="14" refX="12" refY="7" orient="auto"><path d="M0,0 L14,7 L0,14 Z" fill="{LINE}"/></marker></defs>',
    f'  <line x1="800" y1="220" x2="800" y2="300" stroke="{LINE}" stroke-width="6" marker-end="url(#md)"/>',
    box(80, 340, 320, 140, "Files", 40),
    box(440, 340, 320, 140, "Tools", 40),
    box(800, 340, 320, 140, "Memory", 40),
    box(1160, 340, 340, 140, "Checks", 40),
    caption("Harness = model + controls"),
]
files["03-harness-model-plus-parts.svg"] = svg(1600, 900, "\n".join(parts), "Harness parts")

files["04-thin-vs-thick.svg"] = svg(
    1600,
    900,
    f"""
  <rect x="80" y="160" width="680" height="520" rx="12" fill="{BOX}" stroke="{LINE}" stroke-width="6"/>
  <text x="420" y="230" fill="{FG}" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="44" font-weight="700" text-anchor="middle">Thin</text>
  <rect x="160" y="280" width="520" height="320" rx="8" fill="#0a0a0a" stroke="{MUTED}" stroke-width="4"/>
  <text x="420" y="420" fill="{MUTED}" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="36" text-anchor="middle">Chat window</text>
  <text x="420" y="480" fill="{MUTED}" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="28" text-anchor="middle">text in · text out</text>
  <rect x="840" y="160" width="680" height="520" rx="12" fill="{BOX}" stroke="{LINE}" stroke-width="6"/>
  <text x="1180" y="230" fill="{FG}" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="44" font-weight="700" text-anchor="middle">Thick</text>
  <rect x="920" y="280" width="520" height="320" rx="8" fill="#0a0a0a" stroke="{LINE}" stroke-width="6"/>
  <text x="1180" y="400" fill="{FG}" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="36" text-anchor="middle">Agent workspace</text>
  <text x="1180" y="460" fill="{MUTED}" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="28" text-anchor="middle">files · tools · checks</text>
""",
    "Thin vs thick",
)

files["05-goal-context-action-verification.svg"] = svg(
    1600,
    900,
    hflow(["Goal", "Context", "Action", "Verification"], box_w=280, gap=40, fs=34, mid="m5")
    + "\n"
    + caption("Design from behaviour to control"),
    "Goal Context Action Verification",
)

files["06-suggested-harness-actors.svg"] = svg(
    1600,
    900,
    hflow(
        ["User", "Hermes", "Model", "Files", "Tools", "Checks"],
        box_w=200,
        gap=28,
        fs=28,
        mid="m6",
    )
    + "\n"
    + caption("Suggested harness flow"),
    "Suggested harness actors",
)

files["07-bigger-model-vs-context.svg"] = svg(
    1600,
    900,
    f"""
  <rect x="100" y="200" width="600" height="420" rx="12" fill="{BOX}" stroke="{MUTED}" stroke-width="6"/>
  <text x="400" y="320" fill="{MUTED}" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="40" font-weight="700" text-anchor="middle">Bigger model</text>
  <text x="400" y="420" fill="{MUTED}" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="32" text-anchor="middle">alone</text>
  <text x="400" y="520" fill="{MUTED}" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="28" text-anchor="middle">not enough</text>
  <text x="800" y="420" fill="{FG}" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="64" font-weight="700" text-anchor="middle">vs</text>
  <rect x="900" y="200" width="600" height="420" rx="12" fill="{BOX}" stroke="{LINE}" stroke-width="8"/>
  <text x="1200" y="320" fill="{FG}" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="40" font-weight="700" text-anchor="middle">Better context</text>
  <text x="1200" y="420" fill="{FG}" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="36" text-anchor="middle">+ checks</text>
  <text x="1200" y="520" fill="{MUTED}" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="28" text-anchor="middle">structure helps</text>
""",
    "Bigger model vs context",
)

files["08-llm-wiki-tree.svg"] = svg(
    1600,
    900,
    f"""
  <text x="200" y="160" fill="{FG}" font-family="Consolas, Menlo, monospace" font-size="48" font-weight="700">wiki/</text>
  <text x="260" y="260" fill="{FG}" font-family="Consolas, Menlo, monospace" font-size="44">SCHEMA.md</text>
  <text x="260" y="360" fill="{FG}" font-family="Consolas, Menlo, monospace" font-size="44">index.md</text>
  <text x="260" y="460" fill="{FG}" font-family="Consolas, Menlo, monospace" font-size="44">log.md</text>
  <text x="260" y="560" fill="{MUTED}" font-family="Consolas, Menlo, monospace" font-size="40">raw/</text>
  <text x="260" y="660" fill="{MUTED}" font-family="Consolas, Menlo, monospace" font-size="40">entities/</text>
  <line x1="220" y1="200" x2="220" y2="680" stroke="{LINE}" stroke-width="6"/>
  <line x1="220" y1="240" x2="250" y2="240" stroke="{LINE}" stroke-width="6"/>
  <line x1="220" y1="340" x2="250" y2="340" stroke="{LINE}" stroke-width="6"/>
  <line x1="220" y1="440" x2="250" y2="440" stroke="{LINE}" stroke-width="6"/>
  <line x1="220" y1="540" x2="250" y2="540" stroke="{LINE}" stroke-width="6"/>
  <line x1="220" y1="640" x2="250" y2="640" stroke="{LINE}" stroke-width="6"/>
"""
    + caption("Standing structure on disk"),
    "LLM Wiki tree",
)

files["09-obsidian-note-beside-folders.svg"] = svg(
    1600,
    900,
    f"""
  <rect x="120" y="180" width="560" height="520" rx="12" fill="{BOX}" stroke="{LINE}" stroke-width="6"/>
  <text x="400" y="280" fill="{FG}" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="40" font-weight="700" text-anchor="middle">Note</text>
  <rect x="200" y="320" width="400" height="280" rx="8" fill="#0a0a0a" stroke="{MUTED}" stroke-width="4"/>
  <text x="400" y="460" fill="{MUTED}" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="32" text-anchor="middle">Obsidian page</text>
  <rect x="920" y="180" width="560" height="520" rx="12" fill="{BOX}" stroke="{LINE}" stroke-width="6"/>
  <text x="1200" y="280" fill="{FG}" font-family="Consolas, Menlo, monospace" font-size="36" font-weight="700" text-anchor="middle">wiki/</text>
  <text x="1200" y="380" fill="{MUTED}" font-family="Consolas, Menlo, monospace" font-size="32" text-anchor="middle">SCHEMA.md</text>
  <text x="1200" y="460" fill="{MUTED}" font-family="Consolas, Menlo, monospace" font-size="32" text-anchor="middle">index.md</text>
  <text x="1200" y="540" fill="{MUTED}" font-family="Consolas, Menlo, monospace" font-size="32" text-anchor="middle">log.md</text>
"""
    + caption("Note beside folder structure"),
    "Obsidian note beside folders",
)

files["10-cloud-laptop-internet-provider.svg"] = svg(
    1600,
    900,
    hflow(["Laptop", "Internet", "Provider"], box_w=320, gap=60, fs=40, mid="m10")
    + "\n"
    + caption("Proprietary cloud path"),
    "Cloud path",
)

files["11-hosted-open-weight.svg"] = svg(
    1600,
    900,
    hflow(["User", "Hosted model server"], box_w=420, gap=80, fs=36, mid="m11")
    + "\n"
    + caption("Open weights, still hosted"),
    "Hosted open weight",
)

files["12-local-laptop-model.svg"] = svg(
    1600,
    900,
    "\n".join(
        [
            box(200, 300, 400, 220, "Laptop", 48),
            f'  <defs><marker id="loc" markerWidth="14" markerHeight="14" refX="12" refY="7" orient="auto"><path d="M0,0 L14,7 L0,14 Z" fill="{LINE}"/></marker></defs>',
            f'  <line x1="620" y1="410" x2="780" y2="410" stroke="{LINE}" stroke-width="6" marker-end="url(#loc)"/>',
            box(800, 300, 520, 220, "Local model server", 40),
            caption("Same machine · prompt can stay local"),
        ]
    ),
    "Local laptop model",
)

files["13-hermes-run-locations.svg"] = svg(
    1600,
    900,
    f"""
  <rect x="60" y="180" width="460" height="480" rx="12" fill="{BOX}" stroke="{LINE}" stroke-width="6"/>
  <text x="290" y="320" fill="{FG}" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="40" font-weight="700" text-anchor="middle">Laptop</text>
  <text x="290" y="420" fill="{MUTED}" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="30" text-anchor="middle">class default</text>
  <rect x="570" y="180" width="460" height="480" rx="12" fill="{BOX}" stroke="{LINE}" stroke-width="6"/>
  <text x="800" y="320" fill="{FG}" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="40" font-weight="700" text-anchor="middle">Hosted server</text>
  <text x="800" y="420" fill="{MUTED}" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="30" text-anchor="middle">VPS / home box</text>
  <rect x="1080" y="180" width="460" height="480" rx="12" fill="{BOX}" stroke="{LINE}" stroke-width="6"/>
  <text x="1310" y="320" fill="{FG}" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="40" font-weight="700" text-anchor="middle">Always-on</text>
  <text x="1310" y="420" fill="{MUTED}" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="30" text-anchor="middle">gateway / cloud</text>
"""
    + caption("Where Hermes can run"),
    "Hermes run locations",
)

files["14-hermes-model-different-machines.svg"] = svg(
    1600,
    900,
    f"""
  <rect x="120" y="220" width="560" height="360" rx="12" fill="{BOX}" stroke="{LINE}" stroke-width="6"/>
  <text x="400" y="380" fill="{FG}" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="44" font-weight="700" text-anchor="middle">Hermes</text>
  <text x="400" y="460" fill="{MUTED}" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="30" text-anchor="middle">your machine</text>
  <defs><marker id="diff" markerWidth="14" markerHeight="14" refX="12" refY="7" orient="auto"><path d="M0,0 L14,7 L0,14 Z" fill="{LINE}"/></marker></defs>
  <line x1="700" y1="400" x2="880" y2="400" stroke="{LINE}" stroke-width="6" marker-end="url(#diff)"/>
  <text x="790" y="360" fill="{MUTED}" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="26" text-anchor="middle">API</text>
  <rect x="900" y="220" width="560" height="360" rx="12" fill="{BOX}" stroke="{LINE}" stroke-width="6"/>
  <text x="1180" y="380" fill="{FG}" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="44" font-weight="700" text-anchor="middle">Model</text>
  <text x="1180" y="460" fill="{MUTED}" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="30" text-anchor="middle">other machine / cloud</text>
"""
    + caption("Hermes and model can live apart"),
    "Hermes and model different machines",
)

files["15-skills-folders.svg"] = svg(
    1600,
    900,
    f"""
  <rect x="100" y="200" width="400" height="400" rx="12" fill="{BOX}" stroke="{LINE}" stroke-width="6"/>
  <text x="300" y="300" fill="{FG}" font-family="Consolas, Menlo, monospace" font-size="32" font-weight="700" text-anchor="middle">skills/a/</text>
  <text x="300" y="420" fill="{MUTED}" font-family="Consolas, Menlo, monospace" font-size="36" text-anchor="middle">SKILL.md</text>
  <rect x="600" y="200" width="400" height="400" rx="12" fill="{BOX}" stroke="{LINE}" stroke-width="6"/>
  <text x="800" y="300" fill="{FG}" font-family="Consolas, Menlo, monospace" font-size="32" font-weight="700" text-anchor="middle">skills/b/</text>
  <text x="800" y="420" fill="{MUTED}" font-family="Consolas, Menlo, monospace" font-size="36" text-anchor="middle">SKILL.md</text>
  <rect x="1100" y="200" width="400" height="400" rx="12" fill="{BOX}" stroke="{LINE}" stroke-width="6"/>
  <text x="1300" y="300" fill="{FG}" font-family="Consolas, Menlo, monospace" font-size="32" font-weight="700" text-anchor="middle">skills/c/</text>
  <text x="1300" y="420" fill="{MUTED}" font-family="Consolas, Menlo, monospace" font-size="36" text-anchor="middle">SKILL.md</text>
"""
    + caption("One procedure per skill."),
    "Skills folders",
)

files["16-security-allowed-blocked.svg"] = svg(
    1600,
    900,
    f"""
  <rect x="80" y="180" width="560" height="500" rx="12" fill="{BOX}" stroke="{LINE}" stroke-width="8"/>
  <text x="360" y="300" fill="{FG}" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="44" font-weight="700" text-anchor="middle">Allowed</text>
  <text x="360" y="420" fill="{MUTED}" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="34" text-anchor="middle">project folder</text>
  <text x="360" y="500" fill="{MUTED}" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="34" text-anchor="middle">AgentShare</text>
  <rect x="960" y="180" width="560" height="500" rx="12" fill="{BOX}" stroke="#666666" stroke-width="8" stroke-dasharray="16 12"/>
  <text x="1240" y="280" fill="{FG}" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="44" font-weight="700" text-anchor="middle">Blocked</text>
  <text x="1240" y="380" fill="{MUTED}" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="32" text-anchor="middle">private vault</text>
  <text x="1240" y="460" fill="{MUTED}" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="32" text-anchor="middle">passwords</text>
  <text x="1240" y="540" fill="{MUTED}" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="32" text-anchor="middle">keys outside</text>
"""
    + caption("Mount only what the task needs"),
    "Security allowed vs blocked",
)

files["17-docker-sandbox-boundary.svg"] = svg(
    1600,
    900,
    f"""
  <rect x="120" y="140" width="900" height="620" rx="16" fill="{BOX}" stroke="{LINE}" stroke-width="8"/>
  <text x="570" y="220" fill="{FG}" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="40" font-weight="700" text-anchor="middle">Sandbox</text>
  <rect x="280" y="300" width="580" height="280" rx="12" fill="#0a0a0a" stroke="{LINE}" stroke-width="6"/>
  <text x="570" y="440" fill="{FG}" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="44" font-weight="700" text-anchor="middle">Agent</text>
  <text x="570" y="510" fill="{MUTED}" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="28" text-anchor="middle">commands stay inside</text>
  <rect x="1100" y="200" width="400" height="480" rx="12" fill="#0a0a0a" stroke="#666666" stroke-width="6" stroke-dasharray="14 10"/>
  <text x="1300" y="340" fill="{MUTED}" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="34" font-weight="700" text-anchor="middle">Private</text>
  <text x="1300" y="420" fill="{MUTED}" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="30" text-anchor="middle">files</text>
  <text x="1300" y="500" fill="{MUTED}" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="30" text-anchor="middle">outside</text>
  <text x="970" y="400" fill="{MUTED}" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="24" text-anchor="middle">approved only</text>
  <line x1="860" y1="440" x2="1080" y2="440" stroke="{LINE}" stroke-width="5" stroke-dasharray="10 10"/>
"""
    + caption("Container boundary · not a brand logo"),
    "Docker sandbox boundary",
)

files["18-local-gpu-model-hermes.svg"] = svg(
    1600,
    900,
    hflow(["GPU", "Model server", "Hermes"], box_w=340, gap=50, fs=40, mid="m18")
    + "\n"
    + caption("Local model setup"),
    "GPU model Hermes",
)

files["19-cloud-key-secret-store.svg"] = svg(
    1600,
    900,
    f"""
  <rect x="120" y="220" width="560" height="360" rx="12" fill="{BOX}" stroke="{LINE}" stroke-width="8"/>
  <text x="400" y="360" fill="{FG}" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="40" font-weight="700" text-anchor="middle">Secret store</text>
  <text x="400" y="440" fill="{MUTED}" font-family="Consolas, Menlo, monospace" font-size="32" text-anchor="middle">Hermes .env</text>
  <text x="400" y="510" fill="{MUTED}" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="28" text-anchor="middle">API key here</text>
  <rect x="920" y="220" width="560" height="360" rx="12" fill="{BOX}" stroke="#666666" stroke-width="6" stroke-dasharray="14 10"/>
  <text x="1200" y="380" fill="{MUTED}" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="40" font-weight="700" text-anchor="middle">Vault notes</text>
  <text x="1200" y="470" fill="{MUTED}" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="32" text-anchor="middle">no keys</text>
"""
    + caption("Cloud model setup · keep secrets out of sync"),
    "Key in secret store",
)

files["20-smoke-test-folder.svg"] = svg(
    1600,
    900,
    f"""
  <rect x="200" y="160" width="520" height="560" rx="12" fill="{BOX}" stroke="{LINE}" stroke-width="6"/>
  <text x="460" y="260" fill="{FG}" font-family="Consolas, Menlo, monospace" font-size="36" font-weight="700" text-anchor="middle">test/</text>
  <text x="460" y="380" fill="{MUTED}" font-family="Consolas, Menlo, monospace" font-size="34" text-anchor="middle">old-note.md</text>
  <rect x="280" y="440" width="360" height="160" rx="8" fill="#0a0a0a" stroke="{LINE}" stroke-width="6"/>
  <text x="460" y="535" fill="{FG}" font-family="Consolas, Menlo, monospace" font-size="34" font-weight="700" text-anchor="middle">new-file.md</text>
  <text x="1100" y="400" fill="{FG}" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="40" font-weight="700" text-anchor="middle">Smoke test</text>
  <text x="1100" y="480" fill="{MUTED}" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="30" text-anchor="middle">one new file appears</text>
"""
    + caption("Safe diagram · no live terminal screenshot"),
    "Smoke test folder",
)

files["21-full-system.svg"] = svg(
    1600,
    900,
    "\n".join(
        [
            box(40, 80, 280, 100, "User", 34),
            box(400, 80, 280, 100, "Hermes", 34),
            box(760, 80, 280, 100, "Model", 34),
            box(1120, 80, 400, 100, "Chat / Desktop", 30),
            f'  <defs><marker id="fs" markerWidth="12" markerHeight="12" refX="10" refY="6" orient="auto"><path d="M0,0 L12,6 L0,12 Z" fill="{LINE}"/></marker></defs>',
            f'  <line x1="320" y1="130" x2="390" y2="130" stroke="{LINE}" stroke-width="5" marker-end="url(#fs)"/>',
            f'  <line x1="680" y1="130" x2="750" y2="130" stroke="{LINE}" stroke-width="5" marker-end="url(#fs)"/>',
            box(120, 320, 300, 110, "Wiki / vault", 32),
            box(500, 320, 300, 110, "Tools / MCP", 32),
            box(880, 320, 300, 110, "Sandbox", 32),
            box(1260, 320, 280, 110, "Checks", 32),
            f'  <line x1="540" y1="180" x2="270" y2="320" stroke="{LINE}" stroke-width="4"/>',
            f'  <line x1="540" y1="180" x2="650" y2="320" stroke="{LINE}" stroke-width="4"/>',
            f'  <line x1="540" y1="180" x2="1030" y2="320" stroke="{LINE}" stroke-width="4"/>',
            f'  <line x1="540" y1="180" x2="1400" y2="320" stroke="{LINE}" stroke-width="4"/>',
            box(400, 560, 800, 140, "Evidence · approvals · human control", 34),
            f'  <line x1="270" y1="430" x2="600" y2="560" stroke="{LINE}" stroke-width="4"/>',
            f'  <line x1="650" y1="430" x2="700" y2="560" stroke="{LINE}" stroke-width="4"/>',
            f'  <line x1="1030" y1="430" x2="800" y2="560" stroke="{LINE}" stroke-width="4"/>',
            f'  <line x1="1400" y1="430" x2="1000" y2="560" stroke="{LINE}" stroke-width="4"/>',
            caption("Full system · Session 02"),
        ]
    ),
    "Full system",
)

files["22-hermes-mark.svg"] = svg(
    1600,
    900,
    f"""
  <circle cx="800" cy="320" r="140" fill="none" stroke="{LINE}" stroke-width="10"/>
  <line x1="800" y1="180" x2="800" y2="520" stroke="{LINE}" stroke-width="10"/>
  <path d="M720,260 C760,220 840,220 880,260" fill="none" stroke="{LINE}" stroke-width="8"/>
  <path d="M720,380 C760,420 840,420 880,380" fill="none" stroke="{LINE}" stroke-width="8"/>
  <text x="800" y="640" fill="{FG}" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="64" font-weight="700" text-anchor="middle">HERMES</text>
  <text x="800" y="720" fill="{MUTED}" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="28" text-anchor="middle">Teaching mark · inspired by MIT banner art in hermes-agent</text>
  <text x="800" y="780" fill="{MUTED}" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="24" text-anchor="middle">Not the official product icon set</text>
""",
    "Hermes teaching mark",
)

for name, content in files.items():
    (out / name).write_text(content, encoding="utf-8")
    print(name)

print("TOTAL", len(files))
