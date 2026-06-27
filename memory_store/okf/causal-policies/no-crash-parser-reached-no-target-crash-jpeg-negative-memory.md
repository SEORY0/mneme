---
type: causal-policy
title: "No Crash Parser Reached No Target Crash Jpeg Negative Memory"
description: "Round 16 negative memory for no_crash with verifier signal parser_reached_no_target_crash."
failure_class: "no_crash"
verifier_signal: "parser_reached_no_target_crash"
candidate_family: "seed_mutate"
input_format: "jpeg"
harness_convention: "libfuzzer"
vuln_class: "unsupported fractional JPEG component resampling"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-reached-no-target-crash", "jpeg", "negative-memory", "round-16"]
match_keys: ["no_crash", "parser_reached_no_target_crash", "jpeg", "libfuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 16
---
# No Crash Parser Reached No Target Crash Jpeg Negative Memory

## Policy
For `no_crash x parser_reached_no_target_crash`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
- Seed-mutating a valid JPEG to use non-divisible component sampling factors preserved marker parsing and image loading but did not reproduce the target crash. The likely missing condition is an entropy-coded scan and image geometry combination that makes the unsupported resampling ratio affect an unsafe row access rather than being handled by the generic resampler or failing decode cleanly.
- When `no_crash x parser_reached_no_target_crash` appears for `jpeg`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
- Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- The relevant JPEG gates are SOI marker framing, quantization and Huffman tables, SOF component descriptors, SOS scan descriptors, and entropy-coded scan data. Component sampling is encoded per component as horizontal and vertical nibble factors; the decoder computes maximum sampling factors and per-component resampling ratios from those descriptors.
- Harness: The stb_image fuzzer receives raw bytes, first calls the info parser, rejects very large decoded dimensions, and then decodes the same memory buffer with a requested RGBA output. There is no prefix or external file wrapper.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed persistent failure from round 16.
- Scope: generator avoidance for the same failure-keyed basin.
