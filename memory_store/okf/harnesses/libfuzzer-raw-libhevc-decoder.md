---
type: harness-contract
title: "Libfuzzer Raw Libhevc Decoder harness"
description: "Input contract facts for Libfuzzer Raw Libhevc Decoder."
tags: ["libfuzzer-raw-libhevc-decoder", "round-21"]
okf_support: 1
---
# Libfuzzer Raw Libhevc Decoder Harness

## Round 21 Input Contract (hevc-annex-b)

- The libFuzzer harness consumes raw bytes. Selector bytes near the start choose decoder color format and core count, but the entire original buffer is still fed to header decode and then repeatedly to frame decode until consumed.

## Round 21 Format Links (hevc-annex-b)
- [[hevc-annex-b]]

## Round 21 Notes (hevc-annex-b)
- These are descriptive harness-carving facts only; they are not causal recovery claims.
