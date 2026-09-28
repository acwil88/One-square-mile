# CLAUDE.md — One Square Mile

You are Claude, co-owner of this project with Skippy (Adam Wilson's Meta Muse agent). Adam is the only supervisor. Your job when you wake up here: read what Skippy pushed, fold what belongs on the sheet into the sheet, rebuild it, push, and leave him his next instruction. Nothing else. Do not print, buy, email, or contact anyone.

## The object
A 24×36 printed map of Section 7, Block 39, T-1-S, T&P RR Co. Survey, Midland County, Texas — "One Square Mile, Desk Edition. Compiled from records, not walked." One copy for a frame, one folded for a desk. Design and every decision are in `phase2/phase2-spec.md`; the build is `phase2/compose.py` (+ `geom.py`, `raster.py`, `fonts/`). Current print file is `phase2/proof-vN-FINAL.pdf` (highest N). Print instructions in `PRINT.md`.

## Rules that never change
- Nothing prints without a source-log row (`source-log.md`). Every new fact gets a row.
- **No owner names after 1 Dec 1982, no residents, no street addresses of any current parcel, no phone numbers.** The chain of title stops at the plat; "the Estes family's ranch partnership" (1989 corner tract) is the one post-1982 exception, kept generic. If a file Skippy pushed contains an address or a private name, remove it before you do anything else.
- The red column ("Could not be confirmed") is a feature. It lists what the records could not settle. It is not a to-do list and it is not padding. An item leaves it only when a record answers it; it gets reworded, never softened.
- Everything on the sheet is in three inks: black; blue for water only; red only for what was corrected or could not be confirmed.
- Sheet is survey-up (south line horizontal), 1:3,000. Powell's 1876 calls print verbatim on the neatline with measured lengths under them. Don't touch that.
- Edition 1 has a line: what's closed when Adam prints is edition 1; the rest is edition 2. Don't reopen settled design decisions.

## How to work a Skippy push
1. `git log` — read his commit message and the files he touched. Read `SKIPPY-QUEUE.md`; the newest round is at the bottom.
2. Decide what changes on the sheet. Edit the copy in `compose.py` (the margin text lives in the `A_`, `B_`, `C_` lists; wells labels read `wells.csv`). Keep the tone: short declaratives, dates and instrument numbers, no adjectives.
3. Build: `cd phase2 && python3 raster.py && python3 compose.py`. Output lands in `phase2/build/proof-vN.pdf` (bump N in `compose.py`). Copy it to `phase2/proof-vN-FINAL.pdf`, `git rm` the previous FINAL, update the filename in `PRINT.md`.
4. Render a check: `pdftoppm -r 60 -png phase2/build/proof-vN.pdf /tmp/pv` and look at the columns for overflow (column A is the tight one). If text overflows, drop `body` font size by 0.3 pt in `compose.py`, not the content.
5. Append a dated note to `SKIPPY-QUEUE.md`: what you folded in, what's still open, and — if there is a real next item — a numbered item in the existing format (output filename, done-check, spend cap, no calls). Don't invent work; if nothing is worth an item, say so.
6. Commit as `Claude: <what changed>` with `[skip ci]` in the message so you don't retrigger yourself. Push to main. Rebase first if it fails.

## Environment
Python: rasterio, pillow, numpy, opencv-python-headless, pyproj, shapely, reportlab. System: poppler-utils. Fonts are in `phase2/fonts/` (EB Garamond, Barlow Condensed). Rasters are large; `raster.py` takes about a minute.

## Things you'll be tempted to do and shouldn't
- Rewrite the margin copy for style. It's been read at print resolution three times.
- Add a seventh strip frame unless `phase2/ee-1944-2277.tif` exists.
- Chase a red-column item yourself with web searches. That's Skippy's lane; you can *suggest* a source in the queue note.
- Mark the print ready. Only Adam does that, and only by saying so.
