---
status: current
canonical: true
---

# Session 01: Welcome and landscape slideshow

Impress deck for Part B. This folder holds the **deck and images only**. Lecture notes, deep dives and research live elsewhere; see [`NOTES.md`](NOTES.md).

## Design

- Text slides: white text on black. Slide title = lecture block title, then the beat, then up to six plain lines with bold labels where they help, an optional question to the room, and a one-line source.
- Image slides are full screen with one small credit line at the bottom (11 pt): who made it, where, photo or rendering. Course charts carry their source inside the image. Images appear only where they carry the beat.
- One exception: the hype-cycle slide shows the curve next to its explanation, because the curve means nothing without the phase names.
- No rules, underlines, underscores or shadows. Scandinavian minimal: sparse, calm, readable.
- Arguments, labels (*unverified lead* / *claim*) and full image credits are in the speaker notes. No separate credits slide.
- The lecturer's edit of 11 Nov 2026 (52 slides) is the base file. `patch_lecturer_edit.py` adds only the review changes on top of it (56 slides). The lecturer's bullets, wording, links and pages stay as left.

| File | Role |
|---|---|
| `01-welcome-landscape.pptx` | Current teaching deck (PowerPoint; edit this) |
| `01-welcome-landscape.odp` | LibreOffice Impress export of the same deck |
| `images/` | Slide images and `ATTRIBUTION.md` |
| `patch_lecturer_edit.py` | Historical rebuild helper. Needs local base/donor copies; not required for teaching |
| `build_deck.py` | Old generator. Do not run it over the deck: it rebuilds every slide and drops manual edits |
| `make_images.py` | Regenerates course charts. Pass function names to run only some |
| `NOTES.md` | Links to canonical sources and the slide map |

Only the current `.pptx` / `.odp` pair is tracked. Older builds stay off git (local backup only).

Rebuild images (run from the repository root). `make_images.py` needs network access and `xlrd` for Shiller's spreadsheet:

```text
python course/SESSIONS/lectures/01-welcome-landscape-slideshow/make_images.py
```

To refresh the `.odp` from the `.pptx` after hand edits:

```text
soffice --headless -env:UserInstallation=file:///C:/path/to/lo-profile --convert-to odp --outdir course/SESSIONS/lectures/01-welcome-landscape-slideshow course/SESSIONS/lectures/01-welcome-landscape-slideshow/01-welcome-landscape.pptx
```

The separate `-env:UserInstallation` profile lets the conversion run while Impress is open. If Impress has the deck open, close it without saving before converting, or edits made there will fight the export.
