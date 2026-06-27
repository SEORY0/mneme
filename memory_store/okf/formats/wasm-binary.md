---
type: format
title: "WASM Binary"
access_scope: generate
confidence: medium
tags: ["wasm-binary", "format", "round-13"]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
train_only: true
---
# WASM Binary

## Round 13 Facts
- The input is a raw WebAssembly binary module with standard magic/version bytes and type, function, and code sections. Block, loop, and if instructions can use a type-index block signature, allowing multi-parameter block types without an export or start section.
