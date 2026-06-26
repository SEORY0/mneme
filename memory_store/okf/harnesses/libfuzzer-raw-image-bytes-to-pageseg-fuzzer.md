---
type: harness-contract
title: "Libfuzzer Raw Image Bytes To Pageseg Fuzzer harness"
description: "Input contract facts for Libfuzzer Raw Image Bytes To Pageseg Fuzzer."
tags: ["libfuzzer-raw-image-bytes-to-pageseg-fuzzer", "round-6"]
okf_support: 1
---
# Libfuzzer Raw Image Bytes To Pageseg Fuzzer Harness

## Round 6 Input Contract
- The chosen Leptonica target feeds raw bytes to page segmentation routines after pixReadMemSpix succeeds. There is no mode byte; the harness decides paths from whether the same raw buffer can be decoded as the expected Leptonica container.

## Format Links
- [[spix-leptonica-image-family]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
