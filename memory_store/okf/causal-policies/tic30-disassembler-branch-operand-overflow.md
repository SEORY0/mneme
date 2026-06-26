---
type: causal-policy
title: Tic30 Disassembler Branch Operand Overflow
description: Verified recovery for wrong_sink with target_stack_overflow_in_tic30_branch_printing on raw disassembler buffer with harness selector suffix inputs.
failure_class: wrong_sink
verifier_signal: target_stack_overflow_in_tic30_branch_printing
candidate_family: construct
input_format: raw disassembler buffer with harness selector suffix
harness_convention: libfuzzer
access_scope: generate
success_count: 1
confidence: medium
tags: [wrong-sink, target-stack-overflow-in-tic30-branch-printing, construct, raw-disassembler-buffer, verified_recovery]
match_keys: [wrong-sink, target-stack-overflow-in-tic30-branch-printing, raw-disassembler-buffer, stack-buffer-overflow-write]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
---
# Tic30 Disassembler Branch Operand Overflow

- key: `wrong_sink x target_stack_overflow_in_tic30_branch_printing`
- outcome: verified recovery
- confidence: 0.69
- success_count: 1
- failure_count: 0
- formats: [[raw-disassembler-buffer]]

## Failure Shape
A prior candidate reached `wrong_sink` before the verifier-confirmed repair. The successful candidate kept the `raw disassembler buffer with harness selector suffix` recognition envelope and placed the mutation in the cross-field invariant consumed by the target parser or sink.
## Procedure
Select the TIC30 disassembler through the harness suffix, then provide a branch-family instruction that routes through the delayed branch printer. That path allocates a small local operand buffer, while the register operand helper writes using the wider register-name field expected by another operand kind, overflowing the local buffer before the fixed build rejects the instruction.

Retarget from this failure key by preserving the format gate first, then changing exactly the relation named above. Prefer compact construction for construct traces and seed-preserving mutation for seed traces.

## Verifier Contract
The expected signal is `target_stack_overflow_in_tic30_branch_printing` with a vulnerable-build crash and clean fixed build. Parser reachability without the differential crash is not sufficient.

## Negative Guards
Do not store raw payload bytes, exact positions, or submit metadata. Do not widen the mutation after the parser envelope is accepted; if the fixed image also crashes, shrink back to the single boundary relation.
