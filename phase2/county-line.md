# Item 27 — the county line test (2026-09-28)

**Question:** Is the Midland–Martin county line the T&P base line, i.e. the north line of Section 7, Block 39, T-1-S?

**Verdict: No.** The county line runs roughly a mile north of the section's north line. It is not the section's north line, and no labeled county boundary goes on the sheet at the section edge. The 1887 red-ink note gets no second sentence.

## The number

Signed difference (county-line northing minus section north-line northing), EPSG:2277, at three stations across the section:

| station (2277 E) | county line N | Sec 7 north edge N | diff (ft) |
|---|---|---|---|
| 1,725,690 (NW corner) | 10,727,488 | 10,720,684 | **+6,805** |
| 1,728,284 (mid) | 10,727,452 | 10,721,341 | **+6,110** |
| 1,730,877 (NE corner) | 10,727,417 | 10,721,999 | **+5,417** |

Positive = county line is NORTH of the section's north line. Headline number: **+6,110 ft at mid-longitude** (range +5,417 to +6,805 ft across the section, ~1.0–1.3 mi).

The gap shrinks eastward because the county line runs nearly flat E–W (drops ~72 ft over the section's width) while the section's skewed north edge climbs ~1,316 ft over the same span (the ~14° Powell magnetic-needle skew documented in `block39-skew.md`).

## Side tests

Against the City of Midland "County Boundary" polygon (Midland County, MapServer/12), point-in-polygon in EPSG:2277:

- All four Section 7 corners (SE/SW/NW/NE): **inside = Midland side** ✓
- All three EASY TARGET pads: **inside = Midland side** ✓
  - 42-317-45816 (32.06922, −102.17267) → (1,726,782, 10,721,071)
  - 42-317-45818 (32.07058, −102.16656) → (1,728,683, 10,721,535)
  - 42-317-45820 (32.07165, −102.16198) → (1,730,108, 10,721,901)

The pads sit only **+92 to +111 ft north of the section's north edge** — but **~5,400–6,400 ft south of the county line**. Geographically they are in Midland County, even though RRC codes them 317 (Martin). The RRC code follows the lease/permit surveys (Secs 19/30, Blk 39, T1N — Township 1 North), not the surface geography. Flag for the item-23 note: its "pad is in Martin County" reasoning is geographically wrong; the code is explained by the T1N lease location, not the pad location.

## Interpretation

Sec 7 sits in the second tier of sections in Township 1 South (standard numbering: sections 1–6 along the north tier). Its north line is therefore ~1 mile south of the township's north line — and the measured 5,417–6,805 ft gap matches that exactly. The Midland–Martin line is the **north line of Township 1 South** (the T&P township line), not the north line of Section 7.

## Layers cited

1. **TxDOT Texas County Boundaries (line)** — `https://services.arcgis.com/KTcxiTD9dsQw4r7Z/arcgis/rest/services/Texas_County_Boundaries_Line/FeatureServer`, layer 0 ("County", polyline). Queried by envelope over the section, geometry returned in EPSG:2277. The Midland–Martin segment (OID 1010) supplied the northing numbers above.
2. **City of Midland BaseMap MapServer/12 "County Boundary"** — `https://maps.midlandtexas.gov/arcgis/rest/services/ReferenceData/BaseMap/MapServer/12` (single polygon, OID 321, Midland County, 902.0 sq mi, 90 vertices, generalized). Used for the point-in-polygon side tests. Its northern boundary independently lands at N ≈ 10,727,300–10,727,660 across our longitude — consistent with TxDOT.
3. **MCAD Abstracts** — `https://services5.arcgis.com/1pOc2HE5GDuzMESK/arcgis/rest/services/MidlandCADWebService/FeatureServer/1`, `CODE='34' AND Block='39 T1S' AND Surv_Sect='7'` (DESC_='T&P RR CO', area 28,320,481 sq ft), geometry in EPSG:2277. Supplied the four section corners.

All work in EPSG:2277 (NAD83 / Texas South Central, US ft); pad WGS84→2277 via pyproj. Read-only queries, no spend. DONE.
