# 1984 frame alignment — method and error

**Input:** `aerials/ee-1984.tif` (USGS HAP85 320215, 10-28-84, 3900×3523, unrectified scan, ~15 ft/px).
**Output:** `phase2/ee-1984-2277.tif` on the NAIP 2022 grid (EPSG:2277, same extent as `naip2022-2277.tif`). Preview `ee-1984-2277-preview.png`.

## Method
1. Scan stored rotated, north = image-right (same as 1995). Rotated 90° CCW.
2. Aligned to the **1995 frame**, not to NAIP: same season, same film type, and the golf course was unchanged between 1984 and 1995 (rebuilt 2018), so the four ponds are stable control. Pond centroids by dark-threshold in matched windows: Island Circle loop pond, the pair east of the clubhouse, the clubhouse pond, the south pond.
3. Similarity fit 1984→1995: scale 1.815, rotation +2.3°. Residuals 17–30 ft.
4. Chained through the 1995→NAIP transform. Checkerboard against aligned 1995 inspected: roads continue across tiles.

## Error estimate
Relative to 1995: ±30 ft. Absolute: inherits the 1995 frame's **±150 ft**. Fit for the strip.

## Reproduce
```
M_1984_to_naip = [[9.277033907924004, -1.0211027628449187, -16457.382587369055], [1.0211027628449187, 9.277033907924004, -17972.326168323576]]
# applied to the 90°-CCW-rotated scan; output grid = naip2022-2277.tif
```
Aligned by Claude, 2026-09-27.
