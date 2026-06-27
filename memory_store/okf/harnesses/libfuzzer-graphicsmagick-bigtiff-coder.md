---
type: harness-contract
title: "libfuzzer-graphicsmagick-bigtiff-coder harness"
description: "Descriptive harness contract facts for libfuzzer-graphicsmagick-bigtiff-coder."
tags: ["libfuzzer-graphicsmagick-bigtiff-coder", "round-18"]
okf_support: 1
train_only: true
---
# Libfuzzer Graphicsmagick Bigtiff Coder Harness

## Round 18 Input Contract

### Schema / Invariants
- The observed harness runs the GraphicsMagick BIGTIFF coder fuzzer over raw file bytes. There is no external envelope; success depends on the raw bytes being accepted by the TIFF/BIGTIFF reader and reaching the specific coder path.

### Format Links
- [[tiff]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
