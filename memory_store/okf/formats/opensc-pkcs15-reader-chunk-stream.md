---
type: format-family
title: "Opensc Pkcs15 Reader Chunk Stream"
description: "Round 12 factual format contract for opensc pkcs15 reader chunk stream."
resource: cybergym://format/opensc-pkcs15-reader-chunk-stream
tags: ["opensc-pkcs15-reader-chunk-stream", "format-contract", "round-12"]
okf_support: 10
train_only: true
---
# Opensc Pkcs15 Reader Chunk Stream

## Round 12 Factual Contract

### Schema / Invariants
- The fuzz input is a sequence of length-prefixed chunks. The first chunk is used as ATR data and subsequent chunks are consumed as card/APDU responses. APDU response chunks end with status bytes and earlier response bytes are copied into the requested response buffer. The likely target path involves CAC compressed certificate handling and zlib-style decompression into a cached buffer.
- The input is a synthetic smart-card reader transcript rather than a conventional file. The transcript is consumed as a sequence of length-prefixed chunks that emulate connect, transmit, operation input, operation parameter, and key-material responses.

### Harness Links
- [[honggfuzz-libfuzzer-wrapper]]
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 27 Factual Contract

- The OpenSC reader corpus is a virtual smart-card transcript.
- Each chunk is preceded by a little-endian two-byte length.
- The first chunk is treated as the ATR.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 30 Factual Contract

### Schema / Invariants
- The PKCS#15 reader harness consumes a stream of native little-endian length-prefixed chunks. The first chunk is used as the ATR. Later chunks act as APDU responses; when a response chunk has status bytes at the end, the preceding response body is copied into the APDU response buffer only up to the requested response length. SetCOS file selection expects FCI-like APDU bodies whose security attributes are parsed after a successful select-file response.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
