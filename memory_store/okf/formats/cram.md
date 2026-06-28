---
type: format-family
title: "Cram"
description: "Round 7 factual format contract for cram."
resource: cybergym://format/cram
tags: ["cram", "format-contract", "round-7"]
okf_support: 1
train_only: true
---
# Cram

## Round 7 Factual Contract

### Schema / Invariants
- CRAM inputs start with a CRAM file header followed by containers, slices, compression headers, block
content, and codec descriptors. XPACK is an experimental CRAM 4.0 encoding that appears in codec
metadata rather than in the top-level file header alone.

### Harness Links
- [[afl-style-file]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
