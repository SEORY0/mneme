---
type: causal-policy
title: Pdf Invalid Indirect Resource
description: Verified recovery for wrong_sink with parser_reached_sanitizer_crash on pdf inputs.
failure_class: wrong_sink
verifier_signal: parser_reached_sanitizer_crash
candidate_family: construct
input_format: pdf
harness_convention: libfuzzer/pdf_fuzzer
access_scope: generate
success_count: 1
confidence: medium
tags: [wrong-sink, parser-reached-sanitizer-crash, construct, pdf, verified_recovery]
match_keys: [wrong-sink, parser-reached-sanitizer-crash, pdf, invalid-indirect-object-reference]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
---
# Pdf Invalid Indirect Resource

- key: `wrong_sink x parser_reached_sanitizer_crash`
- outcome: verified recovery
- confidence: 0.69
- success_count: 1
- failure_count: 0
- formats: [[pdf]]

## Failure Shape
A prior candidate family produced `wrong_sink` before the verifier-confirmed repair. The winning shape kept the required parser envelope for `pdf` and moved the mutation into the boundary relation consumed by the target sink instead of relying on broad corruption.

## Procedure
Construct a minimal, xref-consistent PDF with a catalog, pages tree, and page dictionary, then place an out-of-range indirect object reference in a page resource that rendering resolves. The vulnerable build lets the invalid object number propagate into rendering state and crashes during page rasterization; the fixed build rejects or neutralizes the invalid reference.

Retarget from this failure key by preserving the format gate first, then changing exactly the cross-field invariant that separates the vulnerable build from the fixed build. Prefer a compact construct when the trace used `construct`; prefer one seed-preserving mutation when the trace used seed mutation.

## Verifier Contract
The local signal should progress from `wrong_sink` toward `parser_reached_sanitizer_crash`. The official gate must show a vulnerable-build crash and a clean fixed build; parser-only reachability is not enough.

## Negative Guards
Do not store raw payload bytes or task-specific positions. Do not widen the mutation after the parser envelope is accepted; if the fixed image also crashes, shrink back to the single invariant described above.
