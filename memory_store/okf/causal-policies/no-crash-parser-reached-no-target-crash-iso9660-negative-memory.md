---
type: causal-policy
title: "No Crash Parser Reached No Target Crash Iso9660 Negative Memory"
description: "Round 10 negative memory for no_crash with verifier signal parser_reached_no_target_crash."
failure_class: "no_crash"
verifier_signal: "parser_reached_no_target_crash"
candidate_family: "seed_mutate"
input_format: "iso9660"
harness_convention: "libfuzzer-libarchive"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-reached-no-target-crash", "negative-memory", "round-10"]
match_keys: ["no_crash", "parser_reached_no_target_crash", "iso9660", "libfuzzer-libarchive", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 10
---
# No Crash Parser Reached No Target Crash Iso9660 Negative Memory

## Policy
For `no_crash x parser_reached_no_target_crash`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
1. A decoded ISO regression seed and mutations to logical block size, root directory extent, and root directory size all reached libarchive without a sanitizer-visible overread.
2. When `no_crash x parser_reached_no_target_crash` appears for `iso9660`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
3. Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- ISO9660 images contain volume descriptors after the reserved system area, a primary volume descriptor with both-endian logical block size and volume size fields, and a root directory record that points to directory extents made of length-prefixed records terminated by zero padding.
- Harness: The libarchive fuzzer feeds the raw input as an archive byte stream with all read formats enabled. A candidate must be a whole ISO image; the parser performs archive format detection before reaching ISO directory traversal.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed round-10 persistent failure.
- Scope: generator avoidance for the same failure-keyed basin.
