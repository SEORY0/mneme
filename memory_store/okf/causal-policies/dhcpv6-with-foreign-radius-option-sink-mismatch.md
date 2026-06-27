---
type: causal-policy
title: "Dhcpv6 With Foreign Radius Option Sink Mismatch"
description: "Verified recovery for wrong_sink with sink_mismatch on dhcpv6-with-foreign-radius-option inputs."
failure_class: wrong_sink
verifier_signal: sink_mismatch
candidate_family: regression_seed_mutate
input_format: dhcpv6-with-foreign-radius-option
harness_convention: libfuzzer
vuln_class: heap-buffer-overflow-read
access_scope: generate
success_count: 1
confidence: medium
tags: [wrong-sink, sink-mismatch, dhcpv6-with-foreign-radius-option, heap-buffer-overflow-read, verified_recovery]
match_keys: [wrong-sink, sink-mismatch, dhcpv6-with-foreign-radius-option, heap-buffer-overflow-read]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
---
# Dhcpv6 With Foreign Radius Option Sink Mismatch

- key: `wrong_sink x sink_mismatch`
- outcome: verified recovery
- confidence: 0.69
- success_count: 1
- failure_count: 0
- formats: [[dhcpv6-with-foreign-radius-option]]

## Failure Shape
A candidate family ended at `wrong_sink` before a verifier-confirmed repair. The successful shape kept the required `dhcpv6-with-foreign-radius-option` parser envelope and moved the mutation into the boundary relation consumed by the target sink instead of relying on broad corruption.

## Procedure
Use a raw DHCPv6 packet that passes the outer packet validator and carries a foreign RADIUS payload inside an option whose declared length contains the whole embedded payload. The embedded RADIUS data must use the long-extended fragment path with at least one fragment that is accepted as part of the same attribute sequence, followed by a trailing fragment that does not have enough remaining bytes for its own header. This keeps the outer DHCPv6 decoder on the foreign-option path and makes the inner RADIUS decoder read past the available fragment bytes.

Retarget from this failure key by preserving the format gate first, then changing exactly the cross-field invariant that separates the vulnerable build from the fixed build. Prefer compact construction for construct traces and seed-preserving mutation for seed traces.

## Verifier Contract
The expected signal is `sink_mismatch` with a vulnerable-build crash and clean fixed build. Parser reachability without the differential crash is not sufficient.

## Negative Guards
Do not store raw payload bytes, exact positions, checksums, or submit metadata. Do not widen the mutation after the parser envelope is accepted; if the fixed image also crashes, shrink back to the single boundary relation.
