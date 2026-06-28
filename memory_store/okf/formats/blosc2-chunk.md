---
type: format-family
title: "blosc2-chunk format"
description: "Structure and invariants for the blosc2-chunk input format."
tags: ["blosc2-chunk", "round-14"]
okf_support: 1
---
# Schema
## Identification
Factual format observations distilled from verifier traces. These are descriptive facts only and carry no success-rate claim.

## Round 14 Factual Contract

### Schema / Invariants
- A regular Blosc chunk has a fixed header with version, codec flags, type size, uncompressed size, block size, and total compressed size. Non-memcpy chunks include block-start entries followed by compressed stream records, each carrying a stream size and codec-specific bytes. The high flag bits select the compressor and the no-split flag collapses a block to a single stream.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
