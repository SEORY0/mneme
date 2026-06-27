---
type: causal-policy
title: "No Crash Udp Nordic Btle Parser Not Reached Or Feature Not Selected Negative Memory"
description: "Negative memory for no_crash with parser_not_reached_or_feature_not_selected on udp-nordic-btle inputs."
failure_class: no_crash
verifier_signal: parser_not_reached_or_feature_not_selected
candidate_family: construct
input_format: udp-nordic-btle
harness_convention: afl-fuzzshark
vuln_class: wild-pointer-dereference
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, parser-not-reached-or-feature-not-selected, udp-nordic-btle, wild-pointer-dereference, negative_memory]
match_keys: [no-crash, parser-not-reached-or-feature-not-selected, udp-nordic-btle, wild-pointer-dereference]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# No Crash Udp Nordic Btle Parser Not Reached Or Feature Not Selected Negative Memory

- key: `no_crash x parser_not_reached_or_feature_not_selected`
- outcome: persistent failure basin
- success_count: 0
- failure_count: 1
- formats: [[udp-nordic-btle]]

## Dead End
The active fuzzer target was the UDP dissector under the IP protocol table, not a direct BTLE target. Raw BTLE, raw Nordic BLE, and UDP-wrapped Nordic BLE shapes across plausible decode paths did not reach the uninitialized acl_data crash.

## Avoid
Do not repeat the same candidate family when the verifier signal matches this key. Treat broad seed mutation, wrapper usage paths, both-image crashes, parser-clean exits, or local-only crashes as evidence that the current surface is not the target differential.

## Recovery Direction
Preserve only independently validated format or harness reachability facts. Re-enter generation by first satisfying the harness contract and the earliest format gate, then use a different target-specific invariant instead of enlarging or randomly mutating the failed family.
