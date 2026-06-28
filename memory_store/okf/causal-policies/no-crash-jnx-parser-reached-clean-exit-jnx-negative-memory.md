---
type: causal-policy
title: "No Crash JNX Parser Reached Clean Exit JNX Negative Memory"
description: "Round 16 negative memory for no_crash with verifier signal jnx_parser_reached_clean_exit."
failure_class: "no_crash"
verifier_signal: "jnx_parser_reached_clean_exit"
candidate_family: "seed_mutate"
input_format: "jnx"
harness_convention: "libfuzzer-graphicsmagick-coder"
vuln_class: "decoder-selection-confusion"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "jnx-parser-reached-clean-exit", "jnx", "negative-memory", "round-16"]
match_keys: ["no_crash", "jnx_parser_reached_clean_exit", "jnx", "libfuzzer-graphicsmagick-coder", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 16
---
# No Crash JNX Parser Reached Clean Exit JNX Negative Memory

## Policy
For `no_crash x jnx_parser_reached_clean_exit`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
- A real JNX fixture reached the selected coder, and mutations changed embedded tile payload class, nested-container shape, and short JPEG marker relations while preserving the outer level and tile tables. All candidates exited cleanly, so the missing condition is the exact decoder-selection state that makes the embedded tile bypass forced JPEG handling and enter a vulnerable secondary reader.
- When `no_crash x jnx_parser_reached_clean_exit` appears for `jnx`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
- Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- JNX is a little-endian tiled raster container with a fixed header, a bounded level table, per-level tile records, and tile payloads addressed by size and file position. Version-three level records are compact fixed-size records; tile records carry bounds, dimensions, payload size, and payload position. The reader prepends a JPEG start marker before handing each tile blob to the generic image loader.
- Harness: The GraphicsMagick coder fuzzer supplies the whole file as raw JNX bytes to the selected JNX reader. There is no fuzzer-side selector, checksum gate, or FuzzedDataProvider carving.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed persistent failure from round 16.
- Scope: generator avoidance for the same failure-keyed basin.
