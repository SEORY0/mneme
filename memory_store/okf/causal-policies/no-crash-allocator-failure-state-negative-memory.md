---
type: causal-policy
title: Allocator Failure State Negative Memory
description: Negative memory for scripts or expressions that execute but do not force the target allocation-failure state.
failure_class: no_crash
verifier_signal: script_executed_without_allocator_failure
candidate_family: construct
input_format: php-script
harness_convention: php-fuzz-execute
access_scope: generate
success_count: 0
confidence: medium
tags: [no_crash, allocator_failure, php_script, negative_memory]
match_keys: [no_crash, script_executed_without_allocator_failure, allocator_failure_state]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
## Policy
A script that executes cleanly under a low-memory hypothesis is negative memory unless it forces failure at the exact reallocation point. The next attempt must tune both the operation and memory-limit shape to fail after the destination enters the vulnerable state.

## Procedure
1. Preserve a harness shape that actually executes the script.
2. Choose the string, array, or buffer operation named by the diagnosis.
3. Grow input until the destination enters reallocation, then tune the memory limit around that point.
4. Avoid unrelated loops that exhaust memory before the target operation.
5. Verify that the failure class changes from clean execution to a sanitizer or official signal.

## Negative Memory
- Do not treat generic low-memory execution as progress.
- Do not use a corpus-directory wrapper for a script-execute target.
- Do not submit clean script executions.
