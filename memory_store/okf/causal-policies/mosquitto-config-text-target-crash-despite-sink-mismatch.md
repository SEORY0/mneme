---
type: causal-policy
title: "Mosquitto Config Text Target Crash Despite Sink Mismatch"
description: "Verified recovery for wrong_sink with target_crash_despite_sink_mismatch on mosquitto-config-text inputs."
failure_class: wrong_sink
verifier_signal: target_crash_despite_sink_mismatch
candidate_family: construct
input_format: mosquitto-config-text
harness_convention: libfuzzer
vuln_class: heap-use-after-free-read
access_scope: generate
success_count: 1
confidence: medium
tags: [wrong-sink, target-crash-despite-sink-mismatch, mosquitto-config-text, heap-use-after-free-read, verified_recovery]
match_keys: [wrong-sink, target-crash-despite-sink-mismatch, mosquitto-config-text, heap-use-after-free-read]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
---
# Mosquitto Config Text Target Crash Despite Sink Mismatch

- key: `wrong_sink x target_crash_despite_sink_mismatch`
- outcome: verified recovery
- confidence: 0.69
- success_count: 1
- failure_count: 0
- formats: [[mosquitto-config-text]]

## Failure Shape
A candidate family ended at `wrong_sink` before a verifier-confirmed repair. The successful shape kept the required `mosquitto-config-text` parser envelope and moved the mutation into the boundary relation consumed by the target sink instead of relying on broad corruption.

## Procedure
Use a minimal Mosquitto broker configuration that first creates the implicit default listener through a default-listener directive, then appends a separate explicit listener so the listener array is reallocated, then uses another default-listener directive. The final directive touches the stale default-listener pointer retained from before reallocation.

Retarget from this failure key by preserving the format gate first, then changing exactly the cross-field invariant that separates the vulnerable build from the fixed build. Prefer compact construction for construct traces and seed-preserving mutation for seed traces.

## Verifier Contract
The expected signal is `target_crash_despite_sink_mismatch` with a vulnerable-build crash and clean fixed build. Parser reachability without the differential crash is not sufficient.

## Negative Guards
Do not store raw payload bytes, exact positions, checksums, or submit metadata. Do not widen the mutation after the parser envelope is accepted; if the fixed image also crashes, shrink back to the single boundary relation.
