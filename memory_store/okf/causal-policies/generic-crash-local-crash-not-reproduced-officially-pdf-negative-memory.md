---
type: causal-policy
title: "Generic Crash Local Crash Not Reproduced Officially PDF Negative Memory"
description: "Round 10 negative memory for generic_crash with verifier signal local_crash_not_reproduced_officially."
failure_class: "generic_crash"
verifier_signal: "local_crash_not_reproduced_officially"
candidate_family: "seed_mutate_and_construct"
input_format: "pdf"
harness_convention: "libfuzzer raw PDF renderer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 0
confidence: medium
tags: ["generic-crash", "local-crash-not-reproduced-officially", "negative-memory", "round-10"]
match_keys: ["generic_crash", "local_crash_not_reproduced_officially", "pdf", "libfuzzer raw PDF renderer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 10
---
# Generic Crash Local Crash Not Reproduced Officially PDF Negative Memory

## Policy
For `generic_crash x local_crash_not_reproduced_officially`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
1. A simple text PDF and multiple font-heavy PDF seeds exercised Poppler rendering.
2. When `generic_crash x local_crash_not_reproduced_officially` appears for `pdf`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
3. Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- Renderable PDFs need a valid page tree, resources, font references, and content streams. Font-related crashes are best approached from real PDFs that embed or select fonts which drive FreeType glyph loading rather than from a bare object skeleton.
- Harness: The harness feeds raw PDF bytes to Poppler and renders pages. There is no FuzzedDataProvider split; parser reachability depends on PDF validity and page renderability.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed round-10 persistent failure.
- Scope: generator avoidance for the same failure-keyed basin.
