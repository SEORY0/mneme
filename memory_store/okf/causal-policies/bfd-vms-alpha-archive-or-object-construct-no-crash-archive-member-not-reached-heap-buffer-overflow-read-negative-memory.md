---
type: negative-memory
title: "Bfd Vms Alpha Archive Or Object Construct No Crash Archive Member Not Reached Heap Buffer Overflow Read Negative Memory"
description: "Round 37 negative memory for no_crash with verifier signal archive_member_not_reached."
failure_class: "no_crash"
verifier_signal: "archive_member_not_reached"
candidate_family: "construct"
input_format: "bfd-vms-alpha-archive-or-object"
harness_convention: "libfuzzer-bfd-archive-only"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 0
failure_count: 2
confidence: medium
tags: ["no-crash", "archive-member-not-reached", "bfd-vms-alpha-archive-or-object", "libfuzzer-bfd-archive-only", "construct", "heap-buffer-overflow-read", "negative-memory", "round-37"]
match_keys: ["no_crash", "archive_member_not_reached", "bfd-vms-alpha-archive-or-object", "libfuzzer-bfd-archive-only", "heap-buffer-overflow-read", "negative-memory", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 37
---
# Bfd Vms Alpha Archive Or Object Construct No Crash Archive Member Not Reached Heap Buffer Overflow Read Negative Memory

- key: `no_crash x archive_member_not_reached`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 2
- related format facts: [[bfd-vms-alpha-archive-or-object]]
- related harness facts: [[libfuzzer-bfd-archive-only]]

## Failure Shape
The EGSD undersized-entry invariant was straightforward to encode, but the harness did not drive that object parser. Standalone VMS object records were rejected by the archive-only check. Generic archive carriers with VMS-like members stayed on the generic archive target path, and VMS library carriers were recognized only far enough to read library indexes rather than opening and parsing the referenced module. The submitted archive probe exited cleanly in the vulnerable build and did not produce an official target match.

## Observed Basin
- Failure trajectory classes: no_crash, no_crash, no_crash, no_crash, no_crash.
- Official confirmation: no server target match for this basin.

## Policy
Treat `no_crash x archive_member_not_reached` on `bfd-vms-alpha-archive-or-object` under `libfuzzer-bfd-archive-only` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described above. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrapper-mismatch, usage-only, timeout, or fixed-image-crash behavior.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `archive_member_not_reached` basin.
4. Promote a recovery from this basin only after a later official target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `archive_member_not_reached`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, timeouts, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 37 after 5 attempts.
- Candidate family: construct.
- Scope: generator repair and basin avoidance only.
