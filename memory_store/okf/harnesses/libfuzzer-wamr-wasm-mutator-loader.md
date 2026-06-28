---
type: harness
title: "Libfuzzer Wamr WASM Mutator Loader"
access_scope: generate
confidence: medium
tags: ["libfuzzer-wamr-wasm-mutator-loader", "harness", "round-13"]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
train_only: true
---
# Libfuzzer Wamr WASM Mutator Loader

## Round 13 Facts
- The selected WAMR wasm-mutator loader fuzzer copies the raw input bytes, initializes the runtime, calls wasm_runtime_load on the module, unloads it if loading succeeds, and destroys the runtime. The crash occurs during module validation/loading; no instantiation or function execution is required.
