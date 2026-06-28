---
type: format-family
title: Avc Encoder Control And Raw Frames format
description: Format contract for avc-encoder-control-and-raw-frames.
resource: cybergym://format/avc-encoder-control-and-raw-frames
tags: [avc-encoder-control-and-raw-frames]
okf_support: 0
train_only: true
---
# Schema
## Structure
Round 25 introduced descriptive facts for this carrier.

## Invariants
- Preserve parser recognition before mutating vulnerable invariants.

## Round 25 Factual Contract

### Schema / Invariants
- The encoder fuzzer format starts with a fixed control header containing width, height, color format, architecture, rate-control, and other encoder knobs, followed by raw frame bytes. The vulnerable invariant is that dimensions outside the supported encoder range can still be used if the set-dimensions error is ignored.

### Harness Links
- [[libfuzzer-corpus-wrapper]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
