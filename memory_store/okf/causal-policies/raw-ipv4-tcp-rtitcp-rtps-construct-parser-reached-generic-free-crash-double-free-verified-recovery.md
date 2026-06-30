---
type: causal-policy
title: "Raw Ipv4 Tcp Rtitcp Rtps Construct Parser Reached Generic Free Crash Double Free Verified Recovery"
description: "Round 28 verified recovery for wrong_sink with verifier signal parser_reached_generic_free_crash."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_generic_free_crash"
candidate_family: "construct"
input_format: "raw-ipv4-tcp-rtitcp-rtps"
harness_convention: "libfuzzer-fuzzshark-ip"
vuln_class: "double-free"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-generic-free-crash", "raw-ipv4-tcp-rtitcp-rtps", "libfuzzer-fuzzshark-ip", "construct", "double-free", "verified-recovery", "round-28"]
match_keys: ["wrong_sink", "parser_reached_generic_free_crash", "raw-ipv4-tcp-rtitcp-rtps", "libfuzzer-fuzzshark-ip", "double-free", "verified_recovery", "construct", "double-free"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 28
---
# Raw Ipv4 Tcp Rtitcp Rtps Construct Parser Reached Generic Free Crash Double Free Verified Recovery

## Policy
For `wrong_sink x parser_reached_generic_free_crash`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Use the fuzzshark IP contract: a raw IPv4 packet carrying TCP payload, not a pcap file. The TCP payload must be parsed as RTI-TCP and contain two RTI-TCP data messages, each carrying a minimal valid RTPS header. The first RTPS message creates and populates the TCP-context private table with packet-scope allocations; the second message inserts the same logical key again, causing the table's GLib free callback to collide with packet-scope wmem ownership. Keep IP/TCP framing internally consistent and avoid unrelated malformed packet fields.
2. Keep the carrier abstract: preserve the gate, invariant, and sink relation rather than task-local bytes, exact offsets, checksums, or identifiers.
3. If the verifier signal changes, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- Format [[raw-ipv4-tcp-rtitcp-rtps]]: The useful carrier is raw IPv4 with a TCP segment. RTI-TCP data messages wrap RTPS messages with a small control/length/magic header; RTPS itself starts with an ASCII magic, protocol version, vendor id, and a GUID prefix. A single RTPS-over-TCP message can parse cleanly; repeated RTPS messages in one TCP packet are needed to exercise replacement of the private-table entry.
- Harness [[libfuzzer-fuzzshark-ip]]: The image is configured as fuzzshark_ip. libFuzzer supplies the raw file bytes directly to Wireshark's frame dissector, and the selected IP dissector is run as a postdissector. The input is therefore a raw IPv4 packet; there is no pcap global header, no pcap record header, and no FuzzedDataProvider carving.

## Negative Memory
- Do not broaden mutations after parser or harness reachability is proven.
- Do not submit candidates that reproduce on the fixed image, crash both images, or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-28 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[raw-ipv4-tcp-rtitcp-rtps]] and [[libfuzzer-fuzzshark-ip]].
