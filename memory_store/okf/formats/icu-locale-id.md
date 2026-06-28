---
type: format-family
title: icu-locale-id format
description: Format contract for icu-locale-id.
resource: cybergym://format/icu-locale-id
tags: [icu-locale-id]
okf_support: 3
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

## Round 18 Factual Contract

### Schema / Invariants
- ICU locale IDs can contain language, script, region, variants, private-use material, and keyword assignments. The language-tag conversion path canonicalizes locale components and maps Unicode locale keywords and attributes into BCP-style extension subtags, which can substantially expand the output relative to the input.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.

## Round 21 Factual Contract (libfuzzer)

### Schema / Invariants
- ICU locale IDs are raw NUL-terminated strings with language, optional script and region, and extension or private-use segments. The right-to-left fast path first asks for script, then extracts a short language subtag and searches a compact language-direction table.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
