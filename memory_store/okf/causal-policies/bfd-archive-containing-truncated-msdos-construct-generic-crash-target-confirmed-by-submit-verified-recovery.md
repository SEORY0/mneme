---
type: causal-policy
title: "BFD Archive Containing Truncated MSDOS Construct Generic Crash Target Confirmed By Submit Verified Recovery"
description: "Round 10 verified recovery for generic_crash with verifier signal generic_crash_target_confirmed_by_submit."
failure_class: "generic_crash"
verifier_signal: "generic_crash_target_confirmed_by_submit"
candidate_family: "construct"
input_format: "bfd-archive-containing-truncated-msdos-member"
harness_convention: "libfuzzer-tempfile-bfd"
vuln_class: "uninitialized-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "generic-crash-target-confirmed-by-submit", "bfd-archive-containing-truncated-msdos-member", "verified-recovery", "round-10"]
match_keys: ["generic_crash", "generic_crash_target_confirmed_by_submit", "bfd-archive-containing-truncated-msdos-member", "libfuzzer-tempfile-bfd", "uninitialized-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 10
---
# BFD Archive Containing Truncated MSDOS Construct Generic Crash Target Confirmed By Submit Verified Recovery

## Policy
For `generic_crash x generic_crash_target_confirmed_by_submit`, preserve the format and harness gates that reached the official target path, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Use a valid Unix archive envelope so BFD enters archive handling, then provide a member that begins like an MS-DOS executable but is truncated before the full DOS header can be read.
2. This reaches the object probe path where a short read must be handled; the vulnerable build continues with invalid state and crashes, while the fixed build rejects it.

## Format Contract
- The BFD archive path expects the global archive magic, fixed-width member headers, member sizes, and even-byte member padding. The MS-DOS object probe begins with a DOS executable signature and then expects enough header bytes to validate follow-on executable metadata.
- Harness: The fuzzer writes the raw input to a temporary file, opens it with BFD auto-detection, and checks archive format. Inputs must therefore be complete file bytes, not an in-memory record stream.

## Negative Memory
- Do not broaden mutations after the parser/harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store raw payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-10 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin.
