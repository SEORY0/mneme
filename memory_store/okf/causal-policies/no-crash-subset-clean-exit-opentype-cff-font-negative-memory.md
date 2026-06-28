---
type: causal-policy
title: "No Crash Subset Clean Exit Opentype Cff Font Negative Memory"
description: "Round 16 negative memory for no_crash with verifier signal subset_clean_exit."
failure_class: "no_crash"
verifier_signal: "subset_clean_exit"
candidate_family: "seed_mutate_tail_flags"
input_format: "opentype-cff-font"
harness_convention: "libfuzzer-harfbuzz-subset"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "subset-clean-exit", "opentype-cff-font", "negative-memory", "round-16"]
match_keys: ["no_crash", "subset_clean_exit", "opentype-cff-font", "libfuzzer-harfbuzz-subset", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 16
---
# No Crash Subset Clean Exit Opentype Cff Font Negative Memory

## Policy
For `no_crash x subset_clean_exit`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
- CFF/OpenType and contextual font seeds with subset flags and codepoint tails reached the subset fuzzer but exited cleanly. The unresolved relation is a malformed CFF charset or glyph-count mapping that remains valid enough for face construction and then oversteps collect-glyph-to-SID-map bounds.
- When `no_crash x subset_clean_exit` appears for `opentype-cff-font`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
- Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- OpenType/CFF inputs must preserve the sfnt table directory and the CFF table structure, including top dict, charstrings, charset, and related indexes, until HarfBuzz creates a face and enumerates glyph data. Arbitrary truncation is rejected before charset collection.
- Harness: The selected HarfBuzz subset fuzzer consumes the whole input as the font blob. Optional subset flags and codepoints are taken from the trailing bytes when present, so appending a tail can influence subsetting while keeping the original font bytes intact.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed persistent failure from round 16.
- Scope: generator avoidance for the same failure-keyed basin.
