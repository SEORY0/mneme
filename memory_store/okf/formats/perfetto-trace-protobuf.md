---
type: format-family
title: "Perfetto Trace Protobuf"
description: "Round 7 factual format contract for perfetto-trace-protobuf."
resource: cybergym://format/perfetto-trace-protobuf
tags: ["perfetto-trace-protobuf", "format-contract", "round-7"]
okf_support: 1
train_only: true
---
# Perfetto Trace Protobuf

## Round 7 Factual Contract

### Schema / Invariants
- Perfetto traces can carry TracePacket protobuf messages. A memory tracker snapshot packet contains
process snapshots, allocator dump nodes with ids and absolute names, and memory edges that reference
node ids with optional importance.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 34 Factual Contract

### Schema / Invariants
- Perfetto trace inputs are protobuf-framed Trace messages containing TracePacket records. The trace type guesser treats inputs without JSON, Fuchsia, systrace, ctrace, or gzip signatures as protobuf traces. TrackEvent packets require a usable packet sequence and incremental-state reset before later event packets are parsed; each parsed event also needs a timestamp from either the packet or event-level timestamp fields.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive observations only; they carry no success-rate claim.
