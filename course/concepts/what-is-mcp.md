# What is an MCP?

A short teaching note for Critical Vibe Coding. Written 2026-10-15. Claims labeled *verified fact* or *technical suggestion*.

## One sentence

*verified fact:* MCP (**Model Context Protocol**) is an open standard for connecting an AI application (Cursor, Claude, Hermes Agent, …) to external programs, data, and tools — in a shared, reusable way.

Official docs call it “like a USB-C port for AI applications”: one plug shape, many devices. Source: [modelcontextprotocol.io](https://modelcontextprotocol.io/docs/getting-started/intro).

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

*verified fact:* Servers expose three primitives (from the MCP spec):

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
