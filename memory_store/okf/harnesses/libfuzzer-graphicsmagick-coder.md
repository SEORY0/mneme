---
type: harness-contract
title: "Libfuzzer Graphicsmagick Coder harness"
description: "Input contract facts for libfuzzer-graphicsmagick-coder."
tags: ["libfuzzer-graphicsmagick-coder", "round-16"]
okf_support: 1
---
# Libfuzzer Graphicsmagick Coder Harness

## Round 16 Input Contract
- The GraphicsMagick coder fuzzer supplies the whole file as raw JNX bytes to the selected JNX reader. There is no fuzzer-side selector, checksum gate, or FuzzedDataProvider carving.

## Round 16 Format Links
- [[jnx]]

## Round 16 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
