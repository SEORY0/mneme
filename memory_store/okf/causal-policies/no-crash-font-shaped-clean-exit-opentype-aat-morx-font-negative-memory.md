---
type: causal-policy
title: "No Crash Font Shaped Clean Exit Opentype Aat Morx Font Negative Memory"
description: "Round 10 negative memory for no_crash with verifier signal font_shaped_clean_exit."
failure_class: "no_crash"
verifier_signal: "font_shaped_clean_exit"
candidate_family: "seed_mutate"
input_format: "opentype-aat-morx-font"
harness_convention: "libfuzzer"
vuln_class: "invalid-memory-access"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "font-shaped-clean-exit", "negative-memory", "round-10"]
match_keys: ["no_crash", "font_shaped_clean_exit", "opentype-aat-morx-font", "libfuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 10
---
# No Crash Font Shaped Clean Exit Opentype Aat Morx Font Negative Memory

## Policy
For `no_crash x font_shaped_clean_exit`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
1. A real AAT morx seed shaped successfully after contextual subtable offset mutation, but the mutated relation was sanitized or did not select an actionable contextual entry.
2. When `no_crash x font_shaped_clean_exit` appears for `opentype-aat-morx-font`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
3. Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- AAT morx fonts are ordinary sfnt fonts with a table directory and a morx table containing chains, subtables, state tables, entries, and substitution table references. Contextual subtables require both a valid state machine and glyph text that drives an entry using mark or current substitution indices.
- Harness: The active binary was the HarfBuzz shape fuzzer. It consumes the entire file as an hb_blob, creates an hb_face and hb_font, shapes fixed ASCII text, then reuses trailing input bytes as UTF-32 text for a second shaping pass. There is no external wrapper or checksum.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed round-10 persistent failure.
- Scope: generator avoidance for the same failure-keyed basin.
