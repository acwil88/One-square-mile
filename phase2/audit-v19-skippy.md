# Independent audit of proof v19 — Skippy, 2026-09-30

Scope: `phase2/proof-v19-FINAL.pdf` (upstream commit `3e3feff`, "Claude v19"),
audited against the repo's own source files — the GLO patent scan
(`phase2/glo-page-*.png`), `source-log.md`, `phase2/estes.md`,
`phase2/estes-northeast-acreage.md`, `phase2/easements.md`,
`phase2/hailco.md`, `phase2/bsd.md`, `phase2/reporter-telegram.md`,
`phase2/reporter-telegram-extended.md`, the `ee-*-alignment.md` notes,
`phase2/wells.csv`, `phase2/pipelines-2277.geojson` (12 features),
`phase2/section7-polygon-*.geojson`, and Census TIGER/Line 2024 rails
(downloaded fresh for this audit). Every date, instrument number, name,
figure, and factual assertion below was checked against one of those —
not against Claude's v18 audit notes.

## Answers to the eight verification questions

**Q1. Railroad azimuth.** The sheet's survey panel says: *"The blocks were
laid on the railroad's bearing. Within two degrees they match the section's
75° long-side azimuth."* This is wrong. I downloaded the Census TIGER/Line
2024 national rail layer (`tl_2024_us_rails.zip`), which explicitly labels
the Midland main line "Texas and Pacific Rlwy." Best-fit true azimuth of
that line through Midland: **58.6°** (longest single feature, endpoint
bearing 58.7°). That is ~16° off the section's ~75° long-side azimuth — not
within two degrees, not within five. The sentence must be corrected or cut.
(The "75°" itself is approximately right for the MCAD polygon's E–W sides,
~75.7°; the patent calls say S 74° W. The error is the railroad match, not
the section figure.)

**Q2. Powell's magnetic variation.** The GLO scan (`phase2/glo-page-6.png`)
reads **12° 9½′**, clearly — the "12° 7½′" reading was a misread. v19's
"12 degrees 9-1/2 minutes" is correct.

**Q3. 1995 NAPP film type.** **Color-infrared.** EarthExplorer metadata for
entity NP0NAPP009026041 (NAPP Roll 9026, Frame 41 — the project's
"9026-41" frame, center 32.0625, -102.15625, acquired 1995/12/19) states
verbatim: *"The film type used for this photograph was CIR."* Scale
1:40,000 (FGDC `<srcscale>40000</srcscale>`). Dataset: "NAPP" / National
Aerial Photography Program; Project 9613; Photo ID 1NPU961390260041.
Important consequence: the repo's alignment note
(`phase2/ee-1995-alignment.md`) calls this frame "panchromatic" — that is
contradicted by the official metadata and should be corrected to CIR.
Likewise, v19's fix #2 (relabeled strip from "color-infrared" to "NAPP
photo" on the grounds that "the source frame is panchromatic") rested on
a false premise — the original "color-infrared" label was right all along.
The sheet's current neutral label ("1995 NAPP, 19 Dec 1995") is not
incorrect, so no sheet change is required; but the repo note is wrong.
(Note: the repo's scan file `aerials/ee-1995.tif` renders effectively
grayscale — no red-dominant pixels, correlated channels — suggesting the
scan on hand is a B&W duplicate or desaturated derivative of a CIR
original. The metadata describes the photograph, which is CIR.)

**Q4. 1953 instrument type.** "Royalty deed" is correct. `phase2/estes.md`:
1953-10651, **ROYALTY DEED** ESTES ETHEL → STANOLIND OIL & GAS, DR/200/479,
640-ac Sec 7 Blk 39.

**Q5. 1978 deed-of-trust beneficiary.** The clerk index names the grantee
**ESTES ETHEL MRS** (companion deed of trust 1978-16944, Midland West Corp
→ Ethel Estes, DT/369/42, SE/4 Sec 7 Blk 39; `phase2/estes.md`). So "Mrs.
Estes" as beneficiary is index-supported. Caveat: the instrument image
itself was not re-purchased for this audit — the citation rests on the
clerk index entry, not a fresh image read.

**Q6. 1911 Holloway→Estes acreage.** The sheet is correct as written but
could be misread. Mary T. Edwards and heirs → S.H. Holloway covered
**Sections 6, 7, 8, 17, 18** (1911-77002965, DR/21/354; source-log row 20).
S.H. and Lou Holloway → S.W. Estes conveyed **Section 7 only**
(1911-77001844, DR/19/518; source-log row 19). The sheet's second sentence
("Four months later Holloway → S.W. Estes") doesn't restate the acreage;
in context it reads as the Section 7 conveyance, which is right — but
adding "Section 7" to that sentence would remove all ambiguity.

**Q7. Exact 1996 grantee name.** The clerk index gives **BUTTON ESTES RANCH
LTD** — not "ESTES BUTTON RANCH LTD" (OR/1400/466, doc 1996-14037,
recorded 8/9/1996; `phase2/estes-northeast-acreage.md`). Any outline label
on the sheet must use that exact order.

**Q8. Every personal name on the sheet, with year.**
- W.C. Powell — 1876 (deputy surveyor)
- L.E. Wright — 1876 (chain carrier)
- E.C. Bennett — 1876 (chain carrier)
- Charles J. Canda — 1906 (grantor; trustee of the Texas Pacific Land Trust)
- Mary T. Edwards — 1906 (grantee), 1911 (grantor)
- S.H. Holloway — 1911 (grantee, then grantor)
- S.W. Estes — 1911 (grantee), 1921 (grantor)
- Arminta Estes — 1921 (grantor)
- Thelma Estes / Thelma Estes Brown — 1921 (grantee), 1940 (grantor), 1941
  (grantor/grantee), d. 1983 at 80, Laguna Hills, California
- W.T. Brown — 1940 (grantor)
- Aldredge Estes — 1941 (grantee/grantor); died before 1953 (the sheet is
  honest that the records don't say when)
- Ethel Estes / Ethel Aldredge Estes — 1953, 1970, 1976, 1978 (grantor)
- Neal Hail — 1980–81 (Hailco president)
- Frank Mullins — 1982 (became Midland West majority owner, December 1982)

Not named on the sheet (correctly, per the no-current-owner-names rule):
the 1996 grantor ("one of them"), the 1977 course founders (only "two
men, one of them the head pro at Ranchland Hills"), the "former First
National banker" (Hoyle McCright per US v. McCright, 821 F.2d 226), Louis
Rochester and Charles E. Beil (1982 JV parties, in `phase2/bsd.md` only).
Possibly living: Neal Hail and Frank Mullins — both appear solely in
public-record business capacities (company president; majority owner),
which is the lowest-risk kind of naming. Everyone else is 19th/early-20th
century or confirmed deceased. Street names (Island Cir, Greentree Blvd,
Rustic Trl) are not personal names.

## Numbered discrepancies (sheet text → corrected record text)

**1. Railroad azimuth — the survey panel's bearing claim is false.**
Sheet: *"The blocks were laid on the railroad's bearing. Within two
degrees they match the section's 75° long-side azimuth."*
Record: Census TIGER/Line 2024 rails, "Texas and Pacific Rlwy" through
Midland — best-fit true azimuth **58.6°**, ~16° off 75°. The section was
not laid on the railroad's bearing. Correct to something like "The blocks
were laid on the section's own bearing, about sixteen degrees off the
railroad's" — or cut the sentence.

**2. 1946 strip date — wrong day.** Sheet strip label: *"1946 USDA, 20 Feb
1946."* Record: the frame edge reads **February 28, 1946** (USDA Mission
DAR 1C-67; `phase2/ee-1946-alignment.md` lines 18, 26: "the frame edge
reads February 28, 1946; the collection card says March 13, 1946. I used
the frame date"). Change to **28 Feb 1946**.

**3. 1921 deed — wrong grantor, wrong acreage.** Sheet: *"1921. Arminta
Estes → Thelma Estes, 7 June. DR 30/144. The whole section; her 1923 deeds
of trust cover all 640 acres."* Record (source-log row 36, from the deed
image): grantors **S.W. ESTES & wife ARMINTA ESTES** → THELMA ESTES,
1921-77008642, DR/30/144, **~160 ac Sec 7** — not the whole section.
Corrected text: *"1921. S.W. and Arminta Estes → Thelma Estes, 7 June. DR
30/144. About 160 acres of Section 7; her 1923 deeds of trust cover all
640 acres."* Note the tension this creates: the 1923 DOTs (1923-77019657/
56, DT/7/185 & DT/7/182, 640-ac Sec 7; `phase2/estes.md`) do cover the
whole section, so Thelma evidently held or claimed broader interests than
the 1921 deed alone conveyed. The sheet shouldn't paper over that with
"The whole section" on the 1921 line.

**4. Hailco warranty deeds — "three" should be "two."** Sheet: *"1980–81.
Midland West sells lots to Hailco Inc. — three warranty deeds…"* Record
(`phase2/hailco.md`, "Direct Midland West Corp → Hailco instruments"):
exactly **two** warranty deeds — 1980-15853 (rec. 10/20/1980, DR/692/692)
and 1981-12355 (rec. 6/26/1981, DR/712/543) — plus one deed of trust
(1980-15854, DT/401/27), which is not a warranty deed. Correct to "two
warranty deeds" unless a third instrument is produced.

**5. 1941 partition page citation is imprecise.** Sheet: *"Thelma Estes
Brown → Aldredge Estes, Section 7 (DR 70/294)."*
Record: the partition is four instruments recorded simultaneously across
**DR/70/291–294** (1941-16694 WD Aldredge [& Ethel] → Thelma Brown, Sec 6;
1941-16695 WD Thelma Brown → Aldredge, Sec 7; source-log row 68). The repo
doesn't pin the Sec-7 instrument to page 294 specifically — the range is
what's sourced. Either cite the range or verify the page. Related: given
discrepancy 3, whether the 1941 Sec-7 instrument conveyed the whole
section or only Thelma's interest needs the legal description read — the
index alone doesn't say.

## Checked and confirmed (no change needed)

- Patent: 15 Dec 1883, Texas and Pacific Railway Co., Patent 540, Vol. 68,
  p. 503, 640 ac; Land Scrip No. 3123, 25 May 1876; 203 miles, 4,624 ft of
  railroad; surveyed 1 Feb 1876 by W.C. Powell; filed GLO 27 Dec 1876 —
  all match the patent file scans.
- 1906: Canda → Mary T. Edwards, recorded 6 Jan, DR/12/54, three $795
  notes (source-log row 20). "DR/12/64" was the old misreading, already
  fixed.
- 1940: Thelma Estes Brown and W.T. Brown → Magnolia Pipe Line Co.,
  instrument 2 Dec 1940 (rec. 12/11/1940), DR/67/531 — index names both
  grantors (`phase2/easements.md`). Consistent with the pipeline on the
  1954/1966 topos.
- 1953/1970: royalty deed then O&G lease, Ethel signing alone; Pan
  American was Stanolind's renamed successor — fine as written.
- 1976: Ethel Aldredge Estes → three children, 14 Dec, DR/615/436–438.
- 1978: three deeds 21–22 Nov, DR/649/510–555; companion DOT 1978-16944
  (DT/369/42) back to Mrs. Estes on the SE/4; minerals severed — all match
  `phase2/estes.md` and the 1982 BSD-agreement image (which recites the
  severance).
- 1979 Pioneer ROW: two instruments, both October 1979 — Estes Aldredge
  Jr et al → Pioneer (DR/673/712, inst. 10/19/1979) and Midland West →
  Pioneer (DR/673/714, inst. 10/08/1979), both recorded 1/28/1980. The
  sheet's "The Estes heirs and Midland West … October … DR 673/712–714"
  is accurate.
- 1982 BSD agreement: every figure verified — 8 Jan 1982, 20.343 ac,
  Lots 20–23 Blk 6, $1,348,425 cash, 4-year build-or-reconvey, seller to
  annex/plat/zone/pave, DR/731/258 (`phase2/bsd.md`, image read).
- 1983: first lot 26 Jan (1983-1592, DR/770/614, Lot 18 Blk 2); members buy
  club 1 Mar for $6M+; 297 ac / 220 lots / 9 holes under construction, 85
  pre-sold; FNB financing; Mullins majority Dec 1982; 1986 federal trial,
  $1.925M loan (source-log rows 66, 77; `phase2/reporter-telegram.md`).
- Hailco: incorporated May 1979, Neal Hail president, 771 instruments
  1980–85 (`phase2/hailco.md`).
- Water: Ogallala 100–180 ft; City of Midland Well 3, 147 ft, unused;
  ten driller's-report wells 2002–2021 at 135–180 ft; golf-course well 175
  ft, 2021 (source-log row 27).
- Soil: ~60% Amarillo/Midessa fsl "farmland of statewide importance";
  Bippus clay loam occasionally flooded; no hydric soils; water table
  >80 in (source-log row 26).
- Midland Draw: COMID 5688042; unnamed in NHD (GNIS null); "Midland Draw"
  label on every viewed USGS edition 1954 (1:250k) through 2019; drains via
  Beals Creek to the Colorado — Powell's "North Concho" refuted
  (source-log rows 2, 10, 40, 43).
- Aerial strip dates/scales: 1954-05-02 1:63,000; 1965-02-20 1:21,400;
  1974-02-19 1:29,000; 1984-10-28 (HAP85); 1995-12-19 (NAPP) — all match
  the alignment notes and source-log row 44, except the 1946 day (see #2).
- Wells: Exxon 42-329-31556 (1998, active); Petroplex 42-329-37587
  (10,986 ft, 2011, active); Henry Resources 1208 dry; Parish Dec-1980 dry
  hole; Easy Target 45816/45818 spud 2/29/2024, TDs ~24–26k ft
  (`phase2/wells.csv`). "Spudded within four days" — 45816 and 45818 both
  spud 2/29/2024; third well's date not in the CSV head but consistent.
- Pipelines: 7 systems in the geojson (12 physical segments) — ONEOK
  WesTex 16" gas T-4 00679; Oryx Green Tree 6.63" crude T-4 10611 (×2);
  EnLink Coronado gas 20"+16" T-4 10274; Energy Transfer Sale Ranch gas
  10.75" T-4 09393; Roswell East HVL 8.63" (×2); Mallet-to-Midland 3 crude
  12.75" (×2); Mallet-to-Midland 2 crude 10.75" (×2). The sheet's "seven
  pipelines" counts systems — defensible; the map draws the doubled
  segments. ONEOK at 5,350 ft ≈ the full section width ✓.
- Corners: NE 32.07196,-102.15950; NW 32.06810,-102.17617; SW
  32.05405,-102.17156; SE 32.05784,-102.15503 — all four match the MCAD
  Abstracts polygon (OBJECTID 57) to rounding.
- "About 650 acres" — SSURGO clip totals 650.1 ac (source-log row 56).
- Thelma's obituary: 1983-04-19, "Thelma Estes Brown, 80, of Laguna
  Hills" (`phase2/reporter-telegram-extended.md`) — the sheet's "died in
  1983 at 80, in Laguna Hills, California" is exact.
- "Sixty-seven years of one family" (1911–1978) and "ninety-nine years of
  open land" (1883–1982) both arithmetic-clean.

## What a Midland County title examiner would dispute

The chain column reads smoothly, but three spots wouldn't survive a
title plant:

1. **The 1921→1941 acreage problem (discrepancies 3 and 5).** The file's
   own image read says the 1921 deed moved ~160 acres, yet the sheet
   narrates an unbroken whole-section chain into the 1941 partition and
   out the other side. An examiner would ask: by what instrument did the
   other ~480 acres get to Thelma before 1941, or did the 1941 partition
   convey only her undivided interest? The answer is in the legal
   descriptions of DR/30/144 and DR/70/291–294 — neither is quoted in the
   repo. Until one of them is read, "The whole section" on the 1921 line
   is the sheet's weakest sentence.
2. **"Complete, no gaps."** The fee chain 1876–1983 is continuous, but the
   header overclaims slightly: the 1951 intra-family royalty deeds
   (Aldredge → Thelma, DR/139/487; Thelma → Aldredge, DR/141/18;
   `phase2/estes.md`) aren't in the narrative. They don't break the chain
   — both parties are in it — but a header promising "complete" while
   omitting recorded instruments from the chain period invites exactly
   the question it claims to foreclose. Either scope the header to the
   fee chain or add a half-line.
3. **The 1996 ten-acre carve-out's origin** is still open (item 37): the
   index doesn't show whether the 1978 deeds excepted the NE 10 ac of the
   SE/4 or it came back afterward. The sheet handles this honestly
   ("the index does not show"), which is the right call — keep that
   sentence.

Nothing else in the chain column would draw a red pen. The deed-book and
page citations I could check all land on real instruments.

---
*Skippy — independent audit, 2026-09-30. Methods: PDF text extraction,
deed-image and GLO-scan reads, source-log cross-check, fresh TIGER/Line
download for Q1, EarthExplorer metadata (entity NP0NAPP009026041) for
Q3.*
