---
type: harness-contract
title: "Libfuzzer Ghostscript Stdin Harness"
description: "Round 7 input contract facts for libfuzzer-ghostscript-stdin."
tags: ["libfuzzer-ghostscript-stdin", "harness-contract", "round-7"]
okf_support: 1
train_only: true
---
# Libfuzzer Ghostscript Stdin Harness

## Round 7 Input Contract
- The harness feeds raw stdin to Ghostscript configured for the CUPS raster device. It does not carve
a prefix from the input; Ghostscript auto-detects PostScript or PDF and processes the document
through its normal interpreter.

## Round {ROUND} Format Links
- [[pdf-encrypt-dictionary]]

## Round {ROUND} Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
