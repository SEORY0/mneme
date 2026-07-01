---
type: harness-contract
title: "Afl File MVG Coder harness"
description: "Input contract facts for afl-file-mvg-coder."
tags: ["afl-file-mvg-coder", "round-32"]
okf_support: 1
---
# Afl File MVG Coder Harness

## Round 32 Input Contract
- The GraphicsMagick MVG coder fuzzer feeds the entire file as raw bytes to the MVG image reader. There is no leading selector, archive wrapper, checksum, or FuzzedDataProvider split. The accepted MVG text is rendered by the coder_MVG_fuzzer binary in a file/stdin style harness.

## Round 32 Format Links
- [[mvg]]

## Round 32 Notes
- These facts are descriptive harness-carving observations only; they are not causal recovery claims.
