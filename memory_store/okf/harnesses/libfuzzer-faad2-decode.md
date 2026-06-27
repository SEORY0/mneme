---
type: harness-contract
title: "Libfuzzer Faad2 Decode harness"
description: "Input contract facts for libfuzzer-faad2-decode."
tags: ["libfuzzer-faad2-decode", "round-11"]
okf_support: 1
train_only: true
---
# Libfuzzer Faad2 Decode Harness

## Round 11 Input Contract
- The harness manually splits the raw buffer from the front: a two-byte little-endian size selects the first init region, and all remaining bytes become the frame passed to NeAACDecDecode. There is no filename, container sniffing stage, or additional FuzzedDataProvider field after the split.

## Format Links
- [[faad2-decode-split-buffer]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
