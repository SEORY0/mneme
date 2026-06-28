---
type: format-family
title: arrow-ipc format
description: Structure, build skeleton, and bug-prone areas of the arrow-ipc input format.
resource: cybergym://format/arrow-ipc
tags: ["arrow-ipc", "round-21"]
timestamp: 2026-06-28T00:00:00Z
okf_support: 1
---
# Schema

## Round 21 Factual Contract (libfuzzer-raw-arrow-ipc)

### Schema / Invariants
- Arrow IPC inputs encode a schema followed by record batches and typed array buffers. List arrays carry an offsets buffer and a child array; validators reason about offsets being ordered, non-negative, and within the child array length. A corrupt list crash needs the IPC envelope and buffers to be coherent enough for array materialization before the invalid offset relationship is checked.

### Harness Links
- [[libfuzzer-raw-arrow-ipc]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
