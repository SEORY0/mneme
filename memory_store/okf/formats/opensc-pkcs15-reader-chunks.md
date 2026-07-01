---
type: format-family
title: "Opensc Pkcs15 Reader Chunks format"
description: "Round 34 factual contract for opensc-pkcs15-reader-chunks."
tags: ["opensc-pkcs15-reader-chunks", "round-34"]
okf_support: 1
train_only: true
---
# Opensc Pkcs15 Reader Chunks format

## Round 34 Factual Contract

### Schema / Invariants
- The reader input is a stream of native-endian length-prefixed chunks. The first chunk supplies the ATR; subsequent chunks are APDU responses whose final status bytes set the card status word and whose preceding bytes become response data. DNIe selection walks the master file and application/file identifiers, FCI responses carry an ISO wrapper plus a proprietary attribute describing DF, plain EF, or compressed EF files, and compressed EF content begins with little-endian uncompressed/compressed lengths followed by a zlib stream. PKCS#15 TokenInfo is ASN.1 with version, manufacturer, and token flags; ODF entries are context-specific choices containing ASN.1 paths to DF files.

### Harness Links
- [[honggfuzz-libfuzzer]]

### Notes
- These facts are descriptive observations only; they carry no success-rate claim.
