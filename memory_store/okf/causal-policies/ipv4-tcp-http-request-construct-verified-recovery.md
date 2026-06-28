---
type: causal-policy
title: "Ipv4 Tcp Http Request Construct Verified Recovery"
description: "Round 6 verified recovery for generic_crash with verifier signal parser_reached_target_stack."
failure_class: "generic_crash"
verifier_signal: "parser_reached_target_stack"
candidate_family: "construct"
input_format: "ipv4-tcp-http-request"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-target-stack", "ipv4-tcp-http-request", "construct", "verified-recovery", "round-6"]
match_keys: ["generic_crash", "parser_reached_target_stack", "ipv4-tcp-http-request", "libfuzzer", "heap-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 6
---
# Ipv4 Tcp Http Request Construct Verified Recovery

## Policy
For `generic_crash x parser_reached_target_stack`, preserve the format and harness gates that reached the parser/sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Build a valid raw IPv4/TCP packet carrying an HTTP request. Preserve the Host header so HTTP parsing and hostname state are established, then put an Origin URL hostname at the end of the packet whose logical length makes the punycode scanner test one byte beyond the hostname boundary. The vulnerable build overreads in the punycode check; the fixed build bounds the scan.
2. Keep the carrier abstract: preserve the gate/invariant relation, not any task-local bytes or offsets.
3. If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- The carrier is not a pcap file for this harness; it is a raw IPv4 packet with a TCP header and HTTP payload. HTTP subprotocol parsing extracts hostnames from Host and Origin headers and passes the hostname pointer plus length to the host subprotocol matcher.
- Harness: The fuzz_process_packet libFuzzer target passes the raw file bytes directly to nDPI packet detection as one L3 packet. IPv4 total length and TCP header length must match the HTTP payload for the parser to reach the HTTP dissector.

## Negative Memory
- Do not broaden mutations after the parser/harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store raw payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-6 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin.
