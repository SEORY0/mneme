---
type: harness-contract
title: "Libfuzzer Leptonica Pix3 harness"
description: "Input contract facts for libfuzzer-leptonica-pix3."
tags: ["libfuzzer-leptonica-pix3", "round-11"]
okf_support: 1
train_only: true
---
# Libfuzzer Leptonica Pix3 Harness

## Round 11 Input Contract
- The libFuzzer harness passes raw bytes to the pix3 target, which reads the input as serialized PIX data and then performs image operations. There is no mode byte or FuzzedDataProvider field layout in the input.

## Format Links
- [[spix-leptonica-image]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
