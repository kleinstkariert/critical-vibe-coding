---
title: Verification
status: current
canonical: true
---

# Verification

[Minimum path](01_minimum-path.md) asks for a verification method: how you check that the result is right. A method can be small. A test command is one. A careful human read is another. Comparing the result with the source is a third.

Write your method on one page. Use the [template](../templates/verification-plan.md). Fill it in for each kind of task. It asks seven questions: which task the check covers, which check, who runs it, what counts as a pass, what evidence you keep, how many repairs the agent may try, and who approves before the work is shared.

## Rules the course uses

- **Repair limit.** Run the failed check after each repair. Stop after three failed repair attempts on the same check. Then change the plan or ask a person. See [howto hermes efficient coding](../PRACTICE/01-harness-and-agents/howto-hermes-efficient-coding.md#3-verification-entry-point).
- **Human approval.** For shared work, a person approves before anything is pushed or published.
- **Report the result.** End each task with a short report: task, changed files, checks (PASS or FAIL), remaining risks, approval needed. The format is in the [AGENTS.md template](../PRACTICE/01-harness-and-agents/agents-md-template.md).
- **A wrong answer is not only a model fault.** Lint finds problems in your notes. It does not prove the model was right. See [what is lint](../PRACTICE/02-knowledge-bases/what-is-lint.md).

## Where to go deeper

- The full verification loop, acceptance conditions and evidence: [Local LLM Coding with Hermes](../PRACTICE/08-verification-and-provenance/local-llm-coding-with-hermes.md#5-verification-loop)
- The record of each check goes in the log: [provenance and process log](03_provenance.md)
