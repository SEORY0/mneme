---
type: causal-policy
title: No Crash Pkcs15 Profile Reader Chunks Pkcs15init Reader Reached Clean Exit Negative Memory
description: Negative memory for no_crash with pkcs15init_reader_reached_clean_exit on pkcs15-profile-reader-chunks inputs.
failure_class: no_crash
verifier_signal: pkcs15init_reader_reached_clean_exit
candidate_family: construct
input_format: pkcs15-profile-reader-chunks
harness_convention: libfuzzer
vuln_class: out-of-bounds-write
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, pkcs15init-reader-reached-clean-exit, pkcs15-profile-reader-chunks, out-of-bounds-write, construct, negative-memory]
match_keys: [no-crash, pkcs15init-reader-reached-clean-exit, pkcs15-profile-reader-chunks, out-of-bounds-write, negative-memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# No Crash Pkcs15 Profile Reader Chunks Pkcs15init Reader Reached Clean Exit Negative Memory

- key: `no_crash x pkcs15init_reader_reached_clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1

## Failure Shape
The candidate preserved the pkcs15-init split between profile text and simulated reader
chunks, but it only exercised clean virtual-reader responses. It did not select a card
profile and DF initialization state that violates the missing profile checks.

## Policy
Treat `pkcs15init_reader_reached_clean_exit` after `no_crash` on `pkcs15-profile-reader-chunks` as evidence that the candidate preserved or missed
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
