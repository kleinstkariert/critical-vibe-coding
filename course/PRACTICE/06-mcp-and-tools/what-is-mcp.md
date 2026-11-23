---
audience: student
status: current
canonical: true
---

# What is an MCP?

*optional extension. Not required for assessment.* MCP is not the assessed tool set. A tool set can be one folder. See [minimum path](../../PROJECT-WORK/minimum-path.md).

A short teaching note for Critical Vibe Coding. Written 2026-10-15. Claims labeled *unverified lead* or *technical suggestion*.

## One sentence

*institutional summary:* MCP (**Model Context Protocol**) is an open standard for connecting an AI application (Cursor, Claude, Hermes Agent, …) to external programs, data, and tools — in a shared, reusable way.

Official docs call it “like a USB-C port for AI applications”: one plug shape, many devices. Source: [modelcontextprotocol.io](https://modelcontextprotocol.io/docs/getting-started/intro).

## Permissions and capability boundary

MCP is not merely a connector. It is a permissions and capability boundary.

- filesystem
- destructive operations
- network
- application scripting
- messages
- mail
- calendar
- personal data

## The waiter metaphor (yes, it works)

A common API metaphor is: **guest → waiter → kitchen**.

| Restaurant | MCP |
|---|---|
| You, the guest | You, the user |
| The restaurant / head waiter | The **AI host** (Cursor, Claude Desktop, Hermes, …) — the app that runs the model |
| A waiter assigned to one kitchen | An **MCP client** (one connection per program) |
| A kitchen | An **MCP server** (Joplin, a filesystem tool, a browser tool, …) |
| The menu | The list of **tools** the kitchen exposes (`search_notes`, `create_note`, …) |
| Ordering a dish | The model calling a tool (`tools/call`) |
| The food coming back | The tool result, fed back into the conversation |

So: MCP is the **communicator between your agent and a certain software program** — but not a one-off custom cable. It is a **shared language** so many agents can talk to many programs the same way.

*technical suggestion:* Keep the metaphor, then add one precision for students: the “waiter” is not the whole AI. The AI (host) decides *what* to order; the MCP waiter only carries the order to that kitchen and brings the result back.

## How it differs from “just an API”

| | Classical API | MCP |
|---|---|---|
| Who speaks it | Each app has its own API shape | One protocol many hosts understand |
| Discovery | You read docs and hard-code calls | The client asks the server: “what tools do you have?” (`tools/list`) |
| Typical role | Your code → service | Model / agent → external world |
| Building blocks | Endpoints | **Tools** (actions), **resources** (context/data), **prompts** (templates) |

*primary evidence:* Servers expose three primitives (from the MCP spec):

- **Tools** — model-controlled actions (search, write a note, run a query)
- **Resources** — application-controlled context (files, records)
- **Prompts** — user-controlled templates

Architecture: one **host** can open several **clients**, each talking to one **server**. Spec: [Architecture](https://modelcontextprotocol.io/specification/2026-07-28/architecture).

## Course-relevant examples

- **Obsidian + Hermes / Cursor on a folder of `.md` files:** often *no* MCP needed. The agent uses plain filesystem tools. The “kitchen” is the disk.
- **Joplin:** notes live in SQLite. The agent cannot usefully edit them as files. Joplin 3.7 ships an **MCP server** so the agent can call note tools while the app (or a CLI API server) is running. That *is* the waiter–kitchen path.
- **Cursor** in this workspace: MCP namespaces are how Cursor talks to browser tools, Origin, etc. — same idea.

## What MCP is not

- Not a model (not “GPT” or “Hermes 4”).
- Not a note app.
- Not magic memory: if the kitchen is closed (Joplin quit, no server), the waiter has nowhere to go.
- Not the same as sync (Nextcloud, Obsidian Sync). Sync moves files; MCP moves *tool calls and results* during a conversation.

## Tiny diagram

```text
You  →  AI host (Cursor / Hermes)
              │
              │  MCP client (“waiter”)
              ▼
        MCP server (“kitchen”: Joplin, …)
              │
              ▼
        Tools / data / results
```

## Sources

- Intro: https://modelcontextprotocol.io/docs/getting-started/intro
- Architecture: https://modelcontextprotocol.io/specification/2026-07-28/architecture
- Tools: https://modelcontextprotocol.io/specification/2026-07-28/server/tools

## CAD and 3D servers (table, from retired Session 06)

*requirement:* the brief names **3D/CAD** alongside code and node tools. MCP is the concrete link: the agent stays the “waiter”; Blender / Fusion / FreeCAD / OpenSCAD / Meshy are kitchens.

| Stack | MCP / bridge (*unverified lead* where linked, 2026-10-18) | Agent role | Caveat |
|---|---|---|---|
| **Blender** (official Lab MCP) | [blender.org/lab/mcp-server](https://www.blender.org/lab/mcp-server/) — Blender **5.1+**, add-on + MCP server + LLM client | Scene query, naming, GeoNodes explain, scripted edits via Python API | Executes LLM-generated code **without guards** — use a throwaway file / VM; not on machines with sensitive data |
| **Autodesk Fusion** (official) | Local HTTP MCP on running Fusion desktop (`http://127.0.0.1:27182/mcp`); enable in Preferences → General → API — [Fusion MCP overview](https://help.autodesk.com/view/fusion360/ENU/?guid=FMCP-OVERVIEW) | Drive live modeling / commands in an open session | Needs Fusion desktop running; Autodesk notes limited reliability on complex assemblies |
| **FreeCAD** (community) | Addon + RPC inside FreeCAD, client via e.g. `uvx freecad-mcp` — [neka-nat/freecad-mcp](https://github.com/neka-nat/freecad-mcp) | Parametric parts, inspect, FEM hooks | FreeCAD must be open with RPC started |
| **OpenSCAD** (community) | `uvx openscad-mcp` — [openscad-mcp](https://pypi.org/project/openscad-mcp/) | Scripted solids, render, printability checks | Mesh export (STL…), not B-rep STEP |
| **build123d** (headless CAD) | `uv tool run … build123d-mcp` — [pzfreo/build123d-mcp](https://github.com/pzfreo/build123d-mcp) | STEP/STL with measure/validate loop; **no CAD GUI required** | Python/uv dependency; good classroom demo of “agent has CAD eyes” |
| **Rhino / Grasshopper** | Community e.g. [EaseHee/rhino-mcp](https://github.com/EaseHee/rhino-mcp) (standalone `rhino3dm` or live bridge) | Geometry + GH bake/export | Not official McNeel MCP (as of research date); treat as optional / cohort-dependent |
| **Meshy** (AI 3D gen) | Official Meshy MCP — `npx add-mcp @meshy-ai/meshy-mcp-server` + API key — [meshy.ai](https://www.meshy.ai/) | Text/image → mesh inside the agent loop | Cloud / paid tiers; printability claims are marketing — still verify in slicer |

Comparison survey (CAD MCP landscape): https://buildcad.ai/guides/cad-mcp-servers  

Broader creative AI canvases (Figma Weave, FLORA, Fuser, …) matter as **prompt/workflow** surfaces in session 7: [[../07-creative-stacks/ai-tools-creative-processes]]. FLORA also documents an external **FLORA MCP** (agent outside the canvas); Meshy has an official MCP — both are optional demos if someone already has accounts.

Harness reminder: MCP servers are harness kitchens — [[../01-harness-and-agents/what-is-harness]] · [[../../SESSIONS/02-agent-harness-and-wiki-architecture]].

**Teaching frame for CAD/3D:**

1. **File-based path** — agent writes OpenSCAD / build123d / Python → you open the file (filesystem tools may be enough).
2. **Live-session path** — MCP into Blender / Fusion / FreeCAD while the app is running (true tool kitchen).
3. **Generative mesh path** — Meshy (or similar) via API/MCP → import into Blender/CAD for cleanup before fab.

Never skip verification for fabrication: manifold mesh, tolerances, materials, machine safety. The agent proposes; the student owns the cut/print.

### Practical (retired Session 06)

- List tools the agent already has (filesystem, web, skills) before adding anything
- Add **one** MCP server relevant to a student:
  - default classroom picks: browser, or **build123d-mcp** / **OpenSCAD** if no CAD license, or Meshy if someone already has a key
  - if someone runs Blender 5.1+ or Fusion: pair them with the official local MCP (localhost only)
- During install, deselect tools the student does not want the agent to have
- Document the tool list in the personal wiki — *technical suggestion:* a short “Tools” section in `SCHEMA.md` (what the agent may call, what it must ask before calling) plus a page listed in `index.md`; see [[../02-knowledge-bases/llm-wiki-standard-files]]
- Optional 15-minute CAD micro-task: “10 mm cube → export STL → open in slicer” *with* the agent attached, then note where you overruled it

### Links (retired Session 06)

| What | Link |
|---|---|
| Blender Lab MCP | https://www.blender.org/lab/mcp-server/ |
| Autodesk Fusion MCP | https://help.autodesk.com/view/fusion360/ENU/?guid=FMCP-OVERVIEW |
| FreeCAD MCP | https://github.com/neka-nat/freecad-mcp |
| build123d-mcp | https://github.com/pzfreo/build123d-mcp |
| OpenSCAD MCP | https://pypi.org/project/openscad-mcp/ |
| Meshy (+ MCP) | https://www.meshy.ai/ |
| CAD MCP comparison (2026) | https://buildcad.ai/guides/cad-mcp-servers |
