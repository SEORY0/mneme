---
type: format-family
title: "Opensc Virtual Reader Chunk Stream format"
description: "Descriptive contract facts for opensc virtual-reader chunk stream."
resource: "cybergym://format/opensc-virtual-reader-chunk-stream"
tags: ["opensc-virtual-reader-chunk-stream", "round-16"]
okf_support: 2
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 16 Factual Contract

### Schema / Invariants
- The OpenSC virtual reader consumes two-byte little-endian chunk lengths followed by chunk data. The first chunk supplies the ATR; later chunks emulate APDU responses with status bytes at the end of each response chunk.
- The IDPrime path is selected by a matching smart-card ATR, then further behavior depends on APDU response chunks that drive application selection, index processing, and private object list construction.

### Harness Links
- [[honggfuzz-style-pkcs15-reader-harness]]
- [[libfuzzer-pkcs15-reader-harness]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.
