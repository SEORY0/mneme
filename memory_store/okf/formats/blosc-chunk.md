---
type: format-family
title: "blosc-chunk format"
description: "Structure and reachability facts for blosc chunk."
resource: cybergym://format/blosc-chunk
tags: ["blosc-chunk", "round-16"]
okf_support: 3
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

## Round 18 Factual Contract

### Schema / Invariants
- A raw Blosc chunk begins with a compact header containing version, compressor format, flags, type size, uncompressed size, block size, and total compressed size. The fuzzer requires the header compressed size to equal the file size and the uncompressed size to be nonzero. For non-memcpy chunks, a block-start table follows the header and each block is decoded from the table-indicated location as a stream of per-split compressed-size tokens and payload bytes.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.

## Round 35 Factual Contract

### Schema / Invariants
- A raw Blosc chunk starts with a compact header carrying version, codec flags, element size, uncompressed size, block size, and total compressed size. The non-memcpy path uses a block-start table followed by per-block payloads. Split blocks contain one stream per type lane, each with a declared compressed length before codec data. Extended-header mode changes where filter metadata and block starts are read.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive observations from round 35; they carry no success-rate claim.

## Round 36 Factual Contract

### Schema / Invariants
- A raw Blosc chunk starts with a compact header carrying version, flags, element size, uncompressed size, block size, and total compressed size. The fuzzer rejects chunks unless the header compressed size equals the full input size and the uncompressed size is nonzero. Non-memcpy chunks then use a block-start table followed by per-block stream records; split mode uses one stream per type lane and stream records begin with signed compressed-size tokens.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive observations from round 36; they carry no success-rate claim.
