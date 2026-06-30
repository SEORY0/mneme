---
type: harness-contract
title: "Honggfuzz Libfuzzer Standalone Harness"
description: "Input contract facts for honggfuzz-libfuzzer-standalone."
tags: ["honggfuzz-libfuzzer-standalone", "round-27"]
okf_support: 1
---
# Honggfuzz Libfuzzer Standalone Harness

## Round 27 Input Contract
- The container wrapper runs a standalone thumbnail fuzzer against the fixed input path.
- The file bytes are passed directly to the libvips image-buffer loader; there is no argv-controlled archive output path, no separate output filename, no mode selector byte, no stdin protocol, and no FuzzedDataProvider split.
- The wrapper is honggfuzz-style around a libFuzzer entry point and reports normal clean exits for accepted non-crashing images.

## Round 27 Format Links
- [[libvips-thumbnail-image-buffer]]

## Round 27 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
