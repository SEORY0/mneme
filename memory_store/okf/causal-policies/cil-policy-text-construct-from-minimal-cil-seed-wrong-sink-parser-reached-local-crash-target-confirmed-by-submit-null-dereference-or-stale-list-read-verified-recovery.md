---
type: causal-policy
title: "Cil Policy Text Construct From Minimal Cil Seed Wrong Sink Parser Reached Local Crash Target Confirmed By Submit Null Dereference Or Stale List Read Verified Recovery"
description: "Round 30 verified recovery for wrong_sink with verifier signal parser_reached_local_crash_target_confirmed_by_submit."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_local_crash_target_confirmed_by_submit"
candidate_family: "construct_from_minimal_cil_seed"
input_format: "cil-policy-text"
harness_convention: "libfuzzer"
vuln_class: "null-dereference-or-stale-list-read"
access_scope: generate
success_count: 1
confidence: medium
tags: ["wrong-sink", "parser-reached-local-crash-target-confirmed-by-submit", "cil-policy-text", "libfuzzer", "construct-from-minimal-cil-seed", "verified-recovery", "round-30"]
match_keys: ["wrong-sink", "parser-reached-local-crash-target-confirmed-by-submit", "cil-policy-text", "libfuzzer", "null-dereference-or-stale-list-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 30
---
# Cil Policy Text Construct From Minimal Cil Seed Wrong Sink Parser Reached Local Crash Target Confirmed By Submit Null Dereference Or Stale List Read Verified Recovery

- key: `wrong-sink x parser-reached-local-crash-target-confirmed-by-submit`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[cil-policy-text]]
- harnesses: [[libfuzzer]]

## Failure Shape
Use the raw CIL policy-text harness with enough class, SID, user, role, type, sensitivity, category, allow, role/type, user/role, user level/range, and SID context scaffolding to pass the compile gates. Place a validatetrans rule inside an optional block and make its right-hand operand a list that begins like a type list but contains a nested empty list. The malformed nested list makes list filling report invalid syntax while the vulnerable builder continues, leaving later expression resolution to consume stale list state; keep all other declarations valid so the fixed build can reject the single malformed relation cleanly.

## Policy
For `wrong-sink x parser-reached-local-crash-target-confirmed-by-submit` on `cil-policy-text`, preserve the parser and harness gates first, then mutate only the causal invariant described by the verified trace. Prefer `construct-from-minimal-cil-seed` while this format and harness contract are present.

## Procedure
1. Preserve the `cil-policy-text` carrier enough for the `libfuzzer` harness to reach the parser path.
2. Keep unrelated envelope fields minimal and stable so verifier feedback stays tied to the target sink.
3. Apply the verified invariant from the failure shape rather than random broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The local class may remain coarse. Treat the official vulnerable-versus-fixed target match as the confirmation gate for this policy.

## Negative Memory
- Do not corrupt the outer `cil-policy-text` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser reachability, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified solve(s), including round 30.
- Scope: generator repair only.
