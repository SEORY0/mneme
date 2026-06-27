---
type: format-family
title: libidn2-raw-domain-or-uint32-codepoints format
description: Structure and reachability facts for libidn2-raw-domain-or-uint32-codepoints inputs.
tags: [libidn2-raw-domain-or-uint32-codepoints]
okf_support: 0
---
# Libidn2 Raw Domain Or Uint32 Codepoints Format

## Round 10 Factual Contract

### Schema / Invariants
- The fuzzer treats raw bytes both as nul-terminated byte strings and, when the total length is word-aligned, as a sequence of native-endian Unicode codepoints for the 4i conversion API. The target copy occurs only after lookup succeeds and returns an ASCII-compatible domain string.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
