# Aerial alignment — status and handoff, 2026-09-27

**Done (Claude):** 1995 (±150 ft), 1984 (±30 ft relative to 1995). Files: `ee-1995-2277.tif`, `ee-1984-2277.tif`, method notes alongside.

**Not done:** 1974, 1965 (in repo), 1954 (not yet in repo).

## Why 1974/1965 are harder, and what I learned
- Both scans are stored rotated, like 1995/1984. 1974's frame text is upside-down (180° or a flip); 1965's title strip is vertical on the right like 1995 (likely north = image-right). Neither is confirmed.
- No subdivision, no ponds. Control is section-line roads, the draw, and oil pads.
- SIFT fails across epochs at every scale I tried (memory-limited to quarter-res on 10k×10k scans).
- Edge template-matching of the aligned 1984 frame into each scan locks onto the film border instead of the ground. The border must be masked out before this can work.
- Metadata scale: 1974 ≈ 2.3 ft/px (1:29,000), 1965 ≈ 1.64 ft/px (1:21,400).

## Recommended method (whoever picks it up)
1. Crop each scan to the photo interior (drop the black film border and title strip).
2. Determine orientation: Hough transform on the road edges gives the dominant road angle; the section grid is skewed ~14° from north, so the two dominant angles identify which 90° rotation/flip is right, up to a 180° ambiguity. Resolve the 180° with Midland's NW edge (fields + houses in 1974 — it must sit SE of the section).
3. Reference = `ee-1984-2277.tif`, not NAIP (closer in time and film). Pick 3–4 section-line road intersections on gridded zooms in both; similarity fit; checkerboard check.
4. Chain to the NAIP grid via the stored 1984 transform in `ee-1984-alignment.md`.
5. Accept ±150–300 ft. At strip scale that is under 5 mm. Document the residuals.

## Handoff
Claude → Skippy for 1974, 1965, and 1954 when it lands. You have the cycles to iterate on GCP picks; through the chat channel each zoom is a full round-trip for me. If you get stuck, push what you have with a note and I'll take the next step.
