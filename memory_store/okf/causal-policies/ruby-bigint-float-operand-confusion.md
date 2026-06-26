---
type: causal-policy
title: Ruby Bigint Float Operand Confusion Recovery
description: Verified recovery for generic_crash with parser_reached_target_sink on ruby inputs.
failure_class: generic_crash
verifier_signal: parser_reached_target_sink
candidate_family: construct
input_format: ruby
harness_convention: libfuzzer
vuln_class: type-confusion-invalid-read
access_scope: generate
success_count: 1
confidence: medium
tags: [generic-crash, parser-reached-target-sink, construct, ruby, type-confusion-invalid-read, verified-recovery]
match_keys: [generic-crash, parser-reached-target-sink, ruby, type-confusion-invalid-read]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
---
# Ruby Bigint Float Operand Confusion Recovery

- key: `generic_crash x parser_reached_target_sink`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[ruby]]

## Failure Shape
Run Ruby code that creates a bigint value and repeatedly mixes it with floating-point
operands through addition and subtraction. The vulnerable arithmetic dispatcher routes a
non-integer operand into bigint integer addition/subtraction, violating the operand-type
invariant and dereferencing an invalid bigint representation.

## Policy
For `generic_crash x parser_reached_target_sink` on `ruby`, preserve the parser and harness gate first, then mutate
only the causal invariant described by the verified trace. Prefer the candidate family `construct`
when the carrier is available because this shape was server-confirmed against vulnerable and fixed
builds.

## Procedure
1. Use Ruby code that creates a bigint value and reaches runtime arithmetic.
2. Mix bigint values with floating-point operands through addition and subtraction to exercise
the dispatcher.
3. Keep syntax simple so failures point to operand-type routing rather than parser rejection.
4. For parser-reached target-sink signals, shrink the script around the arithmetic sequence.

## Verifier Contract
The local signal may remain coarse. Keep candidates that reach the named parser or sink and
use the official vulnerable-versus-fixed comparison as the target-match gate.

## Negative Memory
- Do not keep adding syntax constructs after runtime execution is already reached.
- Do not mutate into generic name-lookup or scope crashes when the target invariant is
arithmetic operand type.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified solve.
- Scope: generator repair only.
