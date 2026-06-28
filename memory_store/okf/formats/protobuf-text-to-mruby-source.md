---
type: format
title: "Protobuf Text To Mruby Source"
access_scope: generate
confidence: medium
tags: ["protobuf-text-to-mruby-source", "format", "round-13"]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
train_only: true
---
# Protobuf Text To Mruby Source

## Round 13 Facts
- The accepted input for the selected target is a text-format protobuf Function. The converter emits a fixed no-argument Ruby method, initializes a first local, wraps statement sequences in begin expressions, and can generate assignments, if/else, ternary expressions, nested statement sequences, array builtin calls, math/time/object calls, constants, variable references, and binary expressions.
