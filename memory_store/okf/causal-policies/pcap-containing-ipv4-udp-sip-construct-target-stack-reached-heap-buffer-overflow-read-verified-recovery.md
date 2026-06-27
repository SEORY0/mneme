---
type: causal-policy
title: "Pcap Containing Ipv4 UDP SIP Construct Target Stack Reached Heap Buffer Overflow Read Verified Recovery"
description: "Round 16 verified recovery for generic_crash with verifier signal target_stack_reached."
failure_class: "generic_crash"
verifier_signal: "target_stack_reached"
candidate_family: "construct"
input_format: "pcap containing IPv4/UDP/SIP"
harness_convention: "libfuzzer pcap file parser"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "target-stack-reached", "pcap-containing-ipv4-udp-sip", "construct", "verified-recovery", "round-16"]
match_keys: ["generic_crash", "target_stack_reached", "pcap containing IPv4/UDP/SIP", "libfuzzer pcap file parser", "heap-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 16
---
# Pcap Containing Ipv4 UDP SIP Construct Target Stack Reached Heap Buffer Overflow Read Verified Recovery

## Policy
For `generic_crash x target_stack_reached`, preserve the format and harness gates that reached the parser/sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
- Build a structurally valid pcap with one Ethernet, IPv4, and UDP packet using a SIP port. Make the UDP payload a recognized SIP request method whose method parser accepts the token but whose total SIP payload length is shorter than the derived URI offset, causing the version search length to underflow while all lower packet layers remain valid.
- Keep the carrier abstract: preserve the gate/invariant relation, not any task-local bytes or offsets.
- If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- The pcap wrapper requires a normal pcap global header and a packet record containing link-layer, IPv4, UDP, and payload bytes. UDP source or destination port controls whether PcapPlusPlus dispatches the payload to SIP parsing.
- Harness: The fuzzer writes the raw input to a temporary pcap file, opens it with PcapPlusPlus, reads the first packet, parses it into protocol layers, and closes the reader. The raw PoC is the complete pcap file, not just packet payload.

## Negative Memory
- Do not broaden mutations after the parser/harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store raw payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-16 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin.
