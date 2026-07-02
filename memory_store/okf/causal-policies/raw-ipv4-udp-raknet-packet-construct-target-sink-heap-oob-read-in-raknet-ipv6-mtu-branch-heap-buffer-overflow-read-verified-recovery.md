---
type: causal-policy
title: "Raw IPV4 UDP Raknet Packet Construct Target Sink Heap Oob Read In Raknet Ipv6 Mtu Branch Heap Buffer Overflow Read Verified Recovery"
description: "Round 29 verified recovery for generic_crash with verifier signal target_sink_heap_oob_read_in_raknet_ipv6_mtu_branch."
failure_class: "generic_crash"
verifier_signal: "target_sink_heap_oob_read_in_raknet_ipv6_mtu_branch"
candidate_family: "construct"
input_format: "raw-ipv4-udp-raknet-packet"
harness_convention: "libfuzzer-ndpi-process-packet"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "target-sink-heap-oob-read-in-raknet-ipv6-mtu-branch", "raw-ipv4-udp-raknet-packet", "libfuzzer-ndpi-process-packet", "construct", "heap-buffer-overflow-read", "verified-recovery", "round-29"]
match_keys: ["generic_crash", "target_sink_heap_oob_read_in_raknet_ipv6_mtu_branch", "raw-ipv4-udp-raknet-packet", "libfuzzer-ndpi-process-packet", "heap-buffer-overflow-read", "generic-crash", "target-sink-heap-oob-read-in-raknet-ipv6-mtu-branch", "raw-ipv4-udp-raknet-packet", "libfuzzer-ndpi-process-packet", "heap-buffer-overflow-read", "verified_recovery", "construct", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 29
---
# Raw IPV4 UDP Raknet Packet Construct Target Sink Heap Oob Read In Raknet Ipv6 Mtu Branch Heap Buffer Overflow Read Verified Recovery

- key: `generic_crash x target_sink_heap_oob_read_in_raknet_ipv6_mtu_branch`
- outcome: verified target match / recovery policy
- success_count: 1
- related format facts: [[raw-ipv4-udp-raknet-packet]]
- related harness facts: [[libfuzzer-ndpi-process-packet]]

## Policy
For `generic_crash x target_sink_heap_oob_read_in_raknet_ipv6_mtu_branch` on `raw-ipv4-udp-raknet-packet`, keep the parser and harness gates that produced the verifier signal, then vary only the causal relation described below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Build a raw IPv4 UDP packet, not a pcap file. Use a RakNet open-connection message shape with the exact payload length expected by that message variant, and choose the address-family branch that treats the embedded address as IPv6. The parser then computes the MTU field position as if the larger address were present even though the variant length is fixed for the shorter layout, producing a minimal out-of-bounds read in the RakNet dissector.
2. Preserve format recognition and the harness input contract while mutating the narrow sink invariant; do not broaden into an off-target crash or a both-image crash.
3. If later verifier output changes the failure key, re-rank against that new key before mutating unrelated fields.

## Format Contract
- Format [[raw-ipv4-udp-raknet-packet]]: nDPI sees a raw IP packet whose UDP payload is parsed as RakNet. RakNet message variants have discriminator-specific fixed lengths and may contain an address-family marker followed by an address and an MTU field. The vulnerable relation is between the fixed variant length and the address-family-dependent MTU location.
- Harness [[libfuzzer-ndpi-process-packet]]: The fuzz_process_packet harness initializes one nDPI flow and passes the whole file buffer directly to ndpi_detection_process_packet. It expects the input to start at the IP header; it does not read a pcap global header, packet record, selector byte, or FuzzedDataProvider fields.

## Negative Memory
- Do not corrupt the outer `raw-ipv4-udp-raknet-packet` recognition gate while retargeting this signal.
- Do not count parser reachability, clean exits, fixed-image crashes, both-image crashes, or local wrong-sink labels as success without official target match.
- Never store payload bytes, exact positions, checksums, submit metadata, or task-local identifiers.

## Evidence Shape
- Support: one round-29 worker trace with official target match.
- Scope: generator repair and retargeting only; pair with [[raw-ipv4-udp-raknet-packet]] and [[libfuzzer-ndpi-process-packet]].
