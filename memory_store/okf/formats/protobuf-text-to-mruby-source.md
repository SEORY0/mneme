---
type: format
title: "Protobuf Text To Mruby Source"
input_format: protobuf-text-to-mruby-source
access_scope: generate
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
---
# Protobuf Text To Mruby Source

## Schema
- The accepted input for the selected target is a text-format protobuf Function. The converter emits a fixed no-argument Ruby method, initializes a first local, wraps statement sequences in begin expressions, and can generate assignments, if/else, ternary expressions, nested statement sequences, array builtin calls, math/time/object calls, constants, variable references, and binary expressions.
