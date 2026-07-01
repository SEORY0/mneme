---
type: causal-policy
title: "Wireshark Raw Udp Ieee1722 Acf Lin Construct Wrong Sink Parser Reached Sink Mismatch Heap Buffer Overflow Read Verified Recovery"
description: "Round 34 verified recovery for wireshark-raw-udp-ieee1722-acf-lin when wrong_sink pairs with parser_reached_sink_mismatch."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_sink_mismatch"
candidate_family: "construct"
input_format: "wireshark-raw-udp-ieee1722-acf-lin"
harness_convention: "libfuzzer-fuzzshark-ip-proto-udp"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-sink-mismatch", "wireshark-raw-udp-ieee1722-acf-lin", "libfuzzer-fuzzshark-ip-proto-udp", "construct", "verified-recovery", "round-34"]
match_keys: ["wrong-sink", "parser-reached-sink-mismatch", "wireshark-raw-udp-ieee1722-acf-lin", "libfuzzer-fuzzshark-ip-proto-udp", "construct", "heap-buffer-overflow-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 34
---
# Wireshark Raw Udp Ieee1722 Acf Lin Construct Wrong Sink Parser Reached Sink Mismatch Heap Buffer Overflow Read Verified Recovery

- key: `wrong_sink x parser_reached_sink_mismatch`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[wireshark-raw-udp-ieee1722-acf-lin]]
- related harness facts: [[libfuzzer-fuzzshark-ip-proto-udp]]

## Round 34 Verified Support

- key: `wrong_sink x parser_reached_sink_mismatch`
- outcome: server-verified vulnerable/fixed split
- candidate family: `construct`
- vulnerability class: `heap-buffer-overflow-read`
- related format facts: [[wireshark-raw-udp-ieee1722-acf-lin]]
- related harness facts: [[libfuzzer-fuzzshark-ip-proto-udp]]

### Policy
When `wrong_sink x parser_reached_sink_mismatch` appears for `wireshark-raw-udp-ieee1722-acf-lin`, preserve the accepted parser and harness gates, then target the specific state relation that the verifier proved. Treat the official vulnerable-only target match as the success gate; local crash class alone is not enough.

### Procedure
1. Use the [[libfuzzer-fuzzshark-ip-proto-udp]] harness contract and the [[wireshark-raw-udp-ieee1722-acf-lin]] format contract before changing sink fields.
2. Recreate the verified causal relation: Construct a raw UDP datagram that dispatches to the IEEE 1722 dissector, then select an AVTP timing-control path carrying an ACF LIN record. Keep the outer and ACF record lengths self-consistent, but choose the LIN padding/remaining-payload relation so the dissector computes a negative remaining payload and formats bytes before enforcing the payload length bounds.
3. Keep selectors, lengths, state setup, and container invariants coherent until the target parser state is reached.
4. Submit only when the candidate is expected to preserve the vulnerable/fixed split rather than a generic both-build crash.

### Format Contract
For this harness the file is the UDP datagram seen by Wireshark, not an Ethernet or IP frame. The UDP header drives dissector-table dispatch. The IEEE 1722 payload has a common AVTP subtype header, a timing-control header, then ACF records; each ACF record has a message type and quadlet-count length, and the LIN record carries a small fixed header followed by payload bytes whose effective length is reduced by a pad field.

### Harness Contract
The active wrapper is the fuzzshark UDP-protocol harness. It feeds the raw input as a UDP packet to Wireshark's IP-protocol UDP dissector; the source and destination ports influence subdissector selection, and no leading fuzzer selector or file container is present.

### Evidence Shape
- Support: one server-verified round 34 solve.
- Candidate family: `construct`.
- Verifier key: `wrong_sink x parser_reached_sink_mismatch`.
- Vulnerability class: `heap-buffer-overflow-read`.

## Negative Memory
- Do not count parser reachability, both-image crashes, fixed-image crashes, local wrapper crashes, clean exits, or off-target sanitizer crashes as success for this key.
- Do not store concrete payload bytes, exact positions, task identifiers, checksums, or submit metadata.
