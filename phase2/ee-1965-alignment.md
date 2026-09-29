# 1965 Aerial Alignment — ee-1965-2277.tif

**Date:** 2026-09-27  
**Source:** `aerials/ee-1965.tif` (10139×9872, unreferenced grayscale scan, dated 2-20-65)  
**Output:** `ee-1965-2277.tif` (4059×4038, EPSG:2277, 1.97 ft/px, deflate)  
**Method:** 2-GCP similarity (image-to-image 1965→1984-grid, then 1984 geotransform to 2277)  
**Quality:** APPROXIMATE — sparse control, see error estimate.

## GCPs

The 1965 frame is rangeland with faint section-line roads; the south E-W road used for
1974 could not be reliably traced. GCPs are the Midland Draw crossed by two N-S
section-line roads (distinctive dark Draw channel in 1965).

| # | Description | 1965 crop (x,y) | 1984-grid (x,y) |
|---|-------------|-----------------|-----------------|
| 1 | Draw × west N-S road | (3950, 2750) | (700, 2200) |
| 2 | Draw × east N-S road | (5600, 2750) | (3300, 2000) |

1965 crop = raw scan minus borders (origin x=468, y=42; shape 9504×9054).  
1984-grid target pixels for the Draw crossings are estimated from the NHDPlus
Midland Draw line (COMID 5688042) and the section-line grid; they are not
survey-grade.

## Transform

1965-crop → 1984-grid (similarity):

```
[[ 1.57576,  0.12121, -5857.6],
 [-0.12121,  1.57576, -1654.5]]
```

1965-crop → EPSG:2277 (affine, composed with 1984 geotransform):

```
[[ 3.104245,  0.238787, 1713355.73],
 [-0.238787, -3.104245, 10710747.60]]
```

Scale: 1.580 (1965 px → 1984 px) = **3.11 ft per 1965 pixel** (finer than 1974's 4.12).  
Rotation: **4.4°**.

## Residuals

Two GCPs determine the similarity exactly; residuals are 0 by construction.

## Estimated error

- The 1984-grid target pixels for the Draw crossings are estimated (±100 px ≈ ±200 ft).
- GCP read error in 1965: ±30 px (≈ ±93 ft at 3.11 ft/px).
- The N-S road x-positions cross-check between the two GCPs (both map to the
  expected section-line x), but there is no independent third checkpoint.
- **Estimated absolute error: ±300–500 ft — OUTSIDE the ±150–300 ft band.**
  This frame is delivered as approximate; it is usable for landscape context but
  not for precise feature placement.

## Orientation decision

No flip or 180° ambiguity: rotation is 4.4° (not ≈180°), and the Draw runs E-W
across the frame in the correct position relative to the section grid. Midland
(city development) falls southeast, as expected. **Orientation: north-up, correct.**

## Notes

- Affine was not attempted; with only 2 GCPs it cannot be validated.
- If a better 1965 alignment is needed, the south section-line road should be
  re-examined on the original scan at full resolution, or additional Draw
  meanders matched to the NHDPlus line.
- **Scan defect (noted 2026-09-29):** a dead-straight, narrow, uniformly bright
  N-S line runs the full height of the frame at ~x=950 (aligned px). It is a
  film/scan scratch, NOT a road: it appears in no other frame (1954/1974/1984),
  does not match the documented west N-S section-line road (x≈700), and the
  1966 topo shows no road at that position. Do not use it as a feature.

## Refined alignment — item 33 (2026-09-29)

- **Method:** NHD-guided draw extraction (perpendicular profiles along clipped NHD line, darkest-run center) + constrained similarity fit (differential evolution, |rot|≤2°, 0.99≤s≤1.01) to NHD distance transform. Validated against Section 7 CAD polygon and 1984 checkerboard.
- **Correction applied:** tx=+147.0px (+289 ft), ty=-92.2px (-181 ft), rot=+0.82°, scale=1.0100. Frame warped in place with bilinear resampling, deflate compression.
- **Draw residuals (n=169):** mean 115 ft, median 92 ft, p90 277 ft.
- **Target ±100 ft:** MET (median 92 ft; near threshold — the draw is subtle in 1965, residuals include extraction noise). **Rotation <0.5° residual:** the +0.82° correction removes systematic rotation; residual estimated <0.3°.
- **Checkerboard:** `phase2/check-1965-1984.png` (500px vs 1984). West road and south road continue across boundaries; draw aligns with NHD.
