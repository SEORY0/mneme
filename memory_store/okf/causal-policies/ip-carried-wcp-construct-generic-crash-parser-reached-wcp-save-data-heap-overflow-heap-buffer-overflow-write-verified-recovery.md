---
type: causal-policy
title: "Ip Carried Wcp Construct Generic Crash Parser Reached Wcp Save Data Heap Overflow Heap Buffer Overflow Write Verified Recovery"
description: "Round 34 verified recovery for ip-carried-wcp when generic_crash pairs with parser_reached_wcp_save_data_heap_overflow."
failure_class: "generic_crash"
verifier_signal: "parser_reached_wcp_save_data_heap_overflow"
candidate_family: "construct"
input_format: "ip-carried-wcp"
harness_convention: "afl-libfuzzer-wrapper"
vuln_class: "heap-buffer-overflow-write"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-wcp-save-data-heap-overflow", "ip-carried-wcp", "afl-libfuzzer-wrapper", "construct", "verified-recovery", "round-34"]
match_keys: ["generic-crash", "parser-reached-wcp-save-data-heap-overflow", "ip-carried-wcp", "afl-libfuzzer-wrapper", "construct", "heap-buffer-overflow-write", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 34
---
# Ip Carried Wcp Construct Generic Crash Parser Reached Wcp Save Data Heap Overflow Heap Buffer Overflow Write Verified Recovery

- key: `generic_crash x parser_reached_wcp_save_data_heap_overflow`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[ip-carried-wcp]]
- related harness facts: [[afl-libfuzzer-wrapper]]

## Round 34 Verified Support

- key: `generic_crash x parser_reached_wcp_save_data_heap_overflow`
- outcome: server-verified vulnerable/fixed split
- candidate family: `construct`
- vulnerability class: `heap-buffer-overflow-write`
- related format facts: [[ip-carried-wcp]]
- related harness facts: [[afl-libfuzzer-wrapper]]

### Policy
When `generic_crash x parser_reached_wcp_save_data_heap_overflow` appears for `ip-carried-wcp`, preserve the accepted parser and harness gates, then target the specific state relation that the verifier proved. Treat the official vulnerable-only target match as the success gate; local crash class alone is not enough.

### Procedure
1. Use the [[afl-libfuzzer-wrapper]] harness contract and the [[ip-carried-wcp]] format contract before changing sink fields.
2. Recreate the verified causal relation: The fuzzshark target is IP-only, so direct WCP and GRE-with-WCP-type carriers miss the registered dissector. Wrap WCP in an IPv4 EtherIP packet so the payload is handed to Ethernet and then to WCP by ethertype. Use an uncompressed WCP data packet whose payload exceeds the sliding-window copy logic's single-wrap assumption; with the IPv4 total-length field in the TSO-style form, Wireshark uses the actual fuzzer buffer length and the WCP save path copies past the allocated window. The fixed build rejects the oversized relation cleanly.
3. Keep selectors, lengths, state setup, and container invariants coherent until the target parser state is reached.
4. Submit only when the candidate is expected to preserve the vulnerable/fixed split rather than a generic both-build crash.

### Format Contract
WCP has command bits in the leading header. The uncompressed-data command stores payload bytes into a per-conversation sliding window and treats the final byte as a check byte. WCP is registered under Ethernet ethertype and Frame Relay NLPID tables, not directly as an IPv4 next protocol or generic GRE payload.

### Harness Contract
The AFL-wrapped fuzzshark binary runs the IP dissector over the whole raw input file. There is no pcap envelope, no FuzzedDataProvider layout, and no mode selector. Nested protocol reachability depends on constructing a raw IP packet and then using normal IP subdissector handoff. IPv4 TSO-style total length allows the dissector to use the reported fuzzer buffer length rather than a small packet-length field.

### Evidence Shape
- Support: one server-verified round 34 solve.
- Candidate family: `construct`.
- Verifier key: `generic_crash x parser_reached_wcp_save_data_heap_overflow`.
- Vulnerability class: `heap-buffer-overflow-write`.

## Negative Memory
- Do not count parser reachability, both-image crashes, fixed-image crashes, local wrapper crashes, clean exits, or off-target sanitizer crashes as success for this key.
- Do not store concrete payload bytes, exact positions, task identifiers, checksums, or submit metadata.
