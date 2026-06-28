---
type: harness-contract
title: "Libfuzzer Ghostscript Cups Raster harness"
description: "Input contract facts for libfuzzer-ghostscript-cups-raster."
tags: ["libfuzzer-ghostscript-cups-raster", "round-11"]
okf_support: 1
train_only: true
---
# Libfuzzer Ghostscript Cups Raster Harness

## Round 11 Input Contract
- The gstoraster-style Ghostscript fuzzer feeds raw stdin bytes to Ghostscript with a CUPS raster device configuration. There is no carved prefix; Ghostscript language detection chooses PDF or PostScript from the bytes.

## Format Links
- [[pdf-with-cmap-stream]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
