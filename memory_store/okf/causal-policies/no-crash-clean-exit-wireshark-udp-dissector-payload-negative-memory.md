---
type: causal-policy
title: "No Crash Clean Exit Wireshark UDP Dissector Payload Negative Memory"
description: "Round 9 negative memory for no_crash with verifier signal clean_exit."
failure_class: "no_crash"
verifier_signal: "clean_exit"
candidate_family: "construct"
input_format: "wireshark-udp-dissector-payload"
harness_convention: "libfuzzer"
vuln_class: "field-size-mismatch"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "clean-exit", "wireshark-udp-dissector-payload", "negative-memory", "round-9"]
match_keys: ["no_crash", "clean_exit", "wireshark-udp-dissector-payload", "libfuzzer", "field-size-mismatch", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 9
---
# No Crash Clean Exit Wireshark UDP Dissector Payload Negative Memory

- key: `no_crash x clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[wireshark-udp-dissector-payload]]
- related harness facts: [[libfuzzer]]

## Failure Shape
- Raw UDP payloads shaped like WLAN management/data frames were consumed by fuzzshark but exited
  cleanly.
- The candidates did not traverse from the UDP dissector table into an IEEE 802.11 subdissector path
  that renders the AID column/string field.

## Policy
Treat `no_crash x clean_exit` on `wireshark-udp-dissector-payload` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
- The described Wireshark bug is in IEEE 802.11 AID field registration/display, so a trigger needs a
  packet that the selected dissector path interprets as WLAN metadata with an AID-bearing element or
  frame before column/string formatting occurs.

## Harness Contract
- The fuzzshark target is configured for the UDP entry in the IP protocol dissector table.
- It supplies the raw input as UDP payload and disables many unrelated dissectors; reaching WLAN
  logic requires a UDP-carried encapsulation path rather than a bare 802.11 frame.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `clean_exit`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 9.
- Scope: generator repair and basin avoidance only.
