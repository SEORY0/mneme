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
