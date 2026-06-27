---
type: causal-policy
title: "No Crash Dpx Image Dpx Parser Processed Cleanly Negative Memory"
description: "Negative memory for no_crash with dpx_parser_processed_cleanly on dpx-image inputs."
failure_class: no_crash
verifier_signal: dpx_parser_processed_cleanly
candidate_family: seed_mutate
input_format: dpx-image
harness_convention: afl-libfuzzer
vuln_class: incorrect-validation
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, dpx-parser-processed-cleanly, dpx-image, incorrect-validation, negative_memory]
match_keys: [no-crash, dpx-parser-processed-cleanly, dpx-image, incorrect-validation]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# No Crash Dpx Image Dpx Parser Processed Cleanly Negative Memory

- key: `no_crash x dpx_parser_processed_cleanly`
- outcome: persistent failure basin
- success_count: 0
- failure_count: 1
- formats: [[dpx-image]]

## Dead End
Repository DPX seeds with odd image widths and descriptor mutations to the CbCr family still processed cleanly. The missing trigger may require a DPX sample whose element packing, transfer characteristics, and pixel data are internally consistent for ColorDifferenceCbCr rather than simply changing the descriptor byte in RGB seeds.

## Avoid
Do not repeat the same candidate family when the verifier signal matches this key. Treat broad seed mutation, wrapper usage paths, both-image crashes, parser-clean exits, or local-only crashes as evidence that the current surface is not the target differential.

## Recovery Direction
Preserve only independently validated format or harness reachability facts. Re-enter generation by first satisfying the harness contract and the earliest format gate, then use a different target-specific invariant instead of enlarging or randomly mutating the failed family.
