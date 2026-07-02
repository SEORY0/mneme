---
type: causal-policy
title: "WASM Binary Construct Parser Reached Loader Then Immediate Reader Oob Heap Buffer Overflow Read Verified Recovery"
description: "Round 29 verified recovery for wrong_sink with verifier signal parser_reached_loader_then_immediate_reader_oob."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_loader_then_immediate_reader_oob"
candidate_family: "construct"
input_format: "wasm-binary"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-loader-then-immediate-reader-oob", "wasm-binary", "libfuzzer", "construct", "heap-buffer-overflow-read", "verified-recovery", "round-29"]
match_keys: ["wrong_sink", "parser_reached_loader_then_immediate_reader_oob", "wasm-binary", "libfuzzer", "heap-buffer-overflow-read", "wrong-sink", "parser-reached-loader-then-immediate-reader-oob", "wasm-binary", "libfuzzer", "heap-buffer-overflow-read", "verified_recovery", "construct", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 29
---
# WASM Binary Construct Parser Reached Loader Then Immediate Reader Oob Heap Buffer Overflow Read Verified Recovery

- key: `wrong_sink x parser_reached_loader_then_immediate_reader_oob`
- outcome: verified target match / recovery policy
- success_count: 1
- related format facts: [[wasm-binary]]
- related harness facts: [[libfuzzer]]

## Policy
For `wrong_sink x parser_reached_loader_then_immediate_reader_oob` on `wasm-binary`, keep the parser and harness gates that produced the verifier signal, then vary only the causal relation described below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Construct a minimal WebAssembly module with valid magic, version, type, function, and code sections. Keep the section ordering and function/code counts consistent, then make the function body's declared body size smaller than the local-declaration vector that follows it. Place an immediate-consuming expression opcode after the oversized locals vector without providing a complete immediate so the vulnerable loader underflows the stored expression length and bytecode preparation reads beyond the real module buffer. The fixed loader rejects the body-size/local-expression mismatch.
2. Preserve format recognition and the harness input contract while mutating the narrow sink invariant; do not broaden into an off-target crash or a both-image crash.
3. If later verifier output changes the failure key, re-rank against that new key before mutating unrelated fields.

## Format Contract
- Format [[wasm-binary]]: WebAssembly binaries start with magic and version bytes, then ordered LEB-length-prefixed sections. A function entry in the code section is itself length-prefixed and contains a vector of local declarations followed by an expression that should terminate with an end opcode. Function-section and code-section counts must agree before the loader reaches function-body parsing.
- Harness [[libfuzzer]]: libFuzzer passes the raw byte buffer directly to the WAMR wasm loader. There is no prefix, selector byte, checksum, or FuzzedDataProvider carving. Module instantiation is not required; a loader-stage malformed module is sufficient.

## Negative Memory
- Do not corrupt the outer `wasm-binary` recognition gate while retargeting this signal.
- Do not count parser reachability, clean exits, fixed-image crashes, both-image crashes, or local wrong-sink labels as success without official target match.
- Never store payload bytes, exact positions, checksums, submit metadata, or task-local identifiers.

## Evidence Shape
- Support: one round-29 worker trace with official target match.
- Scope: generator repair and retargeting only; pair with [[wasm-binary]] and [[libfuzzer]].
