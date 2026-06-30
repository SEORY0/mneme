---
type: causal-policy
title: "Gas Assembly Source Construct Text Wrong Sink Parser Reached Target Stack Via Memset Interceptor Heap Buffer Overflow Write Verified Recovery"
description: "Round 30 verified recovery for wrong_sink with verifier signal parser_reached_target_stack_via_memset_interceptor."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_stack_via_memset_interceptor"
candidate_family: "construct_text"
input_format: "gas-assembly-source"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-write"
access_scope: generate
success_count: 1
confidence: medium
tags: ["wrong-sink", "parser-reached-target-stack-via-memset-interceptor", "gas-assembly-source", "libfuzzer", "construct-text", "verified-recovery", "round-30"]
match_keys: ["wrong-sink", "parser-reached-target-stack-via-memset-interceptor", "gas-assembly-source", "libfuzzer", "heap-buffer-overflow-write"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 30
---
# Gas Assembly Source Construct Text Wrong Sink Parser Reached Target Stack Via Memset Interceptor Heap Buffer Overflow Write Verified Recovery

- key: `wrong-sink x parser-reached-target-stack-via-memset-interceptor`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[gas-assembly-source]]
- harnesses: [[libfuzzer]]

## Failure Shape
Use the raw assembler-source harness contract and emit a minimal .file directive whose file-number field is just beyond the signed/unsigned boundary handled by the DWARF file table. Keep the directive syntactically valid with a quoted source name so GAS reaches dwarf2_directive_file and assign_file_to_slot; the vulnerable build computes an undersized allocation/clear for the expanded file table while the fixed build rejects the overflowing file number.

## Policy
For `wrong-sink x parser-reached-target-stack-via-memset-interceptor` on `gas-assembly-source`, preserve the parser and harness gates first, then mutate only the causal invariant described by the verified trace. Prefer `construct-text` while this format and harness contract are present.

## Procedure
1. Preserve the `gas-assembly-source` carrier enough for the `libfuzzer` harness to reach the parser path.
2. Keep unrelated envelope fields minimal and stable so verifier feedback stays tied to the target sink.
3. Apply the verified invariant from the failure shape rather than random broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The local class may remain coarse. Treat the official vulnerable-versus-fixed target match as the confirmation gate for this policy.

## Negative Memory
- Do not corrupt the outer `gas-assembly-source` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser reachability, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified solve(s), including round 30.
- Scope: generator repair only.
