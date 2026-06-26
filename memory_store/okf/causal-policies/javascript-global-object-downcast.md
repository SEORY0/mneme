---
type: causal-policy
title: JavaScript Global Object Downcast Recovery
description: Verified recovery for wrong_sink with target_stack_ub on javascript inputs.
failure_class: wrong_sink
verifier_signal: target_stack_ub
candidate_family: construct
input_format: javascript
harness_convention: libfuzzer
vuln_class: undefined-behavior-invalid-downcast
access_scope: generate
success_count: 1
confidence: medium
tags: [wrong-sink, target-stack-ub, construct, javascript, undefined-behavior-invalid-downcast, verified-recovery]
match_keys: [wrong-sink, target-stack-ub, javascript, undefined-behavior-invalid-downcast]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
---
# JavaScript Global Object Downcast Recovery

- key: `wrong_sink x target_stack_ub`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[javascript]]

## Failure Shape
Use any syntactically valid JavaScript program so the fuzzer proceeds from parsing into VM
creation. The interpreter construction path instantiates the global object, violating the
object-construction invariant by downcasting a base object during GlobalObject setup before
the derived object is valid.

## Policy
For `wrong_sink x target_stack_ub` on `javascript`, preserve the parser and harness gate first, then mutate
only the causal invariant described by the verified trace. Prefer the candidate family `construct`
when the carrier is available because this shape was server-confirmed against vulnerable and fixed
builds.

## Procedure
1. Start with a syntactically valid JavaScript program that the fuzzer accepts.
2. Avoid parser tricks that stop before VM creation; the target path is global object
construction.
3. Submit when the runtime setup stack reports the invalid downcast or construction-time UB
signal.
4. If parser-clean scripts fail, retarget to initialization reachability rather than token
mutation.

## Verifier Contract
The local signal may remain coarse. Keep candidates that reach the named parser or sink and
use the official vulnerable-versus-fixed comparison as the target-match gate.

## Negative Memory
- Do not spend iterations on malformed syntax once parsing already reaches clean execution.
- Do not require a large program; the vulnerable invariant is in setup, before user script
complexity matters.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified solve.
- Scope: generator repair only.
