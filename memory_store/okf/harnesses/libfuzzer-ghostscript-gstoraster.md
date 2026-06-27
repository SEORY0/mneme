---
type: harness-contract
title: "libfuzzer-ghostscript-gstoraster harness"
description: "Descriptive harness contract facts for libfuzzer-ghostscript-gstoraster."
tags: ["libfuzzer-ghostscript-gstoraster", "round-18"]
okf_support: 2
train_only: true
---
# Libfuzzer Ghostscript Gstoraster Harness

## Round 18 Input Contract

### Schema / Invariants
- The gstoraster harness feeds the raw input as Ghostscript standard input using the cups raster device and fixed device options. There is no fuzzer envelope; the document bytes themselves must select the PostScript features and rendering state.
- The Ghostscript raster harness consumes raw PostScript/PDF bytes from standard input under fixed raster-device arguments. Some Ghostscript fuzzers carve an initial color-scheme byte, but this run's observed target executes through the raw gstoraster path.

### Format Links
- [[postscript-raster-document]]
- [[postscript-sampled-function]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
