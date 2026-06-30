---
type: causal-policy
title: "Jpeg Seed Mutate Wrong Sink Parser Reached Vulnerable Only After Invalid Frame Length Gate Bounds Check Overflow Verified Recovery"
description: "Round 30 verified recovery for wrong_sink with verifier signal parser_reached_vulnerable_only_after_invalid_frame_length_gate."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_vulnerable_only_after_invalid_frame_length_gate"
candidate_family: "seed_mutate"
input_format: "jpeg"
harness_convention: "libfuzzer"
vuln_class: "bounds-check-overflow"
access_scope: generate
success_count: 1
confidence: medium
tags: ["wrong-sink", "parser-reached-vulnerable-only-after-invalid-frame-length-gate", "jpeg", "libfuzzer", "seed-mutate", "verified-recovery", "round-30"]
match_keys: ["wrong-sink", "parser-reached-vulnerable-only-after-invalid-frame-length-gate", "jpeg", "libfuzzer", "bounds-check-overflow"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 30
---
# Jpeg Seed Mutate Wrong Sink Parser Reached Vulnerable Only After Invalid Frame Length Gate Bounds Check Overflow Verified Recovery

- key: `wrong-sink x parser-reached-vulnerable-only-after-invalid-frame-length-gate`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[jpeg]]
- harnesses: [[libfuzzer]]

## Failure Shape
Start from a complete baseline JPEG seed that already satisfies marker, table, frame, scan, and entropy gates. Preserve the seed's tables and entropy stream, make the frame segment length internally invalid so the vulnerable bounds check accepts a wrapped length relation, and pair it with a minimal scan descriptor order violation that is reached only in the vulnerable build. The fixed build rejects the invalid frame-length relation before the later sanitizer sink.

## Policy
For `wrong-sink x parser-reached-vulnerable-only-after-invalid-frame-length-gate` on `jpeg`, preserve the parser and harness gates first, then mutate only the causal invariant described by the verified trace. Prefer `seed-mutate` while this format and harness contract are present.

## Procedure
1. Preserve the `jpeg` carrier enough for the `libfuzzer` harness to reach the parser path.
2. Keep unrelated envelope fields minimal and stable so verifier feedback stays tied to the target sink.
3. Apply the verified invariant from the failure shape rather than random broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The local class may remain coarse. Treat the official vulnerable-versus-fixed target match as the confirmation gate for this policy.

## Negative Memory
- Do not corrupt the outer `jpeg` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser reachability, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified solve(s), including round 30.
- Scope: generator repair only.
