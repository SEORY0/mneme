---
type: causal-policy
title: "Mruby Source Construct Parser Reached With Crash In Bigint String Conversion After Duplicate Uninitialized Bigint Copy Verified Recovery"
description: "Round 24 verified recovery for generic_crash with verifier signal parser_reached with crash in bigint string conversion after duplicate."
failure_class: "generic_crash"
verifier_signal: "parser_reached with crash in bigint string conversion after duplicate"
candidate_family: "construct"
input_format: "mruby-source"
harness_convention: "libfuzzer mruby_load_string"
vuln_class: "uninitialized-bigint-copy"
access_scope: generate
success_count: 1
confidence: medium
tags: ["generic-crash", "parser-reached-with-crash-in-bigint-string-conversion-after-duplicate", "mruby-source", "libfuzzer-mruby-load-string", "construct", "verified-recovery", "round-24"]
match_keys: ["generic-crash", "parser-reached-with-crash-in-bigint-string-conversion-after-duplicate", "mruby-source", "libfuzzer-mruby-load-string", "uninitialized-bigint-copy"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 24
---
# Mruby Source Construct Parser Reached With Crash In Bigint String Conversion After Duplicate Uninitialized Bigint Copy Verified Recovery

- key: `generic_crash x parser_reached with crash in bigint string conversion after duplicate`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[mruby-source]]
- harnesses: [[libfuzzer-mruby-load-string]]

## Failure Shape
Feed raw mruby source that creates a heap-backed large Integer, duplicates it through the generic object duplication path, and then immediately uses the duplicate in a bigint operation such as string conversion. The duplicate object is allocated with bigint type but its internal multi-precision storage is not initialized or deep-copied before use; the fixed build prevents or handles that copy.

## Policy
For `generic_crash x parser_reached with crash in bigint string conversion after duplicate` on `mruby-source`, preserve the format recognition, harness contract, and parser reachability gates before varying the causal invariant. Prefer `construct` only while this format and harness contract are present.

## Procedure
1. Preserve the `mruby-source` carrier and `libfuzzer-mruby-load-string` harness contract until parser reachability is stable.
2. Apply the causal invariant in the failure shape before broad mutation or seed sweeping.
3. Treat local crash class as supporting signal only; keep the candidate only when vulnerable and fixed images diverge on the official target relation.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for recovery policies; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `mruby-source` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, fixed-build crashes, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified round 24 solve after 5 attempts.
- Scope: generator repair and retargeting only.
