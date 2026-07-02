---
type: causal-policy
title: "MRUBY Source Construct Sink Mismatch VM Exec After Codegen Corruption Heap Buffer Overflow Read Verified Recovery"
description: "Round 26 verified recovery for wrong_sink with verifier signal sink_mismatch_vm_exec_after_codegen_corruption."
failure_class: "wrong_sink"
verifier_signal: "sink_mismatch_vm_exec_after_codegen_corruption"
candidate_family: "construct"
input_format: "mruby-source"
harness_convention: "libfuzzer-mruby-load-string"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "sink-mismatch-vm-exec-after-codegen-corruption", "mruby-source", "libfuzzer-mruby-load-string", "construct", "verified-recovery", "round-26"]
match_keys: ["wrong_sink", "sink_mismatch_vm_exec_after_codegen_corruption", "mruby-source", "libfuzzer-mruby-load-string", "heap-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 26
---
# MRUBY Source Construct Sink Mismatch VM Exec After Codegen Corruption Heap Buffer Overflow Read Verified Recovery

- key: `wrong_sink x sink_mismatch_vm_exec_after_codegen_corruption`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[mruby-source]]
- harnesses: [[libfuzzer-mruby-load-string]]

## Failure Shape
Use syntactically valid mruby source that compiles a method containing a local assignment from a non-small 32-bit integer immediate whose low half is nonzero, then immediately uses or returns that local. This reaches the compiler peephole path where a MOVE after OP_LOADI32 is folded by re-emitting the large immediate with the wrong helper, corrupting the generated instruction stream; executing the method exposes the corrupted bytecode in the vulnerable build while the fixed build preserves the instruction shape.

## Policy
For `wrong_sink x sink_mismatch_vm_exec_after_codegen_corruption` on `mruby-source`, preserve the format recognition and harness contract before varying the vulnerable invariant. Prefer `construct` only while that carrier and harness contract remain stable.

## Procedure
1. Preserve the `mruby-source` carrier and `libfuzzer-mruby-load-string` harness contract until parser reachability is stable.
2. Apply the causal invariant in the failure shape before broad mutation or seed sweeping.
3. Treat local crash class as supporting signal only; keep the candidate only when vulnerable and fixed images diverge on the official target relation.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for this recovery policy; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `mruby-source` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, fixed-build crashes, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Format Contract
The input is plain mruby source text. Parser reachability depends on valid Ruby syntax; integer literals outside the compact immediate ranges are emitted through wider integer opcodes during code generation. Method bodies and local assignments are useful carriers because they create temporary registers and later local moves that can trigger peephole rewrites.

## Harness Contract
The libFuzzer harness copies the entire raw input into a newly NUL-terminated buffer, opens a fresh mruby state, calls mrb_load_string on that source, closes the state, and frees the copy. There is no leading selector byte, length prefix, bytecode container, or FuzzedDataProvider split.

## Evidence Shape
- Support: 1 server-verified round 26 solve after 7 attempts.
- Scope: generator repair and retargeting only.
