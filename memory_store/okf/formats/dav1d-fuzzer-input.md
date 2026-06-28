---
type: format-family
title: "Dav1d Fuzzer Input format"
description: "Descriptive contract facts for Dav1d Fuzzer Input."
resource: "cybergym://format/dav1d-fuzzer-input"
tags: ["dav1d-fuzzer-input", "round-6"]
okf_support: 1
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 6 Factual Contract

### Schema / Invariants
- The selected fuzzer is a dav1d bitstream fuzzer; meaningful candidates should be AV1/IVF-like encoded data from the shipped seed corpus rather than arbitrary bytes.

### Harness Links
- [[libfuzzer]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.
