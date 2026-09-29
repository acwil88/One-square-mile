# 1946 USDA Aerial Alignment (Items 30 + 31)

**Status:** APPROXIMATE — use with caution. See error estimate.

## A note for Claude (plain-language summary, 2026-09-29)

**Why the first 1946 frame only covered the north:** The 1946 aerial pulled first (mission DAR, frame 67) happens to end right at the Midland Draw — the Draw runs along the bottom edge of that photo, so everything south of the Draw (about 35–45% of the section) was simply off the edge of the frame. Not a processing error; the ground just wasn't in that picture.

**Which frame I pulled for the south half, and why:** Aerial missions fly overlapping strips, so the next frame south on the same roll covers the missing ground with ~60% forward overlap. I checked the bucket: frame 66 doesn't exist there (404), but frame 68 does — free on the same public TNRIS S3 path as 67. Once warped, frame 68's footprint covers 100% of the 1965 grid, including the entire southern half.

**How I aligned and mosaicked the two:** Same 2-GCP similarity method as the other frames. I transferred the two road×Draw ground control points from frame 67 into frame 68 by FFT template-matching (located to ~30 px, visually verified side-by-side), then fit the similarity transform to the 1965 grid. Sanity check passed: scale 0.9480 vs 0.9511 and rotation −8.42° vs −7.74° for frame 67 — nearly identical, as expected from two frames on the same flight line. Then a feather blend: frame 67 carries the north (it's nearer nadir there), frame 68 carries the south, ramped across 1965-grid rows 1900–2664, i.e. across the Draw. No visible seam.

**Combined error:** ±600–900 ft, APPROXIMATE — same budget as the single-frame alignment. Good enough for the sheet's 1946 strip; not for measuring distances.

**Things to know when you use the mosaic:**
- Use `phase2/ee-1946-2277-full.tif` (9.3 MB). The older `ee-1946-2277.tif` is frame 67 only — kept for reference, don't use it for mile-wide work.
- The blend seam runs E–W across the Draw (grid rows ~1900–2664). Both frames show the Draw well there, so it blends cleanly — but if you ever see a doubled feature near the Draw, that's the seam, not the ground.
- Date discrepancy is real: the frame edge reads February 28, 1946; the collection card says March 13, 1946. I used the frame date. If the sheet dates the 1946 strip, note the discrepancy.
- First look at the new southern half: fields, section-line roads, open rangeland south of the Draw — no obvious ranch headquarters. But nobody has done the careful structure-by-structure read of the south half yet (item 26a only covered the north). If the sheet wants the "no headquarters in 1946" claim to cover the whole mile, that read still needs doing.

---

## Frame 67 (Item 30)

### Source
- **Frame:** USDA Mission DAR 1C-67, flown February 28, 1946
- **File:** `~/workspace/tmp1946/frame67.tif` (47 MB, kept off GitHub)
- **Public URL:** https://tnris-data-warehouse.s3.us-east-1.amazonaws.com/LORE/collection/USDA-1946-DAR/items/bw/02-28-46_1-67.tif
- **Note:** Collection card says March 13, 1946; frame edge reads February 28, 1946. Using the frame date.
- **Size:** 8016×7185 px, 8-bit grayscale, ~1.87 ft/px
- **Coverage:** Frame extends ~2.84×2.55 mi. Section 7 center is in-frame.

### Reference
- **Target:** `phase2/ee-1965-2277.tif` (4059×4038, EPSG:2277)
- **Grid:** Same as 1965 alignment — 1.9685 ft/px, bounds 1724937.03–1732927.19 E, 10714800.00–10722748.82 N

### Method
2-GCP similarity (scale + rotation + translation) from 1946 scan pixels to 1965 grid pixels, then composed with the 1965 grid's EPSG:2277 transform. Warped via rasterio bilinear resampling.

This follows the same method as the 1965 (`ee-1965-alignment.md`) and 1954 (`ee-1954-alignment.md`) alignments.

### Ground Control Points

| GCP | 1946 scan (x, y) | 1965 grid (x, y) | Feature |
|-----|------------------|------------------|---------|
| 1 | (4956, 6960) | (3300, 2000) | East N-S section-line road × Midland Draw. Located via visual grounding on full-res crops; bright road crosses dark Draw channel. |
| 2 | (2219, 6800) | (700, 2200) | West N-S section-line road × Midland Draw. 1965 coords from 1965 alignment note. 1946 x estimated from 1-mile road spacing (4956 − 2737); y from Draw's course. |

### Transform
1946 scan → 1965 grid (pixel-to-pixel similarity):
- **Scale:** 0.9511 (1965 px per 1946 px). Matches expected 1.87/1.9685 = 0.95.
- **Rotation:** −7.74° (clockwise). The 1946 frame is rotated ~7.7° from north-up.
- **Translation:** (−2262.8, −3924.3) px.

Forward (1946→1965):
```
| 0.9425,  0.1282, -2262.84 |
| -0.1282, 0.9425, -3924.28 |
```

Composed with 1965 grid transform for EPSG:2277 output:
```
1946px → 2277: | 1.86,  0.25, 1720482.64 |
               | 0.25, -1.86, 10730473.76 |
```

### Verification
- Warped 1946 compared side-by-side with 1965 grid.
- **Midland Draw:** Aligns well — the dark E-W channel matches in both.
- **West N-S road:** Within ~450 ft (close, but not exact).
- **East road:** The 1946's east road does not clearly correspond to the 1965's east road (may be faint/absent in 1965, or a different road).
- **Scale check:** 0.9511 matches the theoretical 0.95, confirming the GCPs are ~1 mile apart as expected.

### Error Estimate: ±600–900 ft (APPROXIMATE)
- GCP2's 1946 position was estimated, not directly measured (adds uncertainty).
- The 1946 frame is rotated 7.7°, and the similarity model doesn't account for lens distortion or terrain.
- West road checkpoint shows ~450 ft offset.
- Labeled APPROXIMATE, similar to the 1954 alignment (±800–1500 ft).

### Coverage Limitation (SUPERSEDED — see Full-mile mosaic below)
**The 1946 frame does NOT cover the southern ~35–45% of the 1965 grid.** The 1946's Midland Draw is near the frame's southern edge (y≈6960 of 7185); south of the Draw, the frame ends. In the output TIFF, southern pixels are nodata (0).

The 1946 frame primarily covers the area NORTH of the Draw. The 1965 grid extends ~1 mile south of the Draw, which has no 1946 coverage.

---

## Frame 68 — southern half (Item 31, 2026-09-29)

### Source
- **Frame:** USDA Mission DAR 1C-68, flown February 28, 1946 (same mission/roll as 1C-67)
- **File:** `~/workspace/tmp1946/frame68.tif` (51.8 MB, kept off GitHub)
- **Public URL:** https://tnris-data-warehouse.s3.us-east-1.amazonaws.com/LORE/collection/USDA-1946-DAR/items/bw/02-28-46_1-68.tif
- **Note:** Adjacent frame 1C-66 does not exist on the bucket (HTTP 404); 68 is the only neighbor. Frame 68 is ~2690 px south of 67 (~60% forward overlap).
- **Size:** 8040×7165 px, 8-bit grayscale

### Ground Control Points (frame-68 scan pixels → 1965 grid)
Same ground features as frame 67's GCPs, located in frame 68 by FFT template-matching of frame 67's GCP neighborhoods (600×600 px templates), then visually verified side-by-side.

| GCP | frame-68 scan (x, y) | 1965 grid (x, y) | Feature | Match NCC |
|-----|------------------|------------------|---------|-----------|
| 1 | (4979, 4275) | (3300, 2000) | East N-S section-line road × Midland Draw | 0.60 |
| 2 | (2235, 4082) | (700, 2200) | West N-S section-line road × Midland Draw | 0.83 |

### Transform
1968 scan → 1965 grid (pixel-to-pixel similarity):
- **Scale:** 0.9480 (1965 px per 1968 px). Frame 67: 0.9511 (−0.3% — matches, same flight line).
- **Rotation:** −8.42° (clockwise). Frame 67: −7.74° (−0.7° — matches).
- **Translation:** (−1962.6, −1317.6) px.

Forward (frame-68→1965):
```
| 0.9378,  0.1388, -1962.60 |
| -0.1388, 0.9378, -1317.60 |
```

Composed with 1965 grid transform for EPSG:2277 output:
```
frame-68px → 2277: | 1.846,  0.2733, 1721073.56 |
                   | 0.2733, -1.846, 10725342.53 |
```

### Verification
- Warped 68 compared side-by-side with warped 67: the Draw, playa, roads, and field rectangles align cleanly across the full overlap.
- Scale/rotation sanity check vs frame 67 passes (see above).
- Frame 68's warped footprint covers **100% of the 1965 grid** — including the full southern half.

### Error Estimate: ±600–900 ft (APPROXIMATE)
Same budget as frame 67. Template-match transfer adds ~30–60 ft, negligible against the ±600–900 ft. Labeled APPROXIMATE.

---

## Full-mile mosaic (Item 31, 2026-09-29)

- **File:** `phase2/ee-1946-2277-full.tif` (9.3 MB, EPSG:2277, 4059×4038, deflate + predictor-2)
- **Preview:** `phase2/ee-1946-2277-full-preview.png` (1/4 scale)
- **Method:** Feather blend — frame 67 full weight north of 1965-grid row 1900, linear ramp to frame-68-only at row 2664 (67's south edge). 67 is nearer nadir in the north; 68 is nearer nadir in the south.
- **Coverage:** 100.00% of the 1965 grid has 1946 data (59.2% both frames, 40.8% frame 68 only). The southern half of Section 7 — south of the Midland Draw — is now covered.
- **Combined error:** ±600–900 ft (APPROXIMATE), governed by the frame-67/68 alignments.
- **First look at the new southern coverage:** fields, N-S section-line roads, and open rangeland south of the Draw; no obvious ranch headquarters, but a structure-level read of the south half has not been done (item 26a covered the north only).

### Files
- `phase2/ee-1946-2277.tif` (5.2 MB, frame 67 only — superseded by the full mosaic for mile-wide use)
- `phase2/ee-1946-2277-full.tif` (9.3 MB, 67+68 mosaic — **use this**)
- `phase2/ee-1946-2277-full-preview.png`
- `phase2/ee-1946-alignment.md` (this file)

### Notes
- The 1946 frame shows: Midland Draw winding E-W, a large water-filled playa (dark with white caliche rim) west of the west road, one clear N-S section-line road (west), fields in the northeast, and no buildings in Section 7 (buildings visible east of the east road are in the adjacent section).
- The playa is not visible in the 1965 frame (dried up or outside coverage).
- The 1946's east "road" used for GCP1 may be a farm road rather than the section-line road; however, the 1-mile spacing and scale match confirm it's the correct feature for alignment purposes.
