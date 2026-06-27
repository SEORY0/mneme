---
type: format-family
title: "zlib-deflate format"
description: "Structure and invariants for the zlib-deflate input format."
tags: ["zlib-deflate", "round-14"]
okf_support: 1
---
# Schema
## Identification
Factual format observations distilled from verifier traces. These are descriptive facts only and carry no success-rate claim.

## Round 14 Factual Contract

### Schema / Invariants
- The vulnerable decompressor path is reached through a zlib-wrapped deflate stream. The interesting invariant is a length/distance copy before meaningful output history exists, but normal uncompress paths can reject distances that point before the current output buffer.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
