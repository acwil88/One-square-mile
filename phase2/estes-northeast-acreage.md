# Northeast-corner acreage tract — Estes retention (Sec 7 Blk 39 T-1-S)

**Question:** What is the residential property circled at the northeast corner of the section (NOT the Occidental EASY TARGET pad — that is a separate oil pad to the east)?

**Answer:** A ~10-acre private residential acreage tract still held by the Estes family entity — the one corner of Section 7 the family kept when the surrounding land went to Green Tree development.

## MCAD parcel record (observed 2026-09-28, official MCAD ArcGIS parcel layer)

- MCAD property ID: **R4041** (Map ID R000004041; Geo ID 00003910.007.4000)
- Owner (corporate entity): **ESTES BUTTON RANCH LTD**
- Legal: **NE/CRNR SE/4, SEC: 7, BLK: 39-T1S** — northeast corner of the southeast quarter
- Acreage: 10.0 legal acres (shape area 438,455.529 sq ft ≈ 10.07 geometric acres)
- Market value: $100,000 (land_val $0, imprv_val $0 on the record)
- Deed: recorded **9/15/1989, Vol. 0201 Pg. 0380**

## Interpretation

- This is a private residential acreage tract at the NE corner of the SE/4 — NOT part of the Green Tree North subdivision plat.
- "Button Estes" = Aldredge "Little Button" Estes Jr. (see `phase2/estes.md` identity work), of the same Estes family that owned Section 7 from 1911 to 1978.
- Existing research: Midland West acquired ~320 acres from Button Estes for Green Tree development ~1977. This ~10-acre corner is the piece the family retained.
- 1966 topo context (`phase2/nwm-1966-114749-geo.tif`): no ranch-headquarters cluster anywhere on Sec 7 in 1966 — one windmill, one building, one gravel pit, open rangeland. The residential use of this corner postdates the ranch era.

## Open question — the 1989 deed vs. the entity

Earlier research placed Button Estes Ranch Ltd's entity formation in 1996, but MCAD shows a 9/15/1989 deed (Vol. 201 Pg. 380). Unverified whether the 1989 deed was to Button Estes personally, to another family entity, or an intra-family transfer later reflected under the current owner name.

**Next step (needs Adam's approval, ~$1–2):** pull the Vol. 201 Pg. 380 image from the Midland County Clerk portal and read the grantor/grantee. Do NOT record any current private-resident names from that image in the repo — corporate/historical parties only.

## Item 37 — 1989 deed + 1978 carve-out clause (status 2026-09-29)

### The 1989 deed (Vol. 201, p. 380) — PENDING pull
- The image has NOT been pulled yet. It needs a live browser session on the Midland County Clerk portal (midland.tx.publicsearch.us): deed index → Vol. 201 Pg. 380 (recorded 9/15/1989) → cart (~$1–2) → Adam taps to pay via Stripe Link → read grantor, grantee, and instrument type ONLY.
- Privacy rule: if the grantor is an individual family member, record it in the repo only as "a family member → Estes Button Ranch Ltd" — no individual name anywhere.
- What the records already say: MCAD parcel R4041, owner ESTES BUTTON RANCH LTD, legal NE/CRNR SE/4, SEC 7, BLK 39-T1S, 10.0 legal acres, vesting deed recorded 9/15/1989, Vol. 0201 Pg. 0380.

### The 1978 deeds (DR 649/510–555) — images NOT in repo
- The 1978 deed images were read in the clerk portal on 2026-09-26 but were NOT saved — `phase2/images/` holds only the 1982 BSD agreement (`1982-719-bsd-agreement.pdf`, scanned, no text layer). Do not re-buy them for this question unless the 1989 deed leaves the carve-out unexplained.
- Legal descriptions as paraphrased in source-log rows 15–16 (from the 9/26 image reads):
  - DR/649/510 (deed, rec. 11/21/1978): "surface & surface rights only in 160 acres of the SE/4 of Sec 7, Blk 39" — the surface of the FULL SE/4.
  - DR/649/555 (ratification deed, rec. 11/22/1978): "surface & surface rights only in the South 60 acres of the SE/4 of Sec 7, Blk 39".
- **Carve-out clause: UNVERIFIED.** Neither paraphrase records a "save and except" for the 10-acre NE-corner tract — but the full deed text was not re-examined, so an in-deed exception cannot be ruled out from the paraphrases alone. Two live hypotheses:
  1. The 1978 deed's full legal contains an exception reserving the NE-corner 10 acres (not captured in the 9/26 paraphrase).
  2. There is no 1978 exception, and the 10 acres came back to the family via a later instrument — plausibly the 1989 deed itself (a re-conveyance from the developer side to the family entity).
- The 1989 deed pull resolves this: its grantor/grantee will show whether the 10 acres returned from the developer side or moved within the family.

### Next step (blocked on live browser + Adam's $1–2 tap)
1. Browser → midland.tx.publicsearch.us → deed index → Vol. 201 Pg. 380 (recorded 9/15/1989).
2. If the index row itself shows grantor/grantee/type, record that (free); buy the $1–2 image only if the index is ambiguous.
3. Record parties generically per the privacy rule above.
4. Revisit the 1978 exception question only if the 1989 deed doesn't settle it (then re-pull the DR/649/510 image).
5. Mark queue item 37 [x] when the 1989 instrument's parties (generic) and type are stated AND the 1978 carve-out clause is quoted or shown absent.

## Secondary-source note (unverified)

A MineralHolders search (2026-09-28, secondary source, NOT official proof) claims:
- "Estes Button Ranch Ltd" — 8 interests in Martin County
- "Button Estes Ranch Ltd" (separate, similarly named entity, same mailing address) — ~100 interests across 5 counties

Treat as leads only. No mineral conclusion belongs on the map without deed-level confirmation.
