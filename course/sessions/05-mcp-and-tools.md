---
title: Session 05 — MCP and tools
session: 5
---

# Session 05 — MCP and tools — one interface to many systems

Parent: [[../timeline]] · Outline: [[../course-outline]]

## Goals

- Understand MCP as a protocol (not a model, not sync)
- Attach at least one useful tool kitchen to the student agent
- Contrast: filesystem wiki tools vs MCP for apps that are not folders
- Connect the agent to **3D / CAD** stacks named in the course brief (*requirement*: visual/node, GUI, text code, **3D/CAD**)
- Optional peek: Nextcloud as **one** MCP exposing many apps (mail, calendar, Deck, files…) — *technical suggestion*, not required student infra

## Check-in

Phone sync status; Discord bridge; wiki ingest stories; which creative apps do you already use (code / node / CAD / 3D)?

## Student input (optional)

Someone demos a tool integration they already use — browser, git, calendar, or a CAD/3D bridge if available.

## Teacher input

### MCP basics

- Waiter / kitchen metaphor: [[../what-is-mcp]] — host, client, server; tools / resources / prompts
- When you need MCP vs when the disk is enough: Obsidian folder wiki = filesystem tools, no MCP; apps that are not folders (calendar, mail, browser, SQLite note apps, **live CAD/3D sessions**) = MCP
- How Hermes does it (*verified fact*, Hermes docs 2026-10-18): servers go under `mcp_servers` in `~/.hermes/config.yaml`; local **stdio** and remote **HTTP** servers share one config; `hermes mcp` opens a catalog of Nous-reviewed servers; at install Hermes lists every tool the server exposes and lets you **tick only the tools the agent may see** — [Hermes MCP docs](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp)
- Safety: app passwords, localhost vs remote, what not to put in the vault; per-server tool filtering as a design decision (the agent cannot call what you did not tick)
- Optional peek — *technical suggestion:* Nextcloud **Context Agent** is **one** MCP server whose tool groups (mail, calendar, Deck, files, Collectives…) appear as the matching apps are installed — not one server per app. Research note: [[../../research/llmwiki-obsidian-vs-nextcloud-collectives]] · admin manual: https://docs.nextcloud.com/server/stable/admin_manual/ai/app_context_agent.html . Not required student infra.

### Agent ↔ 3D / CAD (course framing)

*requirement:* the brief names **3D/CAD** alongside code and node tools. MCP is the concrete link: the agent stays the “waiter”; Blender / Fusion / FreeCAD / OpenSCAD / Meshy are kitchens.

| Stack | MCP / bridge (*verified fact* where linked, 2026-10-18) | Agent role | Caveat |
|---|---|---|---|
| **Blender** (official Lab MCP) | [blender.org/lab/mcp-server](https://www.blender.org/lab/mcp-server/) — Blender **5.1+**, add-on + MCP server + LLM client | Scene query, naming, GeoNodes explain, scripted edits via Python API | Executes LLM-generated code **without guards** — use a throwaway file / VM; not on machines with sensitive data |
| **Autodesk Fusion** (official) | Local HTTP MCP on running Fusion desktop (`http://127.0.0.1:27182/mcp`); enable in Preferences → General → API — [Fusion MCP overview](https://help.autodesk.com/view/fusion360/ENU/?guid=FMCP-OVERVIEW) | Drive live modeling / commands in an open session | Needs Fusion desktop running; Autodesk notes limited reliability on complex assemblies |
| **FreeCAD** (community) | Addon + RPC inside FreeCAD, client via e.g. `uvx freecad-mcp` — [neka-nat/freecad-mcp](https://github.com/neka-nat/freecad-mcp) | Parametric parts, inspect, FEM hooks | FreeCAD must be open with RPC started |
| **OpenSCAD** (community) | `uvx openscad-mcp` — [openscad-mcp](https://pypi.org/project/openscad-mcp/) | Scripted solids, render, printability checks | Mesh export (STL…), not B-rep STEP |
| **build123d** (headless CAD) | `uv tool run … build123d-mcp` — [pzfreo/build123d-mcp](https://github.com/pzfreo/build123d-mcp) | STEP/STL with measure/validate loop; **no CAD GUI required** | Python/uv dependency; good classroom demo of “agent has CAD eyes” |
| **Rhino / Grasshopper** | Community e.g. [EaseHee/rhino-mcp](https://github.com/EaseHee/rhino-mcp) (standalone `rhino3dm` or live bridge) | Geometry + GH bake/export | Not official McNeel MCP (as of research date); treat as optional / cohort-dependent |
| **Meshy** (AI 3D gen) | Official Meshy MCP — `npx add-mcp @meshy-ai/meshy-mcp-server` + API key — [meshy.ai](https://www.meshy.ai/) | Text/image → mesh inside the agent loop | Cloud / paid tiers; printability claims are marketing — still verify in slicer |

Comparison survey (CAD MCP landscape): https://buildcad.ai/guides/cad-mcp-servers  

Broader creative AI canvases (Figma Weave, FLORA, Fuser, …) matter as **prompt/workflow** surfaces in session 7: [[../ai-tools-creative-processes]]. FLORA also documents an external **FLORA MCP** (agent outside the canvas); Meshy has an official MCP — both are optional demos if someone already has accounts.

Harness reminder: MCP servers are harness kitchens — [[../what-is-harness]] · [[02-agent-harness-and-wiki-architecture]].

**Teaching frame for CAD/3D:**

1. **File-based path** — agent writes OpenSCAD / build123d / Python → you open the file (filesystem tools may be enough).
2. **Live-session path** — MCP into Blender / Fusion / FreeCAD while the app is running (true tool kitchen).
3. **Generative mesh path** — Meshy (or similar) via API/MCP → import into Blender/CAD for cleanup before fab.

Never skip verification for fabrication: manifold mesh, tolerances, materials, machine safety. The agent proposes; the student owns the cut/print.

## Practical

- List tools the agent already has (filesystem, web, skills) before adding anything
- Add **one** MCP server relevant to a student:
  - default classroom picks: browser, or **build123d-mcp** / **OpenSCAD** if no CAD license, or Meshy if someone already has a key
  - if someone runs Blender 5.1+ or Fusion: pair them with the official local MCP (localhost only)
- During install, deselect tools the student does not want the agent to have
- Document the tool list in the personal wiki — *technical suggestion:* a short “Tools” section in `SCHEMA.md` (what the agent may call, what it must ask before calling) plus a page listed in `index.md`; see [[../llm-wiki-standard-files]]
- Optional 15-minute CAD micro-task: “10 mm cube → export STL → open in slicer” *with* the agent attached, then note where you overruled it

## Serves “agent as interface”

The interface is the set of tools the agent can call. Choosing **which** CAD/3D kitchen to wire — and which tools to leave unticked — is designing that interface. Session 6 practices the same idea across more stacks.

## Homework

- Diagram: user → harness → model → tools/knowledge (one page) — include at least one creative-stack kitchen (code **or** CAD/3D) — updates the session 2 diagram for midpoint (8) and final (13)
- Prepare questions for session 6 art framing
- Skim [[../ai-tools-creative-processes]]; mark one tool you might try in session 7

## Materials / References

| What | Link |
|---|---|
| Course note — waiter metaphor, host / client / server | [[../what-is-mcp]] |
| MCP intro (official) | https://modelcontextprotocol.io/docs/getting-started/intro |
| MCP architecture (spec 2026-07-28) | https://modelcontextprotocol.io/specification/2026-07-28/architecture |
| Hermes — MCP feature (config, catalog, tool selection) | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp |
| Hermes — install / vault pointing (course how-to) | [[../howto-hermes-setup]] |
| Where the tool list lives in the wiki (`SCHEMA.md`, `index.md`) | [[../llm-wiki-standard-files]] |
| Blender Lab MCP | https://www.blender.org/lab/mcp-server/ |
| Autodesk Fusion MCP | https://help.autodesk.com/view/fusion360/ENU/?guid=FMCP-OVERVIEW |
| FreeCAD MCP | https://github.com/neka-nat/freecad-mcp |
| build123d-mcp | https://github.com/pzfreo/build123d-mcp |
| OpenSCAD MCP | https://pypi.org/project/openscad-mcp/ |
| Meshy (+ MCP) | https://www.meshy.ai/ |
| CAD MCP comparison (2026) | https://buildcad.ai/guides/cad-mcp-servers |
| AI tools for creative processes (survey) | [[../ai-tools-creative-processes]] |
| Nextcloud one-MCP comparison (optional) | [[../../research/llmwiki-obsidian-vs-nextcloud-collectives]] · https://docs.nextcloud.com/server/stable/admin_manual/ai/app_context_agent.html |
| Full list | [[../references]] |
