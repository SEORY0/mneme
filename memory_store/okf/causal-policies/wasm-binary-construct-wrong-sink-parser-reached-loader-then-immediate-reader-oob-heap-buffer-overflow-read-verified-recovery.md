---
type: causal-policy
title: "Wasm Binary Construct Wrong Sink Parser Reached Loader Then Immediate Reader Oob Heap Buffer Overflow Read Verified Recovery"
description: "Round 30 verified recovery for wrong_sink with verifier signal parser_reached_loader_then_immediate_reader_oob."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_loader_then_immediate_reader_oob"
candidate_family: "construct"
input_format: "wasm-binary"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: medium
tags: ["wrong-sink", "parser-reached-loader-then-immediate-reader-oob", "wasm-binary", "libfuzzer", "construct", "verified-recovery", "round-30"]
match_keys: ["wrong-sink", "parser-reached-loader-then-immediate-reader-oob", "wasm-binary", "libfuzzer", "heap-buffer-overflow-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 30
---
# Wasm Binary Construct Wrong Sink Parser Reached Loader Then Immediate Reader Oob Heap Buffer Overflow Read Verified Recovery

- key: `wrong-sink x parser-reached-loader-then-immediate-reader-oob`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[wasm-binary]]
- harnesses: [[libfuzzer]]

## Failure Shape
Construct a minimal WebAssembly module that passes magic/version plus type, function, and code-section gates with matching function/code counts. In the single code entry, keep the outer section coherent but make the declared function-body size smaller than the locals vector and following expression bytes, then place an immediate-consuming opcode without a complete immediate. The vulnerable loader underflows the expression extent during bytecode preparation; the fixed loader rejects the body-size/local-expression mismatch.

## Policy
For `wrong-sink x parser-reached-loader-then-immediate-reader-oob` on `wasm-binary`, preserve the parser and harness gates first, then mutate only the causal invariant described by the verified trace. Prefer `construct` while this format and harness contract are present.

## Procedure
1. Preserve the `wasm-binary` carrier enough for the `libfuzzer` harness to reach the parser path.
2. Keep unrelated envelope fields minimal and stable so verifier feedback stays tied to the target sink.
3. Apply the verified invariant from the failure shape rather than random broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The local class may remain coarse. Treat the official vulnerable-versus-fixed target match as the confirmation gate for this policy.

## Negative Memory
- Do not corrupt the outer `wasm-binary` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser reachability, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified solve(s), including round 30.
- Scope: generator repair only.
