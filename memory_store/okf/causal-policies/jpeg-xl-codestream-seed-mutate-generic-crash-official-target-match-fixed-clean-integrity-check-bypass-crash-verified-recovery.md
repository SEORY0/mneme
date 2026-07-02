---
type: causal-policy
title: "Jpeg Xl Codestream Seed Mutate Generic Crash Official Target Match Fixed Clean Integrity Check Bypass Crash Verified Recovery"
description: "Round 30 verified recovery for generic_crash with verifier signal official_target_match_fixed_clean."
failure_class: "generic_crash"
verifier_signal: "official_target_match_fixed_clean"
candidate_family: "seed_mutate"
input_format: "jpeg-xl-codestream"
harness_convention: "libfuzzer-djxl"
vuln_class: "integrity-check-bypass-crash"
access_scope: generate
success_count: 1
confidence: medium
tags: ["generic-crash", "official-target-match-fixed-clean", "jpeg-xl-codestream", "libfuzzer-djxl", "seed-mutate", "verified-recovery", "round-30"]
match_keys: ["generic-crash", "official-target-match-fixed-clean", "jpeg-xl-codestream", "libfuzzer-djxl", "integrity-check-bypass-crash"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 30
---
# Jpeg Xl Codestream Seed Mutate Generic Crash Official Target Match Fixed Clean Integrity Check Bypass Crash Verified Recovery

- key: `generic-crash x official-target-match-fixed-clean`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[jpeg-xl-codestream]]
- harnesses: [[libfuzzer-djxl]]

## Failure Shape
Replay a real compact JPEG XL codestream seed through the decoder fuzzer with a valid option tail appended for the harness. Preserve the codestream envelope and mutate exactly one entropy-coded payload byte so the ANS final-state or checksum relation is wrong while the rest of the image remains parseable. Broad malformed inputs and raw tiny inputs are local wrapper crash or clean-exit basins.

## Policy
For `generic-crash x official-target-match-fixed-clean` on `jpeg-xl-codestream`, preserve the parser and harness gates first, then mutate only the causal invariant described by the verified trace. Prefer `seed-mutate` while this format and harness contract are present.

## Procedure
1. Preserve the `jpeg-xl-codestream` carrier enough for the `libfuzzer-djxl` harness to reach the parser path.
2. Keep unrelated envelope fields minimal and stable so verifier feedback stays tied to the target sink.
3. Apply the verified invariant from the failure shape rather than random broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The local class may remain coarse. Treat the official vulnerable-versus-fixed target match as the confirmation gate for this policy.

## Negative Memory
- Do not corrupt the outer `jpeg-xl-codestream` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser reachability, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified solve(s), including round 30.
- Scope: generator repair only.
