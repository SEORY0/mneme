---
type: causal-policy
title: "Ipv4 Tcp Http Response Target Sink Stack Buffer Overflow"
description: "Verified recovery for generic_crash with target_sink_stack_buffer_overflow on ipv4-tcp-http-response inputs."
failure_class: generic_crash
verifier_signal: target_sink_stack_buffer_overflow
candidate_family: construct
input_format: ipv4-tcp-http-response
harness_convention: libfuzzer-ndpi-process-packet
vuln_class: stack-buffer-overflow-read
access_scope: generate
success_count: 1
confidence: medium
tags: [generic-crash, target-sink-stack-buffer-overflow, ipv4-tcp-http-response, stack-buffer-overflow-read, verified_recovery]
match_keys: [generic-crash, target-sink-stack-buffer-overflow, ipv4-tcp-http-response, stack-buffer-overflow-read]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
---
# Ipv4 Tcp Http Response Target Sink Stack Buffer Overflow

- key: `generic_crash x target_sink_stack_buffer_overflow`
- outcome: verified recovery
- confidence: 0.69
- success_count: 1
- failure_count: 0
- formats: [[ipv4-tcp-http-response]]

## Failure Shape
A candidate family ended at `generic_crash` before a verifier-confirmed repair. The successful shape kept the required `ipv4-tcp-http-response` parser envelope and moved the mutation into the boundary relation consumed by the target sink instead of relying on broad corruption.

## Procedure
Build a single IPv4/TCP packet whose payload is an HTTP response. Include a server header for a recognized server family with an obsolete dotted version prefix, then continue the version token long enough that the local fixed-size version buffer is filled without a terminator. This reaches the obsolete-server risk formatting path, where the unterminated version token is read past the stack buffer.

Retarget from this failure key by preserving the format gate first, then changing exactly the cross-field invariant that separates the vulnerable build from the fixed build. Prefer compact construction for construct traces and seed-preserving mutation for seed traces.

## Verifier Contract
The expected signal is `target_sink_stack_buffer_overflow` with a vulnerable-build crash and clean fixed build. Parser reachability without the differential crash is not sufficient.

## Negative Guards
Do not store raw payload bytes, exact positions, checksums, or submit metadata. Do not widen the mutation after the parser envelope is accepted; if the fixed image also crashes, shrink back to the single boundary relation.
