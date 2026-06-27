---
type: causal-policy
title: "Pcap Ipv4 Udp Bittorrent Construct Target Sink Reached Heap Buffer Overflow Read Verified Recovery"
description: "Server-verified recovery for pcap ipv4 udp bittorrent when wrong_sink pairs with target_sink_reached."
failure_class: "wrong_sink"
verifier_signal: "target_sink_reached"
candidate_family: "construct"
input_format: "pcap ipv4 udp bittorrent"
harness_convention: "libfuzzer pcap reader"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "target-sink-reached", "pcap-ipv4-udp-bittorrent", "libfuzzer-pcap-reader", "construct", "verified-recovery", "round-17"]
match_keys: ["wrong-sink", "target-sink-reached", "pcap-ipv4-udp-bittorrent", "libfuzzer-pcap-reader", "construct", "heap-buffer-overflow-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 17
---
# Pcap Ipv4 Udp Bittorrent Construct Target Sink Reached Heap Buffer Overflow Read Verified Recovery

- key: `wrong_sink x target_sink_reached`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[pcap-ipv4-udp-bittorrent]]
- related harness facts: [[libfuzzer-pcap-reader]]

## Policy
When `wrong_sink x target_sink_reached` appears for `pcap ipv4 udp bittorrent`, preserve the parser or harness carrier already shown to reach the target branch. Retarget only the causal invariant named by the verifier signal and vulnerability class; do not broaden into unrelated container families after reachability is established.

## Procedure
1. A complete PCAP envelope with one Ethernet IPv4 UDP packet was required.
2. The UDP ports had to stay in the high-port range and the payload had to satisfy the detector minimum length while containing only a truncated prefix of a recognized Bittorrent discovery probe, so the detector comparison read beyond the exactly allocated packet buffer.
3. Submit only candidates that preserve the same accepted carrier and separate vulnerable-build failure from fixed-build clean behavior.

## Negative Memory
- Do not treat local-only crashes, both-image crashes, or coarse sink labels as success for this key.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[pcap-ipv4-udp-bittorrent]]; the relevant gate is the accepted carrier plus the invariant described above, not a byte-specific recipe.

## Harness Contract
Use [[libfuzzer-pcap-reader]]; preserve the observed input contract before mutating deeper fields.

## Evidence Shape
- Support: 1 server-verified round 17 solve.
- Candidate family: construct.
