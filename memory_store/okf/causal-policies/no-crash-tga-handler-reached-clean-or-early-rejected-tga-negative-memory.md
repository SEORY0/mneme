---
type: causal-policy
title: "No Crash TGA Handler Reached Clean Or Early Rejected TGA Negative Memory"
description: "Round 16 negative memory for no_crash with verifier signal tga_handler_reached_clean_or_early_rejected."
failure_class: "no_crash"
verifier_signal: "tga_handler_reached_clean_or_early_rejected"
candidate_family: "construct_then_seed_truncate"
input_format: "tga"
harness_convention: "afl-style raw stdin image fuzzer"
vuln_class: "unknown-error-handling-memory-corruption"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "tga-handler-reached-clean-or-early-rejected", "tga", "negative-memory", "round-16"]
match_keys: ["no_crash", "tga_handler_reached_clean_or_early_rejected", "tga", "afl-style raw stdin image fuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 16
---
# No Crash TGA Handler Reached Clean Or Early Rejected TGA Negative Memory

## Policy
For `no_crash x tga_handler_reached_clean_or_early_rejected`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
- Minimal and seed-truncated TGA candidates reached the multi-handler image fuzzer but stayed on clean rejection paths. Truncating raw, palette, and RLE bodies did not produce the readRawData error return needed by the vulnerable memset path.
- When `no_crash x tga_handler_reached_clean_or_early_rejected` appears for `tga`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
- Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- TGA inputs use an eighteen-byte little-endian header with image type, optional palette descriptor, dimensions, pixel depth, and descriptor flags. The handler seeks past the image ID, validates supported image type, palette constraints, dimensions, and pixel depth, then reads palette, RLE packets, or raw pixel data according to the type.
- Harness: The kimageformats harness feeds the same raw input bytes through several QImageIOHandler implementations using a QBuffer; no filename extension or outer container is provided. A valid TGA header must survive other handlers and the TGA support checks before pixel data is read.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed persistent failure from round 16.
- Scope: generator avoidance for the same failure-keyed basin.
