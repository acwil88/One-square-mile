# Proof v1 — 2026-09-27

`proof-v1.pdf` — 24 × 36 in, one page, fonts embedded. Built by `compose.py` (+ `geom.py`, `raster.py`, `fonts/`) from the repo assets; re-runnable.

## What's on it
- Main panel at 1:3,000, **survey-up** (south line horizontal; true north 15° right of page-up, arrow drawn). Base: 2022 NAIP, grayscale, lightened, clipped to the section + 90 ft.
- Neatline = MCAD polygon. Powell's 1876 calls verbatim on each edge; measured length, varas, and true bearing beneath each.
- Corners with lat/lon; "Beginning at…" at the NW corner.
- Parcels (hairline), streets with names, golf course outline, SSURGO units (dotted, named), quarter-section lines, SE/4 1978 conveyance (dashed), pipelines (dashed, labeled), wells by status (filled = producing, square + tick = horizontal pad with lateral direction, ⊗ = dry hole, ⊖ = plugged, ○ = permitted).
- Aerial strip: 1984, 1995, 2022 aligned and outlined; 1954/1965/1974 boxed "not yet aligned."
- Three text columns per the spec, updated: the North Concho finding, the survey excess, the wells inventory from `wells.csv`, the variation discrepancy in the red column.

## Known gaps (Skippy)
1. **Midland Draw is not drawn.** No NHD flowline geometry in the repo — only COMIDs in `nhd-check.md`. Pull the flowline(s) for COMID 5688042 and neighbors as GeoJSON (EPSG:2277).
2. **1954 / 1965 / 1974 alignment** — per `alignment-status-2026-09-27.md`.
3. `wells.csv` no longer carries API 42-329-47554 (Well 1MS, east line) that source-log row 24 reported. Confirm which is right.
4. Three APIs inside a Midland County section carry the Martin County prefix 42-317. Explain or add to the red column.

## For Adam (proof stage)
Read the three columns and the title block. Everything else is mechanical. Mark up anything; nothing prints until you say so.
