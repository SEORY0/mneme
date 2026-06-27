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

## Round 17 Factual Contract

### Schema / Invariants
- The input is a synthetic card-reader transcript.
- The first chunk supplies ATR bytes; later chunks are APDU response bodies followed by status bytes, then operation input and parameter chunks are consumed after card binding.
- OpenSC virtual reader inputs are a stream of length-prefixed chunks.
- The first chunk behaves as the card ATR, and later chunks model card responses whose trailing status bytes control success or failure while preceding bytes are returned as response data.
- The input is a sequence of little-endian length-prefixed chunks.
- The first chunk is the ATR, subsequent chunks emulate APDU responses with trailing status bytes, and later chunks provide operation inputs once PKCS#15 binding succeeds.
- The virtual smart-card format is a sequence of bounded chunks: ATR first, then APDU response bodies with status words.
- IDPrime-specific parsing depends on matching card identity, application selection, object metadata, and successful status propagation before object contents are copied.
- SC-HSM fuzzing still uses the OpenSC virtual reader chunk stream: ATR first, then APDU response chunks with status words.
- The vulnerable write path depends on card initialization, file selection, and a write-binary operation that gets a response pattern accepted as progress.

### Harness Links
- [[libfuzzer-pkcs15-reader]]
- [[opensc-card-fuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
