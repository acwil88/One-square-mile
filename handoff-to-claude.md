# One Square Mile — Phase 1 handoff (gather complete)

**To:** Claude (Adam's work agent) — Phase 2 design/layout per the v2 Desk Edition brief
**From:** Skippy — Phase 1 gather, completed 2026-09-26
**Project:** printed, folded 24×36 map of one square mile of West Texas; first run 25 copies; ~$150–300 print estimate (not quoted/approved)

---

## 1. The frame (confirmed — use this, not the old centered-square concept)

**Section 7, Block 39, T-1-S, T&P RR Co. Survey, Midland County, Texas — GLO Abstract 34.**
Triple-confirmed via MCAD abstracts layer, two clerk instruments, and GLO basefile (NOT Block 40).

Approximate corners (WGS84):
- NW 32.0683, -102.1758 | NE 32.0683, -102.1587
- SW 32.0538, -102.1758 | SE 32.0538, -102.1587

The project sponsor's residence sits inside it (Green Tree North, Midland TX — exact address withheld in this public copy) — Lot 005 Blk 001, 0.335 ac, house built 1992.

Map arc: **railroad grant (1883) → Canda → Edwards → Estes ranch (1911–1978) → subdivision (1982) → now.**

## 2. Adam's standing decisions (do not relitigate)

- Title: "Desk Edition — compiled from records, not walked."
- **No current owner names on the sheet.** Title chain stops at "subdivided."
- Nothing prints without a source-log row. Unverified field-dependent details go in the "can't confirm" margin.
- No phone calls. Outreach only by email/mail; emails need Adam's approval of the exact draft.

## 3. Verified chain of title, 1883→1982 (source-log rows 6–9, 11–21, 30)

| Date | Grantor → Grantee | Instrument | Notes |
|---|---|---|---|
| 12/15/1883 | Texas and Pacific Railway Co. (patent) | Patent 540, Vol 68 Pg 503; Bexar Scrip File 020113, Cert 3123 | 640 ac. Scrip issued 5/25/1876 for 203 mi 4,624 ft of railroad built. Surveyed 2/1/1876 by W.C. Powell (chain carriers L.E. Wright, E.C. Bennett). "Waters of North Concho." Originally docketed Martin County, corrected to Midland 1887. Sec 7 odd = railroad section. |
| 12/13/1905 (rec. 1/6/1906) | Charles J. Canda (+ Simeon J. Drake, Sigmund Neustadt) → Mary T. Edwards | DR/12/54 (cited in 1911 deed as Bk 12 p. 64) | Sec 7, Blk 39, 640 ac. **Correction 9/26:** earlier read said John D. Edwards → Mary T. Edwards at DR/12/64 — misreading. Exhaustive portal searches found no John D. Edwards conveyance of this tract. |
| 4/15/1911 (rec. 5/9/1911) | Mary T. Edwards + heirs → S.H. Holloway | 1911-77002965, DR/21/354 | Secs 6-7-8-17-18, Blk 39. Buyer assumed three $795 notes dated 12/13/1905 from the Canda deed. |
| 8/15/1911 (rec. 8/17/1911) | S.H. & Lou Holloway → S.W. Estes | 1911-77001844, DR/19/518 | Sec 7. Start of the Estes era. |
| 6/6/1921 (rec. 6/7/1921) | S.W. & Arminta Estes → Thelma Estes | 1921-77008642, DR/30/144 | ~160 ac Sec 7. |
| 12/14/1976 | Ethel Aldredge Estes → Aldredge Estes Jr. | 1976-13382, DR/615/436 | (Thelma → Ethel appears to be marriage/name change; no conveyance found.) |
| 10/31/1978 | Estes family (Aldredge Jr., Patricia Ann, Ethel, Aldredge III, Virginia Ann) → Midland West Corp. | 1978-16882-1, DR/649/510 | **Surface & surface rights only**, 160 ac SE/4 Sec 7. Minerals severed. $10 consideration. Companion ratification deed 1978-16945-1 (DR/649/555) for south 60 ac of SE/4. Purchase-money DOT 1978-16944 (DT/369/42). Lien released 1979-3388. |
| 2/25/1981 | Midland West Corp. → Hailco Inc. | 1981-3556, DR/701/792 | Warranty deed; plat-joinder parcel. Hailco's identity could not be confirmed (only "Hailco" found online filed 1998 — too late; excluded). |
| 1/13/1982 | BSD Inc. → Midland West Corp. | 1982-719, DR/731/258 | Agreement; legal "SEC 7 39 T1S T&P RR". Nature unverified. |
| 12/1/1982 | **Green Tree North plat recorded** | Instrument 1982-25784, Cabinet C p. 134 | Developer: Midland West Corporation. Chain stops here per Adam's rule. |

## 4. Topo sequence (row 10)

1954 Hobbs 1:250,000 → Northwest Midland 1966 1:24,000 (1968/1975/1985 eds.) → Andrews 1991 1:100,000 → US Topo 2010/2012/2016/2019.
- 1966–1985: open rangeland (oil wells, drill holes, gravel pit). Pipeline labeled "PIPELINE" on all 1966 eds.; absent from US Topo.
- **"Midland Draw" label present on every edition including 2019** — never disappeared.
- First subdivision streets on 1991; fully built out by 2010. Green Tree golf course on no historical scan (modern basemap only).

## 5. Aerial timeline — print-clean set (rows 22–23, 25, 28)

Clean, watermark-free GeoTIFFs from USGS EarthExplorer (EROS account: Adam's, verified) in `~/workspace/one-square-mile/aerials/`:
- `ee-1954.tif` — 1954-05-02, 1:63,000, 10620×9872 B&W (~1.6 m/px). Open rangeland.
- `ee-1965.tif` — 1965-02-20, 1:21,400, 10139×9872 B&W (~0.5 m/px). Still open range; frame verified to enclose full section.
- `ee-1974.tif` — 1974-02-19, 1:29,000, 10193×9872 B&W (~0.7 m/px). First graded corridors/cleared pads.
- `ee-1984.tif` — 1984-10-28 NHAP, 3900×3523 B&W (medium-res = highest NHAP offers). Streets + course under construction.
- `ee-1995.tif` — 1995-12-19 NAPP Color Infrared, 3360×3033 (medium-res = highest NAPP offers). Course mature, mostly built out.
- Previews: `ee-YYYY-preview.jpg` alongside each.
- Older watermarked NETR screenshots (`1937.png` etc.) are reference-only — do not print.
- TxGIO 1944 USAF frame exists but is order-only ($10/frame + fees); no 1930s/40s coverage on EarthExplorer.

## 6. Wells and pipelines (row 24)

RRC GIS, verified 9/26: 4 producing oil wells (APIs 42-329-35206, 42-329-37587, 42-329-31556, 42-329-47554), 4 horizontal pads (42-329-45816, 42-329-40219, 42-329-45818, 42-329-45820), 1 canceled location; N–S laterals from north-edge pads. Crude gathering line crosses northern half NW–SE; best candidate Oryx Midland Oil Gathering LLC T-4 Permit 10611, 6.63", "GREEN TREE" system (linkage likely, unverified). Per-well operators/dates/depths blocked (RRC Identify dead). **1954/1966 topo pipeline not identified → can't-confirm margin.**

## 7. Soils and water (rows 26–27)

- Soils (NRCS Web Soil Survey, SSURGO): ~60% Amarillo + Midessa fine sandy loam (farmland of statewide importance, well drained); Bippus clay loam in the draws with occasional-flooding limitation. All units well drained, water table >80 in, no hydric soils.
- Water (TWDB): Ogallala ~100–180 ft under the section. One City of Midland well inside the section (unused, 147 ft); ~10 residential domestic/irrigation driller's reports in-section (2002–2021, 135–180 ft); Green Tree golf course well 175 ft (2021). Private owner names withheld from TWDB well records.

## 8. Memory/history (brief: `brief-8-memory-history.md`, row 29)

- **Estes family (1911–1978):** S.W. Estes bought from the Holloways 1911. "Button" Estes verified as Aldredge "Little Button" Estes, Jr. (via wife Patricia's obituary) — real cattle operation, registered Herefords, 4-H/FFA. Button Estes Ranch, Ltd. (TX corp 1996) likely holds the severed minerals — inference, flagged. **Map label: "Estes family ranch/farm" — never "Button Estes Ranch"** (no source names the Sec 7 operation).
- **Green Tree:** summer 1977 — Mobley (Ranchland Hills head pro) + John Wood; Hoyle McCright/FNB financing; Midland West Corp. created; 320 acres from Button Estes ("sandy old farm with one sickly tree and tumbleweeds"); dirt-trail access into Feb 1980. Course opened ~1980–81; +9 holes 1985 (explains the 1986 aerial); Tripp Davis Road Course 2018. Federal cases confirm $8.9M FNB loan (*Midland West v. FDIC*; *US v. McCright* $1.925M for course/club).
- **Green Tree North:** plat 12/1/1982, developer Midland West Corp./John Wood; covenants include 2-year build-out with developer repurchase option (rapid-build intent). Earliest homes visible in 1986 aerial.
- Could not confirm: first lot sale/prices/first home; S.W./Arminta/Thelma-Ethel bios; Hailco Inc. identity; Reporter-Telegram coverage (paywalled); Portal to Texas History / Handbook of Texas / THC Atlas hits (none found); McCright obit vs. case conflict (retired 1980 vs. officer activity 1977–82); one unverified forum claim of a presidential pardon — not repeated as fact.

## 9. Can't-confirm margin (draft language in brief §3; also: 1954/1966 pipeline identity, 2022 US Topo scan, BSD Inc. agreement nature)

## 10. Files

- `~/workspace/one-square-mile/` — README.md, source-log.md (rows 1–30), this handoff
- `~/workspace/one-square-mile/aerials/` — ee-1954/1965/1974/1984/1995.tif + previews (+ legacy watermarked NETR pngs, reference only)
- `~/workspace/one-square-mile/brief-8-memory-history.md` — full history brief, 18 sources, margin language

## 11. For Phase 2 (Claude)

Everything above is gather-verified with a source-log row. Open threads for you: none blocking — the deed chain is complete 1883→1982, aerials are print-clean, history is sourced. Remaining judgment calls are design: neatline treatment of the survey section, which decades get full-bleed aerials, margin copy from brief §3, and the 25-copy print spec.
