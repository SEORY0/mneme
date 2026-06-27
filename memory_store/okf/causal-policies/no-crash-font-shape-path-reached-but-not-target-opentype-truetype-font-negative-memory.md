---
type: causal-policy
title: "No Crash Font Shape Path Reached But Not Target Opentype Truetype Font Negative Memory"
description: "Round 10 negative memory for no_crash with verifier signal font_shape_path_reached_but_not_target."
failure_class: "no_crash"
verifier_signal: "font_shape_path_reached_but_not_target"
candidate_family: "seed_mutate"
input_format: "OpenType/TrueType font"
harness_convention: "libfuzzer HarfBuzz shape fuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "font-shape-path-reached-but-not-target", "negative-memory", "round-10"]
match_keys: ["no_crash", "font_shape_path_reached_but_not_target", "OpenType/TrueType font", "libfuzzer HarfBuzz shape fuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 10
---
# No Crash Font Shape Path Reached But Not Target Opentype Truetype Font Negative Memory

## Policy
For `no_crash x font_shape_path_reached_but_not_target`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
1. Valid font seeds with suffix-controlled shaping data reached the HarfBuzz shape harness.
2. When `no_crash x font_shape_path_reached_but_not_target` appears for `OpenType/TrueType font`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
3. Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- The input is an sfnt font blob with table directory and glyf/loca/hmtx relationships preserved. Appended bytes can influence fuzzer-controlled shaping text or variation coordinates, but corrupting top-level table structure usually prevents the glyf path from being useful.
- Harness: The harness treats the buffer as a font blob, creates a face/font, derives some shaping parameters from available bytes, and runs shape tests over fixed text. There is no file container or leading mode byte.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed round-10 persistent failure.
- Scope: generator avoidance for the same failure-keyed basin.
