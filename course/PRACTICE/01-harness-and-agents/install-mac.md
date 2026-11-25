---
title: Install guide. macOS
date: 2026-11-25
tags:
  - course
  - howto
  - install
  - macos
status: current
canonical: true
---

# Install guide. macOS

Follow this file from top to bottom. Do not open the Windows or Linux guides.

## Before you start

- Hermes Desktop needs an Apple Silicon Mac. An Intel Mac uses the Terminal route in section 1. The macOS version that Hermes needs: not verified.
- Use your normal macOS login account. Hermes needs no root and no `sudo`.
- If macOS asks to let Hermes use Desktop, Documents, Downloads, Full Disk Access or Accessibility, click Don't Allow. The first test needs none of them (not verified).
- Do not point Hermes at your vault in class.
- Safety rules and rollback: [safe install rules](../05-security-and-privacy/howto-hermes-safe-install-rules.md). Why this order: [install why](install-why.md).

## 1. Install Hermes Desktop

Hermes Agent is the program that uses a model to read files and call tools. Hermes Desktop is the app window for that program.

### Apple Silicon

1. Open https://hermes-agent.nousresearch.com/desktop. The host must be `hermes-agent.nousresearch.com`. STOP if it is another host.
2. Download the macOS package. Open the DMG. Copy `Hermes.app` to Applications (or `~/Applications`).
3. Check the app before you open it. Open Terminal. Type `codesign --verify --deep --strict --verbose=2 /Applications/Hermes.app` and press Return. The output must end with `satisfies its Designated Requirement`. Then type `spctl --assess --type execute --verbose /Applications/Hermes.app` and press Return. It must say `accepted` and `source=Notarized Developer ID`. If you used `~/Applications`, change the path. Exact output on a Mac for this course: not verified. STOP if a check fails.
4. Open Hermes. If macOS blocks the app, STOP and run the two checks again. Click Open in Privacy and Security only after both checks pass.
5. Do not run Hermes as root.
6. On first start, choose Basic. "Choose provider later" is fine. You set the key in section 2.

### Intel Mac

There is no Desktop app for this Mac. Use the Terminal install in [advanced Hermes config](howto-hermes-advanced-config.md#macos-and-linux-cli). Then continue with section 2 using `hermes model` if Desktop is not open.

Hermes keeps its files in `~/.hermes/`.

## 2. Add an OpenRouter key

The class default is OpenRouter with a free model. No card is needed for model ids that end in `:free`. Create a key at https://openrouter.ai/settings/keys. Free models: 20 requests a minute and 50 a day. Your prompts may be logged. Use public text only. [Free models](https://openrouter.ai/collections/free-models)

1. In Hermes Desktop, open **Settings**, then **Providers**, then **OpenRouter**.
2. Add your API key. Paste the key. Do not type it in a shell command.
3. Choose a small free model that says it supports tools. A class example is `nvidia/nemotron-3-ultra-550b-a55b:free` (not verified on every build). Tell the teacher the name you chose.

Menu labels: **Settings → Providers → OpenRouter → add API key**. Exact wording on screen is not verified. Other providers, cards, and limits: [providers and keys](howto-hermes-providers-and-keys.md). Terminal or `.env` file: that page only.

Do not put the key in the vault, in chat, or in Git. Why, and what to do after a leak: [safe install rules](../05-security-and-privacy/howto-hermes-safe-install-rules.md#5-secrets).

## 3. First chat and smoke test

This test checks that the free OpenRouter model answers in chat. Do not point Hermes at your vault.

1. Set the main model to `nvidia/nemotron-3-ultra-550b-a55b:free` (or the free OpenRouter NVIDIA model you chose in section 2).
2. Open a new chat in Hermes.
3. Send this short prompt: Reply with one short sentence that says you work.
4. Expect a short reply. You are done for class when you get one.

STOP if Hermes names your vault or starts reading folders you did not ask for. Tell the teacher.

## Next steps (advanced)

One short line each. Do these at home, or when the teacher says so.

- Local models: [howto local models](../03-models-and-providers/howto-local-models.md)
- Obsidian and phone sync: [howto obsidian setup and sync](../02-knowledge-bases/howto-obsidian-setup-and-sync.md)
- MCP examples (TouchDesigner): [howto example mcp servers](../06-mcp-and-tools/howto-example-mcp-servers.md)
- Docker sandbox: [howto hermes docker sandbox](../05-security-and-privacy/howto-hermes-docker-sandbox.md)
- Efficient coding harness: [howto hermes efficient coding](howto-hermes-efficient-coding.md)
- CLI install, vault paths, skills, gateway; optional later file write test (not the vault): [advanced Hermes config](howto-hermes-advanced-config.md)
- Providers and keys (all rows, `.env`): [providers and keys](howto-hermes-providers-and-keys.md)
- Uninstall and rollback: [safe install rules](../05-security-and-privacy/howto-hermes-safe-install-rules.md#9-rollback-and-uninstall)
- Why this order: [install why](install-why.md)
