# Skippy — work queue, round 2 (owner: Claude; arbiter: Adam)

Round 1 (items 1–5) is done and folded into `phase2/proof-v2-FINAL.pdf`. Print is on hold one week for this round. Same rules: work top to bottom, push each output when its done-check passes, one `source-log.md` row per new source, mark `[x]` / `[~]` / `[!]` here. **Adam has approved up to $30 total for items 8–10 and given you a Stripe payment link for it. Purchases inside that cap you complete yourself; log each one (item, vendor, amount) in `phase2/spend.md`. Anything that would push the total over $30 stops and asks Adam.** Still no calls, no emails.

## 6. Newer imagery  `[ ]`
Check for (a) NAIP 2024 Texas, 60 cm, quarter-quads `m_3210263_se_13` and `_ne_13` (Planetary Computer STAC or TxGIO); (b) TxGIO StratMap 6-inch or better urban imagery covering the section, any year after 2022. If either exists, deliver it exactly like `naip2022-2277.tif`: same EPSG:2277 frame and extent, same grid, as `phase2/newest-YYYY-2277.tif` + preview, with acquisition date in the source-log row.
**Done when:** the file is on the identical frame (compare `gdalinfo` extents to the 2022 file) or a note says nothing newer than 2022 is published.

## 7. RRC wellbore retry  `[ ]`
Retry the RRC wellbore/lease endpoint for every row in `wells.csv`: operator, spud/completion date, total depth. Fill the CSV; recover the truncated API on the `42-329-xxxxx` dry hole. Two attempts on different days before calling it blocked.
**Done when:** `operator` is filled for every producing well, or `wells-notes.md` records the dates/times the service failed.

## 8. 1944 USAF frame — $10  `[ ]`
Order the 1944-11-26 USAF Mission 805 frame covering the section from TxGIO's historical imagery archive. Order it with the Stripe link and log the spend. When it arrives, align it to the 1965 frame the way you did 1954, deliver `phase2/ee-1944-2277.tif` + alignment note.
**Done when:** frame delivered and aligned, or ordered and awaiting delivery with the order number in `spend.md`.

## 9. Hailco Inc. — ≤$1  `[ ]`
Texas Secretary of State SOSDirect search for "Hailco" (and "Hailco, Inc.") — filing date, registered agent, officers/directors at formation, status. Also search the Midland County Clerk index for any other Hailco instruments 1980–1985. Deliver `phase2/hailco.md`.
**Done when:** who they were is stated with the SOS filing number, or "no filing found" with the search terms used.

## 10. Reporter-Telegram — ≤$20  `[ ]`
Newspapers.com (or the Portal to Texas History if the R-T is there for the period) — one trial or one month, paid with the Stripe link and logged; cancel the renewal the same day so it never bills twice. Search 1977–1983 for: "Green Tree," "Midland West," "Estes" + "ranch," "Hailco," "Ranchland Hills" + "golf." Deliver `phase2/reporter-telegram.md`: date, page, one-sentence summary per hit, and a clipping image for anything about the land sale, the course opening, or the plat. No article text beyond a sentence — summaries only.
**Done when:** the hit list is delivered, or the archive doesn't cover the years.

## 11. Thelma vs. Ethel  `[ ]`
Midland County Clerk index: marriage records and probate 1915–1980 for Thelma Estes, Ethel Estes, Ethel Aldredge, Aldredge Estes. Question to answer: is Thelma Estes (1921 grantee) the same person as Ethel Aldredge Estes (1976 grantor)? Deliver the answer with instrument numbers in `phase2/estes.md`, or "no instrument connects them."
**Done when:** answered either way, with citations.

## 12. Source-log hygiene  `[ ]`
As before: every new file in `phase2/` traceable to a row.

---
Claude's side: fold results into the sheet, re-issue the final, one message to Adam. Print after that.
