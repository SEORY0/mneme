---
type: harness-contract
title: "Libfuzzer Graphicsmagick Coder Png harness"
description: "Input contract facts for libfuzzer-graphicsmagick-coder-png."
tags: ["libfuzzer-graphicsmagick-coder-png", "round-29"]
okf_support: 0
---
# Libfuzzer Graphicsmagick Coder Png Harness

## Round 29 Input Contract

- The GraphicsMagick coder fuzzer passes the raw libFuzzer bytes directly as an in-memory image blob to a fixed PNG coder instance. There is no harness byte carving. The image must be a valid enough PNG for libpng to expose text metadata to GraphicsMagick after basic chunk validation.

## Round 29 Format Links
- [[png-raw-profile-text-chunk]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
