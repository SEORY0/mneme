---
type: causal-policy
title: "No Crash Subset Clean Exit Opentype Font Negative Memory"
description: "Round 16 negative memory for no_crash with verifier signal subset_clean_exit."
failure_class: "no_crash"
verifier_signal: "subset_clean_exit"
candidate_family: "seed_mutate_tail_flags"
input_format: "opentype-font"
harness_convention: "libfuzzer-harfbuzz-subset"
vuln_class: "bounds-check-glyph-closure"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "subset-clean-exit", "opentype-font", "negative-memory", "round-16"]
match_keys: ["no_crash", "subset_clean_exit", "opentype-font", "libfuzzer-harfbuzz-subset", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 16
---
# No Crash Subset Clean Exit Opentype Font Negative Memory

## Policy
For `no_crash x subset_clean_exit`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
- Contextual GSUB and GPOS fixture fonts with subset text and flag-tail variations subset cleanly. The unresolved condition is likely a malformed context lookup table relation such as coverage, class, rule count, or input glyph index inconsistency that survives face construction and reaches glyph-closure bounds checks.
- When `no_crash x subset_clean_exit` appears for `opentype-font`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
- Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- The carrier is a complete OpenType font. The sfnt directory, table records, and GSUB/GPOS lookup structures must remain coherent enough for HarfBuzz to instantiate a face and walk context lookup subtables. Appended trailing bytes are tolerated as extra font data.
- Harness: The subset fuzzer treats the full input as an hb_blob font. For sufficiently large inputs, trailing data can also provide subset flags and UTF-32 codepoints, read from the end of the same buffer, but there is no external file or leading selector.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed persistent failure from round 16.
- Scope: generator avoidance for the same failure-keyed basin.
