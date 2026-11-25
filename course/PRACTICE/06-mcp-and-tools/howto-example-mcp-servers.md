---
title: How-to. Example MCP servers (vvvv and TouchDesigner)
date: 2026-11-25
tags:
  - course
  - howto
  - mcp
  - vvvv
  - touchdesigner
status: current
canonical: true
---

# How-to. Example MCP servers (vvvv and TouchDesigner)

*optional extension.* *not required for assessment.* Do this only after your install guide works: one chat and the smoke test. You can skip it, or swap in another program. External software and MCP servers here are examples. Why: [install why](../01-harness-and-agents/install-why.md).

An MCP is a connector that lets Hermes talk to another program. Read the permissions and capability rule first: [what is mcp](what-is-mcp.md#permissions-and-capability-boundary). The safety rules for all installs: [safe install rules](../05-security-and-privacy/howto-hermes-safe-install-rules.md).

- Windows example: vvvv, a live visual programming environment. It needs Git for Windows, Node.js 22.20 or later, and a .NET SDK. Those installers can ask for UAC. Only these installers may ask for it: the .NET SDK (system-wide, needs administrator rights) and Git for Windows. Node.js: not verified. Read the UAC window. It must show a verified publisher. Click Yes for that one installer, then close it and go back to your normal terminal. Details: [safe install rules](../05-security-and-privacy/howto-hermes-safe-install-rules.md#windows-details).
- macOS example: TouchDesigner. It is used only because the official project is real and current.
- Linux: no example here.

## Windows example: vvvv and vvvv MCP

### vvvv

1. If you want the live editor, install current vvvv gamma from https://vvvv.org
2. You can install the MCP below without vvvv. The vvvv MCP README says: "Works **without a vvvv installation** for all knowledge, search, read, and generate tools." Source: https://github.com/digitalwannabe/vvvv-mcp#readme

### vvvv skills

Skills are instruction files the agent loads for one kind of work. The vvvv skills repo is https://github.com/tebjan/vvvv-skills

The README's recommended install is:

```bash
npx skills add tebjan/vvvv-skills
```

That command needs Node.js 22.20 or later: https://nodejs.org (the `npx skills` README states this version). It also needs Git for Windows for the manual copy below.

The README's manual Windows copy targets Claude Code, not Hermes. Its lines are `cmd` syntax (`%TEMP%`, `xcopy`). They do not work in PowerShell. Source: https://github.com/tebjan/vvvv-skills#manual-installation

The skills tool has an agent name for Hermes. On Windows it may write to `%USERPROFILE%\.hermes\skills`, not to `%LOCALAPPDATA%\hermes\skills`. This is not verified. Use the manual copy for Hermes. Type these lines in Windows Terminal:

```powershell
git clone https://github.com/tebjan/vvvv-skills "$env:TEMP\vvvv-skills"
New-Item -ItemType Directory -Force "$env:LOCALAPPDATA\hermes\skills" | Out-Null
Copy-Item "$env:TEMP\vvvv-skills\skills\*" "$env:LOCALAPPDATA\hermes\skills\" -Recurse
```

Each `SKILL.md` must be one folder down, for example `...\hermes\skills\vvvv-shaders\SKILL.md`. Then type `hermes skills list` and check that the vvvv skills appear.

Do not run the Python patch editor that the `vvvv-fileformat` skill includes. It is not part of this class.

### vvvv MCP

The server is https://github.com/digitalwannabe/vvvv-mcp

The README install, quoted from https://github.com/digitalwannabe/vvvv-mcp#install-end-users :

> Requires [.NET 8 SDK](https://dotnet.microsoft.com/download/dotnet/8.0) or later.

```powershell
dotnet tool install -g vvvv-mcp
vvvv-mcp --setup
```

1. Install the .NET 10 SDK from https://dotnet.microsoft.com/download. The README asks for the .NET 8 SDK or later. .NET 8 left support on 10 Nov 2026. The tool package targets `net8.0`. It is not verified that the tool runs with only .NET 10. If Hermes later reports that .NET 8 is missing, also install the .NET 8 runtime, for class use only.
2. Open a new PowerShell window.
3. Run the first command only: `dotnet tool install -g vvvv-mcp`.
4. Do not run `vvvv-mcp --setup`. The README says it detects Claude Desktop, VS Code, Cursor and Kilo, and writes their config files. Hermes is not on that list. It would change the settings of other programs.
5. Add the server to Hermes by hand. In Windows Terminal, type `notepad "$env:LOCALAPPDATA\hermes\config.yaml"` and press Enter. Add this block. Hermes MCP shape: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp

```yaml
mcp_servers:
  vvvv:
    command: "vvvv-mcp"
    tools:
      include: [search_nodes, get_node_details, list_categories, list_packages, list_knowledge, read_knowledge, search_knowledge, read_patch, explain_patch]
```

   This allows read and search tools only. It leaves out every tool that writes a patch. Two points are not verified: that `command: "vvvv-mcp"` without arguments starts the server, and that these tool names match the current version (they come from the README).
6. Quit Hermes and open it again. Write the tool list in your capability inventory: [what is mcp](what-is-mcp.md#permissions-and-capability-boundary).

Skip the in-editor chat extension. The README marks `VL.MCP.HDE` as an experimental preview. Live tools need that extension. Offline search and patch tools do not.

Student use of vvvv-mcp is non-commercial under its license. Read https://github.com/digitalwannabe/vvvv-mcp/blob/main/LICENSE.md before any paid client work. vvvv itself counts academic research as commercial use. Teaching and learning are free. Source: https://vvvv.org

To undo this example, see step 7 of [safe install rules](../05-security-and-privacy/howto-hermes-safe-install-rules.md#9-rollback-and-uninstall).

## macOS example: TouchDesigner MCP

The example is real. TDMCP is the official TouchDesigner MCP from Derivative. It is in public beta. Checked 20 Nov 2026.

- Repo: https://github.com/TouchDesigner/TDMCP
- Docs: https://docs.derivative.ca/MCP
- Releases: https://github.com/TouchDesigner/TDMCP/releases
- TouchDesigner download: https://derivative.ca/download

The README says the component needs **TouchDesigner 2025.33230 or newer**. Earlier builds will not open it. Quote and version notes: https://github.com/TouchDesigner/TDMCP#start-here

Hermes is not in the README's Install For list. The README says TDMCP "works with any client that speaks streamable-HTTP MCP." The steps below use that HTTP endpoint with Hermes. The endpoint URL is from the README. The YAML shape is from the Hermes MCP page: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp

1. Install TouchDesigner 2025.33230 or newer.
2. Download `TDMCP.tox` from the releases page. Drag it into the root of your project.
3. On the component's MCP page, turn **Active** on.
4. Open the README section linked above. If the localhost URL is not `http://127.0.0.1:13316/mcp`, use the URL from that README. The port here was checked on 20 Nov 2026.
5. Add this block to `~/.hermes/config.yaml`, then restart Hermes:

```yaml
mcp_servers:
  touchdesigner:
    url: "http://127.0.0.1:13316/mcp"
```

6. Ask Hermes what TouchDesigner project it can see.
7. TouchDesigner shows a consent panel. The README says nothing gets control until you allow it there. Click allow only if the panel names your Hermes app.
8. Leave the server on localhost. The README refuses other machines by default. Do not open it to the network.

**Install Skills** on the component is written for the clients in the Install For list. Hermes is not in that list. If the pulse does not place skills in `~/.hermes/skills/`, skip skills. Do not copy the files into a guessed folder.

The server can run Python inside TouchDesigner. Treat that like a shell on your Mac. Security notes from the project: https://github.com/TouchDesigner/TDMCP/blob/main/docs/security.md
