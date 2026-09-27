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
