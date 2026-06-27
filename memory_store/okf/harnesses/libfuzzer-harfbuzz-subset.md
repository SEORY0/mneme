---
type: harness-contract
title: "libfuzzer-harfbuzz-subset harness"
description: "Input contract facts for libfuzzer-harfbuzz-subset."
tags: ["libfuzzer-harfbuzz-subset", "round-14"]
okf_support: 1
---
# Libfuzzer Harfbuzz Subset Harness

## Round 14 Input Contract
- The Harfbuzz packaged target used the subset fuzzer on raw font bytes. The input is a complete font file, not a separate table blob or selector-carved stream.

## Round 14 Format Links
- [[opentype-font]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
