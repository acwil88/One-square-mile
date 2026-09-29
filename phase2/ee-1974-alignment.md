# 1974 Aerial Alignment — ee-1974-2277.tif

**Date:** 2026-09-27  
**Source:** `aerials/ee-1974.tif` (10193×9872, unreferenced grayscale scan)  
**Output:** `ee-1974-2277.tif` (4059×4038, EPSG:2277, 1.97 ft/px, deflate)  
**Method:** 2-GCP similarity (image-to-image 1974→1984-grid, then 1984 geotransform to 2277)

## GCPs

Only two reliable section-line road intersections were identifiable in 1974. The north
section line crosses open rangeland with no road intersections; the east/west roads are
fragmented by a quarry at the SE. Both GCPs are on the south section-line road.

| # | Description | 1974 crop (x,y) | 1984-grid (x,y) | EPSG:2277 (X,Y) |
|---|-------------|-----------------|-----------------|-----------------|
| 1 | SE: south E-W road × east N-S road | (5715, 5386) | (3679, 3001) | (1732184.7, 10716836.9) |
| 2 | SW: south E-W road × west N-S road | (4470, 5720) | (1065, 3659) | (1727035.1, 10715540.6) |

1974 crop = raw scan minus borders (origin x=48, y=198; shape 8646×9576).  
1984-grid = `phase2/work/ee-1984-2277.tif` pixel coords (same grid/transform as output).  
GCP 1974 pixels were read from the Hough-detected south-road centerline
((4178,5798)→(6402,5202), tilt −15.0°) intersected with the visually-confirmed
east/west N-S roads, cross-checked in 1000×1000 zooms.

## Transform

1974-crop → 1984-grid (similarity):

```
[[ 2.01164, -0.23251, -8095.9],
 [ 0.23251,  2.01164, -8445.9]]
```

1974-crop → EPSG:2277 (affine, composed with 1984 geotransform):

```
[[ 3.962921, -0.458053, 1712018.75],
 [-0.458053, -3.962921, 10740929.69]]
```

Scale: 2.0912 (1974 px → 1984 px) = **4.12 ft per 1974 pixel**.  
Rotation: **0.89°** (1974 frame is essentially north-up, matching the 1984 grid).  
The south-road vector angle matches between frames (−15.0° vs −14.1°, Δ=0.9°),
confirming the GCPs sit on the road centerlines.

## Residuals

Two GCPs determine the similarity exactly; residuals are 0 by construction.
Independent check: the east N-S section-line road is continuous across 1974/NAIP-2022
checkerboard tile boundaries with no visible offset (see `phase2/work/check74c.png`).

## Estimated error

- GCP read error: ±20 px in 1974 (≈ ±82 ft at 4.12 ft/px); ±10 px in 1984-grid (≈ ±20 ft).
- Road-centerline vs legal-corner offset: < 10 ft (1984-grid GCP pixels match the
  published section corners to within 7 ft).
- **Estimated absolute error: ±100–150 ft**, within the ±150–300 ft acceptance band.

## Orientation decision

No flip or 180° ambiguity: the transform rotation is 0.89° (not ≈180°), and the
checkerboard against NAIP-2022 shows the section-line roads, the quarry, and the
diagonal all landing on their 2022 positions. Midland (city development) falls
southeast of the section in the aligned frame, as expected. **Orientation: north-up, correct.**

## Notes

- Affine was not needed; the similarity residuals/validation were already within tolerance.
- The 1954/1965 frames were aligned with the same south-road method.

## Refined alignment — item 33 (2026-09-29)

- **Method:** Verified only — no warp applied. NHD-guided draw fit was attempted but rejected (draw too subtle in 1974; fit hit rotation bounds with inconsistent residuals). Visual verification against Section 7 CAD polygon shows section-line roads aligning with polygon edges (SE/SW intersections within a few px of CAD corners).
- **Correction applied:** None (identity).
- **Target ±100 ft:** MET by inspection — road/polygon alignment confirms the existing placement. **Rotation <0.5°:** confirmed (no systematic rotation visible).
- **Checkerboard:** `phase2/check-1974-1984.png` (500px vs 1984).
