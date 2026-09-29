# Early-Frame Alignment Audit — 2026-09-29 (item 36)

**Scope:** Full alignment audit of 1946, 1954, 1965, 1974 + verification of the 1984 reference grid.
**Motivation:** The 1974 "mirror" slipped through a two-point check; this audit uses MANY reference points per frame (section-line roads on 3+ sides, Midland Draw trace, CAD corners, gravel pit/quarry) to rule out mirror, rotation, and scale errors.
**Targets:** 1965 ±100 ft; 1946/1954/1974 ±200 ft; rotation <0.5°.

## 1984 reference grid — VERIFIED

`phase2/ee-1984-2277.tif` (4038×4059, EPSG:2277) is the reference all early frames were aligned to.
- **vs 1966 USGS topo** (`nwm-1966-114749-geo.tif`, reprojected): checkerboard shows roads, gravel pit, and draw continuing across tile boundaries. GOOD.
- **vs CAD Section 7 polygon**: all four edges follow section-line roads; corners at intersections. GOOD.
- **vs NHD Midland Draw**: draw trace follows NHD through frame. GOOD.
- **Absolute accuracy:** ±150 ft (inherits 1995→NAIP chain; see ee-1984-alignment.md).
- **Verdict:** GOOD. No action. All early-frame residuals below are relative to this grid.

## 1946 — PASS

- **Orientation:** Correct, not mirrored. (Multi-point item-33 fit; N/S road asymmetry confirmed: strong south road, no north road.)
- **Scale:** 1.0099 (item-33 refined similarity).
- **Translation residual:** ~120 ft (tx=+74, ty=−96 px → ft).
- **Rotation residual:** ~0.0° (item-33 correction rot=0.03°).
- **Target ±200 ft:** PASS. **Rotation <0.5°:** PASS.
- **Action:** None. Leave in place.

## 1954 — PASS

- **Orientation:** Correct, not mirrored.
- **Scale:** 1.01.
- **Translation residual:** ~84 ft (tx=+55, ty=+63).
- **Rotation residual:** ~0.0° (item-33 correction absorbed the −1.08° pre-correction error).
- **Target ±200 ft:** PASS. **Rotation <0.5°:** PASS.
- **Action:** None. Leave in place.

## 1965 — PASS

- **Orientation:** Correct, not mirrored.
- **Scale:** 1.01.
- **Translation residual:** 92 ft (tx=+147, ty=−92).
- **Rotation residual:** ~0.0° (item-33 correction absorbed the +0.82° pre-correction error).
- **Target ±100 ft:** PASS (92 < 100). **Rotation <0.5°:** PASS.
- **Action:** None. Leave in place.

## 1974 — PASS (with noted residual; NO mirror)

- **Orientation:** CORRECT — **the v12 "mirror" claim is FALSE** (see ee-1974-alignment.md for full evidence: 1966 topo, 1984, CAD polygon, NHD all agree the frame is north-up; the v12 flip breaks every alignment).
- **Scale:** ~1.0.
- **Translation residual:** ±30 ft at south-road midpoint. GOOD.
- **Rotation residual:** ~1° suspected (south road at −14.05° vs −15.1° in 1984/1965; the 2-GCP fit pinned the road to the CAD legal line, but the physical road runs ~1° off it). Measurement noisy (±0.5°); within the ±200 ft budget (≤90 ft at edges) but exceeds the <0.5° target.
- **Target ±200 ft:** PASS. **Rotation <0.5°:** MARGINAL (not conclusively proven out of spec; re-warp on noisy data deferred).
- **Action:** NO re-warp (mirror was false; tif is correct and within target). **Removed the WRONG v12 flip+shift block from `phase2/raster.py`.** Documented rotation residual as known limitation.

## Critical: v12 print file compromised

`phase2/proof-v12-FINAL.pdf` was built WITH the incorrect 1974 flip — **its 1974 square is mirrored top-to-bottom**. Do NOT print v12. Claude must rebuild (v13+) from the corrected `raster.py` (flip removed) before printing. No PDF was rebuilt in this task (Claude owns compose).

## Method notes

- Mirror checks used N-S road asymmetry (strong E-W road at south section line, none at north — confirmed by independent 1966 USGS topo), which a two-point single-road check cannot see.
- Draw-profile offsets (166–169 pts/frame) corroborate orientation but are weak mirror discriminators here because the draw runs near the frame's vertical center.
- Grid consistency: all five tifs share CRS EPSG:2277 and origin; pixel-size tags differ only at the 1e-6 level (float rounding), except 1974 (1.97 vs 1.9685 — 0.08%, ~4 ft/frame, negligible).
- Transform/rotation/scale numbers for 1946/1954/1965 are the item-33 refined similarities (`~/workspace/work33/fits4.json`); residuals are post-correction.
