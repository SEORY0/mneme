---
type: harness-contract
title: "Libfuzzer Ghostscript Tiffsep Device harness"
description: "Input contract facts for libfuzzer-ghostscript-tiffsep-device."
tags: ["libfuzzer-ghostscript-tiffsep-device", "round-11"]
okf_support: 1
train_only: true
---
# Libfuzzer Ghostscript Tiffsep Device Harness

## Round 11 Input Contract
- The oss-fuzz Ghostscript harness calls the generic device fuzzer with the tiffsep1 output device and raw input bytes as stdin. It writes to a temporary TIFF output path, uses a fixed color scheme, and does not carve a leading mode byte or FuzzedDataProvider structure.

## Format Links
- [[postscript-or-pdf]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
