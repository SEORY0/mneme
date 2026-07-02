---
type: causal-policy
title: "Ipv4 UDP STUN Packet Construct Parser Reached Target Sink Heap Buffer Overflow Read Verified Recovery"
description: "Round 27 verified recovery for generic_crash with verifier signal parser_reached_target_sink."
failure_class: "generic_crash"
verifier_signal: "parser_reached_target_sink"
candidate_family: "construct"
input_format: "ipv4-udp-stun-packet"
harness_convention: "libfuzzer-afl-compatible"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-target-sink", "ipv4-udp-stun-packet", "libfuzzer-afl-compatible", "construct", "heap-buffer-overflow-read", "verified-recovery", "round-27"]
match_keys: ["generic_crash", "parser_reached_target_sink", "ipv4-udp-stun-packet", "libfuzzer-afl-compatible", "heap-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 27
---
# Ipv4 UDP STUN Packet Construct Parser Reached Target Sink Heap Buffer Overflow Read Verified Recovery

## Policy
For `generic_crash x parser_reached_target_sink`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Build a complete IPv4/UDP packet so the packet harness exposes the UDP payload to the STUN dissector.
2. Keep the STUN message type and declared body length self-consistent, then end the body with an incomplete attribute header so the parser's attribute loop accepts the fragment and reads the attribute length past the payload boundary.
3. Keep the carrier abstract: preserve the gate/invariant relation, not any task-local bytes or offsets.
4. If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- The fuzzer input is an L3 IPv4 packet.
- The IPv4 total length and UDP length must cover a UDP payload.
- The STUN payload begins with a message type, message length, magic cookie, and transaction identifier, followed by padded attributes whose headers contain a type and length.
- Harness [[libfuzzer-afl-compatible]]:
  - The libFuzzer/AFL-compatible harness passes raw file bytes directly to ndpi_detection_process_packet.
  - There is no FuzzedDataProvider split and no pcap container; bytes must form a packet buffer with IPv4 and UDP headers before the STUN payload.

## Negative Memory
- Do not broaden mutations after the parser or harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-27 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[ipv4-udp-stun-packet]] and [[libfuzzer-afl-compatible]].
