---
type: harness-contract
title: "Libfuzzer Harfbuzz Shape harness"
description: "Round 23 input contract facts for libfuzzer-harfbuzz-shape."
tags: ["libfuzzer-harfbuzz-shape", "round-23"]
okf_support: 2
train_only: true
---
# Libfuzzer Harfbuzz Shape Harness

## Round 23 Input Contract
- The HarfBuzz fuzzer creates a face from the entire input, shapes a fixed ASCII string, and if enough bytes are present also copies the final fixed-size trailer into a UTF-32 buffer for a second shaping pass. The trailer can steer shaping text while the leading bytes remain a valid font.

## Round 23 Format Links
- [[opentype-font-plus-trailing-utf32]]

## Round 23 Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.

## Round 32 Input Contract
- The HarfBuzz shape fuzzer consumes the entire file as a font blob. It creates an hb_face and hb_font, shapes fixed ASCII text, and for larger inputs also treats the final fixed-size trailer as UTF-32 text for a second shaping pass. There is no leading selector byte, archive wrapper, or FuzzedDataProvider carving.

## Round 32 Format Links
- [[opentype-aat-kerx-font]]

## Round 32 Notes
- These facts are descriptive harness-carving observations only; they are not causal recovery claims.
