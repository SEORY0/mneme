---
type: format-family
title: "zstd-legacy format"
description: "Structure and invariants for the zstd-legacy input format."
tags: ["zstd-legacy", "round-14"]
okf_support: 1
---
# Schema
## Identification
Factual format observations distilled from verifier traces. These are descriptive facts only and carry no success-rate claim.

## Round 14 Factual Contract

### Schema / Invariants
- The stream target consumes an initial fuzz seed before the compressed stream. Legacy Zstd frames are selected by a little-endian legacy magic for the old frame version; reaching the sink also requires a syntactically plausible compressed block with literals and sequence headers, not just the frame magic.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
