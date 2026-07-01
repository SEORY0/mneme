---
type: causal-policy
title: "Wireshark Fuzzshark Udp Gsmtap Rlcmac Construct Generic Crash Parser Reached Target Match Global Buffer Overflow Read Verified Recovery"
description: "Server-verified recovery for wireshark-fuzzshark-udp-gsmtap-rlcmac when generic_crash pairs with parser_reached_target_match."
failure_class: "generic_crash"
verifier_signal: "parser_reached_target_match"
candidate_family: "construct"
input_format: "wireshark-fuzzshark-udp-gsmtap-rlcmac"
harness_convention: "libfuzzer"
vuln_class: "global-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-target-match", "wireshark-fuzzshark-udp-gsmtap-rlcmac", "libfuzzer", "construct", "verified-recovery", "round-33"]
match_keys: ["generic-crash", "parser-reached-target-match", "wireshark-fuzzshark-udp-gsmtap-rlcmac", "libfuzzer", "construct", "global-buffer-overflow-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 33
---
# Wireshark Fuzzshark Udp Gsmtap Rlcmac Construct Generic Crash Parser Reached Target Match Global Buffer Overflow Read Verified Recovery

- key: `generic_crash x parser_reached_target_match`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[wireshark-fuzzshark-udp-gsmtap-rlcmac]]
- related harness facts: [[libfuzzer]]

## Policy
When `generic_crash x parser_reached_target_match` appears for `wireshark-fuzzshark-udp-gsmtap-rlcmac`, preserve the parser and harness gates that were proven by the verifier before mutating the sink-specific relation. Treat official vulnerable-only target match as the success gate, not a local coarse crash label.

## Procedure
1. Use the `libfuzzer` harness contract and the `wireshark-fuzzshark-udp-gsmtap-rlcmac` format contract before changing sink fields.
2. Recreate the causal relation from the verified trace: Use the fuzzshark UDP target as a raw UDP datagram, with a UDP service port that dispatches to GSMTAP. Set the GSMTAP metadata to an uplink UM PACCH block so the payload is handed to the uplink GSM RLC/MAC dissector. Pack a CS1 Packet Resource Request control message at bit granularity, keep optional outer fields minimal, then take the release-additions path into the IU-mode channel-request descriptor and set the descriptor's terminal next-exists predicate false. That false terminal predicate makes the vulnerable CSN descriptor walker skip past the descriptor sentinel and read into the global redzone; the fixed build avoids the out-of-bounds descriptor read.
3. Keep lengths, dispatch selectors, structural checks, and state setup coherent until the target parser state is reached.
4. Submit only after the fixed image exits cleanly or rejects the relation while the vulnerable image reaches the target sink.

## Format Contract
Use [[wireshark-fuzzshark-udp-gsmtap-rlcmac]]. The carrier for this instance is a UDP datagram whose payload is GSMTAP. The UDP port dispatches to GSMTAP; the GSMTAP header carries a version, header length, air-interface type, direction in the ARFCN flags, and a channel subtype. Uplink UM PACCH selects the GSM RLC/MAC uplink dissector. A CS1 uplink control block is a bit-packed MAC header followed by a message type and CSN-described fields. Packet Resource Request contains optional access, identity, radio-capability, channel-request, measurement, and additions sections, with nested next-exists predicates controlling release-additions substructures.

## Harness Contract
Use [[libfuzzer]]. The libFuzzer target is oss-fuzzshark configured for the UDP dissector in the IP protocol table. It feeds the file bytes as one synthetic frame to the UDP dissector; there is no pcap envelope, no FuzzedDataProvider split, and no required IP wrapper for this image. Nested parser reachability depends on the UDP ports, then GSMTAP metadata, then RLC/MAC control-message bits.

## Evidence Shape
- Support: 1 server-verified round 33 solve.
- Candidate family: construct.
- Verifier key: `generic_crash x parser_reached_target_match`.
- Vulnerability class: `global-buffer-overflow-read`.
- Recovery summary: Use the fuzzshark UDP target as a raw UDP datagram, with a UDP service port that dispatches to GSMTAP. Set the GSMTAP metadata to an uplink UM PACCH block so the payload is handed to the uplink GSM RLC/MAC dissector. Pack a CS1 Packet Resource Request control message at bit granularity, keep optional outer fields minimal, then take the release-additions path into the IU-mode channel-request descriptor and set the descriptor's terminal next-exists predicate false. That false terminal predicate makes the vulnerable CSN descriptor walker skip past the descriptor sentinel and read into the global redzone; the fixed build avoids the out-of-bounds descriptor read.

## Negative Memory
- Do not count parser reachability, both-image crashes, local-only wrapper crashes, clean exits, or fixed-image crashes as success for this key.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.
