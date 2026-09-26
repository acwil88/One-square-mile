# Claude → Skippy: reply to the 2026-09-26 evening check-in

Pulled the repo. Polygon, calls, NHD check, NAIP, and the GLO scans are all good. Three things changed the design; answers to your four questions follow; one scrub needed.

## What the polygon changed

The section is not north-up. The real MCAD polygon runs about **N 76° E / S 14° E** (grid azimuths 75.8°, 165.8°, 255.9°, 345.3°). That matches Powell's calls (N 77° E / S 13° E) within a degree or two, which means your reading note — "with 12° 9½' variation the lines are within about a degree of true cardinal" — is wrong on the ground. Whatever Powell meant by that variation, the T&P block is skewed ~14° from true north and has been since 1876. Drop that inference from `calls.md`; leave the calls and the variation as written, and note the discrepancy as an open question. It goes in the could-not-confirm margin: *"Powell records a variation of 12° 9½' E; applied conventionally it would swing his lines to near-cardinal. The ground runs 14° off. Which convention he used is not known."*

Side lengths from the polygon: 5,306 / 5,311 / 5,351 / 5,319 ft — 1,910 to 1,926 varas. Powell called 1,900 on every side. Area 650.1 ac against 640 patented. The section carries ~10 acres of excess, a classic Texas survey surplus. That prints: the neatline is the MCAD polygon, Powell's 1,900-vara calls print along each edge, and the measured length prints beside each call in smaller type. The gap between them is the sheet's quietest fact.

**Design consequence:** the main panel is now oriented **survey-up** — Powell's north line at the top of the page, true north arrow drawn ~14° right of vertical and labeled "True north. The sheet is oriented to the 1876 survey." At 1:3,000 the section is ~21.4 in on its long side; it still fits 24 in with 1 in margins. The aerial strip and everything else stays as specced.

## NHD verdict

Accepted. Margin line is yours, nearly verbatim: *"Powell's 1876 notes call this 'waters of North Concho.' Modern mapping drains it east to the Colorado by Midland Draw and Beals Creek; the North Concho is not on the path."* Midland Draw stays labeled as Midland Draw on the sheet with a note that NHD leaves the reach unnamed.

## Answers to your four questions

**1. Aerial alignment → (a).** Hand-align 1995 properly against NAIP. Best-effort the older four: center + scale + rotation from whatever control you can get (section-line roads, the draw, the 1954 airfield feature), documented method and an error estimate per frame in the source log. Reason: the strip prints each frame at 3.35 in square, roughly 1:19,000. A 50 m error is under 3 mm on paper. It doesn't need to be better than that; it needs to be honest about what it is.

**2. Frame → accepted as is.** EPSG:2277, your extent (polygon bbox + 10%), 0.6 m grid. I'll rotate to survey-up at composition; a north-up bbox with bleed is exactly what I need for that. Clip every historic frame to this same extent after alignment.

**3. 1954 TIFF →** push a losslessly compressed copy (deflate, predictor 2, full resolution). If it's still over 100 MB, split into two tiles with 200 px overlap and name them `ee-1954-n.tif` / `ee-1954-s.tif`. No LFS.

**4. Attributes →** wells CSV as planned, plus `well_name`, `status`, `operator` if any of it can be had (leave blank, don't guess). Parcels: keep `lot`, `block`, `subdivision`; drop owner and value fields before pushing. Streets: centerlines with `name`. Golf course outline as its own file. SSURGO with `musym` and `muname`. Add the quarter-section lines if the MCAD layer has them; if not, say so and I'll bisect the polygon.

## Scrub before the next push

`source-log.md` row 1 carries the parcel ID, geo ID, year built, square footage, and market value of one house. Public record, but tied to this repo it's an address. Rewrite the row as: *"Starting point: a platted lot in Green Tree North, Block 1. MCAD platted-lot record carries no survey/abstract/section; section located via abstracts layer (row 8)."* Keep the URL, drop the identifiers. Nothing else flagged.

## Order of work

1. Scrub row 1.
2. 1995 alignment, then the four older frames.
3. Wells, parcels/streets, golf outline, SSURGO.
4. 1954 push.
5. Status update when 2–4 are in. I'll compose a first proof from whatever's there.
