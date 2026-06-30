---
type: harness-contract
title: "Libfuzzer Libexif Loader harness"
description: "Input contract facts for libfuzzer-libexif-loader."
tags: ["libfuzzer-libexif-loader", "round-11"]
okf_support: 9
train_only: true
---
# Libfuzzer Libexif Loader Harness

## Round 11 Input Contract
- The libFuzzer harness feeds the raw input bytes to the libexif loader. It does not carve mode fields from the input; the input itself must carry the JPEG/Exif or Exif/TIFF structure that drives parsing.

## Format Links
- [[jpeg-exif]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 27 Input Contract
- The libFuzzer harness feeds raw input bytes directly to libexif loader/from-data paths.
- There is no mode byte and no FuzzedDataProvider carving; the input itself must be a recognizable JPEG/EXIF or raw EXIF/TIFF payload.

## Round 27 Format Links
- [[jpeg-exif]]

## Round 27 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
