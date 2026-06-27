---
type: harness-contract
title: "Libfuzzer Decoder Target harness"
description: "Input contract facts for libfuzzer decoder target."
tags: ["libfuzzer-decoder-target", "round-11"]
okf_support: 1
train_only: true
---
# Libfuzzer Decoder Target Harness

## Round 11 Input Contract
- FFmpeg oss-fuzz decoder targets instantiate a single codec-specific decoder and feed the input bytes as packet data. The target selected by the local run is the VC1IMAGE fuzzer, with no extra file-format wrapper.

## Format Links
- [[vc1-vc1image-elementary-stream]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
