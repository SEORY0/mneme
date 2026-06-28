---
type: causal-policy
title: "No Crash BFD Opened Object Target Not Reached COFF Object Or Ar Archive Negative Memory"
description: "Round 18 negative memory for no_crash with verifier signal bfd_opened_object_target_not_reached."
failure_class: "no_crash"
verifier_signal: "bfd_opened_object_target_not_reached"
candidate_family: "construct"
input_format: "coff-object-or-ar-archive"
harness_convention: "libfuzzer-bfd"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["no-crash", "bfd-opened-object-target-not-reached", "coff-object-or-ar-archive", "libfuzzer-bfd", "negative-memory", "round-18"]
match_keys: ["no-crash", "bfd-opened-object-target-not-reached", "coff-object-or-ar-archive", "libfuzzer-bfd", "heap-buffer-overflow-read", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 18
---
# No Crash BFD Opened Object Target Not Reached COFF Object Or Ar Archive Negative Memory

- key: `no_crash x bfd_opened_object_target_not_reached`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[coff-object-or-ar-archive]]
- related harness facts: [[libfuzzer-bfd]]

## Failure Shape
- Empty COFF, C_FILE auxiliary-symbol variants, archive-wrapped COFF, a truncated MSDOS-style object, and archive-wrapped truncated MSDOS inputs were accepted or rejected without reaching the comdat/C_FILE auxiliary-symbol sink.
- The missing gate is a COFF object with section/comdat metadata and a symbol-table layout that drives BFD into the C_FILE auxiliary-entry interpretation while leaving an inconsistent auxiliary count.

## Policy
Treat `no_crash x bfd_opened_object_target_not_reached` on `coff-object-or-ar-archive` as a basin to avoid unless a new candidate changes the parser gate, state relation, or target-sink relation described above. Preserve any proven reachability, but discard variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to this same basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `bfd_opened_object_target_not_reached`.
- Do not count parser reachability, local wrapper crashes, both-image crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[coff-object-or-ar-archive]] for descriptive format gates and invariants.

## Harness Contract
Use [[libfuzzer-bfd]] for the input-carving contract.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 18.
- Scope: generator repair and basin avoidance only.

## Round 18 Failure Evidence
- Verifier key: `no_crash x bfd_opened_object_target_not_reached`.
- Candidate family: `construct`.
- Basin summary: Empty COFF, C_FILE auxiliary-symbol variants, archive-wrapped COFF, a truncated MSDOS-style object, and archive-wrapped truncated MSDOS inputs were accepted or rejected without reaching the comdat/C_FILE auxiliary-symbol sink.
