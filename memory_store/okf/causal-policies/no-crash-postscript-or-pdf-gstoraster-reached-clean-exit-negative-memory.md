---
type: causal-policy
title: "No Crash Postscript Or Pdf Gstoraster Reached Clean Exit Negative Memory"
description: "Negative memory for no_crash with gstoraster_reached_clean_exit on postscript-or-pdf inputs."
failure_class: no_crash
verifier_signal: gstoraster_reached_clean_exit
candidate_family: construct
input_format: postscript-or-pdf
harness_convention: libfuzzer-gstoraster
vuln_class: buffer-overflow-write
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, gstoraster-reached-clean-exit, postscript-or-pdf, buffer-overflow-write, negative_memory]
match_keys: [no-crash, gstoraster-reached-clean-exit, postscript-or-pdf, buffer-overflow-write]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# No Crash Postscript Or Pdf Gstoraster Reached Clean Exit Negative Memory

- key: `no_crash x gstoraster_reached_clean_exit`
- outcome: persistent failure basin
- success_count: 0
- failure_count: 1
- formats: [[postscript-or-pdf]]

## Dead End
A valid PostScript probe reached the gstoraster interpreter but did not enable or hit the debug-message buffer copy path. The missing condition is likely a specific debug channel or interpreter feature that emits the vulnerable diagnostic message.

## Avoid
Do not repeat the same candidate family when the verifier signal matches this key. Treat broad seed mutation, wrapper usage paths, both-image crashes, parser-clean exits, or local-only crashes as evidence that the current surface is not the target differential.

## Recovery Direction
Preserve only independently validated format or harness reachability facts. Re-enter generation by first satisfying the harness contract and the earliest format gate, then use a different target-specific invariant instead of enlarging or randomly mutating the failed family.
