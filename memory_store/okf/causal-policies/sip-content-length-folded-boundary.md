---
type: causal-policy
title: Sip Content Length Folded Boundary
description: Verified recovery for wrong_sink with parser_reached_sink_mismatch on sip-text inputs.
failure_class: wrong_sink
verifier_signal: parser_reached_sink_mismatch
candidate_family: construct
input_format: sip-text
harness_convention: libfuzzer
access_scope: generate
success_count: 1
confidence: medium
tags: [wrong-sink, parser-reached-sink-mismatch, construct, sip-text, verified_recovery]
match_keys: [wrong-sink, parser-reached-sink-mismatch, sip-text, out-of-bounds-read]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
---
# Sip Content Length Folded Boundary

- key: `wrong_sink x parser_reached_sink_mismatch`
- outcome: verified recovery
- confidence: 0.69
- success_count: 1
- failure_count: 0
- formats: [[sip-text]]

## Failure Shape
A prior candidate reached `wrong_sink` before the verifier-confirmed repair. The successful candidate kept the `sip-text` recognition envelope and placed the mutation in the cross-field invariant consumed by the target parser or sink.
The trace also records this guardrail: Several earlier malformed endings crashed both vulnerable and fixed builds; the scored variant kept the parser on the numeric/folded-whitespace boundary fixed by the patch.

## Procedure
Provide a syntactically plausible SIP request line and make Content-Length the final parsed header. After a numeric value, end the buffer on a folded-line whitespace pattern so parse_content_length reaches the value parser and reads one byte past the supplied header boundary.

Retarget from this failure key by preserving the format gate first, then changing exactly the relation named above. Prefer compact construction for construct traces and seed-preserving mutation for seed traces.

## Verifier Contract
The expected signal is `parser_reached_sink_mismatch` with a vulnerable-build crash and clean fixed build. Parser reachability without the differential crash is not sufficient.

## Negative Guards
Do not store raw payload bytes, exact positions, or submit metadata. Do not widen the mutation after the parser envelope is accepted; if the fixed image also crashes, shrink back to the single boundary relation.
