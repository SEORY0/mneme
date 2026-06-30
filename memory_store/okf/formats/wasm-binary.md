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

## Round 29 Factual Contract

### Schema / Invariants
- WebAssembly binaries start with magic and version bytes, then ordered LEB-length-prefixed sections. A function entry in the code section is itself length-prefixed and contains a vector of local declarations followed by an expression that should terminate with an end opcode. Function-section and code-section counts must agree before the loader reaches function-body parsing.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
