# Check-in for Claude — 2026-09-26 (evening)

Status + questions on the Phase 2a asset pipeline. Repo: https://github.com/acwil88/One-square-mile (public — pull freely, no token needed).

## What's in the repo now (32 files)

- `README.md`, `.gitignore`, `source-log.md` (rows 1–31), `handoff-to-claude.md`, `brief-8-memory-history.md`
- `phase2/section7-polygon-wgs84.geojson`, `phase2/section7-polygon-2277.geojson` — real MCAD section polygon (rotated parallelogram, ~650.1 ac)
- `phase2/calls.md`, `phase2/glo-patent-file.pdf`, `phase2/glo-patent-file.txt`, `phase2/glo-page-1.png` … `glo-page-9.png` — Powell 1876 calls + patent scans
- `phase2/nhd-check.md` — "waters of North Concho" verdict (drains to Colorado via Midland Draw/Beals Creek)
- `phase2/naip2022-2277.tif` + `phase2/naip2022-preview.png` — 2022 NAIP ortho, see frame spec below
- `aerials/ee-1954-preview.jpg`, `ee-1965-preview.jpg`, `ee-1974-preview.jpg`, `ee-1984-preview.jpg`, `ee-1995-preview.jpg` — preview JPGs of the historic frames
- `aerials/ee-1965.tif`, `ee-1974.tif`, `ee-1984.tif`, `ee-1995.tif` — full-res historic frames

## Reference frame (used for NAIP; proposed as the "identical frame")

- CRS: **EPSG:2277** (NAD83 / Texas South Central, ftUS)
- Extent (ftUS): west 1724937.0, south 10714800.0, east 1732927.2, north 10722748.8
- Grid: 4059 × 4038 px at 1.9685 ft/px (0.6 m native NAIP resolution)
- Coverage: Section 7 polygon + 10% bleed
- Source: USDA NAIP 2022 60 cm, quarter-quads `m_3210263_se_13_060_20220924` + `m_3210263_ne_13_060_20220924` (SW/NW quads don't cover the section), via Planetary Computer STAC

## Blocker: historic frames are unrectified scans

The five `ee-*.tif` frames from EarthExplorer have **no georeferencing at all** — no CRS, no geotransform, no GCPs, no RPCs (verified). They're raw scanned photo frames, some rotated relative to north. So "reproject and clip to the identical frame" needs ground-control alignment per frame first. Automated feature matching against the 2022 NAIP failed (4–8 inlier matches — noise; the landscape changed too much).

Control assessment:
- **1995**: strong — subdivision streets, golf course, Highway 191 all visible. Hand GCP alignment very doable.
- **1984/1974/1965/1954**: sparse — rangeland, Midland Draw, old section-line roads, a 1954 triangular airfield-like feature. Expect 15–50 m accuracy at best, slow work per frame.

## Questions

1. **Aerial strip alignment**: (a) I hand-align 1995 properly and best-effort the older four with documented method + error estimates in the source log; (b) full manual GCP treatment on all five (slow); or (c) approximate center+scale placement, clearly labeled. Which do you want?
2. **Frame spec**: is the NAIP frame above the "identical frame" you want the historic aerials clipped to, or do you want a different extent/resolution?
3. **`ee-1954.tif` (104.9 MB) exceeds GitHub's 100 MB file cap** — it's local-only for now. Want a losslessly compressed full-resolution copy pushed (deflate/LZW — no downsampling), or will you pull it another way?
4. **Upcoming steps** (wells CSV, MCAD parcels/streets/golf outline, SSURGO clip): any column/attribute preferences beyond what's in the brief? Wells CSV currently planned as API, lat, lon, type, lateral azimuth if known + gathering-line GeoJSON.

Standing constraints unchanged: one copy first edition, nothing on the sheet that couldn't print (no owner names/addresses/phones), no calls or emails — Adam's call on anything else.
