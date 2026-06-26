---
type: harness-contract
title: "Libfuzzer Wrapper Mismatch Harness"
description: "Round 7 input contract facts for libfuzzer-wrapper-mismatch."
tags: ["libfuzzer-wrapper-mismatch", "harness-contract", "round-7"]
okf_support: 1
train_only: true
---
# Libfuzzer Wrapper Mismatch Harness

## Round 7 Input Contract
- The actual generated target is the libavc decoder fuzzer from ossfuzz.sh. Local verifier output
showed the wrapper treating the supplied path as a required directory, indicating a harness
invocation mismatch rather than a normal raw-file libFuzzer single-input run.

## Round {ROUND} Format Links
- [[h264-annexb]]

## Round {ROUND} Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
