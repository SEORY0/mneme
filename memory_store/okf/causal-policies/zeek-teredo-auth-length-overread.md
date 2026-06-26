---
type: causal-policy
title: Zeek Teredo Auth Length Overread
description: Verified recovery for wrong_sink with parser_reached_teredo_detect_overread on zeek-fuzzbuffer-raw-ip inputs.
failure_class: wrong_sink
verifier_signal: parser_reached_teredo_detect_overread
candidate_family: seed_mutate
input_format: zeek-fuzzbuffer-raw-ip
harness_convention: libfuzzer
access_scope: generate
success_count: 1
confidence: medium
tags: [wrong-sink, parser-reached-teredo-detect-overread, seed-mutate, zeek-raw-ip, verified_recovery]
match_keys: [wrong-sink, parser-reached-teredo-detect-overread, zeek-raw-ip, heap-buffer-overflow-read]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
---
# Zeek Teredo Auth Length Overread

- key: `wrong_sink x parser_reached_teredo_detect_overread`
- outcome: verified recovery
- confidence: 0.69
- success_count: 1
- failure_count: 0
- formats: [[zeek-raw-ip]]

## Failure Shape
A prior candidate reached `wrong_sink` before the verifier-confirmed repair. The successful candidate kept the `zeek-fuzzbuffer-raw-ip` recognition envelope and placed the mutation in the cross-field invariant consumed by the target parser or sink.
## Procedure
Wrap a raw IP packet in the Zeek packet-fuzzer chunk envelope so UDP dispatch reaches tunnel detection, then mutate the Teredo authentication-length fields so the detector advances beyond the actual UDP payload before reading the next header. The fixed build adds sufficient length checks and exits cleanly.

Retarget from this failure key by preserving the format gate first, then changing exactly the relation named above. Prefer compact construction for construct traces and seed-preserving mutation for seed traces.

## Verifier Contract
The expected signal is `parser_reached_teredo_detect_overread` with a vulnerable-build crash and clean fixed build. Parser reachability without the differential crash is not sufficient.

## Negative Guards
Do not store raw payload bytes, exact positions, or submit metadata. Do not widen the mutation after the parser envelope is accepted; if the fixed image also crashes, shrink back to the single boundary relation.
