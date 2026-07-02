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

## Round 30 Factual Contract

### Schema / Invariants
- The wrapper input starts with little-endian transform control words, followed by two equal profile byte ranges. Each ICC profile has a fixed header with the ICC magic, declared size, device class, color space, PCS, then a big-endian tag directory. Each directory record carries a tag signature plus payload location and size; duplicate tag signatures are invalid even when payload bounds remain otherwise coherent.

### Harness Links
- [[libfuzzer-cms-transform-all-fuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
