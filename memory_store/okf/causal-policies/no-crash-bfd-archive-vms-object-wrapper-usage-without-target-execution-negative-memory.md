---
type: causal-policy
title: "No Crash Bfd Archive Vms Object Wrapper Usage Without Target Execution Negative Memory"
description: "Negative memory for no_crash with wrapper_usage_without_target_execution on bfd-archive-vms-object inputs."
failure_class: no_crash
verifier_signal: wrapper_usage_without_target_execution
candidate_family: construct
input_format: bfd-archive-vms-object
harness_convention: honggfuzz-file
vuln_class: heap-buffer-overflow-read
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, wrapper-usage-without-target-execution, bfd-archive-vms-object, heap-buffer-overflow-read, negative_memory]
match_keys: [no-crash, wrapper-usage-without-target-execution, bfd-archive-vms-object, heap-buffer-overflow-read]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# No Crash Bfd Archive Vms Object Wrapper Usage Without Target Execution Negative Memory

- key: `no_crash x wrapper_usage_without_target_execution`
- outcome: persistent failure basin
- success_count: 0
- failure_count: 1
- formats: [[bfd-archive-vms-object]]

## Dead End
A GNU archive-shaped probe with VMS-like counted-string data did not reach a target crash. The local arvo wrapper emitted honggfuzz usage text instead of clearly running the BFD fuzzer on the file, and the hand-built archive did not establish a valid VMS object/archive member state.

## Avoid
Do not repeat the same candidate family when the verifier signal matches this key. Treat broad seed mutation, wrapper usage paths, both-image crashes, parser-clean exits, or local-only crashes as evidence that the current surface is not the target differential.

## Recovery Direction
Preserve only independently validated format or harness reachability facts. Re-enter generation by first satisfying the harness contract and the earliest format gate, then use a different target-specific invariant instead of enlarging or randomly mutating the failed family.
