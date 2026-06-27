---
type: harness-contract
title: "Oss Fuzz Run Poc harness"
description: "Input contract facts for oss-fuzz-run-poc."
tags: ["oss-fuzz-run-poc", "round-20"]
okf_support: 1
---
# Oss Fuzz Run Poc Harness

## Round 20 Input Contract
- The OSS-Fuzz run_poc wrapper invokes the target decoder fuzzer binary with the candidate file. There is no model or network component; the local binary decodes the input according to the selected compiled decoder harness.

## Round 20 Format Links
- [[ffmpeg-target-decoder-packet-stream]]

## Round 20 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
