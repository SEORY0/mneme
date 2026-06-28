---
type: causal-policy
title: "Mruby Source Construct Parser Reached Target Array Splice Heap Buffer Overflow Read Verified Recovery"
description: "Round 24 verified recovery for wrong_sink with verifier signal parser_reached_target_array_splice."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_array_splice"
candidate_family: "construct"
input_format: "mruby-source"
harness_convention: "honggfuzz-file"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: medium
tags: ["wrong-sink", "parser-reached-target-array-splice", "mruby-source", "honggfuzz-file", "construct", "verified-recovery", "round-24"]
match_keys: ["wrong-sink", "parser-reached-target-array-splice", "mruby-source", "honggfuzz-file", "heap-buffer-overflow-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 24
---
# Mruby Source Construct Parser Reached Target Array Splice Heap Buffer Overflow Read Verified Recovery

- key: `wrong_sink x parser_reached_target_array_splice`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[mruby-source]]
- harnesses: [[honggfuzz-file]]

## Failure Shape
Use valid mruby source that creates an array, performs indexed replacement where the requested removal length extends beyond the current tail, and replaces it with fewer elements. The vulnerable splice logic computes the tail before shortening the effective length, so the later move reads past the valid array storage; the fixed build rejects or adjusts this relation cleanly.

## Policy
For `wrong_sink x parser_reached_target_array_splice` on `mruby-source`, preserve the format recognition, harness contract, and parser reachability gates before varying the causal invariant. Prefer `construct` only while this format and harness contract are present.

## Procedure
1. Preserve the `mruby-source` carrier and `honggfuzz-file` harness contract until parser reachability is stable.
2. Apply the causal invariant in the failure shape before broad mutation or seed sweeping.
3. Treat local crash class as supporting signal only; keep the candidate only when vulnerable and fixed images diverge on the official target relation.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for recovery policies; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `mruby-source` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, fixed-build crashes, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified round 24 solve after 6 attempts.
- Scope: generator repair and retargeting only.
