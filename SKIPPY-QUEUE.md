# Skippy — work queue (owner: Claude; arbiter: Adam)

Single source of truth for what Claude needs from you. Work top to bottom. Each item has a done-check. Push each output as it finishes; append a line to `source-log.md` for anything new. Mark an item `[x]` here when its done-check passes, `[!]` with a one-line reason if blocked. Standing rules unchanged: no calls, no emails, nothing in the repo that couldn't print.

## 1. Midland Draw geometry  `[ ]`
Pull the NHDPlus flowlines for COMID 5688042 and every connected reach within the NAIP frame extent (see `phase2/claude-reply-2026-09-26.md` §2 for the frame). Output `phase2/midland-draw-2277.geojson`, LineString(s), EPSG:2277, properties `comid`, `gnis_name` (may be null), `reachcode`.
**Done when:** the file loads, at least one line crosses the section polygon, and the source-log row cites the WATERS/NHDPlus service URL.

## 2. Wells reconciliation  `[ ]`
(a) `wells.csv` lacks API 42-329-47554 (Well 1MS, east line) that source-log row 24 reported. Either add it with coordinates or state in `phase2/wells-notes.md` why row 24 was wrong.
(b) Three APIs inside the section carry prefix 42-317 (Martin County). In `wells-notes.md`, explain (RRC assigns API county by ___) or say it could not be explained. No guessing — if RRC's own documentation doesn't say, write "not explained."
**Done when:** `wells-notes.md` exists with both answers and `wells.csv` is consistent with it.

## 3. Aerial alignment, 1974 → 1965 → 1954  `[ ]`
Method in `phase2/alignment-status-2026-09-27.md`. Reference is `phase2/ee-1984-2277.tif`. Outputs per frame: `phase2/ee-YYYY-2277.tif` (NAIP grid, EPSG:2277, deflate), `ee-YYYY-2277-preview.png`, `ee-YYYY-alignment.md` (GCPs used, transform, residuals, error estimate). Accept ±300 ft.
**Done when:** a checkerboard against 1984 shows section-line roads continuing across tiles, and the .md states the error. Do 1974 first; if 1954 (1:63,000) won't align to better than ±500 ft, deliver it labeled "approximate" rather than skipping it.

## 4. Print quote  `[ ]`
Web only. Find two Midland-area plotter/blueprint shops that print 24×36 single-sheet color on heavy bond (28# or better), with published or listed prices. Output `phase2/print-quotes.md`: shop, address, price for one sheet, paper options, turnaround, whether they take an emailed PDF. Do not contact them.
**Done when:** two rows with prices, or a note that prices aren't published and the listed phone/email for Adam to use.

## 5. Source-log hygiene  `[ ]`
Every file in `phase2/` should be traceable to a row. Add rows for anything missing.
**Done when:** `grep` of each phase2 filename hits the log.

---
Claude's side, for reference (not yours): compose proof v2 from 1–3, print spec, one message to Adam.
Older instructions in `phase2/claude-reply-2026-09-26.md`, `alignment-status-2026-09-27.md`, and `proof-v1-notes.md` are superseded by this file where they overlap.
