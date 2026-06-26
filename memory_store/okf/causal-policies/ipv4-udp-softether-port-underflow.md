---
type: causal-policy
title: IPv4 UDP SoftEther Port Underflow Recovery
description: Verified recovery for generic_crash with parser_reached_target_sink on ipv4-udp-packet inputs.
failure_class: generic_crash
verifier_signal: parser_reached_target_sink
candidate_family: construct
input_format: ipv4-udp-packet
harness_convention: libfuzzer
vuln_class: heap-buffer-overflow-read
access_scope: generate
success_count: 1
confidence: medium
tags: [generic-crash, parser-reached-target-sink, construct, ipv4-udp-packet, heap-buffer-overflow-read, verified-recovery]
match_keys: [generic-crash, parser-reached-target-sink, ipv4-udp-packet, heap-buffer-overflow-read]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
---
# IPv4 UDP SoftEther Port Underflow Recovery

- key: `generic_crash x parser_reached_target_sink`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[ipv4-udp-packet]]

## Failure Shape
Build a valid network packet envelope so the DPI fuzzer exposes an application payload to
the SoftEther dissector. Use the dissector's key/value address-and-port form with a short
address component followed by the port marker; the vulnerable port-length calculation
underflows from the separator position and copies more bytes than the remaining payload
contains.

## Policy
For `generic_crash x parser_reached_target_sink` on `ipv4-udp-packet`, preserve the parser and harness gate first, then mutate
only the causal invariant described by the verified trace. Prefer the candidate family `construct`
when the carrier is available because this shape was server-confirmed against vulnerable and fixed
builds.

## Procedure
1. Build a valid IPv4 and UDP envelope so the fuzzer exposes the payload to the application
dissector.
2. Use the dissector's address-and-port key/value form rather than arbitrary UDP bytes.
3. Make the address component short and place the port marker so separator arithmetic
underflows or overreads the remaining payload.
4. If the packet is processed cleanly, preserve IP/UDP lengths and vary only the SoftEther
field relation.

## Verifier Contract
The local signal may remain coarse. Keep candidates that reach the named parser or sink and
use the official vulnerable-versus-fixed comparison as the target-match gate.

## Negative Memory
- Do not target raw UDP reachability alone; protocol classification must select the SoftEther
branch.
- Do not break outer length fields while editing the application payload boundary.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified solve.
- Scope: generator repair only.
