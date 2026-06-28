---
type: harness-contract
title: "Libfuzzer Libexif Loader harness"
description: "Input contract facts for libfuzzer-libexif-loader."
tags: ["libfuzzer-libexif-loader", "round-11"]
okf_support: 1
train_only: true
---
# Libfuzzer Libexif Loader Harness

## Round 11 Input Contract
- The libFuzzer harness feeds the raw input bytes to the libexif loader. It does not carve mode fields from the input; the input itself must carry the JPEG/Exif or Exif/TIFF structure that drives parsing.

## Format Links
- [[jpeg-exif]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
