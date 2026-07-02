---
type: causal-policy
title: "Pcap Ipv6 Construct Generic Crash Target Sink Reached Fixed Clean Heap Buffer Overflow Read Verified Recovery"
description: "Verified recovery distilled from a round trace for generic_crash / target_sink_reached_fixed_clean."
failure_class: "generic_crash"
verifier_signal: "target_sink_reached_fixed_clean"
candidate_family: "construct"
input_format: "pcap-ipv6"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "construct", "pcap-ipv6", "heap-buffer-overflow-read", "verified-recovery"]
match_keys: ["generic-crash", "target-sink-reached-fixed-clean", "pcap-ipv6", "libfuzzer", "heap-buffer-overflow-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
provenance: round-35-consolidator
---
# Pcap Ipv6 Construct Generic Crash Target Sink Reached Fixed Clean Heap Buffer Overflow Read Verified Recovery

## Policy
For `generic_crash` with verifier signal `target_sink_reached_fixed_clean` on `pcap-ipv6` under `libfuzzer`, recover by preserving the format and harness gates that reach the target sink, then mutate only the invariant described by the verified recipe. This policy is keyed to the failure signal and is not a byte-level PoC recipe.

## Procedure
1. Build a complete classic pcap with an Ethernet packet whose link type and ethertype select IPv6.
2. Keep the capture record lengths internally consistent, but make the captured IPv6 layer non-empty and shorter than the fixed IPv6 header.
3. This reaches IPv6Layer construction, then parseExtensions reads IPv6 header state from beyond the truncated heap buffer while the fixed build rejects the short layer.

## Format Contract
- Input format: [[pcap-ipv6]].
- Harness contract: [[libfuzzer]].
- Keep parser reachability and sink selection intact before mutating the vulnerable relation.

## Negative Memory
- Do not broaden this into unrelated `pcap-ipv6` failures without the same failure class and verifier signal.
- Do not store task identifiers, raw bytes, exact offsets, checksums, or submit metadata.

## Evidence Shape
- Support: one round 35 verified official target match; vulnerable build reached the target signal and the fixed build did not.

## Diagnosis Notes
A malformed IPv6 extension-chain boundary also reached parseExtensions, but it crashed both images. The successful path is not an extension header length mismatch; it is an undersized captured IPv6 header under an otherwise valid pcap/Ethernet envelope.
