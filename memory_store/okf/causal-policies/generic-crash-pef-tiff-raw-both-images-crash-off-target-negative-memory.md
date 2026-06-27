---
type: causal-policy
title: "Generic Crash Pef Tiff Raw Both Images Crash Off Target Negative Memory"
description: "Negative memory for generic_crash with both_images_crash_off_target on pef-tiff-raw inputs."
failure_class: generic_crash
verifier_signal: both_images_crash_off_target
candidate_family: construct
input_format: pef-tiff-raw
harness_convention: libfuzzer
vuln_class: exception-handling-logic
access_scope: generate
success_count: 0
confidence: medium
tags: [generic-crash, both-images-crash-off-target, pef-tiff-raw, exception-handling-logic, negative_memory]
match_keys: [generic-crash, both-images-crash-off-target, pef-tiff-raw, exception-handling-logic]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# Generic Crash Pef Tiff Raw Both Images Crash Off Target Negative Memory

- key: `generic_crash x both_images_crash_off_target`
- outcome: persistent failure basin
- success_count: 0
- failure_count: 1
- formats: [[pef-tiff-raw]]

## Dead End
Minimal TIFF and PEF-like structures did not reproduce the RawSpeed decodeUncompressed exception-handling behavior. One malformed TIFF/PEF size relation crashed both images, so it was an off-target parser or wrapper failure rather than the described fixed/vulnerable split.

## Avoid
Do not repeat the same candidate family when the verifier signal matches this key. Treat broad seed mutation, wrapper usage paths, both-image crashes, parser-clean exits, or local-only crashes as evidence that the current surface is not the target differential.

## Recovery Direction
Preserve only independently validated format or harness reachability facts. Re-enter generation by first satisfying the harness contract and the earliest format gate, then use a different target-specific invariant instead of enlarging or randomly mutating the failed family.
