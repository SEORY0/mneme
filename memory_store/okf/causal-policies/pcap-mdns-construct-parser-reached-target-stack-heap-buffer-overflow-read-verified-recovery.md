---
type: causal-policy
title: "Pcap Mdns Construct Parser Reached Target Stack Heap Buffer Overflow Read Verified Recovery"
description: "Round 27 verified recovery for wrong_sink with verifier signal parser_reached_target_stack."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_stack"
candidate_family: "construct"
input_format: "pcap-mdns"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-target-stack", "pcap-mdns", "libfuzzer", "construct", "heap-buffer-overflow-read", "verified-recovery", "round-27"]
match_keys: ["wrong_sink", "parser_reached_target_stack", "pcap-mdns", "libfuzzer", "heap-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 27
---
# Pcap Mdns Construct Parser Reached Target Stack Heap Buffer Overflow Read Verified Recovery

## Policy
For `wrong_sink x parser_reached_target_stack`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. The input had to be a complete classic pcap whose linktype and packet headers made ntopng dispatch a Linux-cooked IPv4 TCP packet to the MDNS protocol path.
2. The packet used a captured-frame length larger than the IPv4 total length so the parser's trusted payload stayed small while the pcap buffer still contained trailing frame padding.
3. Inside a response-shaped MDNS payload, a TXT answer declared a large data length and placed sparse TXT segment lengths through that padding so the vulnerable loop advanced the copy source to the end of the pcap reader allocation before copying.
4. Keep the carrier abstract: preserve the gate/invariant relation, not any task-local bytes or offsets.
5. If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- The harness accepts classic pcap, not a raw IP or UDP datagram.
- The global header selects the datalink, each packet record supplies captured and wire lengths, and ntopng trims L4 trust using the IPv4 total length when the captured frame contains padding.
- The MDNS dissector expects a response bit in the DNS flags, derives the number of records from the answer/authority/additional counts, parses DNS-style names, and treats TXT RDATA as a sequence of length-prefixed strings.
- Harness [[libfuzzer]]:
  - The libFuzzer input is opened with libpcap through an in-memory file and must contain a valid pcap stream.
  - The harness sets the interface datalink from the pcap global header, iterates packets with pcap_next_ex, and passes each captured packet plus its pcap header directly to NetworkInterface::dissectPacket.

## Negative Memory
- Do not broaden mutations after the parser or harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-27 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[pcap-mdns]] and [[libfuzzer]].
