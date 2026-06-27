---
type: format-family
title: libavc-encoder-config-plus-frame-bytes format
description: Structure and reachability facts for libavc-encoder-config-plus-frame-bytes inputs.
tags: [libavc-encoder-config-plus-frame-bytes]
okf_support: 0
---
# Libavc Encoder Config Plus Frame Bytes Format

## Round 10 Factual Contract

### Schema / Invariants
- The encoder fuzzer consumes a fixed front-loaded configuration region for dimensions, color format, architecture, rate-control, quality, GOP, SEI, dynamic-change, and end-of-stream flags. Remaining bytes are expanded or split into YUV frame planes according to the selected color format.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
