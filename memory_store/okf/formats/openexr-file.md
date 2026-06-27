---
type: format-family
title: openexr-file format
description: Format contract for openexr-file.
resource: cybergym://format/openexr-file
tags: [openexr-file]
okf_support: 1
train_only: true
---
# Schema
## Structure
Inputs follow the `openexr-file` family contract.

## Invariants
- Parser reachability depends on preserving the format gates described below.

## Round 15 Factual Contract

### Schema / Invariants
- OpenEXR files start with magic/version words followed by typed attributes such as channels,
  compression, data/display windows, line order, pixel aspect, and screen-window fields, then offset
  tables and chunk data. Channel lists contain NUL-terminated names and fixed channel metadata
  records.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
