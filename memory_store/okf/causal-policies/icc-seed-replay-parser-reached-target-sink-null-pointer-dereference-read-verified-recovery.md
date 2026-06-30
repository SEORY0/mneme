---
type: causal-policy
title: "ICC Seed Replay Parser Reached Target Sink Null Pointer Dereference Read Verified Recovery"
description: "Round 26 verified recovery for generic_crash with verifier signal parser_reached_target_sink."
failure_class: "generic_crash"
verifier_signal: "parser_reached_target_sink"
candidate_family: "seed_replay"
input_format: "icc"
harness_convention: "libfuzzer"
vuln_class: "null-pointer-dereference-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-target-sink", "icc", "libfuzzer", "seed-replay", "verified-recovery", "round-26"]
match_keys: ["generic_crash", "parser_reached_target_sink", "icc", "libfuzzer", "null-pointer-dereference-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 26
---
# ICC Seed Replay Parser Reached Target Sink Null Pointer Dereference Read Verified Recovery

- key: `generic_crash x parser_reached_target_sink`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[icc]]
- harnesses: [[libfuzzer]]

## Failure Shape
Use a real ICC profile that satisfies the header, profile-size, magic, tag-table, and illuminant gates, then reaches profile-info handling with parametric transfer curves. The vulnerable extent reader treats aliased curve storage like a sampled table even though there are no table entries, so the table-extents path reads through an invalid table reference; the fixed build guards that state.

## Policy
For `generic_crash x parser_reached_target_sink` on `icc`, preserve the format recognition and harness contract before varying the vulnerable invariant. Prefer `seed_replay` only while that carrier and harness contract remain stable.

## Procedure
1. Preserve the `icc` carrier and `libfuzzer` harness contract until parser reachability is stable.
2. Apply the causal invariant in the failure shape before broad mutation or seed sweeping.
3. Treat local crash class as supporting signal only; keep the candidate only when vulnerable and fixed images diverge on the official target relation.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for this recovery policy; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `icc` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, fixed-build crashes, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Format Contract
ICC parsing requires a coherent profile header, the standard color-management magic, a bounded tag table, and tag records whose declared ranges stay inside the profile. Transfer response curves may be sampled curve tags or parametric curve tags; in this implementation both representations share storage in the curve object, so sampled-table metadata and parametric coefficients overlap.

## Harness Contract
The harness feeds the file bytes directly to the skcms parser and then queries parsed profile information that reads transfer-curve extents. There is no fuzzer-side carving or FuzzedDataProvider layout; parser reachability depends entirely on a self-consistent ICC envelope.

## Evidence Shape
- Support: 1 server-verified round 26 solve after 1 attempts.
- Scope: generator repair and retargeting only.
