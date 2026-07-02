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

## Round 23 Factual Contract

### Schema / Invariants
- The uncompress harness expects a zlib-wrapped deflate stream. Fixed-Huffman blocks can encode literals, length symbols, distance symbols, and an end marker without dynamic table setup; the problematic distance symbols are only useful when paired with a length code that reaches the back-reference copy path.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 36 Factual Contract

### Schema / Invariants
- The carrier is a zlib wrapper around a deflate block with a valid header and checksum. Fixed-Huffman deflate can encode a length symbol, a distance symbol, and an end-of-block marker without a dynamic table. Reserved high distance symbols are invalid in the format but, in the vulnerable decoder, can map to a zero distance rather than being rejected before the copy loop.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive observations from round 36; they carry no success-rate claim.
