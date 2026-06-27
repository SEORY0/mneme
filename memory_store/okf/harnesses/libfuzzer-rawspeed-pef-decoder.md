---
type: harness-contract
title: "Libfuzzer Rawspeed Pef Decoder harness"
description: "Input contract facts for libfuzzer RawSpeed PEF decoder."
tags: ["libfuzzer-rawspeed-pef-decoder", "round-16"]
okf_support: 1
---
# Libfuzzer Rawspeed Pef Decoder Harness

## Round 16 Input Contract
- The selected wrapper runs the PEF TIFF decoder fuzzer directly on raw bytes. It parses the TIFF structure, constructs a PEF decoder, disables crop and unknown-failure strictness, then calls raw decode and metadata decode inside exception handling.

## Round 16 Format Links
- [[tiff-pef-raw-image]]

## Round 16 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
