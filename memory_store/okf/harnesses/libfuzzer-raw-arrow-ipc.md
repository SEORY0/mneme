---
type: harness-contract
title: "Libfuzzer Raw Arrow Ipc harness"
description: "Input contract facts for Libfuzzer Raw Arrow Ipc."
tags: ["libfuzzer-raw-arrow-ipc", "round-21"]
okf_support: 2
---
# Libfuzzer Raw Arrow Ipc Harness

## Round 21 Input Contract (arrow-ipc)

- The build includes Arrow IPC file and stream fuzzers that consume raw bytes as IPC payloads. No FuzzedDataProvider selector was observed; the selected target runs the raw input through the Arrow IPC reader/validator stack.

## Round 21 Format Links (arrow-ipc)
- [[arrow-ipc]]

## Round 21 Notes (arrow-ipc)
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 31 Input Contract

### Input Contract
- The harness is raw libFuzzer bytes passed directly to the Arrow IPC file fuzzer. There is no mode selector and no FuzzedDataProvider carving. The target opens the bytes as an Arrow IPC file, reads record batches through the file reader, then calls full RecordBatch validation on each batch before converting valid batches to text.

### Format Links
- [[arrow-ipc-file]]

### Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.
