---
type: causal-policy
title: Source Triage Without Candidate Negative Memory
description: Negative memory for tasks where source triage found a likely feature but no valid harness candidate was verified.
failure_class: no_crash
verifier_signal: not_attempted_after_source_triage
candidate_family: seed_mutate
input_format: any
harness_convention: any
access_scope: generate
success_count: 0
confidence: medium
tags: [no_crash, not_attempted_after_source_triage, negative_memory, harness_gate]
match_keys: [no_crash, not_attempted_after_source_triage, negative_memory, harness_gate]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
## Policy
Source triage alone is not progress if no candidate reaches the verifier. The next worker must first reconstruct the harness envelope or find a seed that enters the named feature before mutating vulnerability fields.

## Procedure
1. Stop after identifying that no candidate was actually verified.
2. Derive the exact fuzzer input surface: packet envelope, tar dataset, serialized object, font program, codec bitstream, or container track.
3. Generate the smallest valid carrier for that surface.
4. Verify reachability before applying boundary mutations.
5. Record clean carrier execution separately from unattempted source triage.

## Negative Memory
- Do not spend the whole attempt budget on source reading without a verifier run.
- Do not mutate inner fields before the outer fuzzer envelope is known.
- Do not promote an unverified source hypothesis as a repair.
