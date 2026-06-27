---
type: format
title: "Wasm Binary"
input_format: wasm-binary
access_scope: generate
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
---
# Wasm Binary

## Schema
- The input is a raw WebAssembly binary module with standard magic/version bytes and type, function, and code sections. Block, loop, and if instructions can use a type-index block signature, allowing multi-parameter block types without an export or start section.
