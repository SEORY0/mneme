---
type: causal-policy
title: "No Crash Magic Buffer Clean Exit Magic Negative Memory"
description: "Round 10 negative memory for no_crash with verifier signal magic_buffer_clean_exit."
failure_class: "no_crash"
verifier_signal: "magic_buffer_clean_exit"
candidate_family: "construct_text_magic"
input_format: "file-magic raw buffer"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "magic-buffer-clean-exit", "negative-memory", "round-10"]
match_keys: ["no_crash", "magic_buffer_clean_exit", "file-magic raw buffer", "libfuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 10
---
# No Crash Magic Buffer Clean Exit Magic Negative Memory

## Policy
For `no_crash x magic_buffer_clean_exit`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
1. A text-like raw buffer reached the file magic harness but did not select a regex magic rule that makes the wrapped regexec result expose an uninitialized match structure.
2. When `no_crash x magic_buffer_clean_exit` appears for `file-magic raw buffer`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
3. Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- The input is passed as raw bytes to libmagic through magic_buffer. The format is not a normal file container; parser selection depends on matching compiled magic rules, including search and regex rule types.
- Harness: The libFuzzer entry rejects only empty input, then calls magic_buffer on the entire byte string. There is no mode byte, file path, FuzzedDataProvider layout, or checksum gate.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed round-10 persistent failure.
- Scope: generator avoidance for the same failure-keyed basin.
