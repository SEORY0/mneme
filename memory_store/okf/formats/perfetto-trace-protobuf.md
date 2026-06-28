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
