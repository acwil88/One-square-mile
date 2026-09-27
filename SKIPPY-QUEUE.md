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

## 13. Pipeline easements  `[ ]`
Clerk index, Section 7 Blk 39 T-1-S, grantors Estes / Brown / Estes Brown, 1940–1970 and 1975–1980. Grantees with "pipe line," "pipeline," "gas," "petroleum," "oil," "transmission," "gathering" in the name. Deliver `phase2/easements.md`: instrument, date, grantee, what it covers. Buy the image only when the index alone can't name the company.
**Done when:** the 1954/66 line and the 1978 gathering line each have a company name and a year, or the search terms and hit counts show none exist.

## 14. RRC via the side doors  `[ ]`
From the GIS Viewer popup, follow the Well Logs and Drilling Permits links for each of the 14 wells (they resolve to a different host than the blocked web apps). The W-1 permit gives operator + county; the completion log header gives dates + TD. Also try archive.org Wayback for `webapps.rrc.texas.gov` completion pages by API. Fill `wells.csv`.
**Done when:** operator filled for the three producing wells inside the line and the three north-line pads, or all side doors documented as blocked.

## 15. BSD Inc. — ≤$2  `[ ]`
Buy the 1982 agreement image. Comptroller entity search "BSD." Deliver `phase2/bsd.md`.
**Done when:** what the agreement did is stated in one sentence with the instrument number.

## 16. First lot, first house, first price  `[ ]`
Earliest warranty deed out of Midland West Corp or Hailco Inc. to a non-corporate grantee in Green Tree North after 1982-12-01 → date only. Its companion deed of trust → amount. Reporter-Telegram 1983 permits roundups → first address + permit value. MCAD parcel year-built minimum if the layer has it. Deliver `phase2/first-house.md`. **No individual names, in the file or the log.**
**Done when:** a date and a dollar figure with citations.

## 17. Block 39 skew  `[ ]`
Pull the MCAD abstract polygons for every section in Block 39 T-1-S. Report each section's long-side azimuth. One paragraph: is the 14° skew block-wide? Plus a search for any GLO or surveying-history source on how T&P deputy surveyors handled magnetic variation.
**Done when:** the table exists and the paragraph says systematic or not.

## 18. Reporter-Telegram, the rest  `[ ]`
Same free archive, 1950–1976 and 1984–1999. Same terms plus "Estes" + "section 7" and "Midland West" + "plat." Summaries only.
**Done when:** hit list delivered.

## 19. 1944 frame  `[~]` — continues from item 8.

## For Adam (not Skippy): the drive
Fifteen minutes on public streets around the north half. Photograph every well-pad sign and every pipeline marker. Upload the photos to `phase2/field/`. That alone may close 13, 14, and the Martin County question. Optional; the sheet says "not walked" and can keep saying it.
