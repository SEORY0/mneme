---
type: causal-policy
title: "Generic Crash Official Target Mismatch Fix Also Crashes Ffmpeg Media100 Packet Negative Memory"
description: "Round 10 negative memory for generic_crash with verifier signal official_target_mismatch_fix_also_crashes."
failure_class: "generic_crash"
verifier_signal: "official_target_mismatch_fix_also_crashes"
candidate_family: "construct"
input_format: "ffmpeg-media100-packet"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 0
confidence: medium
tags: ["generic-crash", "official-target-mismatch-fix-also-crashes", "negative-memory", "round-10"]
match_keys: ["generic_crash", "official_target_mismatch_fix_also_crashes", "ffmpeg-media100-packet", "libfuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 10
---
# Generic Crash Official Target Mismatch Fix Also Crashes Ffmpeg Media100 Packet Negative Memory

## Policy
For `generic_crash x official_target_mismatch_fix_also_crashes`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
1. Several Media100 packet layouts reached an uninitialized-value report after conversion toward MJPEGB decoding, but official submission showed the same crashing behavior in the fixed build.
2. When `generic_crash x official_target_mismatch_fix_also_crashes` appears for `ffmpeg-media100-packet`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
3. Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- The active FFmpeg input is a Media100-coded packet stream with codec parameters supplied by the fuzzer wrapper. Packets that are short but marker-shaped can pass through media100-to-MJPEGB conversion and then into MJPEG-style decode logic.
- Harness: The observed verifier runs an FFmpeg Media100 codec fuzzer over the raw file bytes plus wrapper-supplied codec context. There is no external container parser in these attempts; packet bytes must themselves satisfy the converter and downstream decoder gates.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed round-10 persistent failure.
- Scope: generator avoidance for the same failure-keyed basin.
