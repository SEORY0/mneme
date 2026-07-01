---
type: format-family
title: libidn2-raw-domain-or-uint32-codepoints format
description: Structure and reachability facts for libidn2-raw-domain-or-uint32-codepoints inputs.
tags: [libidn2-raw-domain-or-uint32-codepoints]
okf_support: 1
---
# Libidn2 Raw Domain Or Uint32 Codepoints Format

## Round 10 Factual Contract

### Schema / Invariants
- The fuzzer treats raw bytes both as nul-terminated byte strings and, when the total length is word-aligned, as a sequence of native-endian Unicode codepoints for the 4i conversion API. The target copy occurs only after lookup succeeds and returns an ASCII-compatible domain string.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 32 Factual Contract

### Schema / Invariants
- The fuzzer treats the same raw bytes first as a nul-terminated byte string and, when the total size is divisible by four, as native-endian 32-bit Unicode codepoints. The target path is the 4i conversion API: it copies codepoints into a temporary UCS-4 buffer, converts to UTF-8, performs IDNA lookup, and then copies the resulting ASCII-compatible domain into a caller-provided output buffer. Multiple labels can make the full domain longer than a single label while keeping each label valid.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
