---
type: harness-contract
title: "Honggfuzz Raw Tempfile Harness"
description: "Round 7 input contract facts for honggfuzz-raw-tempfile."
tags: ["honggfuzz-raw-tempfile", "harness-contract", "round-7"]
okf_support: 1
train_only: true
---
# Honggfuzz Raw Tempfile Harness

## Round 7 Input Contract
- The active Binutils harness writes raw bytes to a temporary file and runs an nm-style BFD flow after
precondition checks. Inputs that BFD does not recognize, or recognizes without symbols, exit cleanly
before the target ECOFF symbol slurp.

## Round {ROUND} Format Links
- [[ecoff-bfd-object]]

## Round {ROUND} Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
