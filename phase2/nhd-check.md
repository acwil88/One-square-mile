# NHD hydrology check — "waters of North Concho" (§3.3)

**Question:** W.C. Powell's 1876 field notes place Section 7, Block 39, T-1-S "on the waters of North Concho." Is that hydrologically true?

**Answer: No — not by modern mapping.** The section drains east via Midland Draw into **Beals Creek**, which flows directly into the **Colorado River**. The North Concho River is nowhere on the drainage path. Powell's 1876 label is best read as a loose or mistaken 19th-century description of the upper-Colorado tributary country, not a hydrologic fact. (Why he wrote it — loose regional naming vs. error — is inferred, not verified.)

## Downstream path (traced in NHDPlus via EPA WATERS)

Starting at the section center (32.061, -102.167), point-indexed to the Midland Draw flowline, then walked downstream along the NHDPlus network (hydroseq → dnhydroseq, jumped by level path):

| # | Waterbody (NHD) | NHDPlus COMID | Reach code | Notes |
|---|---|---|---|---|
| 1 | Midland Draw (reach unnamed in NHD; HUC10 "Whalen Lake-Midland Draw") | 5688042 | 12080005000009 | At the section; order 1; hydroseq 630055334 |
| 2 | Unnamed reach | (level path 630017264, 10 segs) | 12080005000006 | order 2 |
| 3 | Unnamed reach | (level path 630010875, 24 segs) | 12080004000688 | order 4 |
| 4 | **Beals Creek** | 5715109 (downstream-most seg) | 12080007000145 | order 5; 113 segs on this level path |
| 5 | **Colorado River** (terminal) | 3766342 | 12090302000369 | order 6; terminalflag=1; hydroseq 630001920 |

HUC8s crossed: 12080005 "Johnson Draw" → 12080004 "Mustang Draw" → 12080007 "Beals" → 12090302 (Colorado). No Concho-subbasin HUC is entered at any point. Total downstream path length from the section reach: ~1,440 km to the terminal Colorado River flowline.

## How verified

- **EPA WATERS Point Indexing Service** (`ofmpub.epa.gov/waters10/PointIndexing.Service`) snapped POINT(-102.167 32.061) to COMID 5688042, reach 12080005000009, fcode 46003 (stream/river).
- **NHDPlus MapServer** (`watersgeo.epa.gov/arcgis/rest/services/NHDPlus/NHDPlus/MapServer`, layers 2 = Network Flowline, 7 = Subwatershed HUC12): walked the network downstream via `dnhydroseq`/`dnlevelpathid`; every step has `terminalflag=0` until the Colorado River reach. HUC12 at section center: 120800050107 "Thomas Windmill"; HUC10: 1208000501 "Whalen Lake-Midland Draw"; HUC8: 12080005 "Johnson Draw".
- The EPA `UpstreamDownstream.Service` on ofmpub is currently unauthorized (ORDS-22001), so the trace was done manually through the MapServer flowline network instead — same underlying NHDPlus dataset.
- Cross-check: the HUC hierarchy independently agrees — the section's HUC8/10/12 chain contains no North Concho unit, and the traced path's HUC8 sequence never enters one.

## Verified vs. inferred

- **Verified:** the full downstream flowline path (table above); the HUC assignments; the terminal point being the Colorado River; that no reach on the path is named North Concho.
- **Inferred:** that the watercourse at the section is "Midland Draw" (NHD leaves these reaches unnamed; the name comes from the HUC10 "Whalen Lake-Midland Draw" and the historical topo labels); why Powell wrote "North Concho" in 1876 (loose naming vs. error — unknown).
- **Margin-ready language:** "Powell's 1876 notes call this 'waters of North Concho'; modern mapping drains it to the Colorado via Midland Draw and Beals Creek."

## Sources

- https://ofmpub.epa.gov/waters10/PointIndexing.Service (point → COMID 5688042)
- https://watersgeo.epa.gov/arcgis/rest/services/NHDPlus/NHDPlus/MapServer (flowline network walk, WBD HUC names)
- GLO patent file, field notes of W.C. Powell, 2/1/1876 ("waters of North Concho") — `~/workspace/one-square-mile/phase2/glo-patent-file.txt`
