---
type: harness-contract
title: "Honggfuzz Wrapper Svc Dec harness"
description: "Input contract facts for honggfuzz-wrapper-svc-dec."
tags: ["honggfuzz-wrapper-svc-dec", "round-11"]
okf_support: 1
train_only: true
---
# Honggfuzz Wrapper Svc Dec Harness

## Round 11 Input Contract
- The local target is a honggfuzz-style wrapper rather than a straightforward libFuzzer single-buffer target. In local verify, passing one PoC file produced wrapper usage output, so the file bytes were not clearly consumed as a normal decoder frame sequence.

## Format Links
- [[h264-annexb-svc]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
