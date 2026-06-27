---
type: causal-policy
title: "Ipv4 Tcp Http Response Construct Target Sink Stack Buffer Overflow Stack Buffer Overflow Read Verified Recovery"
description: "Round 13 verified recovery for generic_crash with verifier signal target_sink_stack_buffer_overflow."
failure_class: "generic_crash"
verifier_signal: "target_sink_stack_buffer_overflow"
candidate_family: "construct"
input_format: "ipv4-tcp-http-response"
harness_convention: "libfuzzer-ndpi-process-packet"
vuln_class: "stack-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "target-sink-stack-buffer-overflow", "ipv4-tcp-http-response", "construct", "verified-recovery", "round-13"]
match_keys: ["generic_crash", "target_sink_stack_buffer_overflow", "ipv4-tcp-http-response", "libfuzzer-ndpi-process-packet", "stack-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 13
---
# Ipv4 Tcp Http Response Construct Target Sink Stack Buffer Overflow Stack Buffer Overflow Read Verified Recovery

## Policy
For `generic_crash x target_sink_stack_buffer_overflow`, preserve the format and harness gates that reached the parser/sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Build a single IPv4/TCP packet whose payload is an HTTP response. Include a server header for a recognized server family with an obsolete dotted version prefix, then continue the version token long enough that the local fixed-size version buffer is filled without a terminator. This reaches the obsolete-server risk formatting path, where the unterminated version token is read past the stack buffer.
2. Keep the carrier abstract: preserve the gate/invariant relation, not task-local bytes, exact offsets, checksums, or submit metadata.
3. If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- The selected nDPI target consumes a raw layer-three packet, not an Ethernet frame or pcap. For HTTP response parsing, the packet needs an IPv4 header, TCP header, and printable HTTP response payload with CRLF-delimited headers. The server header value is parsed as a named server family followed by a version-like token.

## Harness Contract
- The fuzz_process_packet harness initializes one nDPI flow, calls ndpi_detection_process_packet once on the raw input bytes, then serializes detected flow data. It expects the input to start at the IP header; TCP payload begins after the header length encoded in the TCP data-offset field.

## Negative Memory
- Do not broaden mutations after the parser/harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store raw payload bytes, exact offsets, checksums, task-local identifiers, or submit metadata.

## Evidence Shape
- Support: one round-13 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin.
## Round 13 Reinforcement

- key: `generic_crash x target_sink_stack_buffer_overflow`
- candidate family: `construct`
- related format facts: [[ipv4-tcp-http-response]]
- related harness facts: [[libfuzzer-ndpi-process-packet]]

### Procedure Delta
Build a single IPv4/TCP packet whose payload is an HTTP response. Include a server header for a recognized server family with an obsolete dotted version prefix, then continue the version token long enough that the local fixed-size version buffer is filled without a terminator. This reaches the obsolete-server risk formatting path, where the unterminated version token is read past the stack buffer.

### Format Contract Delta
The selected nDPI target consumes a raw layer-three packet, not an Ethernet frame or pcap. For HTTP response parsing, the packet needs an IPv4 header, TCP header, and printable HTTP response payload with CRLF-delimited headers. The server header value is parsed as a named server family followed by a version-like token.

### Harness Contract Delta
The fuzz_process_packet harness initializes one nDPI flow, calls ndpi_detection_process_packet once on the raw input bytes, then serializes detected flow data. It expects the input to start at the IP header; TCP payload begins after the header length encoded in the TCP data-offset field.

### Evidence Shape
- Support: additional round-13 official target match.
- Scope: generator repair for the same failure-keyed basin.
