---
type: format-family
title: vp9-frame format
description: Format contract for vp9-frame.
resource: cybergym://format/vp9-frame
tags: [vp9-frame]
okf_support: 1
train_only: true
---
# Schema
## Structure
Inputs follow the `vp9-frame` family contract.

## Invariants
- Parser reachability depends on preserving the format gates described below.

## Round 15 Factual Contract

### Schema / Invariants
- The target consumes a single VP9 sample. The parser first checks for a superframe trailer; absent a
  valid trailer it treats the entire buffer as one frame. A useful frame must satisfy the uncompressed
  header gates before compressed header or tile range decoding is attempted.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
