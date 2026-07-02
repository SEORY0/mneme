---
type: format-family
title: "Cram"
description: "Round 7 factual format contract for cram."
resource: cybergym://format/cram
tags: ["cram", "format-contract", "round-7"]
okf_support: 1
train_only: true
---
# Cram

## Round 7 Factual Contract

### Schema / Invariants
- CRAM inputs start with a CRAM file header followed by containers, slices, compression headers, block
content, and codec descriptors. XPACK is an experimental CRAM 4.0 encoding that appears in codec
metadata rather than in the top-level file header alone.

### Harness Links
- [[afl-style-file]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 34 Factual Contract

### Schema / Invariants
- CRAM v3 uses a file definition followed by containers whose headers and blocks are CRC-protected. Mapped slice headers carry reference id/start/span, record count, content IDs, reference-base ID, and MD5. Raw slice-header blocks can be seed-mutated if size relationships and CRCs remain coherent.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive observations only; they carry no success-rate claim.
## Round 37 Factual Contract

### Schema / Invariants
- CRAM starts with a fixed file definition, then a SAM header stored as a container containing a file-header block.
- Later containers carry a compression-header block followed by slice blocks.
- In CRAM v3 and later, container headers and blocks are CRC-protected, so generated or mutated inputs must recompute those checks.
- CRAM v4 switches many container, block, and compression-header integers to variable-length encoding.
- Compression headers contain a preservation map, a record-encoding map keyed by two-character data-series names, and a tag-encoding map.
- XPACK descriptors store bit width, reverse-map cardinality, reverse-map symbols, and a nested subcodec descriptor.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
