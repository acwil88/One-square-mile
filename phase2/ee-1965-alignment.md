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
