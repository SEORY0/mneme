---
type: harness-contract
title: "afl-libfuzzer-ipc-stream-reader harness"
description: "Input contract facts for afl-libfuzzer-ipc-stream-reader."
tags: ["afl-libfuzzer-ipc-stream-reader", "round-35"]
okf_support: 1
train_only: true
---
# afl-libfuzzer-ipc-stream-reader Harness

## Round 35 Input Contract
### Input Contract
- The active target is the IPC stream fuzzer. It treats the supplied file bytes as a raw Arrow IPC stream, opens a RecordBatchStreamReader over an in-memory buffer, repeatedly reads record batches, and calls ValidateFull on each batch. There is no FuzzedDataProvider layout and no separate mode selector; parser reachability depends on preserving Arrow stream framing and FlatBuffer metadata consistency.

### Format Links
- [[arrow-ipc-stream]]

### Notes
- These facts are descriptive harness-carving observations from round 35; they carry no success-rate claim.

## Round 36 Input Contract
- The active target consumes the raw file bytes as one Arrow IPC stream. It opens a RecordBatchStreamReader over an in-memory buffer, reads the initial dictionaries, then reads later dictionary batches and record batches, and calls full validation on decoded record batches. There is no leading mode byte, checksum gate, or FuzzedDataProvider front/back split.

## Round 36 Format Links
- [[arrow-ipc-stream]]

## Round 36 Notes
- These are descriptive harness-carving facts from round 36; they are not causal recovery claims.
