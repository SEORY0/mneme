---
type: negative-memory
title: "No Crash Script Executed Without Target Split Php Source Construct Recursive Array Sort Crash Negative Memory"
description: "Round 25 negative memory for no_crash with verifier signal script_executed_without_target_split."
failure_class: "no_crash"
verifier_signal: "script_executed_without_target_split"
candidate_family: "construct"
input_format: "php-source"
harness_convention: "libfuzzer"
vuln_class: "recursive-array-sort-crash"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "script-executed-without-target-split", "php-source", "libfuzzer", "construct", "negative-memory", "round-25"]
match_keys: ["no_crash", "script_executed_without_target_split", "php-source", "libfuzzer", "recursive-array-sort-crash", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 25
---
# No Crash Script Executed Without Target Split Php Source Construct Recursive Array Sort Crash Negative Memory

- key: `no_crash x script_executed_without_target_split`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[php-source]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Multiple recursive-array layouts reached PHP execution and called the sorting function, including self-recursive, mutually recursive, nested recursive, and mixed scalar/array values. They either executed cleanly or hit wrapper-level errors, and the submitted candidate did not produce a vulnerable-image crash.

## Policy
Treat `no_crash x script_executed_without_target_split` on `php-source` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, wrapper-mismatch, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `script_executed_without_target_split` basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `script_executed_without_target_split`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
The input is PHP source text. Recursive arrays can be created by assigning references into arrays and then passing the array by reference to the sort function. Regular PHP opening tags and statement syntax are required for the execute fuzzer.

## Harness Contract
The effective target is the PHP execute fuzzer, which runs a source file as a PHP request. There is no byte carving; the raw file contents are the script.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 25 after 11 attempts.
- Scope: generator repair and basin avoidance only.
