---
type: causal-policy
title: "Dex Seed Mutate Generic Crash Official Target Match Fixed Clean Parser Loop Invalid Index Crash Verified Recovery"
description: "Round 30 verified recovery for generic_crash with verifier signal official_target_match_fixed_clean."
failure_class: "generic_crash"
verifier_signal: "official_target_match_fixed_clean"
candidate_family: "seed_mutate"
input_format: "dex"
harness_convention: "libfuzzer-yara-dex-module"
vuln_class: "parser-loop-invalid-index-crash"
access_scope: generate
success_count: 1
confidence: medium
tags: ["generic-crash", "official-target-match-fixed-clean", "dex", "libfuzzer-yara-dex-module", "seed-mutate", "verified-recovery", "round-30"]
match_keys: ["generic-crash", "official-target-match-fixed-clean", "dex", "libfuzzer-yara-dex-module", "parser-loop-invalid-index-crash"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 30
---
# Dex Seed Mutate Generic Crash Official Target Match Fixed Clean Parser Loop Invalid Index Crash Verified Recovery

- key: `generic-crash x official-target-match-fixed-clean`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[dex]]
- harnesses: [[libfuzzer-yara-dex-module]]

## Failure Shape
Extract or reuse a structurally valid small DEX seed that reaches YARA's dex module. Preserve the header, ID tables, class definition, and existing encoded method entries, then inflate a class-data encoded-method count using the same compact integer field shape. This makes the vulnerable parser continue past the real encoded-method list into malformed class-data state, while the fixed parser abandons when the encoded loader cannot advance or resolves an undefined method/name relation.

## Policy
For `generic-crash x official-target-match-fixed-clean` on `dex`, preserve the parser and harness gates first, then mutate only the causal invariant described by the verified trace. Prefer `seed-mutate` while this format and harness contract are present.

## Procedure
1. Preserve the `dex` carrier enough for the `libfuzzer-yara-dex-module` harness to reach the parser path.
2. Keep unrelated envelope fields minimal and stable so verifier feedback stays tied to the target sink.
3. Apply the verified invariant from the failure shape rather than random broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The local class may remain coarse. Treat the official vulnerable-versus-fixed target match as the confirmation gate for this policy.

## Negative Memory
- Do not corrupt the outer `dex` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser reachability, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified solve(s), including round 30.
- Scope: generator repair only.
