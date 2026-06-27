---
type: causal-policy
title: "No Crash Udp Dissector Clean Exit Wireshark Udp Dissector Payload Negative Memory"
description: "Round 17 negative memory for no_crash with verifier signal udp_dissector_clean_exit."
failure_class: "no_crash"
verifier_signal: "udp_dissector_clean_exit"
candidate_family: "seed_probe"
input_format: "wireshark udp dissector payload"
harness_convention: "fuzzshark udp dissector"
vuln_class: "length-underflow"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "udp-dissector-clean-exit", "wireshark-udp-dissector-payload", "fuzzshark-udp-dissector", "negative-memory", "round-17"]
match_keys: ["no-crash", "udp-dissector-clean-exit", "wireshark-udp-dissector-payload", "fuzzshark-udp-dissector", "length-underflow", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 17
---
# No Crash Udp Dissector Clean Exit Wireshark Udp Dissector Payload Negative Memory

- key: `no_crash x udp_dissector_clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[wireshark-udp-dissector-payload]]
- related harness facts: [[fuzzshark-udp-dissector]]

## Failure Shape
- A WPA capture seed was not the correct runtime carrier after recovering the failed generation; the active binary is a UDP dissector entry point, not a PCAP reader.
- The Airpdcap path likely needs a UDP payload that hands off to the relevant wireless-decryption code or a different harness-specific selector.

## Policy
Treat `no_crash x udp_dissector_clean_exit` on `wireshark udp dissector payload` as a basin to avoid unless a new candidate changes the parser gate, state relation, or target-sink relation described above. Preserve any proven reachability, but discard variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to this same basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `udp_dissector_clean_exit`.
- Do not count parser reachability, local wrapper crashes, both-image crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[wireshark-udp-dissector-payload]] for descriptive format gates and invariants.

## Harness Contract
Use [[fuzzshark-udp-dissector]] for the input-carving contract.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 17.
- Scope: generator repair and basin avoidance only.
