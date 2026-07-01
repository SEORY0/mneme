---
type: negative-memory
title: "Wireshark Udp Dissector Payload Construct No Crash Udp Dissector Clean Exit Or Target Handoff Not Reached Global Buffer Overflow Read Negative Memory"
description: "Round 33 negative memory for no_crash with verifier signal udp_dissector_clean_exit_or_target_handoff_not_reached."
failure_class: "no_crash"
verifier_signal: "udp_dissector_clean_exit_or_target_handoff_not_reached"
candidate_family: "construct"
input_format: "wireshark-udp-dissector-payload"
harness_convention: "libfuzzer-fuzzshark-ip-proto-udp"
vuln_class: "global-buffer-overflow-read"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["no-crash", "udp-dissector-clean-exit-or-target-handoff-not-reached", "wireshark-udp-dissector-payload", "libfuzzer-fuzzshark-ip-proto-udp", "construct", "global-buffer-overflow-read", "negative-memory", "round-33"]
match_keys: ["no_crash", "udp_dissector_clean_exit_or_target_handoff_not_reached", "wireshark-udp-dissector-payload", "libfuzzer-fuzzshark-ip-proto-udp", "construct", "global-buffer-overflow-read", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 33
---
# Wireshark Udp Dissector Payload Construct No Crash Udp Dissector Clean Exit Or Target Handoff Not Reached Global Buffer Overflow Read Negative Memory

- key: `no_crash x udp_dissector_clean_exit_or_target_handoff_not_reached`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[wireshark-udp-dissector-payload]]
- related harness facts: [[libfuzzer-fuzzshark-ip-proto-udp]]

## Failure Shape
The active fuzzshark target was the UDP dissector reached through the IP protocol table, not a direct NOE or Bluetooth dissector. Direct Bluetooth ATT/GATT-shaped inputs were the wrong envelope. A UDP-to-UAUDP-to-UA-to-NOE-shaped envelope can be constructed, but the extracted source has the direct NOE UA handoff compiled out and the alternate NOE-over-SIP forwarding path is preference-gated, so the vulnerable NOE property lookup did not become reachable in this harness configuration during the attempt budget.

## Policy
Treat `no_crash x udp_dissector_clean_exit_or_target_handoff_not_reached` on `wireshark-udp-dissector-payload` as a basin to avoid unless a new candidate changes the parser gate, state relation, sink relation, or official differential behavior described below. Do not repeat variants that only preserve the same clean-exit, off-target, post-patch-crash, both-image-crash, or target-handoff-missing signal.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing relation from the verifier signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one causal relation at a time and discard candidates that return to `udp_dissector_clean_exit_or_target_handoff_not_reached`.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed vulnerable-only target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `udp_dissector_clean_exit_or_target_handoff_not_reached`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, clean exits, timeouts, or fixed-image crashes as success.
- Never store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[wireshark-udp-dissector-payload]]. The relevant vulnerable code is in the NOE property TLV decoder. NOE method bodies carry a class byte and then property TLVs; each TLV has a property code, optional array index, a short or extended property length, and property bytes. The vulnerable classification helpers search static UTF-8-property and Boolean-property key tables using class/property pairs, but those helpers are only useful after the UDP and UA/NOE dispatch gates have selected the NOE dissector.

## Harness Contract
Use [[libfuzzer-fuzzshark-ip-proto-udp]]. The fuzzshark binary reports configuration for the UDP dissector in the IP protocol table. The raw file is treated as a UDP datagram for that dissector, with UDP source or destination port dispatch selecting higher-level UDP protocols. There is no Ethernet/IP/pcap wrapper and no FuzzedDataProvider layout. Several unrelated protocol dissectors are disabled by fuzzshark preferences before the run.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 33 after 10 attempts.
- Scope: generator repair and basin avoidance only.
