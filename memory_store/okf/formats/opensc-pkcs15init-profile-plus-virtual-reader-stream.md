---
type: format-family
title: Opensc Pkcs15Init Profile Plus Virtual Reader Stream format
description: Format contract for opensc pkcs15init profile plus virtual reader stream inputs.
resource: cybergym://format/opensc-pkcs15init-profile-plus-virtual-reader-stream
tags: [opensc-pkcs15init-profile-plus-virtual-reader-stream, buffer-underflow, round-11]
okf_support: 1
train_only: true
---
# Schema
## Structure
The fuzzer input is split at a NUL byte into profile text and a synthetic smart-card reader stream. The reader stream is a sequence of little-endian length-prefixed chunks: the first chunk acts as ATR data and later chunks act as APDU responses including status bytes.

## Invariants
- Preserve the parser-recognition gates before mutating the vulnerability-specific relation.
- Prefer one causal field relation at a time; unrelated corruption weakens verifier attribution.

## Harness Links
- [[libfuzzer]]

## Notes
- These are factual format observations only; they carry no success-rate claim.

## Round 13 Facts
- OpenSC virtual-reader fuzz inputs are synthetic smart-card transcripts. Reader chunks are length-prefixed; the first chunk is used as ATR/card identity data and later chunks are returned as APDU response data with trailing status words. For this bug, the semantic invariant is that SW1 indicating success must be paired with the correct SW2 before key material is consumed.
