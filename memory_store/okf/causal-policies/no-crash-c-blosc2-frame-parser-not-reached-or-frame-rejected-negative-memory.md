---
type: causal-policy
title: "No Crash C Blosc2 Frame Parser Not Reached Or Frame Rejected Negative Memory"
description: "Negative memory for no_crash with parser_not_reached_or_frame_rejected on c-blosc2-frame inputs."
failure_class: no_crash
verifier_signal: parser_not_reached_or_frame_rejected
candidate_family: seed_mutate
input_format: c-blosc2-frame
harness_convention: libfuzzer
vuln_class: heap-buffer-overflow-read
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, parser-not-reached-or-frame-rejected, c-blosc2-frame, heap-buffer-overflow-read, negative_memory]
match_keys: [no-crash, parser-not-reached-or-frame-rejected, c-blosc2-frame, heap-buffer-overflow-read]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# No Crash C Blosc2 Frame Parser Not Reached Or Frame Rejected Negative Memory

- key: `no_crash x parser_not_reached_or_frame_rejected`
- outcome: persistent failure basin
- success_count: 0
- failure_count: 1
- formats: [[c-blosc2-frame]]

## Dead End
Seed-preserving mutations of header metalayer index metadata and trailer extent metadata stayed clean or were rejected before the vulnerable copy. The likely missing condition is preserving super-chunk construction while placing a metadata content pointer and declared content span in the vulnerable header-copy relation.

## Avoid
Do not repeat the same candidate family when the verifier signal matches this key. Treat broad seed mutation, wrapper usage paths, both-image crashes, parser-clean exits, or local-only crashes as evidence that the current surface is not the target differential.

## Recovery Direction
Preserve only independently validated format or harness reachability facts. Re-enter generation by first satisfying the harness contract and the earliest format gate, then use a different target-specific invariant instead of enlarging or randomly mutating the failed family.
