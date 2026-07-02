---
type: negative-memory
title: "No Crash Wrapper Usage No Target Execution Mruby Script Negative Memory"
description: "Round 28 negative memory for no_crash with verifier signal wrapper_usage_no_target_execution."
failure_class: "no_crash"
verifier_signal: "wrapper_usage_no_target_execution"
candidate_family: "construct"
input_format: "mruby-script"
harness_convention: "honggfuzz-file-wrapper"
vuln_class: "integer-radix-packing"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "wrapper-usage-no-target-execution", "mruby-script", "honggfuzz-file-wrapper", "construct", "integer-radix-packing", "negative-memory", "round-28"]
match_keys: ["no_crash", "wrapper_usage_no_target_execution", "mruby-script", "honggfuzz-file-wrapper", "integer-radix-packing", "negative_memory", "construct", "other"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 28
---
# No Crash Wrapper Usage No Target Execution Mruby Script Negative Memory

- key: `no_crash x wrapper_usage_no_target_execution`
- outcome: negative memory
- success_count: 0
- failure_count: 1
- formats: [[mruby-script]]
- harnesses: [[honggfuzz-file-wrapper]]

## Dead-End Shape
Several syntactically valid mruby scripts targeted the negative-bigint literal path across multiple numeric radices, including variants that force runtime use of the literal. The local arvo wrapper consistently printed the Honggfuzz usage message after accepting the input path and exited cleanly, so the supplied script content did not appear to be executed by the verifier command.

## Policy
For `no_crash x wrapper_usage_no_target_execution` on `mruby-script`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission. Treat `construct` as useful only if it changes the missing gate, state relation, or sink path.

## Procedure
1. When this failure key repeats, preserve only the descriptive reachability facts and retarget the missing invariant before another official submission.
2. Do not spend attempts on candidates that are clean, rejected before the target path, fixed-build-crashing, or wrapper-only reproductions in this same shape.
3. Prefer a different construction family or a deeper harness/format contract when the verifier signal repeats without new parser-depth evidence.

## Format Contract
- Format [[mruby-script]]: The intended input is raw mruby source text. The vulnerable compiler path is reached by integer literals that overflow the immediate integer representation and are stored as bigint literals; negative overflow literals carry both sign and radix information in the packed literal metadata.
- Harness [[honggfuzz-file-wrapper]]: The source harness copies the whole input file into a null-terminated buffer and calls mrb_load_string, with no mode selector or FuzzedDataProvider layout. In this generated arvo image, the command wrapper invokes a Honggfuzz-built binary with the file path, and that binary exits after printing its fuzzing usage instead of evaluating the file.

## Negative Memory
- Do not promote this trace as a recovery unless a later verifier run flips the target relation.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.
- Preserve descriptive format and harness facts separately from this causal negative policy.

## Evidence Shape
- Support: one diagnosed round-28 persistent failure.
- Scope: generator repair and retargeting only.
