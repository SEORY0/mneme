---
type: format-family
title: "Opensc Virtual Reader Chunk Stream Iasecc"
description: "Round 19 factual format contract for opensc-virtual-reader-chunk-stream-iasecc."
resource: cybergym://format/opensc-virtual-reader-chunk-stream-iasecc
tags: ["opensc-virtual-reader-chunk-stream-iasecc", "format-contract", "round-19"]
okf_support: 0
train_only: true
---

# Opensc Virtual Reader Chunk Stream Iasecc

## Round 19 Factual Contract

- The target domain uses OpenSC virtual smart-card data: an initial carved buffer for some fuzz targets, followed by reader chunks that emulate ATR and APDU responses. IASECC paths depend on card detection, application binding, selected files, and TLV-like records carrying lengths for authentication, cryptographic, or PKCS#15 objects.
- Harness link: [[honggfuzz-libfuzzer-compatible]].

### Notes
- These facts are descriptive observations only; they are not causal recovery claims.
