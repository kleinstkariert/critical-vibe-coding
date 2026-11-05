# Session 01 — Welcome & landscape slideshow

Impress deck for Part B. **Deck + images only** — see [`NOTES.md`](NOTES.md) for pointers to lecture prose, session plan, visions script, and un/learn notes (do not duplicate those sources here).

Visual direction: Scandinavian-minimal (cool neutrals, whitespace, restrained type). Tone: serious, lecture-faithful.

| File | Role |
|---|---|
| `01-welcome-landscape.odp` | LibreOffice Impress (primary) |
| `01-welcome-landscape.pptx` | PowerPoint export (same content) |
| `images/` | Slide photographs + `ATTRIBUTION.md` |
| `images/11-gw-ranch-heise.jpg` | Hero ecology / scale beat (Heise / GW Ranch) |
| `build_deck.py` | Regenerates the PPTX from this folder’s images |
| `NOTES.md` | Thin links to canonical sources elsewhere |

Style: [`../../presentation-style.md`](../../presentation-style.md). Argument lives in speaker notes; slides stay sparse.

Rebuild:

```text
python course/lectures/01-welcome-landscape-slideshow/build_deck.py
"C:\Program Files\LibreOffice\program\soffice.exe" --headless --convert-to odp --outdir course/lectures/01-welcome-landscape-slideshow course/lectures/01-welcome-landscape-slideshow/01-welcome-landscape.pptx
```
