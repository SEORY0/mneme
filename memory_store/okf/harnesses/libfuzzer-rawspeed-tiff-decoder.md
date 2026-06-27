---
type: harness-contract
title: "Libfuzzer Rawspeed Tiff Decoder harness"
description: "Input contract facts for libfuzzer-rawspeed-tiff-decoder."
tags: ["libfuzzer-rawspeed-tiff-decoder", "round-16"]
okf_support: 1
---
# Libfuzzer Rawspeed Tiff Decoder Harness

## Round 16 Input Contract
- The selected RawSpeed TIFF decoder fuzzer passes the entire file to RawParser and the IIQ decoder path. There is no leading mode selector or carved fuzzer header; parser exceptions are caught, so a useful signal requires passing format gates and producing a sanitizer-visible fault.

## Round 16 Format Links
- [[iiq-tiff-rawspeed-camera-file]]

## Round 16 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
