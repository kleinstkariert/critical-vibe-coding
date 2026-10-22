---
title: AI tools for creative processes — research list
date: 2026-10-18
tags:
  - course
  - research
  - creative-ai
---

# AI tools for creative processes — research list

Survey for Critical Vibe Coding (extra to the Hermes / Obsidian default stack). Not a recommendation to adopt everything. Labels: *verified fact* (URL checked 2026-10-18) | *technical suggestion*.

Use with: [[sessions/05-mcp-and-tools]] (agent ↔ CAD/3D) · [[sessions/07-agents-across-creative-stacks]] · [[course-outline]].

---

## How to read this list

| Column | Meaning |
|---|---|
| **Role** | Where it sits in a creative pipeline |
| **Agent link** | Speaks MCP / API to an agent, or stays a separate GUI |
| **Course angle** | What to discuss: authorship, lock-in, ecology, verification |

*technical suggestion:* Prefer tools students can open once for a session demo. For fabrication, always verify geometry in a slicer/CAD — generative “print-ready” claims are hypotheses.

---

## 3D generation & print-adjacent

| Tool | Role | Agent link | Notes / URL |
|---|---|---|---|
| **Meshy** | Text/image → 3D; texture, rig; STL/3MF export; printability marketing | Official **MCP** (`@meshy-ai/meshy-mcp-server`) | https://www.meshy.ai/ — *verified fact:* MCP one-liner on homepage |
| **Tripo** | Fast text/image → 3D | API / web | Often compared with Meshy for topology/speed — https://www.tripo3d.ai/ |
| **Rodin (Hyper3D)** | Photoreal PBR-oriented gen | Web / API | Visual-first; check export for fab |
| **Hitem3D** | High-res image/multi-view → 3D | Web | Print-oriented claims — verify |
| **CSM / 3D[AI]** | Capture / video → 3D | Web | Real-world capture workflows |

Classroom: Meshy is the cleanest **agent-wired** example (session 5). Others = session 7 comparison material.

---

## Node canvases & multimodal workflows

| Tool | Role | Agent link | Notes / URL |
|---|---|---|---|
| **Figma Weave** | Node canvas: image / video / audio / 3D; Compositor; workflows → packaged tools; Weave tools inside Figma Design | Figma ecosystem (not a Hermes default) | https://www.figma.com/ — node-platform overview: https://www.figma.com/resource-library/best-node-based-ai-platform/ |
| **FLORA** | Branching creative canvas; side-by-side model runs; **FAUNA** in-canvas agent | FAUNA in-app; also **FLORA MCP** for external agents (Claude/Cursor…) — *verified fact:* docs.flora.ai | https://flora.ai/ · FAUNA: https://docs.flora.ai/editor/fauna |
| **Fuser** | Node canvas + editable compositor layouts, recipes, custom code/web tools | Studio product | https://fuser.studio/ · compare page: https://fuser.studio/compare |
| **ComfyUI** | Local/graph diffusion pipelines | Often paired with agents via custom nodes / API | Self-host; high control, high friction — ecology + skill discussion |
| **Krea** | Real-time / prompt-to-workflow canvas | Web | Fast concepting |
| **InvokeAI** | Self-hosted node editor, friendlier than raw Comfy for some | Local | Open workflow library |
| **Higgsfield AI Canvas** | Campaign boards, templates | Web | Shared-board production |
| **NodeTool** | Multimodal graph; local or cloud; Comfy import | Local/cloud | Pipeline unification |
| **Mavity** | Brand nodes + high-volume flows | Web | Creative-ops angle |

*technical suggestion:* Treat Weave / Flora / Fuser as **workflow authorship** surfaces (who owns the graph?) parallel to LLM Wiki schema authorship.

---

## Image / video / audio (quick map)

| Domain | Examples (common 2026 classroom names) |
|---|---|
| Image | Midjourney, FLUX, Stable Diffusion / SDXL / SD3, Recraft, Ideogram |
| Video | Kling, Runway, Luma Dream Machine, Hailuo, Pika |
| Audio / music / voice | Suno, Udio, ElevenLabs, Mureka |

Peer-course list (HKUST AMCC6500) clusters these similarly — see [[course-outline]]. Prefer **one** demo per modality over a zoo of accounts.

---

## Design + code (GUI / IDE)

| Tool | Role | Agent link | Notes |
|---|---|---|---|
| **Figma** (Design + AI features) | UI/layout; AI assist inside design | Plugins / Weave tools | Separate from “agent owns the vault” |
| **Cursor / VS Code + Copilot** | Text coding agents | Built-in tools / MCP | Default for code stacks in session 7 |
| **vvvv / TouchDesigner / Max** (etc.) | Node media stacks | Usually **no** first-class MCP — file export, OSC, or script bridges | Prompt → patch translation is the pedagogical point |

---

## CAD / DCC with agent bridges (MCP)

Full teaching table lives in [[sessions/05-mcp-and-tools]]. Short index:

| App | MCP status (2026-10-18) |
|---|---|
| Blender Lab MCP | Official experimental — https://www.blender.org/lab/mcp-server/ |
| Autodesk Fusion | Official local + data MCP — Autodesk help “Fusion MCPs Overview” |
| FreeCAD | Community `freecad-mcp` |
| OpenSCAD | Community `openscad-mcp` |
| build123d | `build123d-mcp` (headless) |
| Rhino/GH | Community (e.g. rhino-mcp); no official McNeel MCP yet |

Landscape article: https://buildcad.ai/guides/cad-mcp-servers

---

## Critical questions (use in class)

1. Does the tool **expose** a graph/history you can own, or only a chat that forgets?
2. Can the agent call it (MCP/API), or must a human babysit a GUI?
3. Where does the file land — local vault, vendor cloud, both?
4. What fails for **fabrication** (mesh quality, units, IP of training data)?
5. Energy / subscription / lock-in vs a smaller local pipeline?

---

## Sources checked

- Meshy homepage (MCP install) — 2026-10-18  
- Figma Weave resource library / image-to-3D pages — 2026-10-18  
- Fuser compare — 2026-10-18  
- Blender Lab MCP — 2026-10-18  
- BuildCAD “CAD MCP Servers Compared” — 2026-10-18  
- HKUST AMCC6500 outline (software list pattern) — 2026-10-18  

*todo:* add cohort-specific tools after the session-2 survey (Unity/Unreal plugins, TouchDesigner AI packs, etc.).
