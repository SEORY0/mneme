---
type: format-family
title: icu-locale-id format
description: Format contract for icu-locale-id.
resource: cybergym://format/icu-locale-id
tags: [icu-locale-id]
okf_support: 1
train_only: true
---
# Schema
## Structure
Inputs follow the `icu-locale-id` family contract.

## Invariants
- Parser reachability depends on preserving the format gates described below.

## Round 15 Factual Contract

### Schema / Invariants
- ICU locale IDs include language, script, region, variants, Unicode extension key/type pairs,
  transformed extension data, and private-use subtags. The canonicalizer normalizes separators,
  aliases, and extension ordering into a fixed-size destination buffer.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
