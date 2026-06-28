---
type: harness-contract
title: "Libfuzzer Raw Qbuffer Harness"
description: "Round 7 input contract facts for libfuzzer-raw-qbuffer."
tags: ["libfuzzer-raw-qbuffer", "harness-contract", "round-7"]
okf_support: 1
train_only: true
---
# Libfuzzer Raw Qbuffer Harness

## Round 7 Input Contract
- LibFuzzer supplies raw bytes through a Qt QBuffer to the image handler. The harness calls canRead
and then still calls read, so partial RIFF prefixes can reach the scanner even when the full ANI
header is not accepted.

## Round {ROUND} Format Links
- [[ani-riff]]

## Round {ROUND} Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
