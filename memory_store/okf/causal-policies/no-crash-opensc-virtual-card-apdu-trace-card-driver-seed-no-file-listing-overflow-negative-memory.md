---
type: causal-policy
title: No Crash Opensc Virtual Card Apdu Trace Card Driver Seed No File Listing Overflow Negative Memory
description: Negative memory for no_crash with card_driver_seed_no_file_listing_overflow on opensc virtual card apdu trace inputs.
failure_class: no_crash
verifier_signal: card_driver_seed_no_file_listing_overflow
candidate_family: seed_mutate
input_format: opensc virtual card apdu trace
harness_convention: libfuzzer
vuln_class: buffer-overflow-write
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, card-driver-seed-no-file-listing-overflow, opensc-virtual-card-apdu-trace, buffer-overflow-write, seed-mutate, negative-memory]
match_keys: [no-crash, card-driver-seed-no-file-listing-overflow, opensc-virtual-card-apdu-trace, buffer-overflow-write, negative-memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# No Crash Opensc Virtual Card Apdu Trace Card Driver Seed No File Listing Overflow Negative Memory

- key: `no_crash x card_driver_seed_no_file_listing_overflow`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1

## Failure Shape
A corpus virtual-card APDU trace exercised the card fuzzer but did not reach the sc-hsm
file-listing response path with an overlong listing. The remaining requirement is a trace
that drives file enumeration and returns a length inconsistent with the destination buffer.

## Policy
Treat `card_driver_seed_no_file_listing_overflow` after `no_crash` on `opensc virtual card apdu trace` as evidence that the candidate preserved or missed
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
