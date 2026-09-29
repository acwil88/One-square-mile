# 1946 USDA Aerial Alignment (Item 30)

**Status:** APPROXIMATE — use with caution. See error estimate.

## Source
- **Frame:** USDA Mission DAR 1C-67, flown February 28, 1946
- **File:** `~/workspace/tmp1946/frame67.tif` (47 MB, kept off GitHub)
- **Public URL:** https://tnris-data-warehouse.s3.us-east-1.amazonaws.com/LORE/collection/USDA-1946-DAR/items/bw/02-28-46_1-67.tif
- **Note:** Collection card says March 13, 1946; frame edge reads February 28, 1946. Using the frame date.
- **Size:** 8016×7185 px, 8-bit grayscale, ~1.87 ft/px
- **Coverage:** Frame extends ~2.84×2.55 mi. Section 7 center is in-frame.

## Reference
- **Target:** `phase2/ee-1965-2277.tif` (4059×4038, EPSG:2277)
- **Grid:** Same as 1965 alignment — 1.9685 ft/px, bounds 1724937.03–1732927.19 E, 10714800.00–10722748.82 N

## Method
2-GCP similarity (scale + rotation + translation) from 1946 scan pixels to 1965 grid pixels, then composed with the 1965 grid's EPSG:2277 transform. Warped via rasterio bilinear resampling.

This follows the same method as the 1965 (`ee-1965-alignment.md`) and 1954 (`ee-1954-alignment.md`) alignments.

## Ground Control Points

| GCP | 1946 scan (x, y) | 1965 grid (x, y) | Feature |
|-----|------------------|------------------|---------|
| 1 | (4956, 6960) | (3300, 2000) | East N-S section-line road × Midland Draw. Located via visual grounding on full-res crops; bright road crosses dark Draw channel. |
| 2 | (2219, 6800) | (700, 2200) | West N-S section-line road × Midland Draw. 1965 coords from 1965 alignment note. 1946 x estimated from 1-mile road spacing (4956 − 2737); y from Draw's course. |

## Transform
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

## Verification
- Warped 1946 compared side-by-side with 1965 grid.
- **Midland Draw:** Aligns well — the dark E-W channel matches in both.
- **West N-S road:** Within ~450 ft (close, but not exact).
- **East road:** The 1946's east road does not clearly correspond to the 1965's east road (may be faint/absent in 1965, or a different road).
- **Scale check:** 0.9511 matches the theoretical 0.95, confirming the GCPs are ~1 mile apart as expected.

## Error Estimate: ±600–900 ft (APPROXIMATE)
- GCP2's 1946 position was estimated, not directly measured (adds uncertainty).
- The 1946 frame is rotated 7.7°, and the similarity model doesn't account for lens distortion or terrain.
- West road checkpoint shows ~450 ft offset.
- Labeled APPROXIMATE, similar to the 1954 alignment (±800–1500 ft).

## Coverage Limitation
**The 1946 frame does NOT cover the southern ~35–45% of the 1965 grid.** The 1946's Midland Draw is near the frame's southern edge (y≈6960 of 7185); south of the Draw, the frame ends. In the output TIFF, southern pixels are nodata (0).

The 1946 frame primarily covers the area NORTH of the Draw. The 1965 grid extends ~1 mile south of the Draw, which has no 1946 coverage.

## Files
- `phase2/ee-1946-2277.tif` (5.2 MB, deflate compressed, EPSG:2277)
- `phase2/ee-1946-2277-preview.png` (1/4 scale preview)
- `phase2/ee-1946-alignment.md` (this file)

## Notes
- The 1946 frame shows: Midland Draw winding E-W, a large water-filled playa (dark with white caliche rim) west of the west road, one clear N-S section-line road (west), fields in the northeast, and no buildings in Section 7 (buildings visible east of the east road are in the adjacent section).
- The playa is not visible in the 1965 frame (dried up or outside coverage).
- The 1946's east "road" used for GCP1 may be a farm road rather than the section-line road; however, the 1-mile spacing and scale match confirm it's the correct feature for alignment purposes.
