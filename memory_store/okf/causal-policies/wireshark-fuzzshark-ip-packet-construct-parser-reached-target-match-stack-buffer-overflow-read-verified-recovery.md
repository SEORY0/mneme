---
type: causal-policy
title: "Wireshark Fuzzshark Ip Packet Construct Parser Reached Target Match Stack Buffer Overflow Read Verified Recovery"
description: "Round 27 verified recovery for generic_crash with verifier signal parser_reached_target_match."
failure_class: "generic_crash"
verifier_signal: "parser_reached_target_match"
candidate_family: "construct"
input_format: "wireshark-fuzzshark-ip-packet"
harness_convention: "libfuzzer"
vuln_class: "stack-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-target-match", "wireshark-fuzzshark-ip-packet", "libfuzzer", "construct", "stack-buffer-overflow-read", "verified-recovery", "round-27"]
match_keys: ["generic_crash", "parser_reached_target_match", "wireshark-fuzzshark-ip-packet", "libfuzzer", "stack-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 27
---
# Wireshark Fuzzshark Ip Packet Construct Parser Reached Target Match Stack Buffer Overflow Read Verified Recovery

## Policy
For `generic_crash x parser_reached_target_match`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Use the raw fuzzshark IP packet contract rather than a capture-file wrapper.
2. The packet must drive nested IP-family dissection through a tunnel/PPP/UDP-like chain into an IEEE 802.15.4 frame, then into Zigbee NWK and APS.
3. Within the APS command path, include a transport-key command that causes a key to be added when the per-PAN Zigbee keyring already has an entry, so the vulnerable key comparison reads from the key pointer object rather than the key bytes.
4. Keep the carrier abstract: preserve the gate/invariant relation, not any task-local bytes or offsets.
5. If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- The effective input is a raw packet buffer for Wireshark fuzzshark's IP target.
- A successful carrier can nest protocol dispatch through IP-family headers and a SCOP/IEEE 802.15.4 no-FCS frame before Zigbee NWK and APS parsing.
- The Zigbee APS transport-key command carries a key type followed by a fixed-length key and descriptor fields; the NWK layer supplies PAN hints used by the keyring lookup.
- Harness [[libfuzzer]]:
  - The container wrapper runs the libFuzzer-built fuzzshark IP target on the file copied to the fixed input path.
  - The harness initializes Wireshark, registers the configured IP dissector as a postdissector, wraps the raw file bytes as one synthetic packet record, and calls epan dissection.
  - There is no pcap envelope, mode byte, checksum repair, stdin contract, or FuzzedDataProvider front/back carving.

## Negative Memory
- Do not broaden mutations after the parser or harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-27 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[wireshark-fuzzshark-ip-packet]] and [[libfuzzer]].
