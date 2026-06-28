---
type: format-family
title: "Opensc Fuzz Reader Chunks"
description: "Round 7 factual format contract for opensc-fuzz-reader-chunks."
resource: cybergym://format/opensc-fuzz-reader-chunks
tags: ["opensc-fuzz-reader-chunks", "format-contract", "round-7"]
okf_support: 1
train_only: true
---
# Opensc Fuzz Reader Chunks

## Round 7 Factual Contract

### Schema / Invariants
- The OpenSC reader harness is a sequence of little-endian length-prefixed chunks. The first chunk is
used as ATR data; later chunks are consumed as card transmit responses where the last two bytes are
status words and the preceding bytes are copied as APDU response data.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 10 Factual Contract

### Schema / Invariants
- The fuzzer input is a sequence of little-endian length-prefixed chunks. The first chunk becomes the reader ATR. Later chunks are returned as APDU responses, with the final two response bytes interpreted as status words and the preceding bytes copied as response data.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 12 Factual Contract

### Schema / Invariants
- The input is a concatenation of reader chunks. Each chunk starts with a little-endian length field followed by that many response bytes. The first chunk becomes the card ATR; later chunks are APDU response bodies whose final status bytes become the APDU status words.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 22 Factual Contract

### Schema / Invariants
- The input is a sequence of reader chunks. Each chunk begins with a native-endian small length field followed by that many response bytes. The first chunk is used as the card ATR, later chunks are returned as APDU responses with trailing status words when long enough, and extra chunks can become payload and parameter buffers for PKCS#15 operations.

### Harness Links
- [[honggfuzz-libfuzzer-style-reader-fuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
