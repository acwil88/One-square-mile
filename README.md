# One Square Mile

A printed, folded 24×36 map of one square mile of West Texas — everything knowable *from the record*, on a single sheet. **"Desk Edition — compiled from records, not walked."**

**The mile:** Section 7, Block 39, T-1-S, Texas & Pacific Railway Co. Survey, Midland County, Texas (GLO Abstract 34).
Arc: railroad grant (1883) → Estes family ranch (1911–1978) → Green Tree North subdivision (1982) → now.

**Status (2026-09-26):** Phase 1 gather complete. This repo carries the Phase 2a asset drops as they're produced; Claude pulls from here for composition.

## What's here

- `source-log.md` — every source, numbered rows. Nothing prints without a row.
- `handoff-to-claude.md` — Phase 1 findings: chain of title 1883–1982, topo sequence, wells, soils, water, history.
- `brief-8-memory-history.md` — Estes family / Green Tree research brief with sources and margin-ready "could not confirm" language.
- `aerials/` — watermark-free USGS EarthExplorer frames: 1954, 1965, 1974, 1984 (NHAP), 1995 (NAPP color-IR). JPEG previews live here; full-resolution GeoTIFFs (~100 MB each) are held locally and available on request.
- `phase2/` — composition assets: `calls.md` (W.C. Powell's 1876 field-note calls, verbatim), `section7-polygon-*.geojson` (real MCAD vertices, WGS84 + EPSG:2277), `nhd-check.md` (Midland Draw drainage trace), `glo-patent-file.pdf` (GLO patent file scan).

## Rules of the repo

- Nothing here that couldn't print on the sheet: no current owner names, no private addresses or phones, no resident details. Private well-owner names from public TWDB records are withheld.
- What couldn't be confirmed is listed — in red, on the sheet — never silently dropped.

Built by Skippy (Meta Muse) + Claude (Anthropic), for a resident of the section who is not named on it. No phone calls were made.
