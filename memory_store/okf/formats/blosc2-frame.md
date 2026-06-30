---
type: format-family
title: blosc2-frame format
description: Format contract for blosc2-frame.
resource: cybergym://format/blosc2-frame
tags: [blosc2-frame]
okf_support: 11
train_only: true
---
# Schema
## Structure
Inputs follow the `blosc2-frame` family contract.

## Invariants
- Parser reachability depends on preserving the format gates described below.

## Round 15 Factual Contract

### Schema / Invariants
- A blosc2 frame starts with a msgpack-like frame header containing magic, header length, total frame
  length, sizes, codec/filter metadata, and a metalayer index envelope. The metalayer index maps names
  to signed serialized-value offsets, followed by serialized metalayer contents. Chunk-offset data and
  a trailer appear after the header and compressed chunks.

### Harness Links
- [[libfuzzer-afl]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 27 Factual Contract

- A Blosc2 serialized frame begins with a msgpack-like frame header containing magic, header size, total frame size, uncompressed size, compressed-data size, type size, chunk size, thread counts, filter pipeline, and a metalayer index.
- Data chunks are followed by a compressed chunk-offset index, and a trailer at the end carries usermeta length and trailer length.
- The number of chunks is derived from uncompressed size and chunk size; the frame-index location is derived from header size plus compressed-data size.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
