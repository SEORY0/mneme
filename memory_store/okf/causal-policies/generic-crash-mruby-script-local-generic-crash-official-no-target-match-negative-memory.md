---
type: causal-policy
title: "Generic Crash Mruby Script Local Generic Crash Official No Target Match Negative Memory"
description: "Negative memory for generic_crash with local_generic_crash_official_no_target_match on mruby-script inputs."
failure_class: generic_crash
verifier_signal: local_generic_crash_official_no_target_match
candidate_family: construct
input_format: mruby-script
harness_convention: libfuzzer-mruby-load-string
vuln_class: buffer-overflow-write
access_scope: generate
success_count: 0
confidence: medium
tags: [generic-crash, local-generic-crash-official-no-target-match, mruby-script, buffer-overflow-write, negative_memory]
match_keys: [generic-crash, local-generic-crash-official-no-target-match, mruby-script, buffer-overflow-write]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# Generic Crash Mruby Script Local Generic Crash Official No Target Match Negative Memory

- key: `generic_crash x local_generic_crash_official_no_target_match`
- outcome: persistent failure basin
- success_count: 0
- failure_count: 1
- formats: [[mruby-script]]

## Dead End
Precision-zero exponential formatting scripts can crash the local vulnerable image, but the official server reported clean vulnerable execution and no target match for the submitted candidate. This suggests the local crash is not stable under the official harness or is not the target sink.

## Avoid
Do not repeat the same candidate family when the verifier signal matches this key. Treat broad seed mutation, wrapper usage paths, both-image crashes, parser-clean exits, or local-only crashes as evidence that the current surface is not the target differential.

## Recovery Direction
Preserve only independently validated format or harness reachability facts. Re-enter generation by first satisfying the harness contract and the earliest format gate, then use a different target-specific invariant instead of enlarging or randomly mutating the failed family.
