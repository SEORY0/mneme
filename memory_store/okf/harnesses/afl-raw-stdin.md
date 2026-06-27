---
type: harness-contract
title: "Afl Raw Stdin harness"
description: "Input contract facts for afl-raw-stdin."
tags: ["afl-raw-stdin", "round-20"]
okf_support: 1
---
# Afl Raw Stdin Harness

## Round 20 Input Contract
- The harness runs an expression parser target on raw file bytes provided through stdin or a file argument. There is no file container, leading mode byte, checksum, or FuzzedDataProvider-style split.

## Round 20 Format Links
- [[openvswitch-expression]]

## Round 20 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
