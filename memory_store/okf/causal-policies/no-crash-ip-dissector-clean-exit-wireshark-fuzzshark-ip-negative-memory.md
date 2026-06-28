---
type: causal-policy
title: "No Crash Ip Dissector Clean Exit Wireshark Fuzzshark Ip Negative Memory"
description: "Round 6 negative memory for no_crash with verifier signal ip_dissector_clean_exit."
failure_class: "no_crash"
verifier_signal: "ip_dissector_clean_exit"
candidate_family: "pcap_then_raw_ip_protocol_payloads"
input_format: "wireshark-fuzzshark-ip"
harness_convention: "AFL fuzzshark_ip"
vuln_class: "address-size overread"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "ip-dissector-clean-exit", "wireshark-fuzzshark-ip", "negative-memory", "round-6"]
match_keys: ["no_crash", "ip_dissector_clean_exit", "wireshark-fuzzshark-ip", "AFL fuzzshark_ip", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 6
---
# No Crash Ip Dissector Clean Exit Wireshark Fuzzshark Ip Negative Memory

- key: `no_crash x ip_dissector_clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[wireshark-fuzzshark-ip]]

## Failure Shape
- The first pcap-style carrier was mismatched because the wrapper selected `fuzzshark_ip`; a raw IPv6/IP payload with IEEE1905-like bytes also exited cleanly. The target likely needs a valid raw IP encapsulation that reaches the specific ieee1905 reassembly dissector state with a nonstandard address-size field.

## Policy
Treat `no_crash x ip_dissector_clean_exit` on this format family as negative memory for the attempted carrier. Preserve only verifier-proven reachability, then retarget the missing gate or sink-specific state instead of resubmitting candidates with the same signal.

## Procedure
1. Keep any parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, feature gate, length relation, stateful subobject, or official target sink.
3. Change one relation at a time and reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or nonreproducible basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not treat local generic crashes, wrapper usage paths, clean parser exits, or wrong-sink labels as success.
- Do not broaden random mutation after reachability is known; move to the smallest missing format contract.
- Do not submit another candidate with this exact failure signal unless the candidate changes the causal gate being tested.
- Do not store raw payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: 1 diagnosed persistent failure(s) from round 6.
- Scope: generator repair and basin avoidance only.
