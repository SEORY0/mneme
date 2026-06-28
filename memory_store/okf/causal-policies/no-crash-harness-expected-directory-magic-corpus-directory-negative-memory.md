---
type: causal-policy
title: "No Crash Harness Expected Directory Magic Corpus Directory Negative Memory"
description: "Round 10 negative memory for no_crash with verifier signal harness_expected_directory."
failure_class: "no_crash"
verifier_signal: "harness_expected_directory"
candidate_family: "construct_elf_stub"
input_format: "file-magic corpus-directory"
harness_convention: "afl-wrapper"
vuln_class: "pointer-overflow-undefined-behavior"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "harness-expected-directory", "negative-memory", "round-10"]
match_keys: ["no_crash", "harness_expected_directory", "file-magic corpus-directory", "afl-wrapper", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 10
---
# No Crash Harness Expected Directory Magic Corpus Directory Negative Memory

## Policy
For `no_crash x harness_expected_directory`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
1. The selected wrapper reported that the supplied path needed to be a directory, so the single-file candidate did not exercise the vulnerable file magic path.
2. When `no_crash x harness_expected_directory` appears for `file-magic corpus-directory`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
3. Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- The visible source includes a libmagic fuzz entry that can consume raw buffers, but the selected runtime wrapper did not run that entry as a single-file raw-buffer target. File-magic offset arithmetic bugs require a magic rule path that computes derived offsets from matched input.
- Harness: The verifier output indicated a required directory path instead of a normal libFuzzer single input file. No FuzzedDataProvider layout was observed; the blocker was the wrapper invocation contract.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed round-10 persistent failure.
- Scope: generator avoidance for the same failure-keyed basin.
