---
type: harness-contract
title: "Honggfuzz Pkcs15init harness"
description: "Input contract facts for Honggfuzz Pkcs15init."
tags: ["honggfuzz-pkcs15init", "round-21"]
okf_support: 1
---
# Honggfuzz Pkcs15init Harness

## Round 21 Input Contract (opensc-pkcs15init-reader-chunk-stream-iasecc)

- The active target is fuzz_pkcs15init under a honggfuzz-style wrapper. It accepts one raw input file but interprets it as tool arguments plus reader data, not as a standalone ASN.1 blob.

## Round 21 Format Links (opensc-pkcs15init-reader-chunk-stream-iasecc)
- [[opensc-pkcs15init-reader-chunk-stream-iasecc]]

## Round 21 Notes (opensc-pkcs15init-reader-chunk-stream-iasecc)
- These are descriptive harness-carving facts only; they are not causal recovery claims.
