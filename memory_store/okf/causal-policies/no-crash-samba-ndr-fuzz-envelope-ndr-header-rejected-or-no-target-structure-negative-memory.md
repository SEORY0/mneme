---
type: causal-policy
title: No Crash Samba Ndr Fuzz Envelope Ndr Header Rejected Or No Target Structure Negative Memory
description: Negative memory for no_crash with ndr_header_rejected_or_no_target_structure on samba ndr fuzz envelope inputs.
failure_class: no_crash
verifier_signal: ndr_header_rejected_or_no_target_structure
candidate_family: construct
input_format: samba ndr fuzz envelope
harness_convention: libfuzzer
vuln_class: use-of-uninitialized-value
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, ndr-header-rejected-or-no-target-structure, samba-ndr-fuzz-envelope, use-of-uninitialized-value, construct, negative-memory]
match_keys: [no-crash, ndr-header-rejected-or-no-target-structure, samba-ndr-fuzz-envelope, use-of-uninitialized-value, negative-memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# No Crash Samba Ndr Fuzz Envelope Ndr Header Rejected Or No Target Structure Negative Memory

- key: `no_crash x ndr_header_rejected_or_no_target_structure`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1

## Failure Shape
The NDR fuzz envelope was identified, including the in-versus-out initialization invariant,
but the candidate did not select a structure or function whose size relation crosses from
initialized to uninitialized state.

## Policy
Treat `ndr_header_rejected_or_no_target_structure` after `no_crash` on `samba ndr fuzz envelope` as evidence that the candidate preserved or missed
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
