> **SUPERSEDED 2026-09-29** — §B is no longer needed. Adam's EROS login unlocked EarthExplorer downloads; both 2024 quarter-quads (SE acq 2024-09-09, NE acq 2024-08-26) were pulled as GeoTIFFs and mosaicked onto the exact 2022 grid as `phase2/naip2024-2277.tif`. Skip the MrSID download and Saturday export.

# Adam's Saturday fallback — QGIS on the ThinkPad (only for what Skippy can't close)

Install: QGIS LTR from qgis.org (free). Both jobs below are 15–30 minutes each.

## A. Control points for an old aerial frame (item 33 fallback)
1. Layer → Add Raster → `phase2/naip2022-2277.tif` (this is your reference; it's in EPSG:2277).
2. Raster → Georeferencer. In the Georeferencer window, open the *original scan* (`aerials/ee-1965.tif`, etc. — not the -2277 version).
3. Settings → Transformation: **Helmert** (or Polynomial 1 if Helmert isn't offered), Resampling: Cubic, Target SRS: EPSG:2277, output filename `phase2/ee-YYYY-2277.tif`, tick "Load in project when done."
4. Add points: click a feature in the scan, then "From map canvas," click the same feature on the NAIP. Use intersections: the west section road × the draw, the west road × the north line, a field corner (1946), the pad at the draw (1965), the road junction on the south line (1974). **Four to six points, spread across the frame, corners preferred.** Watch the residual column; anything over ~40 map units (feet) is a bad pick — delete and redo.
5. Start Georeferencing. Check by toggling the new layer over the NAIP at 50% opacity: the west road and the draw should sit on top of each other.
6. Note the residuals; Claude will put them in the caption.
Remember: the scans are stored rotated (north = image right on 1995/1984/1965; 1974 is upside-down). The Georeferencer doesn't care — the points fix it — but don't be surprised.

## B. NAIP 2024 from TxGIO's MrSID (item 34 fallback)
Scripted routes all failed (source-log row 72): Planetary Computer has no 2024 NAIP for this bbox (latest indexed is 2022); the USGS public download API has no NAIP products here and M2M needs a login; TxGIO's 2024 collection is county MrSID mosaics only and nothing in the scripted environment decodes MrSID. So this one is yours — about 20 minutes:

1. Download the Midland County 2024 NAIP mosaic (2.07 GB zip), direct link, no login — use a normal browser (Chrome/Edge), not a script:
   https://data.geographic.texas.gov/7e795b90-d89d-42a0-8bc9-4a7ef9b99e93/resources/naip24-60cm_48329_nccir-ccm.zip
   Inside: `naip24-nc-cir-60cm-midland_48329.sid` (885 MB, 60 cm, 4-band natural-color + color-infrared) plus a `.sdw` world file. Acquisition May–Nov 2024 (leaf-on); published 2025-03-07.
2. Unzip. Layer → Add Raster → the `.sid` file. QGIS opens MrSID natively on Windows.
3. Also load `phase2/naip2022-2277.tif`. Set the project CRS to EPSG:2277 (it should pick it up from the 2022 file).
4. Clip to the section frame: right-click the 2024 layer → Export → Save As. Settings: format GeoTIFF, CRS EPSG:2277, Extent → "Calculate from Layer" → pick the 2022 file, Resolution 1.9685 × 1.9685, filename `phase2/naip2024-2277.tif`, compression DEFLATE.
   By the numbers, the clip bbox (EPSG:2277, section + 10%) is: xmin 1724138.01, ymin 10714005.12, xmax 1733726.20, ymax 10723543.71.
5. Bands: the 2024 mosaic is 4-band (RGB + near-infrared); the 2022 reference is 3-band RGB. To match, use Raster → Conversion → Translate instead of Save As, and in "Additional command-line parameters" put `-b 1 -b 2 -b 3`. (If you'd rather keep all 4 bands, fine — just say so in the commit and Claude will handle it.)
6. Verify: the output must be **4059 × 4038 px**, EPSG:2277. Check Layer Properties → Information. If the dimensions match, commit it and tell Claude — v11 uses it as the base and the last strip square.
