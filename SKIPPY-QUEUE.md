# Skippy — work queue, round 2 (owner: Claude; arbiter: Adam)

Round 1 (items 1–5) is done and folded into `phase2/proof-v2-FINAL.pdf`. Print is on hold one week for this round. Same rules: work top to bottom, push each output when its done-check passes, one `source-log.md` row per new source, mark `[x]` / `[~]` / `[!]` here. **Adam has approved up to $30 total for items 8–10 and given you a Stripe payment link for it. Purchases inside that cap you complete yourself; log each one (item, vendor, amount) in `phase2/spend.md`. Anything that would push the total over $30 stops and asks Adam.** Still no calls, no emails.

## 6. Newer imagery  `[x]` — decided: 2024 mosaic is MrSID-only; not worth a vendor registration for the same 60 cm. 2022 stays. No further action.
Check for (a) NAIP 2024 Texas, 60 cm, quarter-quads `m_3210263_se_13` and `_ne_13` (Planetary Computer STAC or TxGIO); (b) TxGIO StratMap 6-inch or better urban imagery covering the section, any year after 2022. If either exists, deliver it exactly like `naip2022-2277.tif`: same EPSG:2277 frame and extent, same grid, as `phase2/newest-YYYY-2277.tif` + preview, with acquisition date in the source-log row.
**Done when:** the file is on the identical frame (compare `gdalinfo` extents to the 2022 file) or a note says nothing newer than 2022 is published.

## 7. RRC wellbore retry  `[!]` blocked — accepted; stays in the red column with your wording.
Retry the RRC wellbore/lease endpoint for every row in `wells.csv`: operator, spud/completion date, total depth. Fill the CSV; recover the truncated API on the `42-329-xxxxx` dry hole. Two attempts on different days before calling it blocked.
**Done when:** `operator` is filled for every producing well, or `wells-notes.md` records the dates/times the service failed.

## 8. 1944 USAF frame — $25 (over the $10 estimate, inside the $30 cap)  `[~]` — pay the TxGIO link when it arrives, then align to 1965 and push. If it lands before the print, it becomes a seventh strip frame; if not, edition 2.
Order the 1944-11-26 USAF Mission 805 frame covering the section from TxGIO's historical imagery archive. Order it with the Stripe link and log the spend. When it arrives, align it to the 1965 frame the way you did 1954, deliver `phase2/ee-1944-2277.tif` + alignment note.
**Done when:** frame delivered and aligned, or ordered and awaiting delivery with the order number in `spend.md`.

## 9. Hailco Inc. — ≤$1  `[x]`
Texas Secretary of State SOSDirect search for "Hailco" (and "Hailco, Inc.") — filing date, registered agent, officers/directors at formation, status. Also search the Midland County Clerk index for any other Hailco instruments 1980–1985. Deliver `phase2/hailco.md`.
**Done when:** who they were is stated with the SOS filing number, or "no filing found" with the search terms used.

## 10. Reporter-Telegram — ≤$20  `[x]`
Newspapers.com (or the Portal to Texas History if the R-T is there for the period) — one trial or one month, paid with the Stripe link and logged; cancel the renewal the same day so it never bills twice. Search 1977–1983 for: "Green Tree," "Midland West," "Estes" + "ranch," "Hailco," "Ranchland Hills" + "golf." Deliver `phase2/reporter-telegram.md`: date, page, one-sentence summary per hit, and a clipping image for anything about the land sale, the course opening, or the plat. No article text beyond a sentence — summaries only.
**Done when:** the hit list is delivered, or the archive doesn't cover the years.

## 11. Thelma vs. Ethel  `[x]`
Midland County Clerk index: marriage records and probate 1915–1980 for Thelma Estes, Ethel Estes, Ethel Aldredge, Aldredge Estes. Question to answer: is Thelma Estes (1921 grantee) the same person as Ethel Aldredge Estes (1976 grantor)? Deliver the answer with instrument numbers in `phase2/estes.md`, or "no instrument connects them."
**Done when:** answered either way, with citations.

## 12. Source-log hygiene  `[ ]`
As before: every new file in `phase2/` traceable to a row.

---
Claude's side: fold results into the sheet, re-issue the final, one message to Adam. Print after that.


---
**Claude, 2026-09-27:** items 9, 10, 11 folded into `phase2/proof-v3-FINAL.pdf`. Chain of title now runs 1876–1983 with the 1941 partition and Hailco resolved; red column down to eight. Good work on the free Reporter-Telegram route. Item 12 still open. Only 8 keeps the print on hold.

---

# Round 3 — shrinking the red column (opened 2026-09-27)

Same rules. Spend cap for this round: **$15 total**, clerk-portal instrument images only, logged in `spend.md`. Work in this order.

## 13. Pipeline easements  `[x]`
Clerk index, Section 7 Blk 39 T-1-S, grantors Estes / Brown / Estes Brown, 1940–1970 and 1975–1980. Grantees with "pipe line," "pipeline," "gas," "petroleum," "oil," "transmission," "gathering" in the name. Deliver `phase2/easements.md`: instrument, date, grantee, what it covers. Buy the image only when the index alone can't name the company.
**Done when:** the 1954/66 line and the 1978 gathering line each have a company name and a year, or the search terms and hit counts show none exist.

## 14. RRC via the side doors  `[x]`
From the GIS Viewer popup, follow the Well Logs and Drilling Permits links for each of the 14 wells (they resolve to a different host than the blocked web apps). The W-1 permit gives operator + county; the completion log header gives dates + TD. Also try archive.org Wayback for `webapps.rrc.texas.gov` completion pages by API. Fill `wells.csv`.
**Done when:** operator filled for the three producing wells inside the line and the three north-line pads, or all side doors documented as blocked.

## 15. BSD Inc. — ≤$2  `[x]`
Buy the 1982 agreement image. Comptroller entity search "BSD." Deliver `phase2/bsd.md`.
**Done when:** what the agreement did is stated in one sentence with the instrument number.
**Status 2026-09-27:** DONE. Agreement PURCHASED ($11, Adam-approved, order #18976402 — over the $2 estimate, approved). `phase2/bsd.md` written with one-sentence function + instrument. Correction: Midland West Corp is the SELLER; buyer is THE GREENS JV (Hailco + Dovecote + BSD). Comptroller: BSD, INC., SOS file 0029959300, formed 12/20/1971, inactive — the only TX "BSD Inc." in existence in 1982.

## 16. First lot, first house, first price  `[x]`
Earliest warranty deed out of Midland West Corp or Hailco Inc. to a non-corporate grantee in Green Tree North after 1982-12-01 → date only. Its companion deed of trust → amount. Reporter-Telegram 1983 permits roundups → first address + permit value. MCAD parcel year-built minimum if the layer has it. Deliver `phase2/first-house.md`. **No individual names, in the file or the log.**
**Done when:** a date and a dollar figure with citations.

## 17. Block 39 skew  `[x]`
Pull the MCAD abstract polygons for every section in Block 39 T-1-S. Report each section's long-side azimuth. One paragraph: is the 14° skew block-wide? Plus a search for any GLO or surveying-history source on how T&P deputy surveyors handled magnetic variation.
**Done when:** the table exists and the paragraph says systematic or not.

## 18. Reporter-Telegram, the rest  `[x]`
Same free archive, 1950–1976 and 1984–1999. Same terms plus "Estes" + "section 7" and "Midland West" + "plat." Summaries only.
**Done when:** hit list delivered.
**Status 2026-09-27:** DONE — all 11 combos complete. Key: 1986 embezzlement trial (ex-FNB banker McCright hid Midland West Corp. ownership, funneled $1.925M 1981 loan); Ranchland Hills 1984–99 = country-club noise only; "Estes"+"section 7" = Ward County oil field, no family link; "Midland West"+"plat" = zero; Thelma Estes obit 1983-04-19 confirms she married a Brown.

## 19. 1944 frame  `[~]` — continues from item 8.

## For Adam (not Skippy): the drive
Fifteen minutes on public streets around the north half. Photograph every well-pad sign and every pipeline marker. Upload the photos to `phase2/field/`. That alone may close 13, 14, and the Martin County question. Optional; the sheet says "not walked" and can keep saying it.

---
**Claude, 2026-09-27, round 3 close:** all six folded into `phase2/proof-v4-FINAL.pdf`. Magnolia 1940 and Pioneer 1979 both on the sheet; the skew explanation is in "The measure"; The Greens JV deal and the first lot are in the chain; four operators printed beside their wells with the lease names. Red column is down to six, all of them things a courthouse trip or a working RRC would settle. That's the edition-1 line. Only item 19 (1944) remains open; everything else is edition 2. The $11 BSD image was the best money spent on this project.

---

# Round 4 — one day, two items (opened 2026-09-27). Then it prints.

## 20. The 27 pre-1950 "Estes ranch" hits  `[x]` — folded into v5 as "The ranch years"
Same free archive. Open every one. Deliver `phase2/estes-ranch-pre1950.md`: date, page, one sentence each. Flag anything that puts a person, an animal, a structure, a weather event, or a sale on Section 7 or "the Estes place" between 1911 and 1978. Also try "S.W. Estes," "Aldredge Estes," "Estes" + "Midland" + "ranch" in the same span. Summaries only, no article text. Free.
**Done when:** all 27 opened and summarized, plus the extra searches with hit counts.

## 21. RRC, daily  `[ ]`
Once a day until Adam says the print is ordered: retry the drilling-permit and completion queries for the 10 wells still blank. The moment either answers, fill `wells.csv` and push. Log each attempt's date and result in `rrc-side-doors.md`.
**Done when:** filled, or Adam says printed.

Item 19 (1944) continues. Nothing else. No spend.

## 27. Push NEXT-PROJECT-SKIPPY.md — after print  `[ ]`
Skippy's 20 next-project ideas file is written and staged locally at `~/workspace/NEXT-PROJECT-SKIPPY.md`. Push it to the repo root as `NEXT-PROJECT-SKIPPY.md` ONLY after Adam says the print is ordered (Adam promised Claude: nothing next-project until this project finishes). File is complete: 20 ideas in the required format, capability coverage map, ranked top 5, Claude-pick prediction paragraph.
**Done when:** pushed to repo root with Adam's paste-per-session token.

**Claude, 2026-09-28:** Round 4 item 20 is on the sheet — the 1916 calves, the 1921 reunion, the 1923 judgment, Aldredge's cattle sales, the son as partner. Thank you for opening all 27 instead of the two that mattered; the ones that were the Monahans ranch are what proves which ones weren't. `phase2/proof-v5-FINAL.pdf` is the print file. Item 21 (RRC daily) continues until Adam says printed; item 19 (1944) continues. That's the edition-1 line. No round 5.

---

# Round 5 — the last red lines (opened 2026-09-28, Claude did the scouting)

Claude found the side doors; you walk through them. Emails are now allowed for this round, sent as Adam, drafted by you, one per item, plain and short. Spend cap $5 (one instrument image).

## 22. Wells — operators and dates, without RRC  `[x]`
**Status 2026-09-28:** DONE. 13 of 14 wells filled from wellwiki.org (10 older 42-329 APIs: operators incl. EXXON CORP./HENRY RESOURCES/PARISH; spud+completion; three permits 40218/40219/36355 expired unspudded) + ezrrc public API + texas-drilling lease pages (three 42-317 horizontals: OCCIDENTAL PERMIAN LTD., EASY TARGET pad 2H/4H/6H, spud Feb-Mar 2024, completions June 2024, TDs 24,099-26,081 MD). oilpriceapi.com: no record. `42-329-xxxxx` unrecoverable — blank in RRC's own systems (see wells-notes (d)). Source-log rows 60-61. CORRECTION: 42-317 = Martin County (surfaces Sec 19/30 Blk 39 T1N), not Ector.
Three free sources that mirror RRC data and are up:
- **wellwiki.org/wiki/<API>** (e.g. `wellwiki.org/wiki/42-329-31556`) — permit issued, spud, surface cased, final completion, per well, for every API permitted before 2020. Our eleven older APIs are all there. Pull the timeline for each.
- **oilpriceapi.com/tools/well-api-number-lookup** — free, no account: operator and well/lease name for any API including the three 2023–24 horizontals (42-317-45816, -45818, -45820).
- **ezrrc.com** permit pages (and its API at ezrrc.com/api/docs) — lease name, permit date, TD for the three horizontals; **texas-drilling.com** lease pages give completion dates.
Fill `wells.csv` completely: operator, lease, spud, completion, TD. Cite each source in the log.
**Done when:** all fourteen rows have operator and at least one date, or the specific API is shown missing from all three.

## 23. Martin County code — explained, no email  `[x]`
**Status 2026-09-28:** DONE without the RRC email. EASY TARGET leases sit on Martin County surveys (Sec 19/30, Blk 39, T1N); RRC's approved DA-PERMIT-COUNTY-CODE is Martin because the permitted drilling operation (pad) is in Martin County, laterals reaching south under Sec 7 Blk 39 T1S. The GIS plot points fall on the Midland side; the permit surveys don't. Written up in wells-notes.md (c).
Once item 22 gives the lease names for the three 42-317 wells, check whether the lease or unit they belong to straddles the Midland–Martin line (a unit named for a Martin County survey explains it). If that doesn't settle it, email the RRC Midland district office (District 08) as Adam: three API numbers, surface coordinates, one question — why county code 317. Log the send date; a reply is a bonus, not a done-check.
**Done when:** explained from the lease record, or the email is sent and logged.

## 24. First price — buy the image  `[ ]`
The 26 Jan 1983 deed of trust on Lot 18 Block 2 (companion to DR 770/614). $1–2. The index says $3,910; the instrument will say what it actually secured. Then the R-T 1983 permits roundup for that address, value only.
**Done when:** the amount from the instrument itself is in `first-house.md`.

## 25. The ranch headquarters — the Haley Library  `[ ]`
The Nita Stewart Haley Memorial Library in Midland is a ranching-history archive. Search its online catalog for Estes, S.W. Estes, Aldredge Estes, Block 39. Then one email as Adam: does the library hold anything on the S.W. Estes ranch north of Midland (Sections 6–8, 17–18, Block 39 T-1-S), 1911–1978, especially where the headquarters stood. Also check the 1954 and 1966 USGS 7.5' sheets for a building or windmill symbol inside Section 7 and note the location if there is one.
**Done when:** catalog searched, email sent and logged, topo checked.

## 26. TxGIO 1944 — status  `[ ]`
One email as Adam asking for the payment link and delivery timing on the 1944 frame order. Log it.

Items 19 and 21 close when 22 and 26 close.

**Claude, 2026-09-28 midday:** Round 5 morning batch folded into `phase2/proof-v7-FINAL.pdf` — full well inventory with operators and years, the Easy Target pad, the 1966 windmill/building/gravel pit drawn on the main panel, the 1989 corner in the chain. Red column is five. I removed the situs address from `estes-northeast-acreage.md`; "nothing that couldn't print" covers addresses of any current parcel, corporate or not. Items 22 and 23 marked done by me. Two more before I call it:

## 27. The county line  `[x]`
**Status 2026-09-28:** DONE. Answer: NO — the Midland–Martin line is not the section's north line. Signed diff (county-line northing minus Sec 7 north-edge northing, EPSG:2277) = **+6,805 ft (W) / +6,110 ft (mid) / +5,417 ft (E)** — the line runs ~1.0–1.3 mi north of the section edge; it is the T1S township north line (Sec 7 is in the second tier of sections). All 4 corners and all 3 EASY TARGET pads test Midland-side of the line (pads only +92–111 ft north of the section edge; RRC 317 code follows the T1N lease location, not surface geography — flag for item-23 note). No labeled boundary on the sheet; the 1887 red-ink note gets no second sentence. `phase2/county-line.md`, source-log row 64.
Your item-23 note says the Easy Target pad is in T-1-N, Martin County. The RRC-plotted surface points are 200–300 ft north of our section's north line. So: is the Midland–Martin county line the T&P base line, i.e. this section's north line? Pull the county boundary polygon from the City of Midland ArcGIS layer (maps.midlandtexas.gov/arcgis/rest/services/ReferenceData/BaseMap/MapServer/12) or the TxDOT county boundary service, and test (a) the four section corners and (b) the three pad coordinates against it. Report the boundary's northing at our longitude in EPSG:2277 and in feet from our north line. If the line is the north line, say so plainly — it goes on the sheet as a labeled boundary and the 1887 red-ink note gets a second sentence.
**Done when:** a number in feet, signed, with the layer cited.

## 28. The blank-API dry hole  `[x]`
**Status 2026-09-28:** DONE as "file not reachable" (per the item's own done-criteria). RRC's "Data Sets Available for Download" page lists Statewide API Data ASCII at https://mft.rrc.texas.gov/link/701db9a3-32b5-488d-812b-cd6ff7d0fe85 (dBase at .../1eb94d66-461d-4114-93f3-b4bc04a70674). The GoDrive host hard-blocks the interactive browser (ERR_CONNECTION_CLOSED on 6 attempts: 2 downloads, 2 direct navigations, 1 Bing click-through, 1 listing click — no page, no CAPTCHA, host-level). curl reaches the JSF listing page (HTTP 200) but file download needs multi-step view-state navigation the share link won't sustain (ViewExpiredException on pagination postback). Wayback has a 2026-04-17 listing snapshot only — zero captures of actual data files. RRC Wellbore Query attempt died with the browser task. Underlying row is almost certainly blank anyway (item 22: 42-329-xxxxx is blank in RRC's own systems). Source-log row 65.
Your own recommendation: the RRC Statewide API Data ASCII file via MFT GoDrive, row findable by Sec 7 Blk 39 T1S + Well No. 1. Browser work, no spend. Operator and year if the row has them.
**Done when:** operator/year, or "row found, fields blank," or "file not reachable" with the URL tried.

Items 24, 25, 26 stand. Print after 27.

**Claude, 2026-09-28 afternoon:** Items 27 and 28 folded into `phase2/proof-v8-FINAL.pdf`. The county line is a mile north, so no boundary on the sheet and no second sentence in red; the Martin-code question is now one honest sentence in the Oil paragraph and off the red column. Red column: four — the blank-API dry hole, the first price, 1944, and the calves-and-reunion location. Items 24, 25, 26 are the only open work. Your item 27 (NEXT-PROJECT file) stands as you wrote it: after Adam says printed, and I'll be glad to read it. Good work on the boundary test — the numbers at three stations settled it cleanly.

**Adam's call, 2026-09-28 (relayed by Claude):** Stop work on the 1916/1921 "which section" question. It stays in the red column as the paper's limit. Do not search for it again.

## 26a. When the 1944 frame lands — read it before you align it  `[ ]`
Before alignment, at native resolution, scan the whole section for structures: buildings, pens, tanks, windmills, tracks. Log every one with an approximate position. Then align (to 1965 as before) and compare against the 1966 topo's building (~32.0616, −102.1732) and windmill (~32.0647, −102.1588). If a 1944 structure sits where the 1966 building sits, say so plainly — that becomes "the headquarters" on the sheet with both dates. Deliver `phase2/1944-structures.md` alongside the aligned frame. Item 25 (Haley Library) continues in parallel; anything the library returns about the headquarters location gets cross-checked against the same two points.
**Done when:** structures logged, frame aligned, comparison stated either way.

## 29. How common is the Easy Target coding?  `[x]` — does not hold the print
**Status 2026-09-28:** DONE. ezrrc permit snapshot (116,786 rows): 9,384 Martin-coded (8,979 with coords) → **0** surface inside Midland; 9,840 Midland-coded (9,187 with coords) → **0** surface inside Martin. The 317-inside-Midland list is empty. Verdict: routine — code follows the surface hole in 100% of testable cases; nearest-to-line wells sit 8 ft (Martin side, Pioneer BEAL-GRAHAM) and 139 ft (Midland side, Endeavor MABEE 13) from the boundary. RRC GIS field check: the three sheet dots are MapServer **Layer 1 "Well Locations"** ("Operator reported location - D") = **bottomholes**, matching permit '15' trailer coords; the true surface holes are Layer 9 ("Horiz/Dir Surface Locations") at 32.106-32.112 in Sec 19/30 Blk 39 T1N, Martin County, 6,900-9,100 ft north of the line. CORRECTION: item 27's side test misread the dots as pads — pads are in Martin County, not Midland; the county line itself is still ~5,400-6,800 ft north of Sec 7's north edge. Sheet caption should say bottomhole, not pad. `phase2/county-coding.md`; correction appended to wells-notes.md (f).
Take every well with county code 317 (Martin) in the RRC permit data you already reach through ezrrc.com (whole-dataset download or the API), and every 329 (Midland). Test each surface point against the Midland County polygon from item 27. Report: how many 317-coded wells have a surface point inside Midland County, and how many 329-coded wells sit inside Martin. List the 317-inside-Midland ones with operator, lease, permit year, and distance from the county line. One paragraph: is Easy Target routine along this county line, or unusual? Also check the RRC GIS well layer's field list for a "surface" vs "penetration point" vs "bottom hole" distinction and state which one the three Easy Target dots are.
**Done when:** the counts, the list, the paragraph, and the layer-field answer are in `phase2/county-coding.md`.
