---
type: negative-memory
title: "No Crash Configured Udp Dissector Completed Pcap Udp Packet Negative Memory"
description: "Round 19 negative memory for no_crash with verifier signal configured_udp_dissector_completed."
failure_class: "no_crash"
verifier_signal: "configured_udp_dissector_completed"
candidate_family: "construct"
input_format: "pcap-udp-packet"
harness_convention: "afl/libfuzzer-compatible"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "configured-udp-dissector-completed", "pcap-udp-packet", "afl-libfuzzer-compatible", "construct", "negative-memory", "round-19"]
match_keys: ["no-crash", "configured-udp-dissector-completed", "pcap-udp-packet", "afl-libfuzzer-compatible", "heap-buffer-overflow-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 19
---
# No Crash Configured Udp Dissector Completed Pcap Udp Packet Negative Memory

- key: `no_crash x configured_udp_dissector_completed`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[pcap-udp-packet]]
- harnesses: [[afl-libfuzzer-compatible]]

## Failure Shape
The constructed packet reached the fuzzshark target configured for UDP-over-IP dissection but did not route to the idn component described by the task. The main missing piece is the concrete packet encapsulation and dissector-table selector that dispatches to the target idn parser.

## Policy
Treat `no_crash x configured_udp_dissector_completed` on `pcap-udp-packet` as negative memory for the attempted carrier. Preserve only the reachability that was actually observed, then retarget the missing gate or sink-specific state before spending more verification attempts.

## Procedure
1. Keep any parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, feature gate, length relation, stateful subobject, or official target sink.
3. Change one relation at a time and reject variants that return to this same clean-exit, off-target, usage-only, or nonreproducible basin.
4. Promote a recovery from this basin only after a later server-confirmed target match.

## Negative Memory
- Do not resubmit another candidate with this exact failure signal unless it changes the causal gate being tested.
- Do not broaden random mutation after reachability is known; move to the smallest missing format or state contract.
- Do not treat local generic crashes, wrapper usage paths, clean parser exits, or wrong-sink labels as success.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 19.
- Scope: generator repair and basin avoidance only.
