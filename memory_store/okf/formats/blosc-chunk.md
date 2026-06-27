---
type: format-family
title: "blosc-chunk format"
description: "Structure and reachability facts for blosc chunk."
resource: cybergym://format/blosc-chunk
tags: ["blosc-chunk", "round-16"]
okf_support: 2
---
# Blosc Chunk Format

## Round 9 Factual Contract

### Schema / Invariants
- A Blosc chunk starts with a compact header containing version, flags, type size, uncompressed
  size, block size, and compressed size, followed by block-start entries and per-stream records.
- Split blocks use one stream per type lane; negative stream sizes encode special runs and are the
  important malformed field family here.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 16 Factual Contract

### Schema / Invariants
- A compact Blosc chunk starts with version, codec flags, type size, uncompressed size, block size, and total compressed size, followed by block-start entries and per-block stream records. For zlib-backed chunks the high codec flag selects the zlib/miniz format; a no-split flag can reduce a block to one stream. The header compressed size must equal the full input length.

### Harness Links
- [[libfuzzer]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.
