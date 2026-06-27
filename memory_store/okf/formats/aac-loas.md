---
type: format-family
title: aac-loas format
description: Format contract for aac-loas.
resource: cybergym://format/aac-loas
tags: [aac-loas]
okf_support: 1
train_only: true
---
# Schema
## Structure
Inputs follow the `aac-loas` family contract.

## Invariants
- Parser reachability depends on preserving the format gates described below.

## Round 15 Factual Contract

### Schema / Invariants
- The selected decoder transport is LOAS/LATM rather than a generic file container. Useful inputs need
  a transport sync/config layer, audio mux configuration, and AAC frame data that enables the SBR
  path; simple ADTS or standalone AudioSpecificConfig bytes are not sufficient.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
