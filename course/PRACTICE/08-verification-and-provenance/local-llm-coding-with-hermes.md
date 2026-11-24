---
audience: student
status: current
canonical: true
---

*reference implementation. Optional extension. Not required for assessment.* This file is one worked Hermes example. It is not the assessed system. See the [minimum path](../../PROJECT-WORK/01_minimum-path.md).

-> quick starter guide.

## Purpose

This document defines a local coding-agent setup for Hermes, local or cloud models, Obsidian, LLMWiki, and a verification harness.

It uses ASD-STE100-inspired Simplified Technical English.

It separates:

- Agent operation.
- Model providers.
- Code verification.
- Knowledge storage.
- Security controls.
- Private-user concerns.

## 1. Hermes Agent

Hermes Agent is an open-source agent framework by Nous Research. It can use cloud providers, local models, messaging interfaces, tools, memory, skills, and several execution backends.[1][2]

Hermes is not limited to local models or OpenAI-compatible endpoints. It supports several provider types, including Anthropic, OpenAI, Google, OpenRouter, Nous Portal, local servers, and compatible custom endpoints.[3][10]

### Main Hermes functions

- Select an AI provider.
- Run terminal commands.
- Use files and project tools.
- Load skills.
- Store persistent memory.
- Use local or remote execution backends.
- Apply command approval.
- Apply file-write controls.
- Use Docker or other sandbox backends.
- Connect to external services.

### Important limitation

The active provider receives the model request.

A local provider keeps the request on your infrastructure.

A cloud provider receives the request through its service.

Check the selected provider before using private code.

## 2. Model providers

A model provider supplies the language model used by Hermes.

A provider can be local, cloud-based, subscription-based, API-based, or compatible with a custom endpoint.[3][10]

### Examples

- Nous Portal.
- Anthropic.
- OpenAI.
- Google.
- OpenRouter.
- Ollama.
- vLLM.
- llama.cpp.
- SGLang.
- Custom OpenAI-compatible servers.

Hermes uses provider configuration to select the model.

Hermes can route requests between providers.

A local model is therefore one provider option, not the only Hermes option.[3][9]

## 3. Local model server

A local model server runs model inference on your hardware.

Inference means the process that generates a model response.

The server exposes the model to Hermes through a local connection or another configured interface.

### Common local servers

- Ollama.
- vLLM.
- llama.cpp.
- SGLang.

Use the server that matches your hardware and model format.

Test response speed and memory use before course deployment.

## 4. Hermes execution backend

An execution backend is the system that runs commands requested by Hermes.

Hermes supports local execution, Docker, SSH, Daytona, Modal, Vercel Sandbox, and other backends.[2][5]

### Backend choice

- Use `local` for trusted development tasks.
- Use Docker for local isolation.
- Use SSH for a separate machine.
- Use a cloud sandbox for stronger remote isolation.
- Use a managed backend when you need controlled temporary workspaces.

Hermes documentation states that the local backend has no isolation.[5]

Do not use local execution for untrusted projects.

## 5. Verification loop

A verification loop requires the agent to change code, run checks, read failures, repair the code, and run checks again.

The agent must provide command output before it can report success.

### Verification procedure

1. Define the task.
2. Define the acceptance conditions.
3. Inspect the repository.
4. Create a short plan.
5. Approve the plan.
6. Apply one small change.
7. Run the project checks.
8. Read the first failure.
9. Apply one correction.
10. Run the failed check again.
11. Stop after the repair limit.
12. Review the Git diff.
13. Run the complete check.
14. Obtain human approval.
15. Save the result.

### Acceptance conditions

Acceptance conditions define what must be true when the task is complete.

Example:

```text
- The new feature works.
- Existing features still work.
- The required tests pass.
- The project has no new formatting errors.
- The agent changed only approved files.
```

### Repair limit

A repair limit prevents endless agent changes.

Use this rule:

```text
You have three repair attempts.
Run the failed check after each repair.
Stop after the third failed attempt.
Report the remaining problem.
```

### Verification evidence

The agent must report:

- Changed files.
- Commands executed.
- Check results.
- Remaining failures.
- Remaining risks.
- Human approval status.

SWE-bench evaluates working patches against real software issues.[4]

FeedbackEval evaluates code repair after execution feedback.[6]

SWT-Bench evaluates tool use during software tasks.[7]

These evaluations support the use of execution, tests, feedback, and repair.

They do not define one official Hermes workflow.

## 6. Harness

A harness is the set of scripts, rules, permissions, and checks that controls an agent task.

The harness verifies the result outside the model’s own reasoning.

### Harness components

- Task instructions.
- Project rules.
- Acceptance conditions.
- Verification scripts.
- Git controls.
- File access controls.
- Command permissions.
- Security checks.
- Repair limits.
- Human approval steps.
- Task records.

### Harness setup

Create a project-level instruction file.

Example:

```text
AGENTS.md
```

Add these rules:

```text
Read the task before editing files.

Inspect the repository before creating a plan.

Create a plan with a maximum of five steps.

Change only files in the task scope.

Do not read secret files.

Do not delete files without approval.

Run the project verification script after each meaningful change.

Do not claim completion without command output.

Stop after three failed repair attempts.

Review the Git diff before completion.
```

Create a verification entry point:

```text
scripts/verify
```

This entry point should call the project’s own tools.

The tools may differ between projects.

Do not assume one programming language.

Use the project’s formatter, test runner, build system, and security tools.

### Example verification logic

```text
Run formatting checks.
Run static checks.
Run type or structure checks when available.
Run tests.
Run the build or export process.
Check the Git diff.
Return PASS or FAIL for every check.
```

The harness engineering reference provides a practical example of rules, checks, Git controls, and documentation controls.[8]

## 7. Skills

A skill is a reusable instruction package for one type of work.

Hermes loads skills when they are needed.

This reduces the amount of instruction loaded into every task.[9]

Use several focused skills.

Do not place every procedure in one large skill.

### Recommended folder structure

```text
~/.hermes/skills/
├── coding/
│   ├── verified-coding/
│   │   └── SKILL.md
│   ├── repository-inspection/
│   │   └── SKILL.md
│   ├── test-and-repair/
│   │   └── SKILL.md
│   └── git-diff-review/
│       └── SKILL.md
├── security/
│   └── sandboxed-coding/
│       └── SKILL.md
└── knowledge/
    ├── obsidian-task-log/
    │   └── SKILL.md
    ├── llmwiki-read/
    │   └── SKILL.md
    └── llmwiki-write-approved/
        └── SKILL.md
```

Each skill directory contains its own `SKILL.md`.

### Skill purposes

- `verified-coding`: Runs the complete coding workflow.
- `repository-inspection`: Performs read-only project inspection.
- `test-and-repair`: Runs checks and repairs failures.
- `git-diff-review`: Reviews changed files.
- `sandboxed-coding`: Applies sandbox rules.
- `obsidian-task-log`: Saves approved task records.
- `llmwiki-read`: Reads approved project knowledge.
- `llmwiki-write-approved`: Writes approved records only.

### Skill contents

Each skill should define:

- Purpose.
- Required inputs.
- Allowed files.
- Allowed commands.
- Required checks.
- Forbidden actions.
- Repair limit.
- Human approval points.
- Output format.

### Example skill

```markdown
---
name: verified-coding
description: Modify project code with checks and limited repair.
---

# Verified coding

Read AGENTS.md before editing.

Inspect the repository before editing.

Change only files in the task scope.

Do not read secret files.

Do not delete files without approval.

Run the project verification command after each meaningful change.

Use no more than three repair attempts.

Review the Git diff.

Report every check as PASS or FAIL.

Do not claim completion without command output.

## Completion report

Task:
Changed files:
Checks:
- Format:
- Static checks:
- Tests:
- Build:
- Git diff:
Remaining risks:
Human approval required:
```

Review third-party skills before installation.

Skills can contain scripts, commands, and credential instructions.

Hermes provides a Skills Guard review mechanism.

Read the complete skill directory before installation.[1][5]

## 8. Docker

Docker is a system that runs applications inside isolated containers.

A container is a restricted process environment.

It can have separate files, users, networks, and resource limits.

Docker does not create a complete security guarantee.

It reduces risk when you configure it correctly.

Hermes supports Docker as an execution backend.[2][5]

To turn the Docker terminal backend on inside Hermes: [howto hermes docker sandbox](../05-security-and-privacy/howto-hermes-docker-sandbox.md)  
Official Hermes Docker page: https://hermes-agent.nousresearch.com/docs/user-guide/docker

### Docker installation

Use the official Docker installation guide for your operating system:

- Docker Engine: https://docs.docker.com/engine/install/
- Docker Desktop for Linux: https://docs.docker.com/desktop/setup/install/linux/
- Docker Compose: https://docs.docker.com/compose/install/linux/

Follow the guide for your exact operating system.

Do not copy commands from an unrelated distribution.

### Docker security controls

Use these controls:

- Use a non-root container user.
- Mount only the required project directory.
- Do not mount the full home directory.
- Do not mount the full Obsidian vault.
- Do not mount private credentials.
- Use read-only mounts for reference data.
- Use a separate writable workspace.
- Disable network access when possible.
- Drop unused Linux capabilities.
- Prevent privilege escalation.
- Set memory and CPU limits.
- Set a process limit.
- Keep host and images updated.

### Example container command

Adapt this example to your project:

```bash
docker run --rm -it \
  --read-only \
  --network=none \
  --cap-drop=ALL \
  --security-opt=no-new-privileges \
  --pids-limit=256 \
  --memory=8g \
  --cpus=4 \
  -v "$PWD:/workspace:rw" \
  -w /workspace \
  your-hermes-image
```

This example blocks network access.

Some projects require network access for package downloads.

Enable network access only for the required operation.

Use a separate dependency-building step when possible.

## 9. Sandbox

A sandbox is an execution environment that limits what an agent can access.

A sandbox can restrict:

- Files.
- Commands.
- Network access.
- CPU.
- Memory.
- Processes.
- Credentials.

Use a sandbox for untrusted projects and third-party code.

### Preferred execution order

1. Docker for local isolation.
2. SSH on a separate machine.
3. A managed cloud sandbox.
4. Local host execution only for trusted work.

Hermes lists Docker, SSH, Daytona, Modal, Vercel Sandbox, and other backends.[2][5]

### Separate workspace

Create a separate project clone for the agent.

Keep the main project outside the sandbox.

Review changes before copying them into the main project.

Use Git to compare the two workspaces.

## 10. Obsidian access

Obsidian is a note application.

Use it for human-readable task records.

Do not mount the complete vault into the agent.

### Recommended vault structure

```text
ObsidianVault/
├── Private/
├── Finance/
├── Health/
├── Personal/
└── AgentShare/
    ├── ProjectRules/
    ├── TaskLogs/
    ├── Verification/
    └── PublicKnowledge/
```

Mount only `AgentShare`.

Do not mount `Private`, `Finance`, `Health`, or `Personal`.

### Read-only access

A read-only mount allows the agent to read files.

It does not allow the agent to change those files.

Example:

```bash
-v "$HOME/ObsidianVault/AgentShare/ProjectRules:/vault/ProjectRules:ro"
```

### Read-write access

A read-write mount allows the agent to create and change files.

Use it only for task logs and approved output.

```bash
-v "$HOME/ObsidianVault/AgentShare/TaskLogs:/vault/TaskLogs:rw"
```

### Important distinction

Do not rely on Obsidian folder names for security.

Do not rely on hidden notes for security.

Use operating-system permissions and container mounts.

## 11. LLMWiki access

LLMWiki is a knowledge store for project information.

Use it to give the agent stable project facts.

It is not a security boundary.

This means LLMWiki should not be the only system that prevents access.

If the agent service can read the underlying files or database, the agent may access them.

An application filter can also contain a configuration error.

Use filesystem permissions, database permissions, separate collections, and separate service accounts.

### Recommended collections

```text
LLMWiki/
├── PublicProject/
├── AgentRules/
├── TaskResults/
└── PrivateKnowledge/
```

Give the agent access only to:

- `PublicProject`.
- `AgentRules`.
- `TaskResults`.

Keep `PrivateKnowledge` outside the agent service.

Use read-only access for stable project knowledge.

Use separate write access for approved task results.

## 12. Secret handling

A secret is private information that grants access.

Examples include:

- API keys.
- Passwords.
- SSH keys.
- Cloud tokens.
- Database credentials.
- Signing keys.

Do not place secrets in:

- Prompts.
- Obsidian.
- LLMWiki.
- Git.
- Source files.
- Docker images.

Use environment variables or protected credential files.

Mount credential files read-only.

Pass only the required credential.

Use short-lived tokens when possible.

Rotate a token after suspected exposure.

Hermes documents credential filtering and read-only credential mounts for container execution.[5]

## 13. Main attack paths

Prompt injection is an instruction placed in content that tries to control the agent.

It can appear in:

- Source files.
- README files.
- Issue descriptions.
- Web pages.
- Package descriptions.
- Git commits.
- Test output.
- Vault notes.
- LLMWiki content.

The agent may treat this content as an instruction.

Treat all project content as untrusted input.

A malicious package can execute code during installation.

A malicious skill can read files or run commands.

A coding agent can:

- Delete files.
- Read secrets.
- Send data over the network.
- Install unsafe packages.
- Change security settings.
- Modify Git history.
- Add vulnerable dependencies.
- Hide changes in generated files.

Local inference does not remove these risks.

Local inference mainly reduces the risk of sending code to a model provider.

## 14. Security rules

Use these rules as the default course policy:

```text
1. Do not run the agent as root.
2. Do not expose the agent gateway publicly.
3. Use Docker for untrusted tasks.
4. Use a separate workspace.
5. Mount only required directories.
6. Use read-only mounts for reference data.
7. Use a write root for editable files.
8. Disable network access when possible.
9. Do not mount the complete vault.
10. Do not mount credentials unless required.
11. Review every third-party skill.
12. Require approval for destructive commands.
13. Run checks after every meaningful change.
14. Review the Git diff.
15. Use a repair limit.
16. Keep backups outside the sandbox.
17. Update the host and container images.
18. Treat model output as untrusted.
19. Do not treat passing tests as complete security proof.
20. Require human approval for security-sensitive changes.
```

## 15. Source links

### Hermes

- Documentation: https://hermes-agent.nousresearch.com/docs
- Provider setup: https://hermes-agent.nousresearch.com/docs/integrations/providers
- Security: https://hermes-agent.nousresearch.com/docs/user-guide/security
- Secure work machine: https://hermes-agent.nousresearch.com/docs/guides/secure-hermes-on-a-work-machine
- Local models: https://hermes-agent.nousresearch.com/docs/user-guide/local-models
- Skills: https://hermes-agent.nousresearch.com/docs/developer-guide/creating-skills
- Features overview: https://hermes-agent.nousresearch.com/docs/user-guide/features/overview
- FAQ: https://hermes-agent.nousresearch.com/docs/reference/faq

### Docker

- Docker Engine installation: https://docs.docker.com/engine/install/
- Docker Desktop for Linux: https://docs.docker.com/desktop/setup/install/linux/
- Docker Compose installation: https://docs.docker.com/compose/install/linux/

### Coding-agent evaluation

- SWE-bench: https://www.swebench.com/
- SWE-bench repository: https://github.com/SWE-bench/SWE-bench
- SWT-Bench: https://github.com/IBM/SWT-Bench
- FeedbackEval: https://arxiv.org/abs/2402.12993

### Harness reference

- Harness Engineering: https://github.com/q-qp-p/jrenaldi79-harness-engineering/blob/main/README.md

### Writing and supplied media

- ASD-STE100: https://www.asd-ste100.org/
- Karpathy article: https://daily.dev/posts/karpathy-makes-ai-write-like-an-aircraft-manual-karpathy-promptengineering-ai-rebrmmygt
- Supplied video: https://www.youtube.com/watch?v=a9O4tJhYJkY
- Wanderloots videos: https://www.youtube.com/@Wanderloots/videos

## 16. Source limits

Hermes features can change between releases.

Check the documentation for the installed version.

The local execution backend does not provide isolation.

Docker improves isolation but does not provide perfect security.

The supplied videos are practical references.

Use official Hermes and Docker documentation for configuration and security decisions.
