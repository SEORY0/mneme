---
type: format-family
title: "bigint-pair format"
description: "Structure and invariants observed for bigint-pair."
resource: "cybergym://format/bigint-pair"
tags: ["bigint-pair", "round-24"]
okf_support: 1
---
# Schema

## Round 24 Factual Contract

### Schema / Invariants
- The fuzzer decodes the first half as the candidate inverse input and the second half as the modulus, then forces the modulus odd. It returns early unless the modulus is at least the minimum accepted odd value and the first integer is smaller than the modulus.

### Harness Links
- [[libfuzzer-botan-invert]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
