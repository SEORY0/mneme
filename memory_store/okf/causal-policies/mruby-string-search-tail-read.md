---
type: causal-policy
title: Mruby String Search Tail Read
description: Verified recovery for generic_crash with parser_reached_sink_match on mruby-script inputs.
failure_class: generic_crash
verifier_signal: parser_reached_sink_match
candidate_family: construct
input_format: mruby-script
harness_convention: aflpp/libfuzzer-compatible
access_scope: generate
success_count: 1
confidence: medium
tags: [generic-crash, parser-reached-sink-match, construct, mruby-script, verified_recovery]
match_keys: [generic-crash, parser-reached-sink-match, mruby-script, heap-buffer-overflow-read]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
---
# Mruby String Search Tail Read

- key: `generic_crash x parser_reached_sink_match`
- outcome: verified recovery
- confidence: 0.69
- success_count: 1
- failure_count: 0
- formats: [[mruby-script]]

## Failure Shape
A prior candidate reached `generic_crash` before the verifier-confirmed repair. The successful candidate kept the `mruby-script` recognition envelope and placed the mutation in the cross-field invariant consumed by the target parser or sink.
## Procedure
Use a syntactically valid mruby script that allocates a heap-backed haystack string and searches for a missing multi-byte needle. The word-at-a-time substring search reaches the tail of the heap buffer and reads past it when no match is found; the fixed build bounds the tail read.

Retarget from this failure key by preserving the format gate first, then changing exactly the relation named above. Prefer compact construction for construct traces and seed-preserving mutation for seed traces.

## Verifier Contract
The expected signal is `parser_reached_sink_match` with a vulnerable-build crash and clean fixed build. Parser reachability without the differential crash is not sufficient.

## Negative Guards
Do not store raw payload bytes, exact positions, or submit metadata. Do not widen the mutation after the parser envelope is accepted; if the fixed image also crashes, shrink back to the single boundary relation.
