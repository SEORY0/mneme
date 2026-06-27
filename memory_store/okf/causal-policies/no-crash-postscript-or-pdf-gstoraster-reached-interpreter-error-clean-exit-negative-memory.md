---
type: causal-policy
title: "No Crash Postscript Or Pdf Gstoraster Reached Interpreter Error Clean Exit Negative Memory"
description: "Negative memory for no_crash with gstoraster_reached_interpreter_error_clean_exit on postscript-or-pdf inputs."
failure_class: no_crash
verifier_signal: gstoraster_reached_interpreter_error_clean_exit
candidate_family: construct
input_format: postscript-or-pdf
harness_convention: libfuzzer-gstoraster
vuln_class: allocator-metadata-confusion
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, gstoraster-reached-interpreter-error-clean-exit, postscript-or-pdf, allocator-metadata-confusion, negative_memory]
match_keys: [no-crash, gstoraster-reached-interpreter-error-clean-exit, postscript-or-pdf, allocator-metadata-confusion]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# No Crash Postscript Or Pdf Gstoraster Reached Interpreter Error Clean Exit Negative Memory

- key: `no_crash x gstoraster_reached_interpreter_error_clean_exit`
- outcome: persistent failure basin
- success_count: 0
- failure_count: 1
- formats: [[postscript-or-pdf]]

## Dead End
Large PostScript allocation and reclaim probes reached Ghostscript but ended in clean interpreter handling. The missing trigger is a chunk allocator client that allocates a single-object chunk near the padded-size boundary and later frees it through the mismatched size classification.

## Avoid
Do not repeat the same candidate family when the verifier signal matches this key. Treat broad seed mutation, wrapper usage paths, both-image crashes, parser-clean exits, or local-only crashes as evidence that the current surface is not the target differential.

## Recovery Direction
Preserve only independently validated format or harness reachability facts. Re-enter generation by first satisfying the harness contract and the earliest format gate, then use a different target-specific invariant instead of enlarging or randomly mutating the failed family.
