# wells.csv — reconciliation notes (2026-09-26)

## (a) API 42-329-47554 ("Well 1MS at east line") — source-log row 24 was wrong

Row 24 reported a producing oil well, API 42-329-47554, "Well 1MS at east line."
Re-check against the RRC Public GIS Viewer MapServer (2026-09-26):

- `API='4232947554'` and `API='42-329-47554'` on layer 1 (Well Locations): **0 hits**.
- Same queries on layers 9/10 (directional/horizontal): **0 hits**.
- `GIS_WELL_NUMBER LIKE '%1MS%'` restricted to the Section 7 bbox
  (32.0541–32.0720, -102.1762–-102.1550): **0 hits** (196 statewide, none here).

The API does not exist in RRC records and no 1MS-named well exists in the
section. Row 24's "Well 1MS" was a misread during the RRC viewer session —
**it is not added to wells.csv**, and should not be cited. The real producing
wells on the east side are 42-329-37587 (Well 4) and 42-329-31556 (Well 1).

## (b) Why three wells inside the section carry Martin County (42-317) APIs

The three horizontal wells plotted at the section's north edge —

| API | Well | Surface (RRC GIS) | Lateral azimuth |
|---|---|---|---|
| 42-317-45816 | 2H | 32.06922, -102.17267 | 166° (SSE) |
| 42-317-45818 | 4H | 32.07058, -102.16656 | 161° (SSE) |
| 42-317-45820 | 6H | 32.07165, -102.16198 | 342° (NNW) |

— carry county code 317 (Martin County) although their RRC-plotted surface
points fall in Midland County per Census TIGER (the Midland/Martin line at
this longitude lies between 32.085 and 32.09, ~1.3 mi north of the pads).

RRC's own documentation (Oil & Gas Division data dictionary, oga049.pdf,
"DA-PERMIT-COUNTY-CODE") states the rule:

> "THIS DATA ITEM CONTAINS THE COUNTY CODE OF THE COUNTY IN WHICH THE
> DRILLING OPERATION IS TO TAKE PLACE. THIS IS THE COUNTY AS IT HAS BEEN
> APPROVED BY THE RRC; IN SOME CASES, THE COUNTY REPORTED BY THE OPERATOR
> (AND STORED IN THE DATA ITEM DA-COUNTY-CODE) MAY NOT BE THE SAME AS WHAT
> IS STORED HERE. THE COUNTY CODE IDENTIFIES THE COUNTY OR COUNTIES IN
> WHICH A WELL BORE IS LOCATED."

So: **RRC assigns the API county code by the county in which the drilling
operation takes place, as approved by the RRC** — not by the operator's
reported county and not by the GIS-plotted surface point. The north-edge
pads/units sit against the county line (the 6H lateral heads NNW toward it),
and RRC approved these permits under Martin County.

Why RRC approved Martin County for these specific permits (unit acreage
spanning the line vs. a location-plat determination) is not stated in any
RRC public record I could retrieve — the wellbore detail endpoint was
unreachable. That case-level reason is **not explained** in public records.

Source: https://www.rrc.texas.gov/media/ezxjqdmn/oga049.pdf

## Other CSV caveats (unchanged)

- Row `42-329-xxxxx` (dry hole, 32.06533, -102.16395): RRC's GIS returns the
  API truncated to "329". Full API unconfirmed (RRC wellbore endpoint down);
  left as-is, not fabricated.
- `operator` column is blank for all rows: the RRC wellbore/lease endpoint
  failed during the pull. Not filled from guesses.
- `lateral_azimuth_deg` for horizontals was computed from the nearest
  RRC directional-line geometry, not from a confirmed well-to-line join —
  treat as approximate.

## Item 7 — RRC wellbore retry, attempt 1 (2026-09-26 ~21:55 CDT)
Endpoints tried, all failed from this network:
- gis.rrc.texas.gov/arcgis/rest/services (MapServer) — connection failed
- maps.rrc.texas.gov — connection failed
- webapps.rrc.texas.gov (wellbore/lease query) — connection failed
- mft.rrc.texas.gov (bulk data) — connection failed
- api.rrc.texas.gov — 403 on /, 404 on /api/
- webmaps/gisweb/gis2/services .rrc.texas.gov — all connection failed
- AGOL mirrors: only coastal RRC_Wells_Coastal (GLO) found; no Midland coverage.
`operator`, spud/completion, TD still blank for all 14 rows. Attempt 2 scheduled
2026-09-27 (different day per queue rule) before calling it blocked.

## Item 7 — RRC wellbore retry, attempt 2 (2026-09-27 ~06:42 CDT) — FAILED, BLOCKED

Endpoints tried:
1. **GIS Viewer (https://gis.rrc.texas.gov/GISViewer/)** — loads. Well search accepts 8-digit county+sequence format (e.g., "31745816") and zooms to the well; rejects 10-digit/dashed/14-digit formats ("Location not found"). Identify popup returns ONLY: API number, GIS well number, symbol description, location source — plus links to Well Logs, Drilling Permits, Disposal Permits. NO operator, spud date, completion date, or total depth shown. Popup says "(Identify the well to get completion information)" but no completion attributes display.
2. **Wellbore Query (webapps2.rrc.texas.gov/EWA/wellboreQueryAction.do)** — loads intermittently (timeouts/blank loads); when loaded, search criteria are Oil/Gas/Both, District, Lease No./Well ID, Type Well, County — NO API-number search field. Cannot look up specific wells.
3. **Completions Query (webapps.rrc.texas.gov/CMPL/publicHomeAction.do)** — never loads (navigation timeouts, blank page).
4. **Drilling Permits W-1 (webapps.rrc.texas.gov/DP/publicQuerySearchAction.do?countyCode=317&apiSeqNo=45816)** — never loads (blank page / timeouts).

Verdict: the only working RRC endpoint locates wells but exposes no operator/spud/completion/TD; all record systems holding those fields (webapps, webapps2) are unreachable from this environment. Two attempts on different days, both failed → **item 7 marked blocked [~]** per queue done-check. `operator`, spud/completion, TD remain blank for all 14 rows in wells.csv. A future attempt would need working webapps access or an alternate RRC data source.

## (c) Resolution of the Martin County (42-317) question — 2026-09-28 (queue item 23)

The three horizontals are OCCIDENTAL PERMIAN LTD.'s **EASY TARGET** pad (6-well
family: 2H = EASY TARGET 1993OP, 4H = EASY TARGET 3097OP, 6H = EASY TARGET
3099OP), EMMA (BARNETT SHALE) field. Per the ezrrc public API (RRC snapshot
current 2026-09-28), the approved county is **Martin** (canonical 48317) and
the surface sections are **Sec 19/30, Blk 39, T1N** — Martin County surveys.
That settles the question: the permit-approved drilling operation takes place
in Martin County (pad in T1N), with laterals reaching south under Section 7,
Blk 39, T1S (Midland County). The RRC-plotted surface points sit on the
Midland side only because GIS plot points follow the operator's reported
location; the DA-PERMIT-COUNTY-CODE (Martin, as approved) follows the
permit surveys. The operator-reported county and the approved county diverge
exactly as oga049.pdf allows. **No RRC email needed — explained from the
lease record.** Item 23 DONE.

## (d) API 42-329-xxxxx — declared unrecoverable (2026-09-28)

The suffix is blank in RRC's own authoritative systems (MapServer Layer 1:
`"API":"329","GIS_API5":" "`; statewide copies show `42329`; Socrata
uumf-5r4y.json shows the identical truncated record). No wellbore, casing,
plugging, or log records exist digitally; not an orphan well; no lease/operator
layer in the RRC public MapServer (all 41 layers reviewed). RRC Layer 1/24
facts: Dry Hole, Well No. 1, 32.06533251/-102.16394887 (NAD83, location from
"Commission's hardcopy map", UNIQID 662843), Sec 7 Blk 39 T1S, T&P RR Co.
Survey, A-34, Midland County, inactive. Fallback for the map: "Dry hole,
Well No. 1 — API not on file with RRC (location from Commission hardcopy
map)." Recommended next step (browser work): the RRC Statewide API Data
ASCII file via MFT GoDrive — the row is findable by survey/block/section/
well-number despite the blank API.

## (e) Permits that expired unspudded (2026-09-28)

42-329-40218 (perm. issued 2015-05-22, expired 2017-05-22), 42-329-40219
(issued 2015-05-26, expired 2017-05-26), and 42-329-36355 (issued 2009-08-13,
expired 2011-08-13) were never spudded. CSV `status` column left as
"permitted" — Claude's call whether to reflag.

## (f) Correction to the item-27 pad-location reading (2026-09-28, queue item 29)

Item 27's county-line side test treated the three RRC GIS dots
(32.06922/-102.17267, 32.07058/-102.16656, 32.07165/-102.16198) as the Easy
Target *pad* locations and concluded the pads are geographically in Midland
County, ~92-111 ft north of Section 7's north edge. That reading is
**superseded**. The dots are RRC Public GIS Viewer MapServer **Layer 1 ("Well
Locations")** points — source "Operator reported location - D" — i.e. the
**bottomholes** (they match the permit '15' trailer bottomhole coords to
~40-75 ft lat / ~480-910 ft lon). The actual surface holes are Layer 9
("Horiz/Dir Surface Locations") points at 32.106-32.112, Sec 19/30 Blk 39
**T1N — Martin County**, 6,900-9,100 ft north of the county line (see
phase2/county-coding.md). The 317 (Martin) code follows the surface geography
and is correct; a full-county test (8,979 Martin-coded + 9,187 Midland-coded
permits with coordinates) found **zero** surface points across the line in
either direction. The item-27 headline is unaffected: the Midland-Martin line
is ~5,400-6,800 ft (~1.0-1.3 mi) north of Section 7's north edge. Map
implication: the three dots on the sheet are bottomhole locations, not pads —
caption accordingly. Note (c) above (pad in T1N, laterals south under Sec 7)
remains correct.
