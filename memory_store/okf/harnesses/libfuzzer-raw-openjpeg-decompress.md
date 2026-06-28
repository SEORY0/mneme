---
type: harness-contract
title: "Libfuzzer Raw Openjpeg Decompress harness"
description: "Input contract facts for Libfuzzer Raw Openjpeg Decompress."
tags: ["libfuzzer-raw-openjpeg-decompress", "round-21"]
okf_support: 1
---
# Libfuzzer Raw Openjpeg Decompress Harness

## Round 21 Input Contract (jpeg2000)

- The fuzzer consumes raw bytes through OpenJPEG memory stream callbacks. It detects the container family from leading signature bytes, reads the image header, rejects overly large images or tiles, limits the decode area, then calls OpenJPEG decode and end-decompress.

## Round 21 Format Links (jpeg2000)
- [[jpeg2000]]

## Round 21 Notes (jpeg2000)
- These are descriptive harness-carving facts only; they are not causal recovery claims.
