# Session 02 slideshow (Obsidian Slides)

Markdown deck for the Obsidian **core Slides** plugin (`---` between slides), with vault CSS for readable sizing.

| File | Role |
|---|---|
| `02-agent-harness-and-hermes.md` | Teaching deck (Command Palette → **Start presentation**) |
| `cvc-slides.css` | Reveal.js styles: copy to vault `.obsidian/snippets/cvc-slides.css` and enable under Appearance → CSS snippets |

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

Session plan: [[../../sessions/02-agent-harness-and-wiki-architecture]]  
Install: [[../../setup/howto-hermes-setup]] · Efficient coding: [[../../setup/howto-hermes-efficient-coding]]  
Plugin help: https://obsidian.md/help/plugins/slides
