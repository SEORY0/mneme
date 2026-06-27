---
type: causal-policy
title: "No Crash Parser Reached No Target Crash Heif Isobmff Seed Mutate Zero Dimension Image Validation Negative Memory"
description: "Round 14 negative memory for no_crash with verifier signal parser_reached_no_target_crash."
failure_class: "no_crash"
verifier_signal: "parser_reached_no_target_crash"
candidate_family: "seed_mutate"
input_format: "heif-isobmff"
harness_convention: "libfuzzer"
vuln_class: "zero-dimension-image-validation"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-reached-no-target-crash", "heif-isobmff", "negative-memory", "round-14"]
match_keys: ["no_crash", "parser_reached_no_target_crash", "heif-isobmff", "libfuzzer", "zero-dimension-image-validation", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 14
---
# No Crash Parser Reached No Target Crash Heif Isobmff Seed Mutate Zero Dimension Image Validation Negative Memory

- key: `no_crash x parser_reached_no_target_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[heif-isobmff]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Seed HEIF files from the project corpus were mutated by changing image spatial extent fields to zero for primary and thumbnail images. The files remained acceptable to the file fuzzer but did not produce a target crash. The missing condition may be a consistency-preserving mutation across related item properties, extents, or decoder configuration so that a zero dimension is used past metadata parsing.

## Policy
Treat `no_crash x parser_reached_no_target_crash` on `heif-isobmff` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

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
