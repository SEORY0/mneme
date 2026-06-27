---
type: harness
title: "Libfuzzer Wamr Wasm Mutator Loader"
harness_convention: libfuzzer-wamr-wasm-mutator-loader
access_scope: generate
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
---
# Libfuzzer Wamr Wasm Mutator Loader

## Input Contract
- For `wasm-binary`, The selected WAMR wasm-mutator loader fuzzer copies the raw input bytes, initializes the runtime, calls wasm_runtime_load on the module, unloads it if loading succeeds, and destroys the runtime. The crash occurs during module validation/loading; no instantiation or function execution is required.
