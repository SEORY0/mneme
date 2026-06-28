---
type: causal-policy
title: "No Crash Unstable Allocator False Positive Opentype Font Negative Memory"
description: "Round 8 negative memory for no_crash with verifier signal unstable_allocator_false_positive."
failure_class: "no_crash"
verifier_signal: "unstable_allocator_false_positive"
candidate_family: "seed_mutate"
input_format: "opentype-font"
harness_convention: "libfuzzer"
vuln_class: "uninitialized-state-after-serialization-failure"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "unstable-allocator-false-positive", "opentype-font", "negative_memory", "round-8"]
match_keys: ["no_crash", "unstable_allocator_false_positive", "opentype-font", "libfuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 8
---
# No Crash Unstable Allocator False Positive Opentype Font Negative Memory

## Policy
Treat `no_crash x unstable_allocator_false_positive` as a persistent failure basin for `opentype-font` under `libfuzzer`. Preserve any reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Diagnosed Dead End
- A real subset-fuzzer font seed and length-padding mutations sometimes produced local allocator-dependent crashes, but confirmation and the official server did not reproduce a vulnerable-only target match. The missing condition appears to be a font with a VariationStore serialization failure that still leaves the serializer object in a partially initialized state.

## Format and Harness Gates
- Format: The input is an OpenType/TrueType-style font blob. The relevant path is HarfBuzz subsetting of variation data: the font must contain variation-store structures that survive parsing, enter subsetting, and then fail serialization at the specific point where later fields are still inspected.
- Harness: The subset fuzzer consumes the raw input as a font blob. It also derives deterministic allocator pressure from total input size and optionally reads subset flags and text-selection data from the end of the input, so changing trailing length can change allocator behavior and the selected text without changing leading font bytes.

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
