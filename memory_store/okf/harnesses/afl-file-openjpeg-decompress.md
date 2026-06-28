---
type: harness-contract
title: "Afl File Openjpeg Decompress harness"
description: "Input contract facts for afl-file-openjpeg-decompress."
tags: ["afl-file-openjpeg-decompress", "round-16"]
okf_support: 1
---
# Afl File Openjpeg Decompress Harness

## Round 16 Input Contract
- The OpenJPEG decompression fuzzer consumes the entire file as one input. It chooses JP2 versus raw codestream from magic bytes, bounds the decode area internally, and then invokes the normal decompressor without a leading mode byte or sidecar metadata.

## Round 16 Format Links
- [[jpeg2000-jp2-j2k]]

## Round 16 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
