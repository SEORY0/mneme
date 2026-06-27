---
type: causal-policy
title: "No Crash Subset Clean Exit Opentype Sbix Font Negative Memory"
description: "Round 10 negative memory for no_crash with verifier signal subset_clean_exit."
failure_class: "no_crash"
verifier_signal: "subset_clean_exit"
candidate_family: "seed_mutate"
input_format: "opentype-sbix-font"
harness_convention: "libfuzzer-afl-wrapper"
vuln_class: "invalid-memory-access"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "subset-clean-exit", "negative-memory", "round-10"]
match_keys: ["no_crash", "subset_clean_exit", "opentype-sbix-font", "libfuzzer-afl-wrapper", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 10
---
# No Crash Subset Clean Exit Opentype Sbix Font Negative Memory

## Policy
For `no_crash x subset_clean_exit`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
1. A real sbix font seed remained accepted after nulling a strike pointer relation, but the subsetter skipped or sanitized that relation before the vulnerable access.
2. When `no_crash x subset_clean_exit` appears for `opentype-sbix-font`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
3. Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- An sbix font is an sfnt font with normal table directory, cmap/glyf/metrics tables, and an sbix table. The sbix table has a header, a strike offset list, and per-strike glyph image offset arrays. Subsetting must preserve enough cmap and glyph selection for the strike/glyph image path to execute.
- Harness: The active binary was hb-subset-fuzzer under an AFL-style wrapper. It reads the raw file bytes as a font, runs several subset configurations, and may use trailing bytes as codepoints and flags. There is no front selector; valid sfnt structure is the main gate.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed round-10 persistent failure.
- Scope: generator avoidance for the same failure-keyed basin.
