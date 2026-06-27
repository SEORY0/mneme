---
type: causal-policy
title: "No Crash Parser Reached No Target Crash Libidn2 Domain Uint32 Codepoints Negative Memory"
description: "Round 10 negative memory for no_crash with verifier signal parser_reached_no_target_crash."
failure_class: "no_crash"
verifier_signal: "parser_reached_no_target_crash"
candidate_family: "construct"
input_format: "libidn2-raw-domain-or-uint32-codepoints"
harness_convention: "libfuzzer"
vuln_class: "stack-buffer-overflow-write"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-reached-no-target-crash", "negative-memory", "round-10"]
match_keys: ["no_crash", "parser_reached_no_target_crash", "libidn2-raw-domain-or-uint32-codepoints", "libfuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 10
---
# No Crash Parser Reached No Target Crash Libidn2 Domain Uint32 Codepoints Negative Memory

## Policy
For `no_crash x parser_reached_no_target_crash`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
1. The raw fuzzer accepted the size-gated inputs but the tested ASCII, Latin, Arabic, CJK, and mixed codepoint families either did not pass IDNA lookup successfully or did not produce a sanitizer-visible copy beyond the fixed output buffer.
2. When `no_crash x parser_reached_no_target_crash` appears for `libidn2-raw-domain-or-uint32-codepoints`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
3. Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- The fuzzer treats raw bytes both as nul-terminated byte strings and, when the total length is word-aligned, as a sequence of native-endian Unicode codepoints for the 4i conversion API. The target copy occurs only after lookup succeeds and returns an ASCII-compatible domain string.
- Harness: The libFuzzer input is raw bytes with a maximum-size gate. The 4i path is enabled only for word-aligned input; fields are consumed from the front with no file wrapper, checksum, or magic.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed round-10 persistent failure.
- Scope: generator avoidance for the same failure-keyed basin.
