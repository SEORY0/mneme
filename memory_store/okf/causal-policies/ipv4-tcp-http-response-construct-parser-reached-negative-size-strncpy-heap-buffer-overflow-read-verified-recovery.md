---
type: causal-policy
title: "Ipv4 Tcp Http Response Construct Parser Reached Negative Size Strncpy Heap Buffer Overflow Read Verified Recovery"
description: "Round 28 verified recovery for wrong_sink with verifier signal parser_reached_negative_size_strncpy."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_negative_size_strncpy"
candidate_family: "construct"
input_format: "ipv4-tcp-http-response"
harness_convention: "libfuzzer-ndpi-process-packet"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-negative-size-strncpy", "ipv4-tcp-http-response", "libfuzzer-ndpi-process-packet", "construct", "heap-buffer-overflow-read", "verified-recovery", "round-28"]
match_keys: ["wrong_sink", "parser_reached_negative_size_strncpy", "ipv4-tcp-http-response", "libfuzzer-ndpi-process-packet", "heap-buffer-overflow-read", "verified_recovery", "construct", "heap-buffer-overflow-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 28
---
# Ipv4 Tcp Http Response Construct Parser Reached Negative Size Strncpy Heap Buffer Overflow Read Verified Recovery

## Policy
For `wrong_sink x parser_reached_negative_size_strncpy`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Build one coherent raw IPv4/TCP packet whose TCP payload is an HTTP response. Include a Content-Type header so response content classification runs, then provide a Content-Disposition attachment filename field whose quoted filename marker has no filename body. The vulnerable filename-length arithmetic underflows the copy size passed to strncpy in the content classifier; the fixed build rejects or handles that boundary cleanly.
2. Keep the carrier abstract: preserve the gate, invariant, and sink relation rather than task-local bytes, exact offsets, checksums, or identifiers.
3. If the verifier signal changes, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- Format [[ipv4-tcp-http-response]]: The input is a raw layer-three IPv4 packet containing a TCP segment, not a pcap file and not an Ethernet frame. The IPv4 total length and TCP data offset must describe the packet consistently; the HTTP response payload must be printable and CRLF-delimited so nDPI parses response headers including Content-Type and Content-Disposition.
- Harness [[libfuzzer-ndpi-process-packet]]: The fuzz_process_packet libFuzzer target initializes one nDPI flow and passes the entire raw input buffer to ndpi_detection_process_packet. There is no FuzzedDataProvider layout, selector byte, or file container; TCP payload begins after the IP and TCP header lengths encoded in the packet itself.

## Negative Memory
- Do not broaden mutations after parser or harness reachability is proven.
- Do not submit candidates that reproduce on the fixed image, crash both images, or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-28 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[ipv4-tcp-http-response]] and [[libfuzzer-ndpi-process-packet]].
