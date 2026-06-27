---
type: causal-policy
title: "Ipv4 Udp CAPWAP Construct Parser Reached Target Sink Heap Buffer Overflow Read Verified Recovery"
description: "Round 15 server-verified recovery for ipv4-udp-capwap keyed by generic_crash x parser_reached_target_sink."
failure_class: "generic_crash"
verifier_signal: "parser_reached_target_sink"
candidate_family: "construct"
input_format: "ipv4-udp-capwap"
harness_convention: "afl-libfuzzer-raw-packet"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-target-sink", "ipv4-udp-capwap", "afl-libfuzzer-raw-packet", "construct", "heap-buffer-overflow-read", "verified-recovery", "round-15"]
match_keys: ["generic_crash", "parser_reached_target_sink", "ipv4-udp-capwap", "afl-libfuzzer-raw-packet", "heap-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 15
---
# Ipv4 Udp CAPWAP Construct Parser Reached Target Sink Heap Buffer Overflow Read Verified Recovery

- key: `generic_crash x parser_reached_target_sink`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[ipv4-udp-capwap]]
- related harness facts: [[afl-libfuzzer-raw-packet]]

## Policy
When `ipv4-udp-capwap` under `afl-libfuzzer-raw-packet` reaches `parser_reached_target_sink` from `generic_crash`, preserve the accepted parser carrier and retarget only the causal invariant proven by the verifier. Treat local coarse labels as advisory once the vulnerable image fails and the fixed image does not reproduce the target behavior.

## Procedure
1. Preserve the harness contract and format family that reached the parser; do not switch envelopes after reachability is proven.
2. Construct a structurally valid IPv4 UDP packet that nDPI accepts as a UDP flow, select the
   CAPWAP control port, and keep the CAPWAP payload shorter than the later fixed-field read while
   satisfying the initial payload-byte branch. This reaches CAPWAP detection and violates the
   invariant that the payload must contain the control message fields before they are read.
3. Keep mutations focused on the relevant invariant: parser selection, declared length versus available content, selector versus subparser, table count versus records, lifetime ownership, or sink-specific state.
4. If local labels report a non-target sink while the parser branch is reached, submit once before discarding the candidate.
5. If the fixed image also fails, shrink to the smallest boundary relation and avoid broad randomization.

## Format Contract
- The fuzzer input begins at an IP header, not at an Ethernet or pcap wrapper. UDP protocol selection
  comes from the IP protocol field and UDP header. CAPWAP detection keys on UDP control or data ports
  and then interprets the UDP payload as a CAPWAP control/data header with fixed-width fields.

## Harness Contract
- The packet fuzzer passes raw file bytes directly to ndpi_detection_process_packet as one packet.
  There is no pcap framing, argv layer, mode selector, checksum repair requirement, or
  FuzzedDataProvider carving.

## Negative Memory
- Do not replay unrelated seeds after this parser branch is reached.
- Do not count fixed-image crashes, both-image crashes, clean exits, parser rejection, or off-target local stacks as success.
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.

## Evidence Shape
- Support: one server-verified Round 15 solve.
- Candidate family: construct.
