---
type: harness-contract
title: "Libfuzzer Smartcrop Harness"
description: "Input contract facts for libfuzzer-smartcrop."
tags: ["libfuzzer-smartcrop", "round-30"]
okf_support: 0
train_only: true
---
# Libfuzzer Smartcrop Harness

## Round 30 Input Contract

### Input Contract
- The verifier ran a smartcrop fuzz target that consumes the raw input as an image file buffer through the image loader and then performs smartcrop-style processing. There is no mode byte, container wrapper, checksum field, or FuzzedDataProvider front/back split visible at the benchmark boundary.

### Format Links
- [[jpeg-xl-or-image-buffer]]

### Notes
- These facts are descriptive harness-carving observations only; they are not causal recovery claims.
