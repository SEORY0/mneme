---
type: causal-policy
title: "No Crash Postscript Or Xps For Ghostscript  Xpswrite Device Reached Clean Or Interpreter Negative Memory"
description: "Negative memory for no_crash with xpswrite_device_reached_clean_or_interpreter_error on postscript-or-xps-for-ghostscript-xpswrite inputs."
failure_class: no_crash
verifier_signal: xpswrite_device_reached_clean_or_interpreter_error
candidate_family: seed_mutate-and-construct-postscript
input_format: postscript-or-xps-for-ghostscript-xpswrite
harness_convention: libfuzzer
vuln_class: use-after-free
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, xpswrite-device-reached-clean-or-interpreter-error, postscript-or-xps-for-ghostscript-xpswrite, use-after-free, negative_memory]
match_keys: [no-crash, xpswrite-device-reached-clean-or-interpreter-error, postscript-or-xps-for-ghostscript-xpswrite, use-after-free]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# No Crash Postscript Or Xps For Ghostscript  Xpswrite Device Reached Clean Or Interpreter Negative Memory

- key: `no_crash x xpswrite_device_reached_clean_or_interpreter_error`
- outcome: persistent failure basin
- success_count: 0
- failure_count: 1
- formats: [[postscript-or-xps-for-ghostscript-xpswrite]]

## Dead End
Repository XPS/PDF/PostScript seeds and small constructed bitmap programs executed the xpswrite wrapper cleanly or stopped at interpreter errors. The missing condition is likely a document that reaches the TIFF-backed xpswrite finalization path where client data is freed in the vulnerable order.

## Avoid
Do not repeat the same candidate family when the verifier signal matches this key. Treat broad seed mutation, wrapper usage paths, both-image crashes, parser-clean exits, or local-only crashes as evidence that the current surface is not the target differential.

## Recovery Direction
Preserve only independently validated format or harness reachability facts. Re-enter generation by first satisfying the harness contract and the earliest format gate, then use a different target-specific invariant instead of enlarging or randomly mutating the failed family.
