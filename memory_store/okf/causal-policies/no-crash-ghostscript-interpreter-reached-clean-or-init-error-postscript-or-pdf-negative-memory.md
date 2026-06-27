---
type: causal-policy
title: "No Crash Ghostscript Interpreter Reached Clean Or Init Error Postscript Or PDF Negative Memory"
description: "Round 9 negative memory for no_crash with verifier signal ghostscript_interpreter_reached_clean_or_init_error."
failure_class: "no_crash"
verifier_signal: "ghostscript_interpreter_reached_clean_or_init_error"
candidate_family: "construct-postscript"
input_format: "postscript-or-pdf"
harness_convention: "libfuzzer"
vuln_class: "division-by-zero-leading-to-copy-mono-overflow"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "ghostscript-interpreter-reached-clean-or-init-error", "postscript-or-pdf", "negative-memory", "round-9"]
match_keys: ["no_crash", "ghostscript_interpreter_reached_clean_or_init_error", "postscript-or-pdf", "libfuzzer", "division-by-zero-leading-to-copy-mono-overflow", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 9
---
# No Crash Ghostscript Interpreter Reached Clean Or Init Error Postscript Or PDF Negative Memory

- key: `no_crash x ghostscript_interpreter_reached_clean_or_init_error`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[postscript-or-pdf]]
- related harness facts: [[libfuzzer]]

## Failure Shape
- Compact PostScript pattern and zero-matrix image attempts either failed Ghostscript initialization
  or rendered cleanly.
- The missing invariant is a valid tiling or image path that creates NaN phase values and still
  reaches copy_mono fitting on the raster device.

## Policy
Treat `no_crash x ghostscript_interpreter_reached_clean_or_init_error` on `postscript-or-pdf` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
- Ghostscript accepts raw PostScript or PDF on this harness.
- Pattern dictionaries need coherent PatternType, PaintType, TilingType, BBox, step values, matrix,
  and PaintProc entries to reach tiling.
- Image dictionaries need coherent dimensions, bits per component, image matrix, decode array, and
  data source.

## Harness Contract
- The gstoraster fuzzer passes raw stdin-style document bytes into Ghostscript with a cups raster-
  oriented invocation.
- There is no carved header; Ghostscript language detection and document syntax select the parser.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `ghostscript_interpreter_reached_clean_or_init_error`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 9.
- Scope: generator repair and basin avoidance only.
