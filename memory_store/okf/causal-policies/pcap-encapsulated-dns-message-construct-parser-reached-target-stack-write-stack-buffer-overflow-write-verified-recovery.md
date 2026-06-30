---
type: causal-policy
title: "Pcap Encapsulated Dns Message Construct Parser Reached Target Stack Write Stack Buffer Overflow Write Verified Recovery"
description: "Round 29 verified recovery for wrong_sink with verifier signal parser_reached_target_stack_write."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_stack_write"
candidate_family: "construct"
input_format: "pcap-encapsulated-dns-message"
harness_convention: "libfuzzer"
vuln_class: "stack-buffer-overflow-write"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-target-stack-write", "pcap-encapsulated-dns-message", "libfuzzer", "construct", "stack-buffer-overflow-write", "verified-recovery", "round-29"]
match_keys: ["wrong_sink", "parser_reached_target_stack_write", "pcap-encapsulated-dns-message", "libfuzzer", "stack-buffer-overflow-write", "wrong-sink", "parser-reached-target-stack-write", "pcap-encapsulated-dns-message", "libfuzzer", "stack-buffer-overflow-write", "verified_recovery", "construct", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 29
---
# Pcap Encapsulated Dns Message Construct Parser Reached Target Stack Write Stack Buffer Overflow Write Verified Recovery

- key: `wrong_sink x parser_reached_target_stack_write`
- outcome: verified target match / recovery policy
- success_count: 1
- related format facts: [[pcap-encapsulated-dns-message]]
- related harness facts: [[libfuzzer]]

## Policy
For `wrong_sink x parser_reached_target_stack_write` on `pcap-encapsulated-dns-message`, keep the parser and harness gates that produced the verifier signal, then vary only the causal relation described below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Build a complete classic pcap containing one Ethernet/IPv4/UDP packet on a DNS port. Keep the DNS header and record metadata ordinary, then make a resource owner name whose label-decoded text exactly fills the decoder's fixed stack buffer and leaves the last decoded character as a label separator so the trailing terminator write lands just past the buffer.
2. Preserve format recognition and the harness input contract while mutating the narrow sink invariant; do not broaden into an off-target crash or a both-image crash.
3. If later verifier output changes the failure key, re-rank against that new key before mutating unrelated fields.

## Format Contract
- Format [[pcap-encapsulated-dns-message]]: Classic pcap inputs need a valid global header, a packet record with matching captured/original lengths, and an Ethernet frame when the link type is Ethernet. PcapPlusPlus then parses IPv4, UDP, and DNS when a UDP endpoint uses a DNS port and the DNS payload has a plausible header. DNS names are length-label encoded and records follow the fixed DNS header according to the question, answer, authority, and additional counters.
- Harness [[libfuzzer]]: The libFuzzer target writes the entire input buffer to a temporary pcap file, opens it through PcapPlusPlus' pcap reader, reads only the first packet, and constructs a parsed packet from those captured bytes. There is no FuzzedDataProvider split or selector byte; the bytes must be a structurally complete pcap file.

## Negative Memory
- Do not corrupt the outer `pcap-encapsulated-dns-message` recognition gate while retargeting this signal.
- Do not count parser reachability, clean exits, fixed-image crashes, both-image crashes, or local wrong-sink labels as success without official target match.
- Never store payload bytes, exact positions, checksums, submit metadata, or task-local identifiers.

## Evidence Shape
- Support: one round-29 worker trace with official target match.
- Scope: generator repair and retargeting only; pair with [[pcap-encapsulated-dns-message]] and [[libfuzzer]].
