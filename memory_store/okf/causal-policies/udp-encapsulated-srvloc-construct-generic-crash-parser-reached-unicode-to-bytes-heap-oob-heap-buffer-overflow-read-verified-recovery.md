---
type: causal-policy
title: "UDP Encapsulated Srvloc Construct Generic Crash Parser Reached Unicode To Bytes Heap Oob Heap Buffer Overflow Read Verified Recovery"
description: "Round 32 server-verified recovery for udp-encapsulated-srvloc keyed by generic_crash x parser_reached_unicode_to_bytes_heap_oob."
failure_class: "generic_crash"
verifier_signal: "parser_reached_unicode_to_bytes_heap_oob"
candidate_family: "construct"
input_format: "udp-encapsulated-srvloc"
harness_convention: "libfuzzer-fuzzshark-ip-proto-udp"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-unicode-to-bytes-heap-oob", "udp-encapsulated-srvloc", "libfuzzer-fuzzshark-ip-proto-udp", "construct", "heap-buffer-overflow-read", "verified-recovery", "round-32"]
match_keys: ["generic-crash", "parser-reached-unicode-to-bytes-heap-oob", "udp-encapsulated-srvloc", "libfuzzer-fuzzshark-ip-proto-udp", "construct", "heap-buffer-overflow-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 32
---
# UDP Encapsulated Srvloc Construct Generic Crash Parser Reached Unicode To Bytes Heap Oob Heap Buffer Overflow Read Verified Recovery

- key: `generic_crash x parser_reached_unicode_to_bytes_heap_oob`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[udp-encapsulated-srvloc]]
- related harness facts: [[libfuzzer-fuzzshark-ip-proto-udp]]

## Policy
When `udp-encapsulated-srvloc` under `[[libfuzzer-fuzzshark-ip-proto-udp]]` produces `parser_reached_unicode_to_bytes_heap_oob` from `generic_crash`, keep the parser-reaching envelope and retarget the causal invariant that the official verifier accepted. Local sink labels are advisory once the vulnerable image fails and the fixed image stays clean or the server reports target match.

## Procedure
1. Preserve the harness and format contract that reached the parser: `[[udp-encapsulated-srvloc]]` through `[[libfuzzer-fuzzshark-ip-proto-udp]]`.
2. Apply the verified recovery: Use the fuzzshark UDP envelope, not a bare SRVLOC message: provide a minimal UDP datagram whose port dispatch selects the SRVLOC dissector. Inside the UDP payload, build a structurally valid SLP version-1 Attribute Reply with UTF-8 encoding and a non-empty attribute list that reaches the service-address parser. In the address-like subfield consumed by the endian-swapping helper, keep the surrounding record shape valid but make the copied text start with a zero byte followed by nonzero bytes, causing the vulnerable backward-scan logic to step before the allocated string buffer. The fixed build bounds this index movement and exits cleanly.
3. Keep mutations narrow around the gate/invariant relation rather than rebuilding unrelated carriers or adding broad random noise.
4. If local labels report a non-target sink while the parser branch is reached, submit one minimized candidate before discarding it.
5. Reject both-image crashes, fixed-image crashes, parser rejection, and clean exits as non-success even when they look close locally.

## Format Contract
- The active carrier is a UDP datagram containing an SRVLOC/SLP message. The UDP header length and one SRVLOC port are reachability gates. SLP version 1 uses a fixed header with version, function, packet length, flags, dialect, language, encoding, and transaction id, followed by function-specific fields. Attribute Reply carries an error field, an attribute-list length, and attribute-list bytes; the UTF-8 service-address parsing path eventually calls an endian-swapping byte conversion helper for an address component.

## Harness Contract
- The fuzzshark binary is configured for the UDP dissector in the IP protocol table. The raw libFuzzer bytes are treated as a UDP datagram by a postdissector path; there is no IP header, pcap wrapper, leading selector, or FuzzedDataProvider layout. UDP source or destination port dispatches the remaining payload to the SRVLOC dissector.

## Negative Memory
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.
- Do not treat parser reachability alone as success without the official target-match signal.
- Do not repeat a clean-exit or both-image-crash basin once the verifier has characterized it.

## Evidence Shape
- Support: one server-verified Round 32 solve.
- Candidate family: construct.
