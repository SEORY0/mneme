---
type: harness-contract
title: "Afl Compatible Libfuzzer Harfbuzz Subset harness"
description: "Input contract facts for afl-compatible-libfuzzer-harfbuzz-subset."
tags: ["afl-compatible-libfuzzer-harfbuzz-subset", "round-32"]
okf_support: 1
---
# Afl Compatible Libfuzzer Harfbuzz Subset Harness

## Round 32 Input Contract
- The active target is the HarfBuzz subset fuzzer. It reads the PoC as raw font bytes through an AFL-compatible libFuzzer-style wrapper; there is no leading mode selector and no FuzzedDataProvider split. The harness creates an hb_blob and hb_face from the entire input, then runs subsetting over fixed codepoints and, for sufficiently large inputs, also over trailing UTF-32 codepoints copied from the end of the same buffer. The same bytes are still treated as the font blob, so any trailer must not destroy the font envelope.

## Round 32 Format Links
- [[opentype-font]]

## Round 32 Notes
- These facts are descriptive harness-carving observations only; they are not causal recovery claims.
