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

## Round 19 Factual Contract

- Arrow IPC stream data is a sequence of framed FlatBuffer messages. Schema messages define dictionary ids and nested value types; dictionary batch messages carry record-batch payloads and an is-delta flag; record batches follow after required dictionaries are available. The target relation requires a valid nested dictionary stream where a later dictionary batch is treated as a delta and concatenated with an earlier dictionary.
- Harness link: [[afl-libfuzzer]].

### Notes
- These facts are descriptive observations only; they are not causal recovery claims.

## Round 25 Factual Contract

### Schema / Invariants
- Arrow IPC stream inputs use the Arrow streaming/file container with schema messages followed by record batch metadata and buffers. Parser reachability depends on preserving FlatBuffer metadata consistency with the message body and buffer layout.

### Harness Links
- [[afl-file]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

## Round 35 Factual Contract

### Schema / Invariants
- Arrow IPC streams are framed messages containing FlatBuffer metadata and optional aligned body buffers. A stream begins with schema metadata and then record-batch metadata. RecordBatch metadata contains a pre-order field-node vector for logical array lengths and null counts, plus a buffer descriptor vector whose offsets and lengths refer to the message body. Nested arrays such as lists, fixed-size lists, and structs consume multiple field nodes and body buffers in schema order.

### Harness Links
- [[afl-libfuzzer-ipc-stream-reader]]

### Notes
- These facts are descriptive observations from round 35; they carry no success-rate claim.

## Round 36 Factual Contract

### Schema / Invariants
- Arrow IPC streams are continuation-framed FlatBuffer messages. A stream begins with a schema message, then the number of initial dictionary batch messages implied by the schema dictionary fields, then record batches and any later dictionary deltas. Dictionary batch metadata wraps record-batch metadata: field nodes describe logical lengths and null counts, while buffer descriptors point into the following message body. Nested dictionary integration streams can have outer dictionary fields whose dictionary values are list or struct arrays containing additional dictionary-encoded children; those children have their own dictionary batches.

### Harness Links
- [[afl-libfuzzer-ipc-stream-reader]]

### Notes
- These facts are descriptive observations from round 36; they carry no success-rate claim.
