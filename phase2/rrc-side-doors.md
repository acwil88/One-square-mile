# RRC side doors (queue item 14, 2026-09-27)

**Question:** can operator/spud/completion/TD be recovered via alternate routes, now that the main RRC webapps are down?

## Side door 1: Well Logs (WORKS, partially)

The GIS Viewer Identify popup's "Well Logs" link resolves to **https://rrcsearch3.neubus.com/search-profile?profileId=15** (Neubus "neuDocs Enterprise Record Search", Well Log profile). Live and reachable — the 8-digit API search works.

**Found (4 wells):** operator and TD (bottom log depth) recovered from log metadata.

| API | Operator | TD (ft) | Lease / log |
|-----|----------|---------|-------------|
| 42-329-37587 | PETROPLEX ENERGY INC | 10,986 | ESTES BUTTON 7-8 UNIT #4, resistivity + neutron, 09/24/2011 |
| 42-329-35205 | PETROPLEX ENERGY INC | 11,493 | ESTES BUTTON 7 #3, neutron, 02/23/2005 |
| 42-329-39287 | ENDEAVOR ENERGY RESOURCES L.P. | 11,379 | STEPHENS FEE '6' #3, neutron, 06/14/2017 |
| 42-329-36421 | FASKEN OIL AND RANCH LTD | 10,711 | ALDRIDGE #1208R, resistivity + neutron, 12/29/2009 |

**Not found (9 wells):** 42-317-45816, 42-317-45818, 42-329-30936, 42-329-36101, 42-329-31556, 42-329-40218, 42-317-45820, 42-329-36355, 42-329-40219 — Neubus returned "No records found!" for each.

**Limitations:** the Neubus TIF viewer errored and downloads failed, so log-header spud/completion dates remain unavailable. TDs are bottom log depths from metadata, not certified well TDs.

## Side door 2: Drilling Permits (BLOCKED)

Popup link → `https://webapps.rrc.texas.gov/DP/publicQuerySearchAction.do?...` — **unreachable** (browser error, same webapps outage as Round 2). W-1 operator data not recoverable this route.

## Side door 3: Wayback Machine (EMPTY)

- The exact DP query URLs for our APIs were never archived.
- Of 916 archived `webapps.rrc.texas.gov/DP/` URLs: zero captures for countyCode=317 or 329 queries.
- Of 1,699 archived `webapps.rrc.texas.gov/CMPL/` URLs: only one API-based completion search ever archived (apiNo=39531827, not ours); the rest use opaque packetSummaryIds unmappable to our APIs.

## Result

Operators + TDs recovered for 4 of 14 wells (all in-county Midland 329 verticals; `wells.csv` updated). The 42-317 north-line horizontals have no Neubus logs. Spud/completion dates remain unrecoverable — no side door yields them. Item closed as substantially answered: the side doors that open are documented, the ones that don't are documented as blocked.
