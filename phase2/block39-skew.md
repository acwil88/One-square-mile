# Block 39 T-1-S: the 14° skew (queue item 17, 2026-09-27)

**Question:** is Section 7's ~14° rotation from cardinal block-wide, or unique to Sec 7?

## Long-side azimuths, every abstract polygon in Block 39 T-1-S

Source: MCAD Abstracts layer (MidlandCADWebService/FeatureServer/1), `Block='39 T1S'`, 41 polygons, geometry in EPSG:2277. Azimuth = degrees clockwise from true north, normalized 0–180 (a rectangle's two axes read 90° apart).

| Sec | Code | Long-edge az. | | Sec | Code | Long-edge az. |
|-----|------|---------------|-|-----|------|---------------|
| 2 | 1361 | 75.5° | | 22 | 1177 | 76.4° |
| 3 | 1368 | 75.2° | | 22 | 1181 | 165.7° |
| 4 | 878 | 90.9° | | 22 | 1304 | 165.0° |
| 5 | 79 | 165.8° | | 23 | 40 | 165.6° |
| 6 | 720 | 75.8° | | 25 | 41 | 165.5° |
| 7 | 34 | 75.8° | | 26 | 438 | 165.5° |
| 8 | 719 | 165.8° | | 27 | 42 | 76.4° |
| 9 | 80 | 75.5° | | 28 | 686 | 75.3° |
| 10 | 877 | 75.5° | | 29 | 43 | 164.7° |
| 11 | 81 | 76.1° | | 30 | 699 | 76.1° |
| 12 | 1020 | 90.9° | | 31 | 44 | 164.9° |
| 13 | 35 | 75.7° | | 32 | 727 | 165.7° |
| 14 | 667 | 75.5° | | 33 | 45 | 75.3° |
| 15 | 36 | 75.6° | | 34 | 520 | 76.4° |
| 16 | 693 | 75.9° | | 34 | 1167 | 75.8° |
| 17 | 37 | 165.4° | | 35 | 46 | 75.0° |
| 18 | 681 | 75.4° | | 36 | 1 | 75.7° |
| 19 | 38 | 75.4° | | 20 | 687 | 165.8° |
| 20 | 1436 | 76.1° | | 20 | 1166 | 75.2° |
| 21 | 39 | 165.6° | | 22 | 1303 | 76.0° |
| 22 | 671 | 165.6° | | | | |

(Sections 20, 22, 34 appear as multiple patents/subdivisions; each polygon measured separately.)

## Verdict: systematic and block-wide

Every polygon's long axis falls in one of two tight clusters — **~75–76° or ~165–166°** — exactly 90° apart, i.e. the two axes of the same rotated rectangle. Against cardinal (0°/90°), the block is uniformly twisted **~14°** (90 − 76 = 14; 180 − 166 = 14). Two sections read 90.9° (Secs 4, 12), likely re-surveys or digitizing artifacts, but 39 of 41 polygons follow the skew. It is not unique to Section 7.

## Why: magnetic variation, stated on the plat

W.C. Powell's 1876 field notes for Section 7 (GLO Bexar Scrip File 020113, transcribed in `phase2/calls.md`) carry the header **"Variation 12° 9-1/2' East"** — the surveyor's own recorded magnetic declination. His calls (S 13° E, N 77° E, N 13° W…) were run by needle compass; a ~12–14° east variation swings magnetic-north lines that far off true north, which is precisely the rotation the MCAD geometry preserves 150 years later. Contemporary surveying literature notes "many of the old surveys were executed with the needle compass and the variation either assumed or erroneously calculated" (Technology Quarterly / Society of Arts, via compleatsurveyor.com). Texas Natural Resources Code Ch. 21 now requires field notes to state the survey basis, but in 1876 the deputy's compass and his stated variation were the standard. The skew is the fossil of Powell's needle.
