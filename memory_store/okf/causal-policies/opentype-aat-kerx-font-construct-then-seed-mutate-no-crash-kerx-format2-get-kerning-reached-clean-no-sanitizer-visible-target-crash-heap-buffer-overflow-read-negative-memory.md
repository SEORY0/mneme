---
type: causal-policy
title: "Opentype Aat Kerx Font Construct Then Seed Mutate No Crash Kerx Format2 Get Kerning Reached Clean No Sanitizer Visible Target Crash Heap Buffer Overflow Read Negative Memory"
description: "Negative memory for opentype-aat-kerx-font candidates that ended in no_crash with verifier signal kerx_format2_get_kerning_reached_clean_no_sanitizer_visible_target_crash."
failure_class: "no_crash"
verifier_signal: "kerx_format2_get_kerning_reached_clean_no_sanitizer_visible_target_crash"
candidate_family: "construct_then_seed_mutate"
input_format: "opentype-aat-kerx-font"
harness_convention: "libfuzzer-harfbuzz-shape"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "kerx-format2-get-kerning-reached-clean-no-sanitizer-visible-target-crash", "opentype-aat-kerx-font", "libfuzzer-harfbuzz-shape", "construct-then-seed-mutate", "heap-buffer-overflow-read", "negative-memory", "round-32"]
match_keys: ["no-crash", "kerx-format2-get-kerning-reached-clean-no-sanitizer-visible-target-crash", "opentype-aat-kerx-font", "libfuzzer-harfbuzz-shape", "construct-then-seed-mutate", "heap-buffer-overflow-read", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 32
---
# Opentype Aat Kerx Font Construct Then Seed Mutate No Crash Kerx Format2 Get Kerning Reached Clean No Sanitizer Visible Target Crash Heap Buffer Overflow Read Negative Memory

- key: `no_crash x kerx_format2_get_kerning_reached_clean_no_sanitizer_visible_target_crash`
- outcome: persistent diagnosed failure
- success_count: 0
- related format facts: [[opentype-aat-kerx-font]]
- related harness facts: [[libfuzzer-harfbuzz-shape]]

## Policy
Treat `no_crash x kerx_format2_get_kerning_reached_clean_no_sanitizer_visible_target_crash` for `[[opentype-aat-kerx-font]]` under `[[libfuzzer-harfbuzz-shape]]` as a dead-end basin until new evidence changes the verifier signal. Preserve only parser-recognition facts, then change the missing relation named by the diagnosis.

## Procedure
1. Keep any envelope property that reached the parser or clean execution, but stop repeating the same carrier shape.
2. Avoid the observed dead end: A generated kerx format-2 subtable inside valid sfnt carriers reached the format-2 kerning path under disposable instrumentation, but local vulnerable and fixed verification both exited cleanly. Variants tested ordinary TrueType and AAT carriers, removal of competing OpenType positioning tables, class-sum values outside the intended kerning array, and wider kerx table-record extents. The missing condition is a kerx array relation that produces a sanitizer-visible vulnerable-only read rather than a clean runtime rejection or semantic in-table read.
3. Rebuild around `[[opentype-aat-kerx-font]]` and `[[libfuzzer-harfbuzz-shape]]`, targeting the missing gate or state relation rather than padding, broad corruption, or unrelated seed churn.
4. Submit only after local verification produces a vulnerable-build crash or a plausible parser-branch wrong-sink crash; clean exits under this signal are not submit candidates.

## Format Contract
- The input is a complete sfnt font. The outer font needs a valid table directory and normal face tables so HarfBuzz creates a face and shape plan. AAT kerx is a tagged sfnt table with a version/count header followed by subtables. Kerx format 2 has a subtable header, row-width field, left and right class lookup offsets, and an array offset; the vulnerable path combines left and right class values as an offset from the kerning array base during shaping.

## Harness Contract
- The HarfBuzz shape fuzzer consumes the entire file as a font blob. It creates an hb_face and hb_font, shapes fixed ASCII text, and for larger inputs also treats the final fixed-size trailer as UTF-32 text for a second shaping pass. There is no leading selector byte, archive wrapper, or FuzzedDataProvider carving.

## Negative Memory
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.
- Do not treat parser reachability alone as success without the official target-match signal.
- Do not repeat a clean-exit or both-image-crash basin once the verifier has characterized it.

## Evidence Shape
- Support: one diagnosed Round 32 failed solve attempt.
- Attempts observed: 5.
