---
type: causal-policy
title: "Opentype Font Plus Trailing Utf32 Seed Mutate Target Stack Reached Despite Local Sink Mismatch Use Of Uninitialized Value Verified Recovery"
description: "Round 23 verified recovery for wrong_sink with verifier signal target_stack_reached_despite_local_sink_mismatch."
failure_class: "wrong_sink"
verifier_signal: "target_stack_reached_despite_local_sink_mismatch"
candidate_family: "seed_mutate"
input_format: "opentype-font-plus-trailing-utf32"
harness_convention: "libfuzzer-harfbuzz-shape"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 1
confidence: medium
tags: ["wrong-sink", "target-stack-reached-despite-local-sink-mismatch", "opentype-font-plus-trailing-utf32", "libfuzzer-harfbuzz-shape", "seed-mutate", "verified-recovery", "round-23"]
match_keys: ["wrong-sink", "target-stack-reached-despite-local-sink-mismatch", "opentype-font-plus-trailing-utf32", "libfuzzer-harfbuzz-shape", "use-of-uninitialized-value"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 23
---
# Opentype Font Plus Trailing Utf32 Seed Mutate Target Stack Reached Despite Local Sink Mismatch Use Of Uninitialized Value Verified Recovery

- key: `wrong_sink x target_stack_reached_despite_local_sink_mismatch`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[opentype-font-plus-trailing-utf32]]
- harnesses: [[libfuzzer-harfbuzz-shape]]

## Failure Shape
Start from a real shaping-test font that contains the Syriac stretch feature. Append trailing UTF-32 text consumed by the fuzzer and use a sequence dominated by the Syriac abbreviation mark so Arabic shaping applies the stretch feature and marks an unsafe-to-break range over glyphs created by feature expansion.

## Policy
For `wrong_sink x target_stack_reached_despite_local_sink_mismatch` on `opentype-font-plus-trailing-utf32`, preserve the format recognition, harness contract, and parser reachability gates before varying the causal invariant. Prefer `seed_mutate` while this format and harness contract are present.

## Procedure
1. Preserve the `opentype-font-plus-trailing-utf32` carrier enough for the `libfuzzer-harfbuzz-shape` harness to reach the observed parser path.
2. Keep envelope fields minimal and internally consistent so verifier feedback remains tied to the target relation.
3. Apply the verified invariant from the failure shape before broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for this policy; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `opentype-font-plus-trailing-utf32` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, fixed-build crashes, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified round 23 solve after 5 attempts.
- Scope: generator repair only.
