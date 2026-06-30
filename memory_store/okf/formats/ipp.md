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

## Round 28 Factual Contract

### Schema / Invariants
- An IPP message starts with a fixed-size request header, followed by group tags and value-tagged attributes, ending with an end tag. Attribute records encode a value tag, a big-endian name length, the attribute name, a big-endian value length, and the typed value bytes. A zero name length on a subsequent value means the value belongs to the current attribute. Language-qualified text/name values are composite values containing a language length and language string followed by a text length and text string.

### Harness Links
- [[libfuzzer-file-fuzzipp]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
