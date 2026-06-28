---
type: harness-contract
title: "Libfuzzer Graphicsmagick Mvg harness"
description: "Input contract facts for libfuzzer-graphicsmagick-mvg."
tags: ["libfuzzer-graphicsmagick-mvg", "round-11"]
okf_support: 1
train_only: true
---
# Libfuzzer Graphicsmagick Mvg Harness

## Round 11 Input Contract
- The GraphicsMagick MVG fuzzer feeds the entire input buffer as raw MVG bytes to the image reader. There is no mode byte, archive wrapper, or FuzzedDataProvider carving.

## Format Links
- [[mvg]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
