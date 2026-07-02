---
type: harness-contract
title: "Libfuzzer Pkcs15 Reader harness"
description: "Input contract facts for libfuzzer pkcs15 reader."
tags: ["libfuzzer-pkcs15-reader", "round-17"]
okf_support: 1
train_only: true
---
# Libfuzzer Pkcs15 Reader Harness

## Round 17 Input Contract
- This build uses a nonstandard chunk reader: each chunk length is effectively taken from one leading byte while two bytes are consumed for the length field, and the chunk data pointer is not advanced by the chunk body in the same way as the later proper reader.
- The harness installs a virtual reader, connects a card using the first chunk as ATR, then consumes additional chunks as APDU responses during PKCS#15 bind and object operations.

## Round 17 Format Links
- [[opensc-virtual-reader-chunk-stream]]

## Round 17 Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.

## Round 17 Format Links
- [[opensc-virtual-reader-chunk-stream]]

## Round 17 Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.

## Round 26 Factual Contract


### Input Contract
- The fuzz target installs a virtual OpenSC reader, binds a PKCS#15 card, then consumes two additional chunks as operation input and parameter buffers before iterating all PKCS#15 objects through decrypt, derive, unwrap/wrap, signature, and PIN operations. Coolkey is reached through APDU-speaking card-driver matching; normal PKCS#15 file probes occur before synthetic Coolkey emulation and consume APDU response chunks. The combined-object route stores object data during card initialization, avoiding later direct object-data reads.

### Format Links
- [[opensc-coolkey-reader-chunks]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.

## Round 34 Factual Contract

### Input Contract
- The fuzz target installs a fake OpenSC reader, connects a card, binds PKCS#15, then consumes two more chunks as operation input and parameters before iterating PKCS#15 objects. Before synthetic CoolKey binding, normal PKCS#15 file probes consume APDU response chunks, so the transcript needs explicit failing probe responses to keep the later operation chunks aligned.
- The libFuzzer target feeds raw bytes to a virtual OpenSC reader. The reader consumes length-prefixed chunks front-to-back: connect consumes ATR, card-driver matching and PKCS#15 binding consume APDU response chunks, then the harness consumes two additional chunks as operation input and parameter buffers before iterating discovered PKCS#15 objects through decrypt, derive, wrap, signature, and PIN APIs. CoolKey is reached through APDU-speaking card-driver matching; a generic ATR can avoid earlier ATR table matches and leave early APDU chunks for CoolKey selection.
- The libFuzzer target feeds raw bytes to a virtual OpenSC reader. The harness consumes chunks from front to back: one ATR chunk during connect, APDU-response chunks during card matching and PKCS#15 binding, then two more chunks as operation input and parameters before it iterates PKCS#15 objects through crypto and PIN APIs. APDU chunks shorter than a status pair synthesize an invalid-instruction status.

### Format Links
- [[opensc-coolkey-reader-chunks]]

### Notes
- These facts are descriptive observations only; they carry no success-rate claim.
## Round 37 Input Contract

### Input Contract
- The libFuzzer wrapper feeds the raw file as a smart-card transcript.
- There is no FuzzedDataProvider or leading mode byte; reachability depends on the exact order in which the OpenSC reader consumes ATR and APDU-response chunks.
- The fuzz target consumes the raw input as fake smart-card reader data, not as a file format with checksums and not through FuzzedDataProvider.
- Chunk boundaries determine the ATR and each APDU response.
- Each response must carry a successful status word to keep initialization moving into the CardOS-specific parser.

### Format Links
- [[opensc-cardos-fake-reader-apdu]]
- [[opensc-pkcs15-reader-chunk-stream]]

### Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
