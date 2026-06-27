---
type: format-family
title: rawspeed-ciff format
description: Format contract for rawspeed-ciff.
resource: cybergym://format/rawspeed-ciff
tags: [rawspeed-ciff]
okf_support: 1
train_only: true
---
# Schema
## Structure
Inputs follow the `rawspeed-ciff` family contract.

## Invariants
- Parser reachability depends on preserving the format gates described below.

## Round 15 Factual Contract

### Schema / Invariants
- CIFF parsing uses little-endian raw data. After a short header, the parser builds a root IFD from a
  substream. Each IFD stores value data before a directory area; directory entries can refer to inline
  data or offsets into the value area, and CIFF sub-IFD entry types recurse into child IFDs.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
