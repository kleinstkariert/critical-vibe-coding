"""Insert image-only slides after named headings. Does not edit existing prose."""
from pathlib import Path

deck = Path(__file__).resolve().parents[1] / "02-agent-harness-and-hermes.md"
text = deck.read_text(encoding="utf-8")
lines = text.splitlines(keepends=True)

# After heading title (exact match on stripped line), insert these wikilinks
# as new slides immediately after that slide's trailing --- separator.
# Filenames only: Obsidian resolves unique names in the vault.
INSERT_AFTER = [
    ("# Session 02", ["01-hermes-terminal-banner.svg"]),
    ("# Critical Vibe Coding", ["02-user-agent-tools-result.svg"]),
    ("# What is a harness?", ["03-harness-model-plus-parts.svg"]),
    ("# Thin harness vs thick harness", ["04-thin-vs-thick.svg"]),
    ("# Harness design", ["05-goal-context-action-verification.svg"]),
    ("# Suggested harness flow", ["06-suggested-harness-actors.svg"]),
    ("# Why structure matters", ["07-bigger-model-vs-context.svg"]),
    ("# LLM Wiki", ["08-llm-wiki-tree.svg"]),
    ("# Obsidian and the LLM Wiki", ["09-obsidian-note-beside-folders.svg"]),
    ("# Hermes", ["22-hermes-mark.svg"]),
    ("# Skills", ["15-skills-folders.svg"]),
    ("# Security: local is not enough", ["16-security-allowed-blocked.svg"]),
    ("# Docker sandbox", ["17-docker-sandbox-boundary.svg"]),
    ("# Where Hermes can run", ["13-hermes-run-locations.svg"]),
    (
        "# Run location: Hermes Cloud / hosted agent",
        ["14-hermes-model-different-machines.svg"],
    ),
    (
        "# What models exist",
        [
            "10-cloud-laptop-internet-provider.svg",
            "11-hosted-open-weight.svg",
            "12-local-laptop-model.svg",
        ],
    ),
    ("# Local models in Hermes", ["18-local-gpu-model-hermes.svg"]),
    ("# Subscription / API key", ["19-cloud-key-secret-store.svg"]),
    ("# Install order", ["20-smoke-test-folder.svg"]),
    ("# Practical · Homework", ["21-full-system.svg"]),
]


def find_heading_index(lines, heading):
    for i, line in enumerate(lines):
        if line.strip() == heading:
            return i
    return None


def find_slide_end_separator(lines, start_idx):
    """Return index of the --- that ends the slide starting at start_idx."""
    for i in range(start_idx + 1, len(lines)):
        if lines[i].strip() == "---":
            return i
    return None


# Process from bottom to top so indices stay valid
ordered = []
for heading, imgs in INSERT_AFTER:
    idx = find_heading_index(lines, heading)
    if idx is None:
        print("SKIP missing heading:", heading)
        continue
    sep = find_slide_end_separator(lines, idx)
    if sep is None:
        print("SKIP no separator after:", heading)
        continue
    ordered.append((sep, heading, imgs))

ordered.sort(key=lambda t: t[0], reverse=True)

inserted = 0
for sep, heading, imgs in ordered:
    block_parts = []
    for img in imgs:
        block_parts.append("\n")
        block_parts.append(f"![[{img}]]\n")
        block_parts.append("\n")
        block_parts.append("---\n")
        inserted += 1
    block = "".join(block_parts)
    # Insert after the separator line
    lines.insert(sep + 1, block)
    print(f"OK after {heading}: {len(imgs)} image slide(s)")

deck.write_text("".join(lines), encoding="utf-8")
print("INSERTED", inserted)
