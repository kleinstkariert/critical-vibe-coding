---
title: How-to. Hermes Docker sandbox click-path
date: 2026-11-18
tags:
  - course
  - howto
  - hermes
  - docker
  - sandbox
---

# How-to. Turn on the Hermes Docker sandbox

*reference implementation. Advanced path. Not required for assessment.* This page is one Hermes sandbox example. See [[minimum-path]].

Short click-path only. For Docker concepts, mounts, and generic container flags, use [[Local LLM Coding with Hermes]] (§8 Docker, §9 Sandbox).

Official Nous docs:

- Hermes Docker page: https://hermes-agent.nousresearch.com/docs/user-guide/docker
- Security (container isolation): https://hermes-agent.nousresearch.com/docs/user-guide/security
- Configuration (Docker backend): https://hermes-agent.nousresearch.com/docs/user-guide/configuration

Source types: [[../syllabus/references#source-types]]. A label names the source kind. It is not independent verification. Labels: *technical suggestion*. Check the docs for your Hermes version.

---

## Two Docker jobs

| Job | What it means |
|---|---|
| **Hermes in Docker** | The Hermes process runs inside a container (`/opt/data` mount). See the Docker page above. |
| **Docker terminal backend** | Hermes runs on the host. Agent commands run inside a sandbox container. This note. |

---

## 1. Prerequisites

1. Install Docker for your OS (links in [[Local LLM Coding with Hermes]] §8).
2. Confirm Docker works:

```bash
docker version
```

3. Keep Hermes installed on the host for this path: [[howto-hermes-setup]]

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

Hermes Docker containers apply hard flags such as capability drop and no-new-privileges. Still use a non-root workflow on the host and limited mounts. Details: security docs above.

---

## 4. Approvals

Keep approvals on for dangerous actions while you learn.

Do not set `approvals.mode: off` on a personal laptop unless you understand the risk.

Review the Git diff after agent edits.

Course rules: [[howto-hermes-setup]] §5d · [[Local LLM Coding with Hermes]]

---

## 5. Checklist

- [ ] `docker version` works
- [ ] `terminal.backend` is `docker`
- [ ] Only required folders are mounted
- [ ] Network is off unless the task needs it
- [ ] Approvals stay on for class work
- [ ] Diff reviewed before you accept changes

---

## Sources

- https://hermes-agent.nousresearch.com/docs/user-guide/docker
- https://hermes-agent.nousresearch.com/docs/user-guide/security
- https://hermes-agent.nousresearch.com/docs/user-guide/configuration
- [[Local LLM Coding with Hermes]]
- [[howto-hermes-setup]]
