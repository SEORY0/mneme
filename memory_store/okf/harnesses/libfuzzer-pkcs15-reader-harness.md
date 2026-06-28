---
type: harness-contract
title: "Libfuzzer Pkcs15 Reader Harness harness"
description: "Input contract facts for libfuzzer pkcs15 reader harness."
tags: ["libfuzzer-pkcs15-reader-harness", "round-16"]
okf_support: 1
---
# Libfuzzer Pkcs15 Reader Harness Harness

## Round 16 Input Contract
- The harness consumes the raw file as a sequence of virtual-reader chunks, with the first chunk becoming the ATR and later chunks serving card responses. PKCS#15 object operations are only reached after successful card connection and binding.

## Round 16 Format Links
- [[opensc-virtual-reader-chunk-stream]]

## Round 16 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
