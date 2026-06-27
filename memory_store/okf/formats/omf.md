---
type: format-family
title: omf format
description: Format contract for omf.
resource: cybergym://format/omf
tags: [omf]
okf_support: 1
train_only: true
---
# Schema
## Structure
Inputs follow the `omf` family contract.

## Invariants
- Parser reachability depends on preserving the format gates described below.

## Round 15 Factual Contract

### Schema / Invariants
- OMF records begin with a one-byte record type from a recognized set, followed by record metadata
  that plugin detection may inspect before full parsing. Truncated prefixes can reach the vulnerable
  boundary when they look enough like a valid OMF record to select the plugin.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
