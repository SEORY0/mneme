---
type: format-family
title: Opensc Pkcs15Init Profile Plus Virtual Reader Stream format
description: Format contract for opensc pkcs15init profile plus virtual reader stream inputs.
resource: cybergym://format/opensc-pkcs15init-profile-plus-virtual-reader-stream
tags: [opensc-pkcs15init-profile-plus-virtual-reader-stream, buffer-underflow, round-11]
okf_support: 2
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

## Round 31 Factual Contract

### Schema / Invariants
- The input prefix is parsed as pkcs15-init profile text and must be terminated before the reader stream. The stream is a sequence of little-endian length-prefixed chunks: the first chunk is ATR data, and each later chunk is an APDU response whose trailing status word drives success or rejection. OpenPGP card state is represented as BER-like data-object TLVs; constructed objects can contain child data objects, and global tag search walks earlier constructed branches before later ones. A valid carrier needs a selectable OpenPGP application, card capability/object metadata, PIN-status data, algorithm attributes, a full fingerprint table for binding, and a key-generation response containing RSA public-key material.

### Harness Links
- [[libfuzzer-opensc-pkcs15init]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
