---
type: harness-contract
title: "Afl Libfuzzer Raw Bytes Harness"
description: "Round 7 input contract facts for afl-libfuzzer-raw-bytes."
tags: ["afl-libfuzzer-raw-bytes", "harness-contract", "round-7"]
okf_support: 1
train_only: true
---
# Afl Libfuzzer Raw Bytes Harness

## Round 7 Input Contract
- The fuzzer passes the raw input buffer directly to the AgentX parser; there is no file wrapper,
checksum, mode selector, or FuzzedDataProvider carving.

## Round {ROUND} Format Links
- [[agentx-pdu]]

## Round {ROUND} Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 30 Input Contract

### Input Contract
- The selected libgit2 object fuzzer feeds the raw input bytes directly to git_object__from_raw and tries multiple Git object types including commit. There is no mode selector, checksum, file wrapper, or FuzzedDataProvider front/back carving.

### Format Links
- [[git-raw-object]]

### Notes
- These facts are descriptive harness-carving observations only; they are not causal recovery claims.
