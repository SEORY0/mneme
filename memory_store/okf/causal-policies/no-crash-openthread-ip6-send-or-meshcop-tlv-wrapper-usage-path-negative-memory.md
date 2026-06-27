---
type: causal-policy
title: "No Crash Openthread Ip6 Send Or Meshcop Tlv Wrapper Usage Path Negative Memory"
description: "Negative memory for no_crash with wrapper_usage_path on openthread-ip6-send-or-meshcop-tlv inputs."
failure_class: no_crash
verifier_signal: wrapper_usage_path
candidate_family: construct
input_format: openthread-ip6-send-or-meshcop-tlv
harness_convention: honggfuzz-wrapper
vuln_class: stack-buffer-overflow
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, wrapper-usage-path, openthread-ip6-send-or-meshcop-tlv, stack-buffer-overflow, negative_memory]
match_keys: [no-crash, wrapper-usage-path, openthread-ip6-send-or-meshcop-tlv, stack-buffer-overflow]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# No Crash Openthread Ip6 Send Or Meshcop Tlv Wrapper Usage Path Negative Memory

- key: `no_crash x wrapper_usage_path`
- outcome: persistent failure basin
- success_count: 0
- failure_count: 1
- formats: [[openthread-ip6-send-or-meshcop-tlv]]

## Dead End
The selected binary reported the ip6-send honggfuzz usage path for every candidate family, so the PoC bytes did not appear to reach the OpenThread packet or MeshCoP handlers under the single-file verifier invocation. Distinct attempts covered CLI commissioner commands, NCP/HDLC-style bytes, IPv6/UDP/CoAP-style bytes, a mutated in-repo radio frame seed, and a raw CoAP/MeshCoP payload.

## Avoid
Do not repeat the same candidate family when the verifier signal matches this key. Treat broad seed mutation, wrapper usage paths, both-image crashes, parser-clean exits, or local-only crashes as evidence that the current surface is not the target differential.

## Recovery Direction
Preserve only independently validated format or harness reachability facts. Re-enter generation by first satisfying the harness contract and the earliest format gate, then use a different target-specific invariant instead of enlarging or randomly mutating the failed family.
