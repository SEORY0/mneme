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
