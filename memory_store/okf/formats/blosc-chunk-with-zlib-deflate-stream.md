---
type: format-family
title: "Blosc Chunk With Zlib Deflate Stream"
description: "Round 36 factual format contract for blosc-chunk-with-zlib-deflate-stream."
tags: ["blosc-chunk-with-zlib-deflate-stream", "round-36", "format-contract"]
okf_support: 1
train_only: true
---
# Blosc Chunk With Zlib Deflate Stream

## Round 36 Factual Contract

### Schema / Invariants
- A regular Blosc chunk begins with version, codec/flag bits, type size, uncompressed size, block size, and total compressed size. The decompression fuzzer requires the header compressed size to equal the file size and the uncompressed size to be nonzero. Non-memcpy chunks carry a block-start table after the compact header; each block stream then starts with a compressed-stream length followed by codec bytes. The high codec flag bits select the zlib/miniz backend, and the no-split flag collapses the block to one stream. Deflate fixed-Huffman symbols are canonical codes carried least-significant-bit first, so the practical builder must reverse fixed-code values before writing bits.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive observations from round 36; they carry no success-rate claim.
