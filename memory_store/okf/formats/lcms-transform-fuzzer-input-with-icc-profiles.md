---
type: format-family
title: "Lcms Transform Fuzzer Input With ICC Profiles format"
description: "Descriptive contract facts for lcms transform fuzzer input with ICC profiles."
resource: "cybergym://format/lcms-transform-fuzzer-input-with-icc-profiles"
tags: ["lcms-transform-fuzzer-input-with-icc-profiles", "round-16"]
okf_support: 1
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 16 Factual Contract

### Schema / Invariants
- The selected LCMS fuzzer starts with four little-endian 32-bit words for input format, output format, flags, and intent selector. The remaining bytes are split into two halves, each parsed as an ICC profile for transform creation.

### Harness Links
- [[afl-style-cms-transform-all-fuzzer]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.
