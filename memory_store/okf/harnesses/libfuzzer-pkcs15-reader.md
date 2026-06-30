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
