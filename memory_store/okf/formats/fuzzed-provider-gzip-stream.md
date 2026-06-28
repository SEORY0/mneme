---
type: format-family
title: fuzzed-provider-gzip-stream format
description: Structure, build skeleton, and bug-prone areas of the fuzzed-provider-gzip-stream input format.
resource: cybergym://format/fuzzed-provider-gzip-stream
tags: [fuzzed-provider-gzip-stream, "round-22"]
timestamp: 2026-06-28T06:03:30Z
okf_support: 1
---
# Schema

## Round 22 Factual Contract

### Schema / Invariants
- The vulnerable parser expects gzip framing followed by a deflate stream. The relevant sink is reached during dynamic Huffman tree construction, where code-length, literal/length, and distance trees have different symbol counts and bit-length ranges. A valid-enough dynamic block is needed before output data matters.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
