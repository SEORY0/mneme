---
type: harness-contract
title: "Libfuzzer Virtual Io Libsndfile Harness"
description: "Round 7 input contract facts for libfuzzer-virtual-io-libsndfile."
tags: ["libfuzzer-virtual-io-libsndfile", "harness-contract", "round-7"]
okf_support: 1
train_only: true
---
# Libfuzzer Virtual Io Libsndfile Harness

## Round 7 Input Contract
- The libFuzzer harness exposes the raw bytes through libsndfile virtual I/O. There is no carved
prefix; the RIFF magic, WAVE form type, and chunk sizes drive parser reachability.

## Round {ROUND} Format Links
- [[riff-wav-cart]]

## Round {ROUND} Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
