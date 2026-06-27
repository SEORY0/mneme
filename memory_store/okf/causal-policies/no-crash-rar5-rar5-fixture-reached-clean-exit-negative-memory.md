---
type: causal-policy
title: "No Crash Rar5 Rar5 Fixture Reached Clean Exit Negative Memory"
description: "Negative memory for no_crash with rar5_fixture_reached_clean_exit on rar5 inputs."
failure_class: no_crash
verifier_signal: rar5_fixture_reached_clean_exit
candidate_family: seed_mutate
input_format: rar5
harness_convention: libfuzzer
vuln_class: heap-buffer-overflow
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, rar5-fixture-reached-clean-exit, rar5, heap-buffer-overflow, negative_memory]
match_keys: [no-crash, rar5-fixture-reached-clean-exit, rar5, heap-buffer-overflow]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# No Crash Rar5 Rar5 Fixture Reached Clean Exit Negative Memory

- key: `no_crash x rar5_fixture_reached_clean_exit`
- outcome: persistent failure basin
- success_count: 0
- failure_count: 1
- formats: [[rar5]]

## Dead End
The in-tree RAR5 different-window-size fixture parsed without a crash under the single-buffer libarchive fuzzer. The remaining gap is likely reproducing the multi-volume continuation state that the unit test exercises through archive sequencing rather than only replaying one raw archive buffer.

## Avoid
Do not repeat the same candidate family when the verifier signal matches this key. Treat broad seed mutation, wrapper usage paths, both-image crashes, parser-clean exits, or local-only crashes as evidence that the current surface is not the target differential.

## Recovery Direction
Preserve only independently validated format or harness reachability facts. Re-enter generation by first satisfying the harness contract and the earliest format gate, then use a different target-specific invariant instead of enlarging or randomly mutating the failed family.
