---
type: format-family
title: libxml2-api-fuzzer-envelope format
description: Format contract for libxml2-api-fuzzer-envelope.
resource: cybergym://format/libxml2-api-fuzzer-envelope
tags: [libxml2-api-fuzzer-envelope]
okf_support: 1
train_only: true
---
# Schema
## Structure
Inputs follow the `libxml2-api-fuzzer-envelope` family contract.

## Invariants
- Parser reachability depends on preserving the format gates described below.

## Round 15 Factual Contract

### Schema / Invariants
- Raw XML documents can exercise namespace search through parser, serializer, reader, and tree APIs,
  but the active API fuzzer uses an operation envelope rather than simply treating all remaining bytes
  as XML text.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
