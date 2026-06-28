---
type: harness-contract
title: "Libfuzzer Raw Arrow Ipc harness"
description: "Input contract facts for Libfuzzer Raw Arrow Ipc."
tags: ["libfuzzer-raw-arrow-ipc", "round-21"]
okf_support: 1
---
# Libfuzzer Raw Arrow Ipc Harness

## Round 21 Input Contract (arrow-ipc)

- The build includes Arrow IPC file and stream fuzzers that consume raw bytes as IPC payloads. No FuzzedDataProvider selector was observed; the selected target runs the raw input through the Arrow IPC reader/validator stack.

## Round 21 Format Links (arrow-ipc)
- [[arrow-ipc]]

## Round 21 Notes (arrow-ipc)
- These are descriptive harness-carving facts only; they are not causal recovery claims.
