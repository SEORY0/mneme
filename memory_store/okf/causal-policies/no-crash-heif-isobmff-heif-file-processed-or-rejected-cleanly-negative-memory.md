---
type: causal-policy
title: "No Crash Heif Isobmff Heif File Processed Or Rejected Cleanly Negative Memory"
description: "Negative memory for no_crash with heif_file_processed_or_rejected_cleanly on heif-isobmff inputs."
failure_class: no_crash
verifier_signal: heif_file_processed_or_rejected_cleanly
candidate_family: seed_mutate
input_format: heif-isobmff
harness_convention: afl-libfuzzer
vuln_class: missing-input-buffer-check
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, heif-file-processed-or-rejected-cleanly, heif-isobmff, missing-input-buffer-check, negative_memory]
match_keys: [no-crash, heif-file-processed-or-rejected-cleanly, heif-isobmff, missing-input-buffer-check]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# No Crash Heif Isobmff Heif File Processed Or Rejected Cleanly Negative Memory

- key: `no_crash x heif_file_processed_or_rejected_cleanly`
- outcome: persistent failure basin
- success_count: 0
- failure_count: 1
- formats: [[heif-isobmff]]

## Dead End
Valid HEIF seeds, brand mutations, short brand-only boxes, and truncated metadata boxes all reached or were rejected by the HEIF handler without a sanitizer signal. The missing trigger is likely a libheif memory-read edge after the Qt handler's canRead gate, not just a short or empty input.

## Avoid
Do not repeat the same candidate family when the verifier signal matches this key. Treat broad seed mutation, wrapper usage paths, both-image crashes, parser-clean exits, or local-only crashes as evidence that the current surface is not the target differential.

## Recovery Direction
Preserve only independently validated format or harness reachability facts. Re-enter generation by first satisfying the harness contract and the earliest format gate, then use a different target-specific invariant instead of enlarging or randomly mutating the failed family.
