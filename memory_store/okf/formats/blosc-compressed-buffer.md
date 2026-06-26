---
type: format-family
title: "Blosc Compressed Buffer format"
description: "Round 8 descriptive format facts for blosc compressed buffer."
resource: cybergym://format/blosc-compressed-buffer
tags: ["blosc-compressed-buffer", "round-8"]
okf_support: 1
---
# Blosc Compressed Buffer Format

## Round 8 Factual Contract

### Schema / Invariants
- The decompression harness expects the Blosc buffer size to agree with the cbytes field and validates nbytes/blocksize before decompression. Compressor selection is encoded in the Blosc header, but merely changing the format bits on a buffer compressed by another codec does not produce a useful Lizard payload.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

