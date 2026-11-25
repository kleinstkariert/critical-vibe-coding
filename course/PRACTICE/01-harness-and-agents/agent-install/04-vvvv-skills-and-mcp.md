---
title: Agent. vvvv skills and MCP
date: 2026-11-25
status: current
canonical: true
---

# Agent. vvvv skills and MCP

Windows example only. Optional. Human detail: [howto-example-mcp-servers.md](../../06-mcp-and-tools/howto-example-mcp-servers.md) · permissions: [what-is-mcp.md](../../06-mcp-and-tools/what-is-mcp.md#permissions-and-capability-boundary)

Needs: Git for Windows, Node.js 22.20+, .NET SDK. Those installers may ask for UAC. Hermes itself must stay non-elevated.

## vvvv skills (PowerShell)

Do not use `cmd` `xcopy` lines. Manual copy for Hermes:

```powershell
git clone https://github.com/tebjan/vvvv-skills "$env:TEMP\vvvv-skills"
New-Item -ItemType Directory -Force "$env:LOCALAPPDATA\hermes\skills" | Out-Null
Copy-Item "$env:TEMP\vvvv-skills\skills\*" "$env:LOCALAPPDATA\hermes\skills\" -Recurse
hermes skills list
```

- Each skill: `...\hermes\skills\<name>\SKILL.md`
- Optional: `npx skills add tebjan/vvvv-skills` (needs Node 22.20+). Hermes target path not verified.
- Do not run the Python patch editor from `vvvv-fileformat`.

## vvvv MCP

```powershell
dotnet tool install -g vvvv-mcp
```

- Do **not** run `vvvv-mcp --setup`. It does not list Hermes. It can rewrite other apps' configs.
- Edit `%LOCALAPPDATA%\hermes\config.yaml`:

```yaml
mcp_servers:
  vvvv:
    command: "vvvv-mcp"
    tools:
      include: [search_nodes, get_node_details, list_categories, list_packages, list_knowledge, read_knowledge, search_knowledge, read_patch, explain_patch]
```

- Read/search tools only. No write tools.
- `command: "vvvv-mcp"` without args: not verified. Tool names from README: not verified against live build.
- Restart Hermes. Record tools in the capability inventory.

## STOP

- STOP if UAC appears for Hermes. Elevate only for .NET / Git installers with a verified publisher.
- STOP if asked to run `vvvv-mcp --setup`.
