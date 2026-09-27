# 1954 Aerial Alignment — ee-1954-2277.tif — APPROXIMATE

**Date:** 2026-09-27  
**Source:** `aerials/ee-1954.tif` (10620×9872, unreferenced grayscale scan, dated 2 MAY 54)  
**Output:** `ee-1954-2277.tif` (4059×4038, EPSG:2277, 1.97 ft/px, deflate)  
**Method:** 2-GCP similarity (1954→1984-grid via Draw bends matched through 1965, then 1984 geotransform)  
**Quality:** APPROXIMATE — error exceeds ±500 ft. See below.

## GCPs

Sparse control. The 1954 frame shows Midland city (SE), the Midland Draw, and
rangeland section-line roads, but no confident section-corner road intersections.
GCPs are two Midland Draw meander bends, matched from 1954 to the (already
approximate) 1965 alignment, then transferred to the 1984-grid.

| # | Description | 1954 crop (x,y) | 1984-grid (x,y) |
|---|-------------|-----------------|-----------------|
| 1 | Draw bend A | (5000, 3375) | (2355, 2074) |
| 2 | Draw bend B | (5750, 3450) | (3931, 1953) |

1954 crop = raw scan minus borders (origin x=366, y=78; shape 9474×9666).  
1984-grid targets are derived through the 1965 alignment (itself ±300–500 ft),
so they compound the error.

## Transform

1954-crop → 1984-grid (similarity):

```
[[ 2.06455,  0.36779, -9209.1],
 [-0.36779,  2.06455, -3054.9]]
```

1954-crop → EPSG:2277 (affine, composed with 1984 geotransform):

```
[[ 4.067173,  0.724544, 1706795.12],
 [ 0.724544, -4.067173, 10728767.00]]
```

Scale: 2.097 (1954 px → 1984 px) = **4.13 ft per 1954 pixel**.  
Rotation: **10.1°**.

## Residuals

Two GCPs determine the similarity exactly; residuals are 0 by construction.

## Estimated error — EXCEEDS ±500 ft

- The 1984-grid GCP targets inherit the 1965 alignment error (±300–500 ft).
- The Draw bend matches between 1954 and 1965 are visual (±50 px in 1954 ≈ ±200 ft).
- Cross-check: the Midland Draw in the warped 1954 sits ~500 px (~1000 ft) north
  of its position in the warped 1965, confirming a large systematic offset.
- **Estimated absolute error: ±800–1500 ft — well outside the ±500 ft threshold.**
- **This frame is labeled APPROXIMATE.** Usable only for coarse landscape context
  (city extent, Draw course, field patterns), NOT for locating section features.

## Orientation decision

No flip or 180° ambiguity: rotation is 10.1° (not ≈180°). The 1954 city street
grid falls in the southeast of the aligned frame, matching the known geography
(Midland southeast of Section 7). **Orientation: north-up, correct.**

## Notes

- Affine was not attempted; with 2 GCPs (one derived through another approximate
  alignment) it cannot be validated.
- A better 1954 alignment would require matching the 1954 city street grid
  directly to modern streets (3+ GCPs) or finding the section-line roads in 1954.
  That was not achieved in this pass.
- Filename note: this file is the approximate 1954 alignment; do not use for
  precise measurement.
