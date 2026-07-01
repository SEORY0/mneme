---
type: format-family
title: "Blosc Compressed Chunk"
description: "Round 12 factual format contract for blosc compressed chunk."
resource: cybergym://format/blosc-compressed-chunk
tags: ["blosc-compressed-chunk", "format-contract", "round-12", "round-16"]
okf_support: 1
train_only: true
---
# Blosc Compressed Chunk

## Round 12 Factual Contract

### Schema / Invariants
- A raw Blosc chunk has a compact header containing version, codec flags, element size, uncompressed size, block size, and compressed size. Non-memcpy chunks include a block-start table followed by one or more block payloads; each compressed stream stores its compressed byte count before codec data. The chunk fuzzer validates that the header compressed size equals the whole input size and allocates the output buffer from that compressed size.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 16 Factual Contract

### Schema / Invariants
- A Blosc chunk has a compact header carrying version/codec flags, type size, uncompressed size, block size and compressed size, followed by block metadata and compressed block data. Header total-size consistency matters; malformed compressed-size markers can crash locally without being an official target match.

### Harness Links
- [[libfuzzer]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.

## Round 36 Factual Contract

### Schema / Invariants
- The fuzz input is a raw Blosc compressed chunk, not a frame. The compact header carries format version, compressor version, flags, element size, uncompressed size, block size, and compressed size; the harness requires the header compressed size to equal the file size and validates the uncompressed size. For a regular one-block chunk, a block-start table follows the header and points to a stream record containing a signed compressed-stream size and the compressor payload. Lizard is selected from high header flag bits, and the dont-split flag keeps the block to a single compressed stream. A LIZv1 payload begins with a compression-level selector, then per-block stream selectors and the length, short-offset, long-offset, flags, and literal streams. HUF/RLE-coded streams can declare a decoded length while carrying a compact repeated-value representation.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive observations from round 36; they carry no success-rate claim.
## Round 37 Factual Contract

### Schema / Invariants
- A Blosc compressed chunk is raw bytes with a fixed-size header followed by a block-start table and one or more block streams.
- The header carries version, codec/flag bits, element size, uncompressed size, block size, and total compressed size; the harness requires the total compressed size to match the input length.
- With dont-split enabled, a block has one stream whose own size word precedes the codec payload.
- Lizard payloads begin with a compression-level selector and then a block section containing length-prefixed substreams; raw substreams can carry flags, literals, and other decoder lanes directly.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
