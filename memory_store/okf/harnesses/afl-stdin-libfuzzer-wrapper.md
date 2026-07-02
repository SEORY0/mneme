---
type: harness-contract
title: "Afl Stdin Libfuzzer Wrapper Harness"
description: "Input contract facts for afl-stdin-libfuzzer-wrapper."
tags: ["afl-stdin-libfuzzer-wrapper", "round-30"]
okf_support: 0
train_only: true
---
# Afl Stdin Libfuzzer Wrapper Harness

## Round 30 Input Contract

### Input Contract
- The harness passes the whole input file directly to the FDK AAC decoder opened for LOAS/LATM transport. There is no FuzzedDataProvider, mode byte, archive wrapper, or secondary file format. The target binary is an AFL-style stdin/file wrapper around a libFuzzer target and decodes until the stream is exhausted or rejected.

### Format Links
- [[aac-loas-latm]]

### Notes
- These facts are descriptive harness-carving observations only; they are not causal recovery claims.
