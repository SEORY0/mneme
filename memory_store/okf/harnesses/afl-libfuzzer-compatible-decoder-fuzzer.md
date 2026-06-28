---
type: harness-contract
title: "afl/libfuzzer-compatible decoder fuzzer harness"
description: "Input contract facts for afl/libfuzzer-compatible decoder fuzzer."
tags: ["afl-libfuzzer-compatible-decoder-fuzzer", "round-14"]
okf_support: 1
---
# Afl Libfuzzer Compatible Decoder Fuzzer Harness

## Round 14 Input Contract
- The decoder fuzzer treats the last fixed-size suffix as codec configuration and scans the preceding bytes for a fixed delimiter that separates packets. Without the delimiter, the config suffix can be decoded as packet data and mask the intended geometry.

## Round 14 Format Links
- [[ffmpeg-midivid-packet]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
