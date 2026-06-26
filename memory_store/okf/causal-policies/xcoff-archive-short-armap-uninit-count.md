---
type: causal-policy
title: Xcoff Archive Short Armap Uninit Count
description: Verified recovery for wrong_sink with parser_reached_sink_mismatch on xcoff-archive inputs.
failure_class: wrong_sink
verifier_signal: parser_reached_sink_mismatch
candidate_family: construct
input_format: xcoff-archive
harness_convention: libfuzzer
access_scope: generate
success_count: 1
confidence: medium
tags: [wrong-sink, parser-reached-sink-mismatch, construct, xcoff-archive, verified_recovery]
match_keys: [wrong-sink, parser-reached-sink-mismatch, xcoff-archive, uninitialized-read]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
---
# Xcoff Archive Short Armap Uninit Count

- key: `wrong_sink x parser_reached_sink_mismatch`
- outcome: verified recovery
- confidence: 0.69
- success_count: 1
- failure_count: 0
- formats: [[xcoff-archive]]

## Failure Shape
A prior candidate reached `wrong_sink` before the verifier-confirmed repair. The successful candidate kept the `xcoff-archive` recognition envelope and placed the mutation in the cross-field invariant consumed by the target parser or sink.
## Procedure
Construct a recognized XCOFF big archive with the global 64-bit symbol-table offset enabled. Keep the archive/member headers parseable, then make the armap member body shorter than the initial symbol-count field so the armap reader consumes uninitialized bytes while interpreting the count.

Retarget from this failure key by preserving the format gate first, then changing exactly the relation named above. Prefer compact construction for construct traces and seed-preserving mutation for seed traces.

## Verifier Contract
The expected signal is `parser_reached_sink_mismatch` with a vulnerable-build crash and clean fixed build. Parser reachability without the differential crash is not sufficient.

## Negative Guards
Do not store raw payload bytes, exact positions, or submit metadata. Do not widen the mutation after the parser envelope is accepted; if the fixed image also crashes, shrink back to the single boundary relation.
