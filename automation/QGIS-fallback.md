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
1. Download the Midland County 2024 NAIP mosaic (URL in `phase2/newest-imagery.md` — Skippy will put the exact link there).
2. Layer → Add Raster → the `.sid` file. QGIS opens MrSID natively on Windows.
3. Load `phase2/naip2022-2277.tif` too. Right-click it → Layer CRS → set project CRS to EPSG:2277.
4. Right-click the 2024 layer → Export → Save As: format GeoTIFF, CRS EPSG:2277, **Extent: click "Calculate from Layer" and choose the 2022 file**, Resolution: 1.9685 × 1.9685 (map units), filename `phase2/naip2024-2277.tif`. Compression: DEFLATE.
5. Commit it. That's the whole job.
