---
type: causal-policy
title: Sip Leading Linebreak Overread
description: Verified recovery for wrong_sink with sink_mismatch_but_target_parser_crash on sip inputs.
failure_class: wrong_sink
verifier_signal: sink_mismatch_but_target_parser_crash
candidate_family: construct
input_format: sip
harness_convention: libfuzzer
access_scope: generate
success_count: 1
confidence: medium
tags: [wrong-sink, sink-mismatch-but-target-parser-crash, construct, sip, verified_recovery]
match_keys: [wrong-sink, sink-mismatch-but-target-parser-crash, sip, heap-buffer-overflow-read]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
---
# Sip Leading Linebreak Overread

- key: `wrong_sink x sink_mismatch_but_target_parser_crash`
- outcome: verified recovery
- confidence: 0.69
- success_count: 1
- failure_count: 0
- formats: [[sip]]

## Failure Shape
A prior candidate reached `wrong_sink` before the verifier-confirmed repair. The successful candidate kept the `sip` recognition envelope and placed the mutation in the cross-field invariant consumed by the target parser or sink.
## Procedure
The SIP parser gate accepts raw message bytes longer than the trivial-size guard. A payload made only of leading line-break whitespace exhausts the buffer inside the initial line-skip loop, violating the invariant that the bounds check must happen before dereferencing the next byte.

Retarget from this failure key by preserving the format gate first, then changing exactly the relation named above. Prefer compact construction for construct traces and seed-preserving mutation for seed traces.

## Verifier Contract
The expected signal is `sink_mismatch_but_target_parser_crash` with a vulnerable-build crash and clean fixed build. Parser reachability without the differential crash is not sufficient.

## Negative Guards
Do not store raw payload bytes, exact positions, or submit metadata. Do not widen the mutation after the parser envelope is accepted; if the fixed image also crashes, shrink back to the single boundary relation.
