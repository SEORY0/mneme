---
type: causal-policy
title: "Binutils Disassembler Buffer With Trailer Selector Construct Generic Crash Vulnerable Only Segfault Submit Target Match Stack Buffer Overflow Write Verified Recovery"
description: "Round 30 verified recovery for generic_crash with verifier signal vulnerable_only_segfault_submit_target_match."
failure_class: "generic_crash"
verifier_signal: "vulnerable_only_segfault_submit_target_match"
candidate_family: "construct"
input_format: "binutils-disassembler-buffer-with-trailer-selector"
harness_convention: "libfuzzer-binutils-disassembler"
vuln_class: "stack-buffer-overflow-write"
access_scope: generate
success_count: 1
confidence: medium
tags: ["generic-crash", "vulnerable-only-segfault-submit-target-match", "binutils-disassembler-buffer-with-trailer-selector", "libfuzzer-binutils-disassembler", "construct", "verified-recovery", "round-30"]
match_keys: ["generic-crash", "vulnerable-only-segfault-submit-target-match", "binutils-disassembler-buffer-with-trailer-selector", "libfuzzer-binutils-disassembler", "stack-buffer-overflow-write"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 30
---
# Binutils Disassembler Buffer With Trailer Selector Construct Generic Crash Vulnerable Only Segfault Submit Target Match Stack Buffer Overflow Write Verified Recovery

- key: `generic-crash x vulnerable-only-segfault-submit-target-match`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[binutils-disassembler-buffer-with-trailer-selector]]
- harnesses: [[libfuzzer-binutils-disassembler]]

## Failure Shape
Use the raw binutils disassembler-buffer carrier and select the VAX disassembler through the fixed trailer. A simple recursive index-mode chain exits cleanly because it corrupts the private fetch base before the saved bailout state is used. The working carrier uses a multi-operand wide VAX instruction: the first operand recursively walks index modes, then a wide terminal addressing mode copies controlled non-mode bytes into later private fields; the following operand forces a fetch/bailout through that corrupted private state. The fixed build rejects the recursive index-mode overflow before the corruption path.

## Policy
For `generic-crash x vulnerable-only-segfault-submit-target-match` on `binutils-disassembler-buffer-with-trailer-selector`, preserve the parser and harness gates first, then mutate only the causal invariant described by the verified trace. Prefer `construct` while this format and harness contract are present.

## Procedure
1. Preserve the `binutils-disassembler-buffer-with-trailer-selector` carrier enough for the `libfuzzer-binutils-disassembler` harness to reach the parser path.
2. Keep unrelated envelope fields minimal and stable so verifier feedback stays tied to the target sink.
3. Apply the verified invariant from the failure shape rather than random broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The local class may remain coarse. Treat the official vulnerable-versus-fixed target match as the confirmation gate for this policy.

## Negative Memory
- Do not corrupt the outer `binutils-disassembler-buffer-with-trailer-selector` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser reachability, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified solve(s), including round 30.
- Scope: generator repair only.
