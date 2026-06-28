---
type: harness-contract
title: "Afl Style File Harness"
description: "Round 7 input contract facts for afl-style-file."
tags: ["afl-style-file", "harness-contract", "round-7"]
okf_support: 1
train_only: true
---
# Afl Style File Harness

## Round 7 Input Contract
- The htslib hts_open fuzzer reads the raw file or stdin bytes as an HTS file and dispatches by file
signature. There is no front-carved mode selector.

## Round {ROUND} Format Links
- [[cram]]

## Round {ROUND} Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
