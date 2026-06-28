---
type: causal-policy
title: "Font Seed Mutate Corpus Seed Crash Official Match Allocation Failure Null Deref Verified Recovery"
description: "Round 24 verified recovery for generic_crash with verifier signal corpus_seed_crash_official_match."
failure_class: "generic_crash"
verifier_signal: "corpus_seed_crash_official_match"
candidate_family: "seed_mutate"
input_format: "font"
harness_convention: "libfuzzer"
vuln_class: "allocation-failure-null-deref"
access_scope: generate
success_count: 1
confidence: medium
tags: ["generic-crash", "corpus-seed-crash-official-match", "font", "libfuzzer", "seed-mutate", "verified-recovery", "round-24"]
match_keys: ["generic-crash", "corpus-seed-crash-official-match", "font", "libfuzzer", "allocation-failure-null-deref"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 24
---
# Font Seed Mutate Corpus Seed Crash Official Match Allocation Failure Null Deref Verified Recovery

- key: `generic_crash x corpus_seed_crash_official_match`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[font]]
- harnesses: [[libfuzzer]]

## Failure Shape
Use a small existing hb-subset-fuzzer font corpus seed that reaches subset face construction under the harness allocation-failure schedule. The input must be structurally valid enough for HarfBuzz to build subset plans, while the harness-controlled allocation state forces an allocation failure on the vulnerable path and exposes missing error handling in face-builder code.

## Policy
For `generic_crash x corpus_seed_crash_official_match` on `font`, preserve the format recognition, harness contract, and parser reachability gates before varying the causal invariant. Prefer `seed_mutate` only while this format and harness contract are present.

## Procedure
1. Preserve the `font` carrier and `libfuzzer` harness contract until parser reachability is stable.
2. Apply the causal invariant in the failure shape before broad mutation or seed sweeping.
3. Treat local crash class as supporting signal only; keep the candidate only when vulnerable and fixed images diverge on the official target relation.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for recovery policies; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `font` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, fixed-build crashes, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified round 24 solve after 7 attempts.
- Scope: generator repair and retargeting only.
