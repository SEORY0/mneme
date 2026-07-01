---
type: causal-policy
title: "UDP Rftap Btle Rf L2cap Avdtp Construct Generic Crash Parser Reached Wild Addr Read In Avdtp Wild Pointer Dereference Read Verified Recovery"
description: "Round 36 verified recovery for generic_crash with verifier signal parser_reached_wild_addr_read_in_avdtp."
failure_class: "generic_crash"
verifier_signal: "parser_reached_wild_addr_read_in_avdtp"
candidate_family: "construct"
input_format: "udp-rftap-btle-rf-l2cap-avdtp"
harness_convention: "libfuzzer-fuzzshark-ip-proto-udp"
vuln_class: "wild-pointer-dereference-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-wild-addr-read-in-avdtp", "udp-rftap-btle-rf-l2cap-avdtp", "libfuzzer-fuzzshark-ip-proto-udp", "construct", "wild-pointer-dereference-read", "verified-recovery", "round-36"]
match_keys: ["generic_crash", "parser_reached_wild_addr_read_in_avdtp", "udp-rftap-btle-rf-l2cap-avdtp", "libfuzzer-fuzzshark-ip-proto-udp", "wild-pointer-dereference-read", "generic-crash", "parser-reached-wild-addr-read-in-avdtp", "verified_recovery", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 36
---
# UDP Rftap Btle Rf L2cap Avdtp Construct Generic Crash Parser Reached Wild Addr Read In Avdtp Wild Pointer Dereference Read Verified Recovery

- key: `generic_crash x parser_reached_wild_addr_read_in_avdtp`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[udp-rftap-btle-rf-l2cap-avdtp]]
- related harness facts: [[libfuzzer-fuzzshark-ip-proto-udp]]

## Failure Shape
Route the UDP payload through the enabled RFtap heuristic and choose the pcap packet-data link type for Bluetooth LE RF capture. The Bluetooth RF metadata must mark the frame as a directed data-channel PDU so the downstream AVDTP dissector has a concrete packet direction. The embedded LE frame then carries a non-advertising access address, a complete L2CAP connectionless message, and an AVDTP signaling payload. This reaches the BTLE path that allocates ACL metadata without initializing disconnect-frame pointer fields, then AVDTP dereferences those fields while creating channel state.

## Policy
When `generic_crash x parser_reached_wild_addr_read_in_avdtp` appears for `udp-rftap-btle-rf-l2cap-avdtp` under `libfuzzer-fuzzshark-ip-proto-udp`, preserve the parser, format, and harness gates that the verifier proved before mutating the sink-specific relation. Treat official vulnerable/fixed divergence as the success gate; local crash labels are supporting signals only.

## Procedure
1. Start from the `[[udp-rftap-btle-rf-l2cap-avdtp]]` format contract and `[[libfuzzer-fuzzshark-ip-proto-udp]]` harness contract; keep recognition, dispatch selectors, lengths, and state setup coherent until parser reachability is stable.
2. Apply the causal relation from the failure shape before broad mutation or seed sweeping.
3. Change one invariant at a time: selector-to-subparser, declared length-to-available data, container count-to-record body, lifetime/ownership state, or allocation-size relation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image exits cleanly, rejects the relation, or otherwise avoids the target crash.

## Verifier Contract
This policy is ranked by one round-36 official target match. Re-rank or quarantine it if later use returns only clean exits, wrong sinks, wrapper-specific crashes, or fixed-image crashes.

## Negative Memory
- Do not corrupt the outer `udp-rftap-btle-rf-l2cap-avdtp` recognition gate while retargeting this signal.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: 1 server-verified round 36 solve after 9 attempts.
- Candidate family: construct.
- Scope: generator repair and retargeting only.
