---
type: harness-contract
title: "Honggfuzz Style File Harness"
description: "Input contract facts for honggfuzz-style-file."
tags: ["honggfuzz-style-file", "round-12"]
okf_support: 0
train_only: true
---
# Honggfuzz Style File Harness

## Round 12 Input Contract
- There is no file header or selector. Inputs over the decompressed buffer capacity are ignored. A crash can come from the target bug or from the harness aborting when compression/decompression does not round-trip exactly, so official fixed-image behavior is essential.

## Round 12 Format Links
- [[raw-lzxpress-roundtrip-plain-bytes]]

## Round 12 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
