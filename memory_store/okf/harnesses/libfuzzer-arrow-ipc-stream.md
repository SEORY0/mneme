---
type: harness-contract
title: "Libfuzzer Arrow IPC Stream harness"
description: "Input contract facts for libfuzzer-arrow-ipc-stream."
tags: ["libfuzzer-arrow-ipc-stream", "round-16"]
okf_support: 1
---
# Libfuzzer Arrow IPC Stream Harness

## Round 16 Input Contract
- The Arrow IPC stream fuzzer consumes the raw input bytes directly as an IPC stream and opens record batches through the standard stream reader. There is no leading mode byte, external schema file, or checksum gate.

## Round 16 Format Links
- [[arrow-ipc-stream]]

## Round 16 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
