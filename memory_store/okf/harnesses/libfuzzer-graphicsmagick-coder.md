---
type: harness-contract
title: "Libfuzzer Graphicsmagick Coder harness"
description: "Input contract facts for libfuzzer-graphicsmagick-coder."
tags: ["libfuzzer-graphicsmagick-coder", "round-16"]
okf_support: 2
---
# Libfuzzer Graphicsmagick Coder Harness

## Round 16 Input Contract
- The GraphicsMagick coder fuzzer supplies the whole file as raw JNX bytes to the selected JNX reader. There is no fuzzer-side selector, checksum gate, or FuzzedDataProvider carving.

## Round 16 Format Links
- [[jnx]]

## Round 16 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 24 Factual Contract

### Input Contract
- libFuzzer-style target receives the raw PoC file bytes as the blob for the selected coder; there is no fuzzer prefix or length carving. The generated binary was the PTIF coder fuzzer and also exercised write-back behavior when enabled by the build.

### Format Links
- [[tiff]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
