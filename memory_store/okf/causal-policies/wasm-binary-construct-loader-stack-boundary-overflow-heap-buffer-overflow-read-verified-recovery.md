---
type: causal-policy
title: "WASM Binary Construct Loader Stack Boundary Overflow Heap Buffer Overflow Read Verified Recovery"
description: "Round 13 verified recovery for wrong_sink with verifier signal loader_stack_boundary_overflow."
failure_class: "wrong_sink"
verifier_signal: "loader_stack_boundary_overflow"
candidate_family: "construct"
input_format: "wasm-binary"
harness_convention: "libfuzzer-wamr-wasm-mutator-loader"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "loader-stack-boundary-overflow", "wasm-binary", "construct", "verified-recovery", "round-13"]
match_keys: ["wrong_sink", "loader_stack_boundary_overflow", "wasm-binary", "libfuzzer-wamr-wasm-mutator-loader", "heap-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 13
---
# WASM Binary Construct Loader Stack Boundary Overflow Heap Buffer Overflow Read Verified Recovery

## Policy
For `wrong_sink x loader_stack_boundary_overflow`, preserve the format and harness gates that reached the parser/sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Build a minimal WebAssembly module with a normal empty function type and a second block type carrying many integer parameters. In the function body, enter stack-polymorphic state, then open a typed conditional block using that parameter-heavy block type. This makes the loader synthesize dummy frame offsets for unavailable block parameters and then copy parameter offsets at the frame-offset boundary.
2. Keep the carrier abstract: preserve the gate/invariant relation, not task-local bytes, exact offsets, checksums, or submit metadata.
3. If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- The input is a raw WebAssembly binary module with standard magic/version bytes and type, function, and code sections. Block, loop, and if instructions can use a type-index block signature, allowing multi-parameter block types without an export or start section.

## Harness Contract
- The selected WAMR wasm-mutator loader fuzzer copies the raw input bytes, initializes the runtime, calls wasm_runtime_load on the module, unloads it if loading succeeds, and destroys the runtime. The crash occurs during module validation/loading; no instantiation or function execution is required.

## Negative Memory
- Do not broaden mutations after the parser/harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store raw payload bytes, exact offsets, checksums, task-local identifiers, or submit metadata.

## Evidence Shape
- Support: one round-13 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin.
