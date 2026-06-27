---
type: causal-policy
title: "Md3 Parser Reached"
description: "Verified recovery for generic_crash with parser_reached on md3 inputs."
failure_class: generic_crash
verifier_signal: parser_reached
candidate_family: seed_mutate
input_format: md3
harness_convention: libfuzzer
vuln_class: heap-buffer-overflow-read
access_scope: generate
success_count: 1
confidence: medium
tags: [generic-crash, parser-reached, md3, heap-buffer-overflow-read, verified_recovery]
match_keys: [generic-crash, parser-reached, md3, heap-buffer-overflow-read]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
---
# Md3 Parser Reached

- key: `generic_crash x parser_reached`
- outcome: verified recovery
- confidence: 0.69
- success_count: 1
- failure_count: 0
- formats: [[md3]]

## Failure Shape
A candidate family ended at `generic_crash` before a verifier-confirmed repair. The successful shape kept the required `md3` parser envelope and moved the mutation into the boundary relation consumed by the target sink instead of relying on broad corruption.

## Procedure
Start from a valid MD3 model so Assimp's signature detection, header validation, surface validation, mesh construction, and post-processing all succeed. Mutate only the main header's tag metadata so the model advertises a nonempty tag table, but the tag-table start leaves less than one full tag record in the file. The vulnerable loader validates surfaces but not the complete tag table before creating tag nodes, so it reads a tag name from beyond the available input.

Retarget from this failure key by preserving the format gate first, then changing exactly the cross-field invariant that separates the vulnerable build from the fixed build. Prefer compact construction for construct traces and seed-preserving mutation for seed traces.

## Verifier Contract
The expected signal is `parser_reached` with a vulnerable-build crash and clean fixed build. Parser reachability without the differential crash is not sufficient.

## Negative Guards
Do not store raw payload bytes, exact positions, checksums, or submit metadata. Do not widen the mutation after the parser envelope is accepted; if the fixed image also crashes, shrink back to the single boundary relation.
