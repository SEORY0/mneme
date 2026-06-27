---
type: causal-policy
title: "C Blosc2 Frame Parser Reached Frame Get Vlmetalayers"
description: "Verified recovery for generic_crash with parser_reached_frame_get_vlmetalayers on c-blosc2-frame inputs."
failure_class: generic_crash
verifier_signal: parser_reached_frame_get_vlmetalayers
candidate_family: seed_mutate
input_format: c-blosc2-frame
harness_convention: "libfuzzer whole-buffer frame decompressor"
vuln_class: invalid-negative-length-memory-access
access_scope: generate
success_count: 1
confidence: medium
tags: [generic-crash, parser-reached-frame-get-vlmetalayers, c-blosc2-frame, invalid-negative-length-memory-access, verified_recovery]
match_keys: [generic-crash, parser-reached-frame-get-vlmetalayers, c-blosc2-frame, invalid-negative-length-memory-access]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
---
# C Blosc2 Frame Parser Reached Frame Get Vlmetalayers

- key: `generic_crash x parser_reached_frame_get_vlmetalayers`
- outcome: verified recovery
- confidence: 0.69
- success_count: 1
- failure_count: 0
- formats: [[c-blosc2-frame]]

## Failure Shape
A candidate family ended at `generic_crash` before a verifier-confirmed repair. The successful shape kept the required `c-blosc2-frame` parser envelope and moved the mutation into the boundary relation consumed by the target sink instead of relying on broad corruption.

## Procedure
Start from a valid contiguous c-blosc2 frame seed so the frame header, frame length, chunk table, trailer length footer, and decompressor setup remain valid. Replace only the variable-length metalayer trailer body with a reader-compatible indexed entry whose content marker is present but whose signed content length is negative. The vulnerable trailer parser stores that negative length and then uses it as an allocation/copy size; the fixed build rejects the negative length.

Retarget from this failure key by preserving the format gate first, then changing exactly the cross-field invariant that separates the vulnerable build from the fixed build. Prefer compact construction for construct traces and seed-preserving mutation for seed traces.

## Verifier Contract
The expected signal is `parser_reached_frame_get_vlmetalayers` with a vulnerable-build crash and clean fixed build. Parser reachability without the differential crash is not sufficient.

## Negative Guards
Do not store raw payload bytes, exact positions, checksums, or submit metadata. Do not widen the mutation after the parser envelope is accepted; if the fixed image also crashes, shrink back to the single boundary relation.
