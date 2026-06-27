---
type: causal-policy
title: "Wasm Binary Loader Stack Boundary Overflow"
description: "Verified recovery for wrong_sink with loader_stack_boundary_overflow on wasm-binary inputs."
failure_class: wrong_sink
verifier_signal: loader_stack_boundary_overflow
candidate_family: construct
input_format: wasm-binary
harness_convention: libfuzzer-wamr-wasm-mutator-loader
vuln_class: heap-buffer-overflow-read
access_scope: generate
success_count: 1
confidence: medium
tags: [wrong-sink, loader-stack-boundary-overflow, wasm-binary, heap-buffer-overflow-read, verified_recovery]
match_keys: [wrong-sink, loader-stack-boundary-overflow, wasm-binary, heap-buffer-overflow-read]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
---
# Wasm Binary Loader Stack Boundary Overflow

- key: `wrong_sink x loader_stack_boundary_overflow`
- outcome: verified recovery
- confidence: 0.69
- success_count: 1
- failure_count: 0
- formats: [[wasm-binary]]

## Failure Shape
A candidate family ended at `wrong_sink` before a verifier-confirmed repair. The successful shape kept the required `wasm-binary` parser envelope and moved the mutation into the boundary relation consumed by the target sink instead of relying on broad corruption.

## Procedure
Build a minimal WebAssembly module with a normal empty function type and a second block type carrying many integer parameters. In the function body, enter stack-polymorphic state, then open a typed conditional block using that parameter-heavy block type. This makes the loader synthesize dummy frame offsets for unavailable block parameters and then copy parameter offsets at the frame-offset boundary.

Retarget from this failure key by preserving the format gate first, then changing exactly the cross-field invariant that separates the vulnerable build from the fixed build. Prefer compact construction for construct traces and seed-preserving mutation for seed traces.

## Verifier Contract
The expected signal is `loader_stack_boundary_overflow` with a vulnerable-build crash and clean fixed build. Parser reachability without the differential crash is not sufficient.

## Negative Guards
Do not store raw payload bytes, exact positions, checksums, or submit metadata. Do not widen the mutation after the parser envelope is accepted; if the fixed image also crashes, shrink back to the single boundary relation.
