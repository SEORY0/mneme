---
type: harness-contract
title: "Afl Libfuzzer Tempfile Harness"
description: "Round 7 input contract facts for afl-libfuzzer-tempfile."
tags: ["afl-libfuzzer-tempfile", "harness-contract", "round-7"]
okf_support: 1
train_only: true
---
# Afl Libfuzzer Tempfile Harness

## Round 7 Input Contract
- The fuzzer writes the raw input bytes to a temporary config file and calls the LXC config reader.
There is no outer binary envelope or checksum.

## Round {ROUND} Format Links
- [[lxc-config-text]]

## Round {ROUND} Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
