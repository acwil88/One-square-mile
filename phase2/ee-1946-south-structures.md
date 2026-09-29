# 1946 USDA aerial — structures read, SOUTHERN half (item 32)

## Frame
- **Mosaic:** `phase2/ee-1946-2277-full.tif` (EPSG:2277, 4059×4038, ~1.97 ft/px), frames DAR 1C-67 + 1C-68 feather-blended
- **Date:** February 28, 1946 (frame edge; collection card says March 13, 1946 — discrepancy stands)
- **Area read:** everything south of the Midland Draw in Section 7 (1965-grid rows ~2200–4038), i.e. the frame-68-only ground item 26a never covered
- **Method:** eight native-resolution tiles (2 rows × 4 cols) covering the full southern half, each read at 1:1, plus contrast-enhanced close-ups of every anomaly. Section boundary from `phase2/section7-polygon-2277.geojson` (Midland CAD Abstracts, OBJECTID 57) via point-in-polygon test. Same visual-read method as the northern half (`phase2/usda1946-structures.md`).
- **Error caveat:** the mosaic is APPROXIMATE (±600–900 ft). Boundary calls within ~900 ft of a section line are flagged as such.

## Findings — inside Section 7, south of the Draw

1. **Building cluster on/near the west line — 32.055634, -102.170137** (grid row 3369, col 1294). Two to three small bright rectangular buildings (20–40 ft each) with cleared/disturbed ground around them and a dark rectangular feature immediately north (possible stock tank, corral, or small plot — not resolved). A faint track connects the cluster to the N-S road ~100 ft west. Per the CAD polygon this is ~600 ft inside the west line — but that is inside the alignment error budget, so treat as **on/near the west line, plausibly just inside Section 7**. This is NOT the 1966 topo's building (that site, 32.0616,-102.1732, is ~2,200 ft north and is EMPTY in 1946 — verified on a 600×600 native-res crop: road, two-track, rangeland, no structure).
2. **1966 building site (32.0616, -102.1732): no structure in 1946.** Confirmed empty.
3. **Cultivation:** several dark dryland-field rectangles — one mid-west (tile s00), one large block bottom-center (tile s11), one large block in the SE (tile s13), plus field corners elsewhere. No farmsteads attached to the in-section fields.
4. **Roads:** the west and east N-S section-line roads continue south of the Draw; several faint E-W and diagonal two-track trails cross the rangeland.
5. **No windmill** visible anywhere in the southern half. **No corrals/pens** clearly identifiable. **No ranch headquarters complex** — nothing approaching a multi-building HQ with corrals.

## Outside Section 7 (context, not the mile)
- **Farmstead at 32.053560, -102.175269** (grid row 3739, col 480): house/barn-sized dark rectangular building plus outbuildings and cleared ground at a field corner, ~1,150 ft west of the section's west line — in the adjacent section. The neighboring section had an active farmstead in 1946; Section 7's west-line cluster may belong to the same operation working across the line.

## What this means
- The northern half's "no buildings" finding (item 26a) does **not** extend to the whole mile. The southern half has one small building cluster on/near the west line.
- The **"no ranch headquarters in February 1946"** conclusion still stands for the full mile: the west-line cluster is two to three small buildings, not an HQ complex — no corrals, no windmill, no headquarters-scale footprint anywhere in the section.
- If the sheet states "no buildings," qualify it: one small outbuilding cluster sits on/near the west line (~600 ft inside per the CAD polygon, within alignment error of the boundary).
- The 1966 topo's building (west-central road) and windmill (north bank of Draw) were both built between 1946 and 1966 — confirmed on both halves now.

## Files
- This note: `phase2/ee-1946-south-structures.md`
- Read from: `phase2/ee-1946-2277-full.tif` (item 31 mosaic)
- Section boundary: `phase2/section7-polygon-2277.geojson` (in git history; working-tree copy restored via `git show` — not currently checked out)
