---
type: negative-memory
title: "Bfd VMS Alpha Archive Or Object Construct No Crash Archive Member Not Reached Heap Buffer Overflow Read Negative Memory"
description: "Round 36 negative memory for no_crash with verifier signal archive_member_not_reached."
failure_class: "no_crash"
verifier_signal: "archive_member_not_reached"
candidate_family: "construct"
input_format: "bfd-vms-alpha-archive-or-object"
harness_convention: "libfuzzer-bfd-archive-only"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["no-crash", "archive-member-not-reached", "bfd-vms-alpha-archive-or-object", "libfuzzer-bfd-archive-only", "construct", "heap-buffer-overflow-read", "negative-memory", "round-36"]
match_keys: ["no_crash", "archive_member_not_reached", "bfd-vms-alpha-archive-or-object", "libfuzzer-bfd-archive-only", "heap-buffer-overflow-read", "no-crash", "archive-member-not-reached", "negative_memory", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 36
---
# Bfd VMS Alpha Archive Or Object Construct No Crash Archive Member Not Reached Heap Buffer Overflow Read Negative Memory

- key: `no_crash x archive_member_not_reached`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[bfd-vms-alpha-archive-or-object]]
- related harness facts: [[libfuzzer-bfd-archive-only]]

## Failure Shape
The vulnerable counted-string helper is reached through VMS object parsing, but this harness only opens the raw input and asks BFD whether it is an archive. Standalone VMS objects are not accepted by the archive-only check, generic archive carriers keep member target selection on the generic archive path, and VMS library carriers are recognized enough to read index structures without opening embedded modules. The attempted carriers therefore did not make BFD parse the malicious VMS object section containing the counted name.

## Observed Basin
- Failure trajectory classes: no_crash.
- Official confirmation: no server target match for this basin.

## Policy
Treat `no_crash x archive_member_not_reached` on `bfd-vms-alpha-archive-or-object` under `libfuzzer-bfd-archive-only` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described above. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrapper-mismatch, usage-only, or fixed-image-crash behavior.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `archive_member_not_reached` basin.
4. Promote a recovery from this basin only after a later official target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `archive_member_not_reached`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 36 after 5 attempts.
- Scope: generator repair and basin avoidance only.
