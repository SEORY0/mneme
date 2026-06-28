---
type: causal-policy
title: "Not Reached Not Attempted After Triage Wireshark Rrc Packet Negative Memory"
description: "Round 17 negative memory for not_reached with verifier signal not_attempted_after_triage."
failure_class: "not_reached"
verifier_signal: "not_attempted_after_triage"
candidate_family: "none"
input_format: "wireshark-rrc-packet"
harness_convention: "libfuzzer"
vuln_class: "use-after-free"
access_scope: generate
success_count: 0
confidence: medium
tags: ["not-reached", "not-attempted-after-triage", "wireshark-rrc-packet", "libfuzzer", "negative-memory", "round-17"]
match_keys: ["not-reached", "not-attempted-after-triage", "wireshark-rrc-packet", "libfuzzer", "use-after-free", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 17
---
# Not Reached Not Attempted After Triage Wireshark Rrc Packet Negative Memory

- key: `not_reached x not_attempted_after_triage`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[wireshark-rrc-packet]]
- related harness facts: [[libfuzzer]]

## Failure Shape
- Source triage found the generic fuzzshark dissector harness and an RRC lifetime bug involving a freed string buffer, but no concrete dissector payload was produced in this pass.

## Policy
Treat `not_reached x not_attempted_after_triage` on `wireshark-rrc-packet` as a basin to avoid unless a new candidate changes the parser gate, state relation, or target-sink relation described above. Preserve any proven reachability, but discard variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to this same basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `not_attempted_after_triage`.
- Do not count parser reachability, local wrapper crashes, both-image crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[wireshark-rrc-packet]] for descriptive format gates and invariants.

## Harness Contract
Use [[libfuzzer]] for the input-carving contract.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 17.
- Scope: generator repair and basin avoidance only.
