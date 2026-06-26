---
type: causal-policy
title: No Crash Pcap Flow Cleanup Reached Without Invalid Union State Negative Memory
description: Negative memory for no_crash with verifier signal pcap_flow_cleanup_reached_without_invalid_union_state.
failure_class: no_crash
verifier_signal: pcap_flow_cleanup_reached_without_invalid_union_state
candidate_family: seed-sweep
input_format: any
harness_convention: any
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, pcap-flow-cleanup-reached-without-invalid-union-state, negative_memory]
match_keys: [no-crash, pcap-flow-cleanup-reached-without-invalid-union-state, negative_memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# No Crash Pcap Flow Cleanup Reached Without Invalid Union State Negative Memory

- key: `no_crash x pcap_flow_cleanup_reached_without_invalid_union_state`
- outcome: persistent failure basin
- support_count: 1
- candidate_families: seed-sweep
- observed_formats: pcap

## Policy
Treat this verifier signal as negative memory for the attempted candidate family. Preserve any parser reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Procedure
Use the diagnosis as a selector map: keep the valid base, then change the missing protocol/table/module state rather than increasing file size or randomizing payload bytes.

## Diagnosed Dead Ends
- Protocol-focused pcap corpus samples, including fuzz, TLS, DTLS, and QUIC traffic, did not leave the nDPI flow protocol union in an invalid partially-classified state before cleanup. A better candidate needs packets that enter the SoftEther or VPN protocol detector far enough to write protocol-specific union data, then fail classification and free the flow through the generic cleanup path.

## Negative Memory
Do not repeat the same carrier plus broad mutation after this signal. Do not promote the diagnosis into a recovery until a later verifier-confirmed candidate flips the official gate.
