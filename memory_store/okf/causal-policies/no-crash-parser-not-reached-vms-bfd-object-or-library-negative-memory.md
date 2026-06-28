---
type: causal-policy
title: "No Crash Parser Not Reached Vms BFD Object Or Library Negative Memory"
description: "Round 16 negative memory for no_crash with verifier signal parser_not_reached."
failure_class: "no_crash"
verifier_signal: "parser_not_reached"
candidate_family: "seed_mutate+construct"
input_format: "vms-bfd-object-or-library"
harness_convention: "libfuzzer"
vuln_class: "stack-buffer-overflow-write"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-not-reached", "vms-bfd-object-or-library", "negative-memory", "round-16"]
match_keys: ["no_crash", "parser_not_reached", "vms-bfd-object-or-library", "libfuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 16
---
# No Crash Parser Not Reached Vms BFD Object Or Library Negative Memory

## Policy
For `no_crash x parser_not_reached`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
- Generic COFF object seeds, archive stubs, and VMS-looking byte patterns did not make BFD identify and traverse a VMS library index. The missing gate is a recognized VMS object/library envelope with a valid index tree whose key length and key block number fields are internally plausible but inconsistent for traversal.
- When `no_crash x parser_not_reached` appears for `vms-bfd-object-or-library`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
- Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- BFD format dispatch first recognizes an object or archive flavor before format-specific callbacks run. The VMS library path has indexed records with key material and key-block metadata; the described overflow is in index traversal after the VMS library structures are accepted.
- Harness: The BFD fuzzer consumes raw bytes as an input file and lets BFD auto-detect the format. There is no selector byte; reaching the sink requires BFD to classify the bytes as a VMS object/library and invoke the VMS index traversal code.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed persistent failure from round 16.
- Scope: generator avoidance for the same failure-keyed basin.
