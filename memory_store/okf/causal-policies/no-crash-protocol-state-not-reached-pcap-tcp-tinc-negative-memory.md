---
type: causal-policy
title: "No Crash Protocol State Not Reached Pcap Tcp Tinc Negative Memory"
description: "Round 8 negative memory for no_crash with verifier signal protocol_state_not_reached."
failure_class: "no_crash"
verifier_signal: "protocol_state_not_reached"
candidate_family: "construct"
input_format: "pcap-tcp-tinc"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "protocol-state-not-reached", "pcap-tcp-tinc", "negative_memory", "round-8"]
match_keys: ["no_crash", "protocol_state_not_reached", "pcap-tcp-tinc", "libfuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 8
---
# No Crash Protocol State Not Reached Pcap Tcp Tinc Negative Memory

## Policy
Treat `no_crash x protocol_state_not_reached` as a persistent failure basin for `pcap-tcp-tinc` under `libfuzzer`. Preserve any reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Diagnosed Dead End
- Constructed pcap/TCP flows with TINC-looking payloads did not reach the protocol state that scans the final textual field. The likely missing gate is nDPI flow classification and bidirectional TCP session state, not the terminal malformed payload shape itself.

## Format and Harness Gates
- Format: The outer input is an offline pcap with Ethernet/IP/TCP packets. The TINC detector expects text records inside TCP payloads; the vulnerable path requires earlier state advances from greeting-like records and then a later record with numeric fields followed by a final alphanumeric field whose terminating newline is assumed.
- Harness: The fuzzer runs the nDPI pcap reader. It opens the raw input as an offline pcap, copies each captured packet according to its captured length, and passes packets through the normal workflow classifier before protocol-specific dissectors run.

## Procedure
1. Before retrying this basin, rebuild the carrier around the exact harness contract and confirm parser reachability.
2. Replace the failed mutation family with a more specific invariant that would change the verifier signal.
3. Avoid broad seed mutation, oversized mutation, or off-target crash chasing when this same signal recurs.

## Negative Memory
- Do not promote this basin into a recovery policy until an official vulnerable/fixed verifier target match is observed.
- Do not preserve raw bytes, offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-8 persistent failure trace.
- Scope: generator avoidance and retargeting for the same failure key.
