---
type: causal-policy
title: Pcre2 Jit Short Body Prescan
description: Verified recovery for wrong_sink with sink_mismatch_but_target_parser_crash on pcre2-fuzzer inputs.
failure_class: wrong_sink
verifier_signal: sink_mismatch_but_target_parser_crash
candidate_family: construct
input_format: pcre2-fuzzer
harness_convention: libfuzzer
access_scope: generate
success_count: 1
confidence: medium
tags: [wrong-sink, sink-mismatch-but-target-parser-crash, construct, pcre2-fuzzer, verified_recovery]
match_keys: [wrong-sink, sink-mismatch-but-target-parser-crash, pcre2-fuzzer, heap-buffer-overflow-read]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
---
# Pcre2 Jit Short Body Prescan

- key: `wrong_sink x sink_mismatch_but_target_parser_crash`
- outcome: verified recovery
- confidence: 0.69
- success_count: 1
- failure_count: 0
- formats: [[pcre2-fuzzer]]

## Failure Shape
A prior candidate reached `wrong_sink` before the verifier-confirmed repair. The successful candidate kept the `pcre2-fuzzer` recognition envelope and placed the mutation in the cross-field invariant consumed by the target parser or sink.
## Procedure
The PCRE2 fuzzer requires its option prefix before regex text. Supplying the required prefix followed by a very short body reaches the JIT quantifier pre-scan, violating the invariant that lookahead in the scan must be guarded for minimal post-prefix input length.

Retarget from this failure key by preserving the format gate first, then changing exactly the relation named above. Prefer compact construction for construct traces and seed-preserving mutation for seed traces.

## Verifier Contract
The expected signal is `sink_mismatch_but_target_parser_crash` with a vulnerable-build crash and clean fixed build. Parser reachability without the differential crash is not sufficient.

## Negative Guards
Do not store raw payload bytes, exact positions, or submit metadata. Do not widen the mutation after the parser envelope is accepted; if the fixed image also crashes, shrink back to the single boundary relation.
