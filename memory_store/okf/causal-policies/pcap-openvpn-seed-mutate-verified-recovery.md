---
type: causal-policy
title: "PCAP Openvpn Seed Mutate Verified Recovery"
description: "Round 6 verified recovery for generic_crash with verifier signal parser_reached_target_stack."
failure_class: "generic_crash"
verifier_signal: "parser_reached_target_stack"
candidate_family: "seed_mutate"
input_format: "pcap-openvpn"
harness_convention: "afl-libfuzzer-wrapper"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-target-stack", "pcap-openvpn", "seed-mutate", "verified-recovery", "round-6"]
match_keys: ["generic_crash", "parser_reached_target_stack", "pcap-openvpn", "afl-libfuzzer-wrapper", "heap-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 6
---
# PCAP Openvpn Seed Mutate Verified Recovery

## Policy
For `generic_crash x parser_reached_target_stack`, preserve the format and harness gates that reached the parser/sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Start from an in-repo OpenVPN capture that already establishes a bidirectional flow and reaches the OpenVPN dissector. Preserve the first hard-reset packet that stores the session id, then mutate only the server-side packet-id-array length relation so the later session-id comparison reads past the captured packet payload. The fixed build rejects the inconsistent packet before the compare.
2. Keep the carrier abstract: preserve the gate/invariant relation, not any task-local bytes or offsets.
3. If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- The input is a complete pcap file with a standard capture header and packet records. OpenVPN over TCP carries a transport length prefix before the OpenVPN opcode and session fields; the vulnerable dissector tracks the client session id across packets and later uses a packet-id-array length field to locate the remote session id in the server packet.
- Harness: The AFL-style reader fuzzer writes the raw input to a temporary pcap file, opens it with libpcap, allocates an exact-size buffer for each captured packet, and feeds packets through the normal nDPI workflow with tunnel decoding enabled.

## Negative Memory
- Do not broaden mutations after the parser/harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store raw payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-6 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin.
