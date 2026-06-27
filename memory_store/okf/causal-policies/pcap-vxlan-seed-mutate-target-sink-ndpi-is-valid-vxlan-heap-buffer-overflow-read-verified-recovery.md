---
type: causal-policy
title: "Pcap Vxlan Seed Mutate Target Sink Ndpi Is Valid Vxlan Heap Buffer Overflow Read Verified Recovery"
description: "Server-verified recovery for pcap-vxlan when generic_crash pairs with target_sink_ndpi_is_valid_vxlan."
failure_class: "generic_crash"
verifier_signal: "target_sink_ndpi_is_valid_vxlan"
candidate_family: "seed_mutate"
input_format: "pcap-vxlan"
harness_convention: "libfuzzer-pcap-file"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "target-sink-ndpi-is-valid-vxlan", "pcap-vxlan", "libfuzzer-pcap-file", "seed-mutate", "verified-recovery", "round-17"]
match_keys: ["generic-crash", "target-sink-ndpi-is-valid-vxlan", "pcap-vxlan", "libfuzzer-pcap-file", "seed-mutate", "heap-buffer-overflow-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 17
---
# Pcap Vxlan Seed Mutate Target Sink Ndpi Is Valid Vxlan Heap Buffer Overflow Read Verified Recovery

- key: `generic_crash x target_sink_ndpi_is_valid_vxlan`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[pcap-vxlan]]
- related harness facts: [[libfuzzer-pcap-file]]

## Policy
When `generic_crash x target_sink_ndpi_is_valid_vxlan` appears for `pcap-vxlan`, preserve the parser or harness carrier already shown to reach the target branch. Retarget only the causal invariant named by the verifier signal and vulnerability class; do not broaden into unrelated container families after reachability is established.

## Procedure
1. Start from a valid VXLAN pcap seed and keep the outer Ethernet/IP/UDP/VXLAN headers recognizable.
2. Shorten the captured packet length so the tunnel detector accepts the packet as long enough for its flawed check but the later VXLAN reserved-byte tests read beyond the copied packet buffer.
3. Submit only candidates that preserve the same accepted carrier and separate vulnerable-build failure from fixed-build clean behavior.

## Negative Memory
- Do not treat local-only crashes, both-image crashes, or coarse sink labels as success for this key.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[pcap-vxlan]]; the relevant gate is the accepted carrier plus the invariant described above, not a byte-specific recipe.

## Harness Contract
Use [[libfuzzer-pcap-file]]; preserve the observed input contract before mutating deeper fields.

## Evidence Shape
- Support: 1 server-verified round 17 solve.
- Candidate family: seed_mutate.
