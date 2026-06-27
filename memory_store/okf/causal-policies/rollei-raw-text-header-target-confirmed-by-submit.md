---
type: causal-policy
title: "Rollei Raw Text Header Target Confirmed By Submit"
description: "Verified recovery for wrong_sink with target_confirmed_by_submit on rollei-raw-text-header inputs."
failure_class: wrong_sink
verifier_signal: target_confirmed_by_submit
candidate_family: construct
input_format: rollei-raw-text-header
harness_convention: "libfuzzer whole-buffer LibRaw"
vuln_class: stack-buffer-overflow-read
access_scope: generate
success_count: 1
confidence: medium
tags: [wrong-sink, target-confirmed-by-submit, rollei-raw-text-header, stack-buffer-overflow-read, verified_recovery]
match_keys: [wrong-sink, target-confirmed-by-submit, rollei-raw-text-header, stack-buffer-overflow-read]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
---
# Rollei Raw Text Header Target Confirmed By Submit

- key: `wrong_sink x target_confirmed_by_submit`
- outcome: verified recovery
- confidence: 0.69
- success_count: 1
- failure_count: 0
- formats: [[rollei-raw-text-header]]

## Failure Shape
A candidate family ended at `wrong_sink` before a verifier-confirmed repair. The successful shape kept the required `rollei-raw-text-header` parser envelope and moved the mutation into the boundary relation consumed by the target sink instead of relying on broad corruption.

## Procedure
Use the raw camera signature that selects the Rollei metadata parser, then provide a header line that exactly fills the parser line buffer without a delimiter or line terminator. The vulnerable buffer datastream returns that line without ensuring string termination, so the later metadata parser string scan reads past the local line buffer. The fixed build adds the missing termination and exits cleanly.

Retarget from this failure key by preserving the format gate first, then changing exactly the cross-field invariant that separates the vulnerable build from the fixed build. Prefer compact construction for construct traces and seed-preserving mutation for seed traces.

## Verifier Contract
The expected signal is `target_confirmed_by_submit` with a vulnerable-build crash and clean fixed build. Parser reachability without the differential crash is not sufficient.

## Negative Guards
Do not store raw payload bytes, exact positions, checksums, or submit metadata. Do not widen the mutation after the parser envelope is accepted; if the fixed image also crashes, shrink back to the single boundary relation.
