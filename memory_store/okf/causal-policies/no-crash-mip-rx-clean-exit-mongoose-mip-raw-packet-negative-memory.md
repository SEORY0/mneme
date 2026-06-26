---
type: causal-policy
title: "No Crash Mip Rx Clean Exit Mongoose Mip Raw Packet Negative Memory"
description: "Round 6 negative memory for no_crash with verifier signal mip_rx_clean_exit."
failure_class: "no_crash"
verifier_signal: "mip_rx_clean_exit"
candidate_family: "raw_ethernet_and_ip_icmp_echo"
input_format: "mongoose-mip-raw-packet"
harness_convention: "libfuzzer mongoose fuzz wrapper"
vuln_class: "icmp-reply overflow"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "mip-rx-clean-exit", "mongoose-mip-raw-packet", "negative-memory", "round-6"]
match_keys: ["no_crash", "mip_rx_clean_exit", "mongoose-mip-raw-packet", "libfuzzer mongoose fuzz wrapper", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 6
---
# No Crash Mip Rx Clean Exit Mongoose Mip Raw Packet Negative Memory

- key: `no_crash x mip_rx_clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[mongoose-mip-raw-packet]]

## Failure Shape
- Raw Ethernet, raw IPv4, and Ethernet/IPv6 ICMP echo variants with oversized payloads all executed cleanly. The target path likely requires matching the mock interface address and packet-carving expectations exactly so rx_icmp constructs an oversized reply in the fixed-size transmit buffer.

## Policy
Treat `no_crash x mip_rx_clean_exit` on this format family as negative memory for the attempted carrier. Preserve only verifier-proven reachability, then retarget the missing gate or sink-specific state instead of resubmitting candidates with the same signal.

## Procedure
1. Keep any parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, feature gate, length relation, stateful subobject, or official target sink.
3. Change one relation at a time and reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or nonreproducible basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not treat local generic crashes, wrapper usage paths, clean parser exits, or wrong-sink labels as success.
- Do not broaden random mutation after reachability is known; move to the smallest missing format contract.
- Do not submit another candidate with this exact failure signal unless the candidate changes the causal gate being tested.
- Do not store raw payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: 1 diagnosed persistent failure(s) from round 6.
- Scope: generator repair and basin avoidance only.
