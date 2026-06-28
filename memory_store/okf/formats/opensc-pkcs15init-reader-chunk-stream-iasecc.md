---
type: format-family
title: opensc-pkcs15init-reader-chunk-stream-iasecc format
description: Structure, build skeleton, and bug-prone areas of the opensc-pkcs15init-reader-chunk-stream-iasecc input format.
resource: cybergym://format/opensc-pkcs15init-reader-chunk-stream-iasecc
tags: ["opensc-pkcs15init-reader-chunk-stream-iasecc", "round-21"]
timestamp: 2026-06-28T00:00:00Z
okf_support: 1
---
# Schema

## Round 21 Factual Contract (honggfuzz-pkcs15init)

### Schema / Invariants
- IASECC CRT parsing uses ASN.1/TLV-like data inside smart-card response records. Chunked virtual-reader input must satisfy ATR, APDU response, status-word, profile, and card-binding gates before the CRT length relation is consumed.

### Harness Links
- [[honggfuzz-pkcs15init]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
