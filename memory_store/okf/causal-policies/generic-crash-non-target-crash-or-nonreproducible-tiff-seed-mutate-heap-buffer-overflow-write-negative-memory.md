---
type: causal-policy
title: "Generic Crash Non Target Crash Or Nonreproducible Tiff Seed Mutate Heap Buffer Overflow Write Negative Memory"
description: "Round 14 negative memory for generic_crash with verifier signal non_target_crash_or_nonreproducible."
failure_class: "generic_crash"
verifier_signal: "non_target_crash_or_nonreproducible"
candidate_family: "seed_mutate"
input_format: "tiff"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-write"
access_scope: generate
success_count: 0
confidence: medium
tags: ["generic-crash", "non-target-crash-or-nonreproducible", "tiff", "negative-memory", "round-14"]
match_keys: ["generic_crash", "non_target_crash_or_nonreproducible", "tiff", "libfuzzer", "heap-buffer-overflow-write", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 14
---
# Generic Crash Non Target Crash Or Nonreproducible Tiff Seed Mutate Heap Buffer Overflow Write Negative Memory

- key: `generic_crash x non_target_crash_or_nonreproducible`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[tiff]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Mutating real high-bit-depth TIFF samples to request WebP compression reached the active PTIF coder and produced one local crash, but the official server did not reproduce it as a vulnerable target match. Other high-bit-depth grayscale and truecolor variants decoded and wrote cleanly, so the missing condition is likely a more exact PTIF/WebP writer state rather than the general bit-depth gate alone.

## Policy
Treat `generic_crash x non_target_crash_or_nonreproducible` on `tiff` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest carrier that the verifier proved reaches the parser, decoder, or harness path.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, parser-not-reached, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not count parser reachability, local crashes, clean exits, fixed-image crashes, usage banners, or sink mismatches as success.
- Do not repeat this candidate family unless the new attempt changes the causal gate named above.
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from Round 14.
- Scope: generator repair and basin avoidance only.
