---
type: causal-policy
title: Format Recognition Negative Memory
description: Negative memory for candidates rejected before the intended packed, object, or binary-container format is recognized.
failure_class: no_crash
verifier_signal: format_not_recognized
candidate_family: construct
input_format: binary-container
harness_convention: any
access_scope: generate
success_count: 0
confidence: medium
tags: [no_crash, format_not_recognized, clean_rejection, negative_memory]
match_keys: [no_crash, format_not_recognized, clean_rejection, negative_memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
## Policy
A clean recognition failure is negative memory for synthetic minimal binaries. Start from a known-recognized packed, archive, object, or executable carrier, then mutate the internal table that owns the vulnerable invariant.

## Procedure
1. Stop using hand-written skeletons after a clean format-recognition miss.
2. Choose a seed or constructor that the target tool already recognizes as the expected container family.
3. Preserve outer magic, directory, section, and packing metadata.
4. Mutate only the internal size, table, stream, or dynamic-record relationship named by the diagnosis.
5. Verify recognition before any boundary mutation is considered progress.

## Negative Memory
- Do not append plausible records to an unrecognized binary shell.
- Do not corrupt the top-level magic or directory when the bug is inside a later metadata walk.
- Do not submit clean rejection candidates.

## Evidence Shape
- Support: diagnosed round failures with format-recognition and clean-rejection signals.
- Scope: generator repair only.
