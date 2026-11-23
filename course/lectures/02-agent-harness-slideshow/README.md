---
audience: student
status: current
canonical: true
---

# Session 02 slideshow (Obsidian Slides)

*reference implementation.* The Hermes steps in this deck are one worked example. They are an *optional extension*. They are *not required for assessment*. See [minimum path](../../minimum-path.md).

Markdown deck for the Obsidian **core Slides** plugin (`---` between slides), with vault CSS for readable sizing.

| File | Role |
|---|---|
| `02-agent-harness-and-hermes.md` | Teaching deck: day timeline + Hermes setup (Command Palette → **Start presentation**) |
| `cvc-slides.css` | Reveal.js styles: copy to vault `.obsidian/snippets/cvc-slides.css` and enable under Appearance → CSS snippets |

Comparison concept (not a deck): [hermes vs coding agents](../../concepts/hermes-vs-coding-agents.md)  
OpenCode: [howto opencode setup](../../setup/howto-opencode-setup.md) · [howto hermes opencode pairing](../../setup/howto-hermes-opencode-pairing.md)

## Font size (master knob)

Obsidian Slides uses reveal.js. Default scale is too large (~2.5em) and clips tables.

1. Put `cvc-slides.css` in: `Vault/.obsidian/snippets/cvc-slides.css`
2. Settings → Appearance → CSS snippets → enable **cvc-slides**
3. Edit the master scale in that file:

```css
.reveal {
  font-size: 32px; /* body ~28–36px; raise/lower this one number */
}
.reveal h1 {
  font-size: 1.35em; /* relative to .reveal */
}
.reveal table {
  font-size: 0.72em;
}
```

`cssclasses` on the note do **not** style the presentation view. Use the vault snippet.

Session plan: [02 agent harness and wiki architecture](../../SESSIONS/02-agent-harness-and-wiki-architecture.md)  
Install: [howto hermes setup](../../setup/howto-hermes-setup.md) · Efficient coding: [howto hermes efficient coding](../../setup/howto-hermes-efficient-coding.md)  
Plugin help: https://obsidian.md/help/plugins/slides
