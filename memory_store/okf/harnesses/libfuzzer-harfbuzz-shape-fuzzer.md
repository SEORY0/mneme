---
type: harness-contract
title: "Libfuzzer Harfbuzz Shape Fuzzer harness"
description: "Input contract facts for libfuzzer-harfbuzz-shape-fuzzer."
tags: ["libfuzzer-harfbuzz-shape-fuzzer"]
okf_support: 0
---
# Libfuzzer Harfbuzz Shape Fuzzer Harness

## Round 10 Input Contract
- The harness treats the buffer as a font blob, creates a face/font, derives some shaping parameters from available bytes, and runs shape tests over fixed text. There is no file container or leading mode byte.

## Round 10 Format Links
- [[opentype-truetype-font]]

## Round 10 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
