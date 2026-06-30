---
type: causal-policy
title: "Dxf Seed Mutate Generic Crash Parser Reached Cleanup Crash Type Confusion Invalid Memory Read Verified Recovery"
description: "Round 30 verified recovery for generic_crash with verifier signal parser_reached_cleanup_crash."
failure_class: "generic_crash"
verifier_signal: "parser_reached_cleanup_crash"
candidate_family: "seed_mutate"
input_format: "dxf"
harness_convention: "libfuzzer/libredwg-llvmfuzz"
vuln_class: "type-confusion-invalid-memory-read"
access_scope: generate
success_count: 1
confidence: medium
tags: ["generic-crash", "parser-reached-cleanup-crash", "dxf", "libfuzzer-libredwg-llvmfuzz", "seed-mutate", "verified-recovery", "round-30"]
match_keys: ["generic-crash", "parser-reached-cleanup-crash", "dxf", "libfuzzer-libredwg-llvmfuzz", "type-confusion-invalid-memory-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 30
---
# Dxf Seed Mutate Generic Crash Parser Reached Cleanup Crash Type Confusion Invalid Memory Read Verified Recovery

- key: `generic-crash x parser-reached-cleanup-crash`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[dxf]]
- harnesses: [[libfuzzer-libredwg-llvmfuzz]]

## Failure Shape
Start from a real DXF seed so the section graph and object table are accepted. Add an object-context-data record whose declared field schema contains a handle-typed scale slot, and rely on the DXF defaulting path that treats any field named scale as a 3D-point value. Omitting the explicit scale value causes cleanup to later interpret the point-written storage as a handle reference, producing a vulnerable-build crash while the fixed build rejects the type mismatch.

## Policy
For `generic-crash x parser-reached-cleanup-crash` on `dxf`, preserve the parser and harness gates first, then mutate only the causal invariant described by the verified trace. Prefer `seed-mutate` while this format and harness contract are present.

## Procedure
1. Preserve the `dxf` carrier enough for the `libfuzzer-libredwg-llvmfuzz` harness to reach the parser path.
2. Keep unrelated envelope fields minimal and stable so verifier feedback stays tied to the target sink.
3. Apply the verified invariant from the failure shape rather than random broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The local class may remain coarse. Treat the official vulnerable-versus-fixed target match as the confirmation gate for this policy.

## Negative Memory
- Do not corrupt the outer `dxf` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser reachability, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified solve(s), including round 30.
- Scope: generator repair only.
