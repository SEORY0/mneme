---
type: format-family
title: ipp format
description: Format contract for ipp.
resource: cybergym://format/ipp
tags: [ipp]
okf_support: 1
train_only: true
---
# Schema
## Structure
Inputs follow the `ipp` family contract.

## Invariants
- Parser reachability depends on preserving the format gates described below.

## Round 15 Factual Contract

### Schema / Invariants
- IPP messages start with a version, operation/status, request id, then group tags and attributes.
  Each attribute has a value tag, big-endian name length and name, big-endian value length, and value
  bytes. A repeated value for the current attribute is encoded with an empty name, allowing setOf
  values and type-conversion logic to run.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
