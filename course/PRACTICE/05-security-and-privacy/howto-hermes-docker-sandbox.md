---
title: How-to. Hermes Docker sandbox click-path
date: 2026-11-18
tags:
  - course
  - howto
  - hermes
  - docker
  - sandbox
status: current
canonical: true
---

# How-to. Turn on the Hermes Docker sandbox

*reference implementation. Advanced path. Not required for assessment.* This page is one Hermes sandbox example. See [minimum path](../../PROJECT-WORK/01_minimum-path.md).

This page is an advanced safety module. Use it as a demonstration or in a separate workshop. It is not the novice baseline.

The novice baseline is read-only inspection first, a disposable project, command approvals (the default mode is `smart`; type `hermes config set approvals.mode manual` to be asked every time), a Git or filesystem snapshot before write tasks (Hermes writes files without asking), a narrow work folder as a habit, and no private vault. Those steps are in [safe install rules](howto-hermes-safe-install-rules.md) and in section 6 of [install windows](../01-harness-and-agents/install-windows.md), [install linux](../01-harness-and-agents/install-linux.md), and [install mac](../01-harness-and-agents/install-mac.md).

Docker adds filesystem sharing, path translation, ownership, network, performance, GPU access, images, and Windows/macOS virtualisation, so it is not the two-hour baseline.

Privileges for Docker itself, from the Docker docs (checked 25 Nov 2026):

- Windows: Docker Desktop has a per-user install that needs no administrator rights, and an all-users install that does. Some settings marked "Requires password" still ask for UAC. Enabling WSL 2 for the first time needs administrator rights. Membership of the `docker-users` group is equal to administrator rights on the host. Source: https://docs.docker.com/desktop/setup/install/windows-install
- Linux: the `docker` group gives root-level privileges to its members. Source: https://docs.docker.com/engine/install/linux-postinstall/
- macOS: not verified.

Short click-path only. For Docker concepts, mounts, and generic container flags, use [Local LLM Coding with Hermes](../08-verification-and-provenance/local-llm-coding-with-hermes.md) (§8 Docker, §9 Sandbox).

Official Nous docs:

- Hermes Docker page: https://hermes-agent.nousresearch.com/docs/user-guide/docker
- Security (container isolation): https://hermes-agent.nousresearch.com/docs/user-guide/security
- Configuration (Docker backend): https://hermes-agent.nousresearch.com/docs/user-guide/configuration

Source types: [references](../../REFERENCES/bibliography.md#source-types). A label names the source kind. It is not independent verification. Labels: *technical suggestion*. Check the docs for your Hermes version.

---

## Two Docker jobs

| Job | What it means |
|---|---|
| **Hermes in Docker** | The Hermes process runs inside a container (`/opt/data` mount). See the Docker page above. |
| **Docker terminal backend** | Hermes runs on the host. Agent commands run inside a sandbox container. This note. |

---

## 1. Prerequisites

1. Install Docker for your OS (links in [Local LLM Coding with Hermes](../08-verification-and-provenance/local-llm-coding-with-hermes.md) §8).
2. Confirm Docker works:

```bash
docker version
```

3. Keep Hermes installed on the host for this path: [howto hermes setup](../01-harness-and-agents/howto-hermes-setup.md)

---

## 2. Turn on the Docker backend

Fast path (*institutional summary* from Hermes configuration docs):

```bash
hermes config set terminal.backend docker
```

Or edit `~/.hermes/config.yaml` (Windows: under the Hermes data home):

```yaml
terminal:
  backend: docker
```

Optional Desktop / setup UI: use the terminal / backend picker if your build shows it (`hermes setup` paths). Prefer the command above when unsure.

Check:

```bash
hermes config get terminal.backend
```

If Docker fails, fix Docker or switch back:

```bash
hermes config set terminal.backend local
```

---

## 3. Mount, network, user

Keep the workspace small. Do not mount the full home directory or private vault folders.

Useful keys (*institutional summary* from Hermes docs; names can change by version):

| Goal | Config idea |
|---|---|
| Mount the project folder into `/workspace` | `terminal.docker_mount_cwd_to_workspace: true` |
| Air-gap agent commands | `terminal.docker_network: false` |
| Fresh container per session | `terminal.container_persistent: false` |
| CPU / memory caps | `terminal.container_cpu` / `terminal.container_memory` |

Example sketch:

```yaml
terminal:
  backend: docker
  docker_mount_cwd_to_workspace: true
  docker_network: false
  container_persistent: true
```

Some tasks need network for package installs. Enable network only for that step.

Hermes Docker containers apply hard flags such as capability drop and no-new-privileges. Still keep the host session unprivileged (no Administrator window on Windows, no root on macOS and Linux) and limit the mounts. Details: security docs above.

---

## 4. Approvals

Hermes asks for approval only before dangerous shell commands. The default mode is `smart`. In `smart`, a helper model approves low-risk commands for you. To be asked every time, type `hermes config set approvals.mode manual`. Hermes does not ask before it writes a file. Docker limits what the container can see. It does not add a prompt for file writes.

Do not set `approvals.mode: off` on a personal laptop unless you understand the risk.

Review the Git diff after agent edits.

Course rules: [howto hermes setup](../01-harness-and-agents/howto-hermes-setup.md) §5d · [Local LLM Coding with Hermes](../08-verification-and-provenance/local-llm-coding-with-hermes.md)

---

## 5. Checklist

- [ ] `docker version` works
- [ ] `terminal.backend` is `docker`
- [ ] Only required folders are mounted
- [ ] Network is off unless the task needs it
- [ ] Approval mode is `manual` or `smart`, not `off`
- [ ] Diff reviewed before you accept changes

---

## Sources

- https://hermes-agent.nousresearch.com/docs/user-guide/docker
- https://hermes-agent.nousresearch.com/docs/user-guide/security
- https://hermes-agent.nousresearch.com/docs/user-guide/configuration
- [Local LLM Coding with Hermes](../08-verification-and-provenance/local-llm-coding-with-hermes.md)
- [howto hermes setup](../01-harness-and-agents/howto-hermes-setup.md)
