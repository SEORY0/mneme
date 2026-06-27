---
type: format-family
title: "Arrow IPC Stream format"
description: "Descriptive contract facts for arrow-ipc-stream."
resource: "cybergym://format/arrow-ipc-stream"
tags: ["arrow-ipc-stream", "round-16"]
okf_support: 1
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 16 Factual Contract

### Schema / Invariants
- Arrow IPC streams are framed messages containing FlatBuffer schema and record-batch metadata followed by aligned buffers. Binary-view and string-view arrays use normal buffers plus a variadic-buffer-count vector that tells the reader how many additional character buffers belong to each array.

### Harness Links
- [[libfuzzer-arrow-ipc-stream]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.
