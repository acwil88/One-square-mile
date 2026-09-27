# 1995 frame alignment — method and error

**Input:** `aerials/ee-1995.tif` (USGS NAPP 9026-41, 12-19-95, 3360×3033, unrectified scan).
**Output:** `phase2/ee-1995-2277.tif` — warped onto the NAIP 2022 grid (EPSG:2277, 4059×4038 @ 1.9685 ftUS/px, same extent as `naip2022-2277.tif`). Deflate, nodata 0. Preview: `ee-1995-2277-preview.png`.

## Method
1. The scan is stored rotated: north points to image-right (the frame's title strip is vertical; Midland appears SW of the section instead of SE). Rotated 90° CCW first.
2. Automated feature matching (SIFT, edge template matching) failed — winter 1995 panchromatic vs summer 2022 color, and the golf course was rebuilt in 2018, so ponds and fairways are not stable control.
3. Three road intersections that exist in both images were picked by hand on gridded zooms:
   - Greentree Blvd × the N–S street into the Island Circle loop (north of the clubhouse)
   - Greentree Blvd × the west section-line road
   - Greentree Blvd × the east N–S road
4. Similarity transform (scale, rotation, translation) fit by least squares.
   Scale 5.143 NAIP px per 1995 px (≈10.1 ft per 1995 px). Residual rotation -8.6° after the 90° flip.
5. Checkerboard overlay against NAIP inspected: roads continue across tiles; offsets of roughly 70–190 ft visible in places.

## Error estimate
**±150 ft (±45 m)** typical, worse toward the frame edges (no lens/relief correction). At the aerial strip's print scale (~1:19,000) that is under 3 mm. Not fit for the main panel; fit for the strip. Refinable with more GCPs if anyone cares.

## Reproduce
```
M = [[5.0857294429708215, -0.7672148541114058, -2323.2826525198934], [0.7672148541114058, 5.0857294429708215, -6755.222599469495]]
# applied to the 90°-CCW-rotated scan, output grid = naip2022-2277.tif
```
Aligned by Claude, 2026-09-26.
