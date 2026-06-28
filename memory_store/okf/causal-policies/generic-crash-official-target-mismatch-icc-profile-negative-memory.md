---
type: causal-policy
title: "Generic Crash Official Target Mismatch Icc Profile Negative Memory"
description: "Round 8 negative memory for generic_crash with verifier signal official_target_mismatch."
failure_class: "generic_crash"
verifier_signal: "official_target_mismatch"
candidate_family: "construct"
input_format: "icc-profile"
harness_convention: "libfuzzer"
vuln_class: "divide-by-zero"
access_scope: generate
success_count: 0
confidence: medium
tags: ["generic-crash", "official-target-mismatch", "icc-profile", "negative_memory", "round-8"]
match_keys: ["generic_crash", "official_target_mismatch", "icc-profile", "libfuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 8
---
# Generic Crash Official Target Mismatch Icc Profile Negative Memory

## Policy
Treat `generic_crash x official_target_mismatch` as a persistent failure basin for `icc-profile` under `libfuzzer`. Preserve any reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Diagnosed Dead End
- Minimal ICC profiles with parametric tone curve tags could be opened, and some malformed gray curve variants crashed the local wrapper, but server submission did not reproduce the target. The submitted crash was likely a harness/local artifact or non-target malformed-profile path, not the intended parametric-curve evaluation divide-by-zero.

## Format and Harness Gates
- Format: ICC profiles have a fixed-size header followed by a tag table of signature, data location, and size entries. Tone-curve tags can use the parametric curve type, which stores a curve type selector and fixed-point parameters; different selectors require different parameter counts.
- Harness: The profile fuzzer writes raw input to a temporary ICC file, opens it with lcms, reads selected raw and structured tags, saves the profile again, and closes it. The raw fuzz bytes are not carved; all structure comes from the ICC parser.

## Procedure
1. Before retrying this basin, rebuild the carrier around the exact harness contract and confirm parser reachability.
2. Replace the failed mutation family with a more specific invariant that would change the verifier signal.
3. Avoid broad seed mutation, oversized mutation, or off-target crash chasing when this same signal recurs.

## Negative Memory
- Do not promote this basin into a recovery policy until an official vulnerable/fixed verifier target match is observed.
- Do not preserve raw bytes, offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-8 persistent failure trace.
- Scope: generator avoidance and retargeting for the same failure key.
