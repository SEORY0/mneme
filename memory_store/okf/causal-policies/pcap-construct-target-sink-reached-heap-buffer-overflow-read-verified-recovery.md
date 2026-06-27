---
type: causal-policy
title: "Pcap Construct Target Sink Reached Heap Buffer Overflow Read Verified Recovery"
description: "Round 9 verified recovery for generic_crash with verifier signal target_sink_reached."
failure_class: "generic_crash"
verifier_signal: "target_sink_reached"
candidate_family: "construct"
input_format: "pcap"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "target-sink-reached", "pcap", "construct", "verified-recovery", "round-9"]
match_keys: ["generic_crash", "target_sink_reached", "pcap", "libfuzzer", "heap-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 9
---
# Pcap Construct Target Sink Reached Heap Buffer Overflow Read Verified Recovery

## Policy
For `generic_crash x target_sink_reached`, preserve the format and harness gates that reached the target path, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Build a structurally valid PCAP with an Ethernet packet that uses stacked VLAN tags to leave the
  parser positioned on an MPLS ethertype while the following MPLS header is truncated.
1. The PCAP and record lengths must remain internally valid so libpcap reaches the packet reader;
  the only violated invariant is that the MPLS word is shorter than the reader assumes.

## Format Contract
- The harness expects a complete PCAP file, not a raw packet.
- A valid global header and packet record are required.
- The vulnerable path is reached through Ethernet linktype parsing, VLAN ethertype rechecks, and
  then MPLS ethertype handling.

## Harness Contract
- The libFuzzer input is written to a temporary PCAP file and opened with libpcap.
- Each captured packet is copied into an exactly sized heap allocation before
  ndpi_workflow_process_packet processes it, so packet-record caplen directly controls the heap
  buffer boundary.

## Related Knowledge
- Format facts: [[pcap]]
- Harness facts: [[libfuzzer]]

## Negative Memory
- Do not broaden mutations after the parser/harness gate is proven.
- Do not submit candidates that reproduce on the fixed image, move to an off-target wrapper crash, or only preserve a local-only crash signal.
- Do not store raw payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-9 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin.
