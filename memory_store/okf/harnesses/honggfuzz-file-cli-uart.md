---
type: harness-contract
title: "Honggfuzz File Cli Uart Harness"
description: "Input contract facts for honggfuzz-file-cli-uart."
tags: ["honggfuzz-file-cli-uart", "round-37", "harness-contract"]
okf_support: 1
train_only: true
---
# Honggfuzz File Cli Uart Harness
## Round 37 Input Contract

### Input Contract
- The active harness is the CLI UART receiver.
- It passes the whole file to the UART receive callback as raw command bytes, with no mode selector, checksum, or FuzzedDataProvider layout.
- A carriage return or newline terminates and executes the command.

### Format Links
- [[openthread-cli-uart-dataset-tlv]]

### Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
