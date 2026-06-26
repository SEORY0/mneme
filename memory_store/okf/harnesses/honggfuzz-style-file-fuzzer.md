---
type: harness-contract
title: "Honggfuzz Style File Fuzzer Harness"
description: "Round 7 input contract facts for honggfuzz-style-file-fuzzer."
tags: ["honggfuzz-style-file-fuzzer", "harness-contract", "round-7"]
okf_support: 1
train_only: true
---
# Honggfuzz Style File Fuzzer Harness

## Round 7 Input Contract
- The harness rejects short inputs. It reads selector and option bytes from the front of the file,
optionally consumes fixed-size null-terminated time fields and decoder parameters, and then calls
the parser on the remaining bytes.

## Round {ROUND} Format Links
- [[fluent-bit-parser-fuzzer-control-plus-record]]

## Round {ROUND} Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
