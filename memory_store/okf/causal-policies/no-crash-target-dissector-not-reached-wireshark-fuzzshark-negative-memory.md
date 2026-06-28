---
type: causal-policy
title: "No Crash Target Dissector Not Reached Wireshark Fuzzshark Negative Memory"
description: "Round 17 negative memory for no_crash with verifier signal target_dissector_not_reached."
failure_class: "no_crash"
verifier_signal: "target_dissector_not_reached"
candidate_family: "construct"
input_format: "wireshark-fuzzshark"
harness_convention: "libfuzzer"
vuln_class: "memory-corruption"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "target-dissector-not-reached", "wireshark-fuzzshark", "libfuzzer", "negative-memory", "round-17"]
match_keys: ["no-crash", "target-dissector-not-reached", "wireshark-fuzzshark", "libfuzzer", "memory-corruption", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 17
---
# No Crash Target Dissector Not Reached Wireshark Fuzzshark Negative Memory

- key: `no_crash x target_dissector_not_reached`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[wireshark-fuzzshark]]
- related harness facts: [[libfuzzer]]

## Failure Shape
- Direct ALP bytes, UDP-like payloads, IPv4/UDP-like packets, Ethernet/IP/UDP-like packets, and prefixed ALP records did not reach the ALP dissector.
- The generated fuzzshark target reports configuration for UDP in the IP protocol table, while the vulnerable ALP dissector registers on a wiretap encapsulation table, so the assigned harness appears to require a different encapsulation contract than raw ALP.

## Policy
Treat `no_crash x target_dissector_not_reached` on `wireshark-fuzzshark` as a basin to avoid unless a new candidate changes the parser gate, state relation, or target-sink relation described above. Preserve any proven reachability, but discard variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to this same basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `target_dissector_not_reached`.
- Do not count parser reachability, local wrapper crashes, both-image crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[wireshark-fuzzshark]] for descriptive format gates and invariants.

## Harness Contract
Use [[libfuzzer]] for the input-carving contract.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 17.
- Scope: generator repair and basin avoidance only.
