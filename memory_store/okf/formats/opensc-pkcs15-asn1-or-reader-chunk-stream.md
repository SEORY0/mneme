---
type: format-family
title: Opensc Pkcs15 Asn1 Or Reader Chunk Stream format
description: Format contract for opensc-pkcs15-asn1-or-reader-chunk-stream inputs.
resource: cybergym://format/opensc-pkcs15-asn1-or-reader-chunk-stream
tags: [opensc-pkcs15-asn1-or-reader-chunk-stream, invalid-ec-key-type-handling, round-11]
okf_support: 1
train_only: true
---
# Schema
## Structure
OpenSC fuzz inputs are either direct ASN.1 blobs for PKCS#15 object decoders or a sequence of little-endian length-prefixed chunks. In the reader harness, the first chunk is an ATR and later chunks are APDU response data with trailing status bytes.

## Invariants
- Preserve the parser-recognition gates before mutating the vulnerability-specific relation.
- Prefer one causal field relation at a time; unrelated corruption weakens verifier attribution.

## Harness Links
- [[libfuzzer]]

## Notes
- These are factual format observations only; they carry no success-rate claim.
