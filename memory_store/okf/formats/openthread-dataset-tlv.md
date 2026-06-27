---
type: format-family
title: openthread-dataset-tlv format
description: Format contract for openthread-dataset-tlv.
resource: cybergym://format/openthread-dataset-tlv
tags: [openthread-dataset-tlv]
okf_support: 1
train_only: true
---
# Schema
## Structure
Inputs follow the `openthread-dataset-tlv` family contract.

## Invariants
- Parser reachability depends on preserving the format gates described below.

## Round 15 Factual Contract

### Schema / Invariants
- OpenThread operational datasets are TLV streams. Each record has a type, length, and value;
  timestamp-style TLVs and delay timer TLVs require minimum value lengths before their contents are
  interpreted. A malformed dataset can use a recognized TLV type with an undersized value to test
  those minimum-length checks.

### Harness Links
- [[unavailable-after-gen-extraction-failure]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
