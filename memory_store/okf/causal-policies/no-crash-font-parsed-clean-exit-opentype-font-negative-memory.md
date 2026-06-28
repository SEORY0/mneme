---
type: causal-policy
title: "No Crash Font Parsed Clean Exit Opentype Font Negative Memory"
description: "Round 12 negative memory for no_crash with verifier signal font_parsed_clean_exit."
failure_class: "no_crash"
verifier_signal: "font_parsed_clean_exit"
candidate_family: "seed_mutate"
input_format: "opentype-font"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "font-parsed-clean-exit", "opentype-font", "negative-memory", "round-12"]
match_keys: ["no_crash", "font_parsed_clean_exit", "opentype-font", "libfuzzer", "heap-buffer-overflow-read", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 12
---
# No Crash Font Parsed Clean Exit Opentype Font Negative Memory

- key: `no_crash x font_parsed_clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[opentype-font]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Valid OpenType/TrueType seeds reached the HarfBuzz font parser and subsetter but did not trigger the ArrayOf memory-barrier issue. No table mutation tested produced a stable crash before the round budget moved on.

## Policy
Treat `no_crash x font_parsed_clean_exit` on `opentype-font` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
The input is a complete OpenType/TrueType font blob with normal table-directory structure. The relevant vulnerable family is used by array-like table records whose first element can be accessed after reading the array length.

## Harness Contract
The HarfBuzz subset fuzzer treats the whole input as a font blob, creates a face, gathers Unicode coverage, and runs subsetting. For larger inputs, trailing bytes can influence subset text and flags, but there is no external wrapper format.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `font_parsed_clean_exit`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 12.
- Scope: generator repair and basin avoidance only.
