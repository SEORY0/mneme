---
type: causal-policy
title: "Bigint Pair Construct Parser Reached Use Of Uninitialized Value Verified Recovery"
description: "Round 24 verified recovery for wrong_sink with verifier signal parser_reached."
failure_class: "wrong_sink"
verifier_signal: "parser_reached"
candidate_family: "construct"
input_format: "bigint-pair"
harness_convention: "libfuzzer-botan-invert"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 1
confidence: medium
tags: ["wrong-sink", "parser-reached", "bigint-pair", "libfuzzer-botan-invert", "construct", "verified-recovery", "round-24"]
match_keys: ["wrong-sink", "parser-reached", "bigint-pair", "libfuzzer-botan-invert", "use-of-uninitialized-value"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 24
---
# Bigint Pair Construct Parser Reached Use Of Uninitialized Value Verified Recovery

- key: `wrong_sink x parser_reached`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[bigint-pair]]
- harnesses: [[libfuzzer-botan-invert]]

## Failure Shape
Use an even-length input split into two equal big-endian integers, with the second integer forced odd by the harness and larger than the first. Choose operands large enough to enter the word-block conditional add/subtract helpers in constant-time modular inversion; the block helper stack temporary remains partly uninitialized and is consumed during the correction path. Small operands do not reach that helper family.

## Policy
For `wrong_sink x parser_reached` on `bigint-pair`, preserve the format recognition, harness contract, and parser reachability gates before varying the causal invariant. Prefer `construct` only while this format and harness contract are present.

## Procedure
1. Preserve the `bigint-pair` carrier and `libfuzzer-botan-invert` harness contract until parser reachability is stable.
2. Apply the causal invariant in the failure shape before broad mutation or seed sweeping.
3. Treat local crash class as supporting signal only; keep the candidate only when vulnerable and fixed images diverge on the official target relation.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for recovery policies; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `bigint-pair` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, fixed-build crashes, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified round 24 solve after 10 attempts.
- Scope: generator repair and retargeting only.
