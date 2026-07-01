---
type: harness-contract
title: "Libfuzzer Kimageformats Raw Qbuffer harness"
description: "Input contract facts for libfuzzer-kimageformats-raw-qbuffer."
tags: ["libfuzzer-kimageformats-raw-qbuffer", "round-33"]
okf_support: 1
---
# Libfuzzer Kimageformats Raw Qbuffer Harness

## Round 33 Input Contract

### Input Contract
- The kimageformats libFuzzer harness feeds the PoC bytes directly into a QBuffer, then calls the TGA QImageIOHandler canRead and read methods. There is no filename extension, pcap wrapper, selector byte, checksum, or FuzzedDataProvider front/back carving; all reachability is controlled by the raw TGA bytes.

### Format Links
- [[tga]]

### Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.
