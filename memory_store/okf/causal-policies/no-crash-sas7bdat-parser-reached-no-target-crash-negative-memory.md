---
type: causal-policy
title: No Crash Sas7bdat Parser Reached No Target Crash Negative Memory
description: Negative memory for no_crash with parser_reached_no_target_crash on sas7bdat inputs.
failure_class: no_crash
verifier_signal: parser_reached_no_target_crash
candidate_family: seed_mutate
input_format: sas7bdat
harness_convention: afl
vuln_class: heap-buffer-overflow-read
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, parser-reached-no-target-crash, sas7bdat, heap-buffer-overflow-read, seed-mutate, negative-memory]
match_keys: [no-crash, parser-reached-no-target-crash, sas7bdat, heap-buffer-overflow-read, negative-memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# No Crash Sas7bdat Parser Reached No Target Crash Negative Memory

- key: `no_crash x parser_reached_no_target_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1

## Failure Shape
Valid SAS7BDAT seed envelopes reached the page parser, but bounded mutations of subheader
pointer length fields either stayed within parser error handling or were rejected before the
vulnerable over-read path. The missing trigger is likely a pointer-table shape that
preserves a recognized subheader while making the vulnerable build consume data past the
page boundary without tripping the current parse guards.

## Policy
Treat `parser_reached_no_target_crash` after `no_crash` on `sas7bdat` as evidence that the candidate preserved or missed
the wrong invariant. The next generator should keep any proven reachability gate, then retarget to
the smallest missing format contract or sink-specific state instead of repeating the same carrier.

## Procedure
1. Preserve only the envelope features that the verifier proved reached parsing or harness execution.
2. Identify the missing target condition named by the verifier signal: parser reachability, sink selection, structural subobject, length relation, checksum gate, or protocol classification.
3. Change one causal relation at a time and reject variants that move backward to bad format, usage-only wrapper output, or the same clean-exit basin.
4. If the signal says parser or sink was not reached, prefer a more faithful seed or format-specific carrier before mutating bug-trigger fields.
5. If the signal says parser reached cleanly, stop broad fuzzing and violate the exact boundary named by the vulnerability class.

## Negative Memory
- Do not resubmit this failure shape without a new verifier signal.
- Do not widen mutations after reachability is established.
- Do not confuse local wrapper crashes, usage paths, or clean parser exits with official target matches.
- Do not store raw payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: 1 diagnosed persistent failure.
- Scope: generator repair and basin avoidance only.
