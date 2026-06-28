---
type: causal-policy
title: "Not Verified Parser Not Reached Openthread Meshcop TLV Or Packet Negative Memory"
description: "Round 18 negative memory for not_verified with verifier signal parser_not_reached."
failure_class: "not_verified"
verifier_signal: "parser_not_reached"
candidate_family: "analysis_only"
input_format: "openthread meshcop tlv or packet"
harness_convention: "libfuzzer"
vuln_class: "logic-error"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["not-verified", "parser-not-reached", "openthread-meshcop-tlv-or-packet", "libfuzzer", "negative-memory", "round-18"]
match_keys: ["not-verified", "parser-not-reached", "openthread-meshcop-tlv-or-packet", "libfuzzer", "logic-error", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 18
---
# Not Verified Parser Not Reached Openthread Meshcop TLV Or Packet Negative Memory

- key: `not_verified x parser_not_reached`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[openthread-meshcop-tlv-or-packet]]
- related harness facts: [[libfuzzer]]

## Failure Shape
- The selected source tree contains several OpenThread fuzz harnesses, and the vulnerable accessor is only reached after a MeshCoP Channel Mask TLV is embedded in a message path that calls the static channel-mask reader.
- I did not produce a packet envelope that demonstrably reaches that message path.

## Policy
Treat `not_verified x parser_not_reached` on `openthread meshcop tlv or packet` as a basin to avoid unless a new candidate changes the parser gate, state relation, or target-sink relation described above. Preserve any proven reachability, but discard variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to this same basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_not_reached`.
- Do not count parser reachability, local wrapper crashes, both-image crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[openthread-meshcop-tlv-or-packet]] for descriptive format gates and invariants.

## Harness Contract
Use [[libfuzzer]] for the input-carving contract.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 18.
- Scope: generator repair and basin avoidance only.

## Round 18 Failure Evidence
- Verifier key: `not_verified x parser_not_reached`.
- Candidate family: `analysis_only`.
- Basin summary: The selected source tree contains several OpenThread fuzz harnesses, and the vulnerable accessor is only reached after a MeshCoP Channel Mask TLV is embedded in a message path that calls the static channel-mask reader.
