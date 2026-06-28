---
type: causal-policy
title: "UDP RTCP Compound Construct Parser Reached Target Sink Verified Recovery"
description: "Round 10 verified recovery for generic_crash with verifier signal parser_reached_target_sink."
failure_class: "generic_crash"
verifier_signal: "parser_reached_target_sink"
candidate_family: "construct"
input_format: "udp-rtcp-compound"
harness_convention: "libfuzzer-fuzzshark-ip-proto-udp"
vuln_class: "heap-buffer-overflow-write"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-target-sink", "udp-rtcp-compound", "verified-recovery", "round-10"]
match_keys: ["generic_crash", "parser_reached_target_sink", "udp-rtcp-compound", "libfuzzer-fuzzshark-ip-proto-udp", "heap-buffer-overflow-write", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 10
---
# UDP RTCP Compound Construct Parser Reached Target Sink Verified Recovery

## Policy
For `generic_crash x parser_reached_target_sink`, preserve the format and harness gates that reached the official target path, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Wrap a compound RTCP payload in a UDP datagram with a destination port accepted by the RTCP heuristic.
2. The first RTCP packet must be a heuristic-accepted packet type; the second is transport-wide congestion-control feedback whose advertised packet status count is smaller than the number of received packets encoded by the status chunk.
3. The vulnerable dissector allocates arrays from the small count but writes entries for the chunk coverage.

## Format Contract
- RTCP over UDP uses UDP port heuristics and compound RTCP framing. Transport-wide feedback carries sender/source identifiers, a base sequence, a packet-status count, reference time, feedback count, packet-status chunks, and receive deltas. Status-vector or run-length chunks can describe more packet states than the count field if not validated.
- Harness: The fuzzshark target is configured as the UDP dissector in the IP protocol table, so the raw input is a UDP datagram payload for that dissector rather than an Ethernet frame. RTCP heuristic dispatch also depends on UDP port parity and the first RTCP packet in the compound payload.

## Negative Memory
- Do not broaden mutations after the parser/harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store raw payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-10 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin.
