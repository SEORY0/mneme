---
type: causal-policy
title: "Opentype Font Seed Mutate OTS Stat Serialize Uninitialized Fallback Use Of Uninitialized Value Verified Recovery"
description: "Round 20 verified recovery for generic_crash with verifier signal ots_stat_serialize_uninitialized_fallback."
failure_class: "generic_crash"
verifier_signal: "ots_stat_serialize_uninitialized_fallback"
candidate_family: "seed_mutate"
input_format: "opentype-font"
harness_convention: "libfuzzer-ots"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 1
confidence: medium
tags: ["generic-crash", "ots-stat-serialize-uninitialized-fallback", "opentype-font", "libfuzzer-ots", "seed-mutate", "verified-recovery", "round-20"]
match_keys: ["generic-crash", "ots-stat-serialize-uninitialized-fallback", "opentype-font", "libfuzzer-ots", "use-of-uninitialized-value"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 20
---
# Opentype Font Seed Mutate OTS Stat Serialize Uninitialized Fallback Use Of Uninitialized Value Verified Recovery

- key: `generic_crash x ots_stat_serialize_uninitialized_fallback`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[opentype-font]]
- harnesses: [[libfuzzer-ots]]

## Failure Shape
Start from a valid small OpenType font and let a font-building library keep the table directory and checksums coherent. Add a STAT table whose original header version omits the elided fallback name field, but whose axis-value content requires the sanitizer to upgrade the table minor version during parsing. The crash is reached when serialization writes the upgraded table form and reads the fallback field that was absent in the input structure.

## Policy
For `generic_crash x ots_stat_serialize_uninitialized_fallback` on `opentype-font`, preserve the parser and harness gates first, then mutate only the causal invariant described by the verified trace. Prefer `seed_mutate` while this format and harness contract are present.

## Procedure
1. Preserve the `opentype-font` carrier enough for the `libfuzzer-ots` harness to reach the parser path.
2. Keep unrelated envelope fields minimal and stable so verifier feedback stays tied to the target sink.
3. Apply the verified invariant from the failure shape rather than random broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The local class may remain coarse. Treat the official vulnerable-versus-fixed target match as the confirmation gate for this policy.

## Negative Memory
- Do not corrupt the outer `opentype-font` recognition gate while retargeting this signal.
- Do not treat off-target crashes or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified round 20 solve.
- Scope: generator repair only.
