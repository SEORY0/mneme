---
type: harness-contract
title: "Libfuzzer Skia Image Filter Deserialize Harness"
description: "Input contract facts for libfuzzer-skia-image-filter-deserialize."
tags: ["libfuzzer-skia-image-filter-deserialize", "round-30"]
okf_support: 0
train_only: true
---
# Libfuzzer Skia Image Filter Deserialize Harness

## Round 30 Input Contract

### Input Contract
- libFuzzer passes the input bytes directly to SkImageFilter::Deserialize with no mode byte or FuzzedDataProvider carving. If deserialization returns an image filter, the harness attaches it to a paint and draws a small bitmap through that paint on a fixed-size canvas, which evaluates the image filter and plays back any embedded picture content.

### Format Links
- [[skia-serialized-image-filter-skp]]

### Notes
- These facts are descriptive harness-carving observations only; they are not causal recovery claims.
