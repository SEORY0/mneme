---
type: harness-contract
title: "afl-rawspeed-tiff-decoder harness"
description: "Descriptive harness contract facts for afl-rawspeed-tiff-decoder."
tags: ["afl-rawspeed-tiff-decoder", "round-18"]
okf_support: 1
train_only: true
---
# Afl Rawspeed TIFF Decoder Harness

## Round 18 Input Contract

### Schema / Invariants
- The active verifier binary is a RawSpeed TIFF decoder fuzzer specialized for the SRW decoder. It reads the input as raw bytes from a file/stdin, parses it as a TIFF tree, constructs the selected decoder, disables crop and unknown-camera failures, and calls raw decoding and metadata decoding. There is no FuzzedDataProvider split.

### Format Links
- [[samsung-srw-tiff]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
