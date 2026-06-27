---
type: format-family
title: "blosc-chunk format"
description: "Structure and reachability facts for blosc chunk."
resource: cybergym://format/blosc-chunk
tags: ["blosc-chunk"]
okf_support: 1
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
