# Item 6 — Newer imagery: findings (2026-09-26/27)

## 6a. NAIP 2024 Texas — EXISTS, downloaded, decode blocked

- **Collection:** Texas NAIP Imagery 2024, TxGIO DataHub
  `7e795b90-d89d-42a0-8bc9-4a7ef9b99e93`
- **Acquisition:** May–Nov 2024 (leaf-on, statewide). Published 2025-03-07.
- **Product:** 60 cm, 4-band RGBIR. TxGIO distributes it ONLY as
  Compressed County Mosaics (CCM) — no DOQQ tiles posted yet
  ("When the DOQQ tiles become available the data will be posted here!").
- **Midland County file:** `naip24-60cm_48329_nccir-ccm.zip`
  (2,216,684,370 bytes), downloaded 2026-09-26 to
  `phase2/.dl/naip24-midland.zip` (kept out of git).
  Contains `naip24-nc-cir-60cm-midland_48329.sid` (885 MB MrSID)
  + `.sdw` world file (0.6 m pixels) + `.aux` + seamlines shapefile.
- **Planetary Computer:** re-queried 2026-09-26 — zero 2024 NAIP items
  for the section bbox (only 2022 exists there).
- **Blocker:** the county mosaic is MrSID (`.sid`), a proprietary
  LizardTech wavelet format. No decoder in this environment
  (GDAL 3.8.4 has no MrSID driver; the free Decode SDK requires a
  LizardTech developer registration). `gdalinfo`:
  "not recognized as a supported file format."
- **Not pursued:** random-mirror DSDK binaries, Wine-based converters
  (untrusted); AWS `naip-analytic` bucket is Requester Pays
  (no anonymous access); USDA APFO image service unreachable from
  this network.

### To finish the decode (needs Adam's tap)

Option A — free LizardTech developer registration, download the
MrSID Decode SDK for Linux, then run its bundled `mrsiddecode`:
`mrsiddecode -i naip24-nc-cir-60cm-midland_48329.sid -o naip24-midland.tif`
Option B — pull the 2024 DOQQs as GeoTIFF from USGS EarthExplorer
once TxGIO/USGS posts them (EROS login already active).

Then clip to the exact 2022 frame with:
`gdalwarp -t_srs EPSG:2277 -te 1724937.030 10714800.004 1732927.188 10722748.823 -tr 1.968503937007874 1.968503937007874 -r cubic <src> phase2/newest-2024-2277.tif`
Target frame (from `gdalinfo naip2022-2277.tif`): EPSG:2277,
4059×4038, 1.9685 ft pixels, RGB.

## 6b. Post-2022 StratMap 6-inch urban imagery — NONE for Midland

- Queried the TxGIO DataHub API 2026-09-26: all 106 "stratmap"
  collections and all 70 collections matching "midland."
- Result: no StratMap-family imagery collection with acquisition
  ≥ 2022 covers Midland County (or exists at all in the catalog).
  Midland's imagery holdings top out at Texas NAIP 2022, then 2024.
- The "Texas Imagery Service" collection (2020) is older than 2022.
- Conclusion: nothing six-inch-or-better and post-2022 exists for
  this section. NAIP 2024 (60 cm) is the newest imagery published.
