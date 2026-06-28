---
type: negative-memory
title: "No Crash Small Precision Clean Large Precision Both Image Oom Mruby Source Construct Buffer Overflow Or Allocation Overrun Negative Memory"
description: "Round 25 negative memory for no_crash with verifier signal small_precision_clean_large_precision_both_image_oom."
failure_class: "no_crash"
verifier_signal: "small_precision_clean_large_precision_both_image_oom"
candidate_family: "construct"
input_format: "mruby-source"
harness_convention: "libfuzzer"
vuln_class: "buffer-overflow-or-allocation-overrun"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "small-precision-clean-large-precision-both-image-oom", "mruby-source", "libfuzzer", "construct", "negative-memory", "round-25"]
match_keys: ["no_crash", "small_precision_clean_large_precision_both_image_oom", "mruby-source", "libfuzzer", "buffer-overflow-or-allocation-overrun", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 25
---
# No Crash Small Precision Clean Large Precision Both Image Oom Mruby Source Construct Buffer Overflow Or Allocation Overrun Negative Memory

- key: `no_crash x small_precision_clean_large_precision_both_image_oom`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[mruby-source]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Raw mruby source reached runtime sprintf formatting. Small over-boundary float precisions executed cleanly, while extremely large precision values caused both vulnerable and fixed images to abort through allocator limits, so they are not scoring PoCs. The likely missing relation is a precision/format combination that reaches fmt_fp's stack formatting path without expanding the destination string into the allocator-failure basin.

## Policy
Treat `no_crash x small_precision_clean_large_precision_both_image_oom` on `mruby-source` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, wrapper-mismatch, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `small_precision_clean_large_precision_both_image_oom` basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `small_precision_clean_large_precision_both_image_oom`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
The input is ordinary mruby source text. sprintf format strings are parsed at runtime; width and precision can be literal decimal fields or supplied by star arguments. Float conversions flow through the mruby sprintf implementation into floating-point formatting helpers.

## Harness Contract
The harness copies the entire input to a newly NUL-terminated string, opens an mruby VM, loads and executes the source, then closes the VM. There is no file header, selector byte, or provider carving.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 25 after 16 attempts.
- Scope: generator repair and basin avoidance only.
