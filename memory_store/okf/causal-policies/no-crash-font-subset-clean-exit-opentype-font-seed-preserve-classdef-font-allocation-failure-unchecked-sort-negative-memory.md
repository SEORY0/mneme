---
type: causal-policy
title: "No Crash Font Subset Clean Exit Opentype Font Seed Preserve Classdef Font Allocation Failure Unchecked Sort Negative Memory"
description: "Round 14 negative memory for no_crash with verifier signal font_subset_clean_exit."
failure_class: "no_crash"
verifier_signal: "font_subset_clean_exit"
candidate_family: "seed_preserve_classdef_font"
input_format: "opentype-font"
harness_convention: "libfuzzer-harfbuzz-subset"
vuln_class: "allocation-failure-unchecked-sort"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "font-subset-clean-exit", "opentype-font", "negative-memory", "round-14"]
match_keys: ["no_crash", "font_subset_clean_exit", "opentype-font", "libfuzzer-harfbuzz-subset", "allocation-failure-unchecked-sort", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 14
---
# No Crash Font Subset Clean Exit Opentype Font Seed Preserve Classdef Font Allocation Failure Unchecked Sort Negative Memory

- key: `no_crash x font_subset_clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[opentype-font]]
- related harness facts: [[libfuzzer-harfbuzz-subset]]

## Failure Shape
A repo ClassDef-focused OpenType seed reached the subset fuzzer without failure. Triggering the target likely requires mutating a ClassDef table count/range so allocation fails or returns null while the later qsort path still sees a nonzero class array.

## Policy
Treat `no_crash x font_subset_clean_exit` on `opentype-font` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest carrier that the verifier proved reaches the parser, decoder, or harness path.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, parser-not-reached, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not count parser reachability, local crashes, clean exits, fixed-image crashes, usage banners, or sink mismatches as success.
- Do not repeat this candidate family unless the new attempt changes the causal gate named above.
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from Round 14.
- Scope: generator repair and basin avoidance only.
