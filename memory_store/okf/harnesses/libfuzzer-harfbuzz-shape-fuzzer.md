---
type: harness-contract
title: "Libfuzzer Harfbuzz Shape Fuzzer harness"
description: "Input contract facts for libfuzzer-harfbuzz-shape-fuzzer."
tags: ["libfuzzer-harfbuzz-shape-fuzzer"]
okf_support: 3
---
# Libfuzzer Harfbuzz Shape Fuzzer Harness

## Round 10 Input Contract
- The harness treats the buffer as a font blob, creates a face/font, derives some shaping parameters from available bytes, and runs shape tests over fixed text. There is no file container or leading mode byte.

## Round 10 Format Links
- [[opentype-truetype-font]]

## Round 10 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 32 Input Contract
- The HarfBuzz shape fuzzer consumes raw font bytes as one hb_blob, creates an hb_face and hb_font, shapes fixed ASCII text, then shapes a UTF-32 buffer copied from the input trailer. It also calls miscellaneous face/font APIs for color, math, name, variation, glyph origin, and glyph extents. No external wrapper, checksum, mode selector, or FuzzedDataProvider layout is present.
- The hb-shape libFuzzer harness consumes the raw input bytes as an hb_blob font with no leading selector and no FuzzedDataProvider carving. It shapes fixed ASCII text first, and for larger inputs also interprets trailing bytes as UTF-32 text. Classic kern application depends on HarfBuzz selecting the kern table during shaping rather than a GPOS kern feature.
- The selected HarfBuzz shape fuzzer consumes the whole file as a raw font blob. It creates an hb_face and hb_font, shapes fixed text, copies the final input bytes as UTF-32 text for a second shaping pass, and passes the last UTF-32 word as the glyph/codepoint selector to miscellaneous face/font APIs including glyph extents. There is no FuzzedDataProvider split or leading mode byte.

## Round 32 Format Links
- [[opentype-cff]]
- [[opentype-font]]

## Round 32 Notes
- These facts are descriptive harness-carving observations only; they are not causal recovery claims.
