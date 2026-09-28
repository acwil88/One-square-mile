# Item 29 — county-code vs surface-geography test (2026-09-28)

**Question:** How common is the Easy Target coding — 317 (Martin) on wells whose
surface points fall inside Midland County?

**Data:** RRC Drilling Permit Master end-of-month snapshot via the ezrrc public
API (`drilling-permits-monthly`, snapshot 2026-09-25, 116,786 rows), filtered on
the normalized `county_code` ('MARTIN' / 'MIDLAND' — ezrrc resolves the code to
the county name). Surface points from the permit '14' GPS trailer record
(`surface_latitude`/`surface_longitude`). County polygons from the TxDOT Texas
County Boundaries polygon service (item-27 source),
`https://services.arcgis.com/KTcxiTD9dsQw4r7Z/arcgis/rest/services/Texas_County_Boundaries/FeatureServer/0`,
queried in WGS84; point-in-polygon by ray casting.

## The two counts

| permit county code | permits in snapshot | with surface coords | surface inside the *other* county |
|---|---|---|---|
| 317 (Martin) → inside Midland County | 9,384 | 8,979 | **0** |
| 329 (Midland) → inside Martin County | 9,840 | 9,187 | **0** |

Permits without surface coordinates are pre-GPS-trailer filings (nulls in the
'14' record); they cannot be tested and are excluded from the denominators.

## The 317-inside-Midland list

**Empty — no such well exists in the snapshot.** The closest Martin-coded
surface points to the Midland County boundary, all on the Martin side:

| API | operator | lease | well | permit issued | dist. to line |
|---|---|---|---|---|---|
| 42-317-46152 | PIONEER NATURAL RES. USA, INC. | BEAL-GRAHAM E26G | 107H | 2024-06-17 | 8 ft |
| 42-317-46154 | PIONEER NATURAL RES. USA, INC. | BEAL-GRAHAM E26H | 108H | 2024-06-17 | 12 ft |
| 42-317-46155 | PIONEER NATURAL RES. USA, INC. | BEAL-GRAHAM E26I | 109H | 2024-06-17 | 17 ft |

And the closest Midland-coded surface points to the Martin boundary:

| API | operator | lease | well | permit issued | dist. to line |
|---|---|---|---|---|---|
| 42-329-35115 | ENDEAVOR ENERGY RESOURCES L.P. | MABEE 13 | 3 (vertical) | 2018-07-19 | 139 ft |
| 42-329-45335 | OCCIDENTAL PERMIAN LTD. | SOUTH CURTIS RANCH | 0428JP | 2021-12-15 | 188 ft |
| 42-329-45329 | OCCIDENTAL PERMIAN LTD. | SOUTH CURTIS RANCH | 0418MP | 2021-12-14 | 221 ft |

## Routine or unusual?

Entirely routine. Across 18,166 coordinated permits in the two counties, the
county code follows the surface hole's geography in 100% of testable cases —
zero crossings in either direction. Operators on both sides drill right up to
the line (8 ft on the Martin side, 139 ft on the Midland side), so a
Martin-coded pad sitting just north of the boundary is the normal pattern, not
an anomaly. Easy Target is unremarkable: a Martin County pad (surface holes
6,900–9,100 ft north of the county line, Sec 19/30 Blk 39 T1N) with laterals
reaching ~2.5 mi south to bottomholes under northern Midland County. The 317
code is geographically correct for the drilling operation's surface location.

## What the three Easy Target dots are (RRC GIS layer field check)

The RRC Public GIS Viewer MapServer
(`https://gis.rrc.texas.gov/server/rest/services/rrc_public/RRC_Public_Viewer_Srvs/MapServer`)
carries two relevant point layers:

- **Layer 1, "Well Locations"** — fields include `GIS_LAT83`/`GIS_LONG83`,
  `GIS_LOCATION_SOURCE`, `GIS_SYMBOL_DESCRIPTION`. For 42-317-45816/45818/45820
  it plots 32.06922/-102.17267, 32.07058/-102.16656, 32.07165/-102.16198 —
  exactly the three dots used on the sheet — with source
  **"Operator reported location - D"** (D = directional), symbol "Oil/Gas Well".
- **Layer 9, "Horiz/Dir Surface Locations"** — for the same three APIs it plots
  32.11187/-102.18690, 32.10575/-102.17761, 32.10612/-102.17309, symbol
  **"Horizontal Drainhole"** — the true surface holes, in Martin County,
  matching the permit '14' trailer and the wellbore database
  (`api_county`/`loc_county`/`res_cnty_code` = 317, Sec 19/30 Blk 39 T1N).

The layer-1 dots match the permit '15' trailer **bottomhole** coordinates
(32.06912/-102.17092, 32.07078/-102.16378, 32.07154/-102.16050) to ~40–75 ft in
latitude and ~480–910 ft in longitude — the offset is the operator-reported
as-drilled directional location vs. the planned bottomhole. **The three dots
are the bottomhole (downhole/toe) locations, not the surface holes and not the
pads.** (Layer 10, "Horizontal/Directional Lines", holds the lateral geometry.)

## Correction to the item-27 side test

Item 27's county-line.md side test read these three layer-1 dots as the
*pads* and concluded the pads are "geographically in Midland County … only
+92 to +111 ft north of the section's north edge." That reading was wrong: the
dots are the bottomholes. The pads (surface holes) are in **Martin County**,
1.3–1.7 mi north of the county line. The item-27 headline stands — the
Midland–Martin line is ~5,400–6,800 ft (≈1.0–1.3 mi) north of Section 7's north
edge, and no boundary label goes on the sheet — but the "pads are in Midland
County" sentence is superseded. Note (c) in wells-notes.md (item 23) had it
right all along: pad in T1N (Martin), laterals reaching south under Sec 7 T1S.

Map implication: if the sheet captions the three Easy Target dots as pads or
surface locations, the caption should say bottomhole (or just "well") —
the pads themselves sit ~2.5 mi north, off the sheet's north edge in
Martin County.
