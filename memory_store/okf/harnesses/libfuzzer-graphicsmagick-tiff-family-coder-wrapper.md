---
type: harness-contract
title: "Libfuzzer Graphicsmagick Tiff Family Coder Wrapper harness"
description: "Input contract facts for Libfuzzer Graphicsmagick Tiff Family Coder Wrapper."
tags: ["libfuzzer-graphicsmagick-tiff-family-coder-wrapper", "round-6"]
okf_support: 1
---
# Libfuzzer Graphicsmagick Tiff Family Coder Wrapper Harness

## Round 6 Input Contract
- The task is file/raw-input driven through a GraphicsMagick coder fuzzer selected by the wrapper; raw file bytes are supplied as the image input, not argv options. Local wrapper selection may target a TIFF-family sub-coder rather than the exact ReadTIFFImage path.

## Format Links
- [[tiff]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
