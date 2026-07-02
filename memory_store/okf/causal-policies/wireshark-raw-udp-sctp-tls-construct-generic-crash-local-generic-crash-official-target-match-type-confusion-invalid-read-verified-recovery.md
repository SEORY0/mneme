---
type: causal-policy
title: "Wireshark Raw Udp Sctp Tls Construct Generic Crash Local Generic Crash Official Target Match Type Confusion Invalid Read Verified Recovery"
description: "Server-verified recovery for wireshark-raw-udp-sctp-tls when generic_crash pairs with local_generic_crash_official_target_match."
failure_class: "generic_crash"
verifier_signal: "local_generic_crash_official_target_match"
candidate_family: "construct"
input_format: "wireshark-raw-udp-sctp-tls"
harness_convention: "libfuzzer-fuzzshark-ip-proto-udp"
vuln_class: "type-confusion-invalid-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "local-generic-crash-official-target-match", "wireshark-raw-udp-sctp-tls", "libfuzzer-fuzzshark-ip-proto-udp", "construct", "verified-recovery", "round-33"]
match_keys: ["generic-crash", "local-generic-crash-official-target-match", "wireshark-raw-udp-sctp-tls", "libfuzzer-fuzzshark-ip-proto-udp", "construct", "type-confusion-invalid-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 33
---
# Wireshark Raw Udp Sctp Tls Construct Generic Crash Local Generic Crash Official Target Match Type Confusion Invalid Read Verified Recovery

- key: `generic_crash x local_generic_crash_official_target_match`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[wireshark-raw-udp-sctp-tls]]
- related harness facts: [[libfuzzer-fuzzshark-ip-proto-udp]]

## Policy
When `generic_crash x local_generic_crash_official_target_match` appears for `wireshark-raw-udp-sctp-tls`, preserve the parser and harness gates that were proven by the verifier before mutating the sink-specific relation. Treat official vulnerable-only target match as the success gate, not a local coarse crash label.

## Procedure
1. Use the `libfuzzer-fuzzshark-ip-proto-udp` harness contract and the `wireshark-raw-udp-sctp-tls` format contract before changing sink fields.
2. Recreate the causal relation from the verified trace: Feed fuzzshark's UDP target a valid UDP datagram that selects the SCTP-over-UDP tunneling path. Inside the SCTP payload, use a complete DATA chunk whose SCTP application port is associated with TLS, while keeping the SCTP payload protocol identifier nonzero and not claimed by a PPI-specific dissector. SCTP then dispatches TLS through its port table and passes the PPI-derived pointer as the dissector data argument; vulnerable TLS treats that non-string pointer as an application-dissector name before record parsing, while the fixed build rejects the mismatched data type.
3. Keep lengths, dispatch selectors, structural checks, and state setup coherent until the target parser state is reached.
4. Submit only after the fixed image exits cleanly or rejects the relation while the vulnerable image reaches the target sink.

## Format Contract
Use [[wireshark-raw-udp-sctp-tls]]. For this carrier, the outer bytes are a raw UDP datagram with a normal UDP header and payload. UDP port dispatch can select SCTP's UDP tunneling dissector. SCTP uses a common header followed by padded chunks; a complete DATA chunk carries a TSN, stream identifiers, a payload protocol identifier, and application payload. SCTP upper-layer dissection checks the PPI table before falling back to source and destination SCTP port tables, so an unclaimed nonzero PPI plus a TLS-associated SCTP port reaches TLS with non-null SCTP metadata as the data argument.

## Harness Contract
Use [[libfuzzer-fuzzshark-ip-proto-udp]]. The oss-fuzzshark libFuzzer binary is compiled for the UDP dissector selected from the IP protocol table and registers that handle as a postdissector. The submitted bytes are passed directly as the UDP dissector's tvb; there is no Ethernet, IP, pcap, or FuzzedDataProvider wrapper. The fuzzer disables recursive network dissectors such as IP while keeping UDP's normal port-table and heuristic dispatch behavior.

## Evidence Shape
- Support: 1 server-verified round 33 solve.
- Candidate family: construct.
- Verifier key: `generic_crash x local_generic_crash_official_target_match`.
- Vulnerability class: `type-confusion-invalid-read`.
- Recovery summary: Feed fuzzshark's UDP target a valid UDP datagram that selects the SCTP-over-UDP tunneling path. Inside the SCTP payload, use a complete DATA chunk whose SCTP application port is associated with TLS, while keeping the SCTP payload protocol identifier nonzero and not claimed by a PPI-specific dissector. SCTP then dispatches TLS through its port table and passes the PPI-derived pointer as the dissector data argument; vulnerable TLS treats that non-string pointer as an application-dissector name before record parsing, while the fixed build rejects the mismatched data type.

## Negative Memory
- Do not count parser reachability, both-image crashes, local-only wrapper crashes, clean exits, or fixed-image crashes as success for this key.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.
