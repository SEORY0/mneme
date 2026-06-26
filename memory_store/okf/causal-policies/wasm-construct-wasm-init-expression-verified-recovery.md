---
type: causal-policy
title: "Wasm Construct Wasm Init Expression Verified Recovery"
description: "Round 6 verified recovery for generic_crash with verifier signal target_evaluate_expression_crash."
failure_class: "generic_crash"
verifier_signal: "target_evaluate_expression_crash"
candidate_family: "construct_wasm_init_expression"
input_format: "wasm"
harness_convention: "libfuzzer wasm3 module loader"
vuln_class: "heap-buffer-overflow-write"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "target-evaluate-expression-crash", "wasm", "construct-wasm-init-expression", "verified-recovery", "round-6"]
match_keys: ["generic_crash", "target_evaluate_expression_crash", "wasm", "libfuzzer wasm3 module loader", "heap-buffer-overflow-write", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 6
---
# Wasm Construct Wasm Init Expression Verified Recovery

## Policy
For `generic_crash x target_evaluate_expression_crash`, preserve the format and harness gates that reached the parser/sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Build a valid WebAssembly module that passes magic/version/type/function/export/code gates and exports the function name the harness calls. Add a valid memory/data segment whose initialization expression preserves module structure but pushes many constants before expression termination, overflowing the interpreter stack used by EvaluateExpression. The fixed build rejects or bounds this expression state while the vulnerable build writes past the stack buffer.
2. Keep the carrier abstract: preserve the gate/invariant relation, not any task-local bytes or offsets.
3. If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- A minimal Wasm module needs the standard magic/version, a function type, a function section, an exported function matching the harness lookup, executable code for that function, and any memory/data sections referenced by active data segments. Init expressions are bytecode streams terminated by an end opcode.
- Harness: The libFuzzer harness feeds raw bytes to `m3_ParseModule`, loads the module into a runtime with a small stack, looks up an exported `fib` function, and calls it. Data/global initialization expressions are evaluated during module loading before the exported call.

## Negative Memory
- Do not broaden mutations after the parser/harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store raw payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-6 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin.
