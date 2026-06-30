---
type: harness-contract
title: "Afl Libfuzzer Compatible Whole Buffer Frame Decompressor harness"
description: "Input contract facts for afl++ libfuzzer-compatible whole-buffer frame decompressor."
tags: ["afl-libfuzzer-compatible-whole-buffer-frame-decompressor", "round-28"]
okf_support: 0
---
# Afl Libfuzzer Compatible Whole Buffer Frame Decompressor Harness

## Round 28 Input Contract

- The harness is an afl++ standalone wrapper around a libFuzzer-style decompress-frame target. It reads the whole PoC file into memory and passes those raw bytes directly to the frame decompressor; there is no selector byte, no FuzzedDataProvider carving, and no checksum recomputation requirement.

## Round 28 Format Links
- [[c-blosc2-frame]]

## Round 28 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
