---
type: causal-policy
title: "Generic Crash Local Crash Not Reproduced Officially Palm Pdb Image Negative Memory"
description: "Round 10 negative memory for generic_crash with verifier signal local_crash_not_reproduced_officially."
failure_class: "generic_crash"
verifier_signal: "local_crash_not_reproduced_officially"
candidate_family: "seed_mutate"
input_format: "palm/pdb image"
harness_convention: "libfuzzer image coder roundtrip"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 0
confidence: medium
tags: ["generic-crash", "local-crash-not-reproduced-officially", "negative-memory", "round-10"]
match_keys: ["generic_crash", "local_crash_not_reproduced_officially", "palm/pdb image", "libfuzzer image coder roundtrip", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 10
---
# Generic Crash Local Crash Not Reproduced Officially Palm Pdb Image Negative Memory

## Policy
For `generic_crash x local_crash_not_reproduced_officially`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
1. Repository PALM/PDB fixtures exercise the GraphicsMagick PDB coder, and several gray/RGB seeds produced local generic crashes, but official submission did not reproduce the target.
2. When `generic_crash x local_crash_not_reproduced_officially` appears for `palm/pdb image`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
3. Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- Palm/PDB images carry a database-style header followed by image metadata and scanline payloads. Low-bit-depth grayscale variants require row padding and bit packing, while scanline/RLE variants add per-row encoding rules.
- Harness: The fuzzer passes raw file bytes to the GraphicsMagick coder target. The target auto-detects image format and exercises decode/encode behavior; no leading selector byte is consumed by the harness.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed round-10 persistent failure.
- Scope: generator avoidance for the same failure-keyed basin.
