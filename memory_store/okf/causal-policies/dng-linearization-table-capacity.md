---
type: causal-policy
title: Dng Linearization Table Capacity
description: Verified recovery for wrong_sink with parser_reached_target_sink on dng inputs.
failure_class: wrong_sink
verifier_signal: parser_reached_target_sink
candidate_family: construct
input_format: dng
harness_convention: libfuzzer
access_scope: generate
success_count: 1
confidence: medium
tags: [wrong-sink, parser-reached-target-sink, construct, dng, verified_recovery]
match_keys: [wrong-sink, parser-reached-target-sink, dng, heap-buffer-overflow-write]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
---
# Dng Linearization Table Capacity

- key: `wrong_sink x parser_reached_target_sink`
- outcome: verified recovery
- confidence: 0.69
- success_count: 1
- failure_count: 0
- formats: [[dng]]

## Failure Shape
A prior candidate reached `wrong_sink` before the verifier-confirmed repair. The successful candidate kept the `dng` recognition envelope and placed the mutation in the cross-field invariant consumed by the target parser or sink.
## Procedure
Build a minimal little-endian DNG/TIFF envelope with enough baseline image tags and one valid uncompressed strip so RawSpeed decodes a tiny image. Add a linearization table whose element count exceeds the fixed lookup-table capacity. Metadata handling passes that table into the dithering lookup builder, which writes past the allocated lookup storage; the fixed build enforces the table-size invariant.

Retarget from this failure key by preserving the format gate first, then changing exactly the relation named above. Prefer compact construction for construct traces and seed-preserving mutation for seed traces.

## Verifier Contract
The expected signal is `parser_reached_target_sink` with a vulnerable-build crash and clean fixed build. Parser reachability without the differential crash is not sufficient.

## Negative Guards
Do not store raw payload bytes, exact positions, or submit metadata. Do not widen the mutation after the parser envelope is accepted; if the fixed image also crashes, shrink back to the single boundary relation.
