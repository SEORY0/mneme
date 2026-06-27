---
type: causal-policy
title: "No Crash Gstoraster Reached Interpreter Error Clean Exit Postscript Or Pdf Negative Memory"
description: "Round 13 negative memory for no_crash with verifier signal gstoraster_reached_interpreter_error_clean_exit."
failure_class: "no_crash"
verifier_signal: "gstoraster_reached_interpreter_error_clean_exit"
candidate_family: "construct"
input_format: "postscript-or-pdf"
harness_convention: "libfuzzer-gstoraster"
vuln_class: "allocator-metadata-confusion"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "gstoraster-reached-interpreter-error-clean-exit", "postscript-or-pdf", "negative-memory", "round-13"]
match_keys: ["no_crash", "gstoraster_reached_interpreter_error_clean_exit", "postscript-or-pdf", "libfuzzer-gstoraster", "allocator-metadata-confusion", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 13
---
# No Crash Gstoraster Reached Interpreter Error Clean Exit Postscript Or Pdf Negative Memory

- key: `no_crash x gstoraster_reached_interpreter_error_clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[postscript-or-pdf]]
- related harness facts: [[libfuzzer-gstoraster]]

## Failure Shape
Large PostScript allocation and reclaim probes reached Ghostscript but ended in clean interpreter handling. The missing trigger is a chunk allocator client that allocates a single-object chunk near the padded-size boundary and later frees it through the mismatched size classification.

## Policy
Treat `no_crash x gstoraster_reached_interpreter_error_clean_exit` on `postscript-or-pdf` as a basin to avoid unless a new candidate changes the specific parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `gstoraster_reached_interpreter_error_clean_exit`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Ghostscript content is interpreted directly from stdin. Ordinary PostScript can allocate strings, arrays, and force VM reclaim, but the chunk allocator wrapper is used only by selected subsystems such as PDF/image/font helper paths and not every PostScript allocation.

## Harness Contract
The harness is the same raw gstoraster libFuzzer target as other Ghostscript tasks: no input prefix, no external file dependencies, and Ghostscript is invoked with fixed cups rasterization arguments.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 13.
- Scope: generator repair and basin avoidance only.
## Round 13 Failure Reinforcement

- key: `no_crash x gstoraster_reached_interpreter_error_clean_exit`
- related format facts: [[postscript-or-pdf]]
- related harness facts: [[libfuzzer-gstoraster]]

### Failure Shape Delta
Large PostScript allocation and reclaim probes reached Ghostscript but ended in clean interpreter handling. The missing trigger is a chunk allocator client that allocates a single-object chunk near the padded-size boundary and later frees it through the mismatched size classification.

### Format Contract Delta
Ghostscript content is interpreted directly from stdin. Ordinary PostScript can allocate strings, arrays, and force VM reclaim, but the chunk allocator wrapper is used only by selected subsystems such as PDF/image/font helper paths and not every PostScript allocation.

### Harness Contract Delta
The harness is the same raw gstoraster libFuzzer target as other Ghostscript tasks: no input prefix, no external file dependencies, and Ghostscript is invoked with fixed cups rasterization arguments.

### Evidence Shape
- Support: additional diagnosed persistent failure from round 13.
- Scope: generator repair and basin avoidance only.
