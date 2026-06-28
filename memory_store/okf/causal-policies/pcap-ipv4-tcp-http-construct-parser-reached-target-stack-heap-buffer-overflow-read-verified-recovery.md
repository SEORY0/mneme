---
type: causal-policy
title: "Pcap Ipv4 Tcp Http Construct Parser Reached Target Stack Heap Buffer Overflow Read Verified Recovery"
description: "Round 8 verified recovery for generic_crash with verifier signal parser_reached_target_stack."
failure_class: "generic_crash"
verifier_signal: "parser_reached_target_stack"
candidate_family: "construct"
input_format: "pcap-ipv4-tcp-http"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-target-stack", "pcap-ipv4-tcp-http", "construct", "verified-recovery", "round-8"]
match_keys: ["generic_crash", "parser_reached_target_stack", "pcap-ipv4-tcp-http", "libfuzzer", "heap-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 8
---
# Pcap Ipv4 Tcp Http Construct Parser Reached Target Stack Heap Buffer Overflow Read Verified Recovery

## Policy
For `generic_crash x parser_reached_target_stack`, preserve the format and harness gates that reached the target path, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Build a valid pcap containing one Ethernet/IPv4/TCP packet on an HTTP port. Use an HTTP request first line that is recognized as HTTP but ends exactly at the logical TCP payload boundary, with no following header bytes. This makes the HTTP parser create a HeaderField at the end of the message; the vulnerable constructor computes a zero-sized field and then dereferences the end pointer, while the fixed build treats the zero-sized field as end-of-header.
2. Keep the carrier abstract: preserve the gate/invariant relation, not task-local bytes, offsets, checksums, or submission metadata.
3. If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- The harness input is a complete pcap file, not a raw packet. It needs a pcap global header, one packet record, an Ethernet IPv4 frame, a valid IPv4 total length, a TCP header, and an HTTP-looking payload on a port that PcapPlusPlus classifies as HTTP. The target parser uses the TCP payload as a text-based protocol message.
- Harness: The libFuzzer target writes the raw input bytes to a temporary pcap file, opens it with PcapFileReaderDevice, reads the first packet, constructs a parsed Packet, and only prints IPv4 addresses after parsing. There is no selector byte or FuzzedDataProvider carving.

## Negative Memory
- Do not broaden mutations after the parser/harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store raw payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-8 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin.
