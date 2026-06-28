---
type: causal-policy
title: "Not Verified Target Not Reached SIP Uri Or SIP Message Negative Memory"
description: "Round 18 negative memory for not_verified with verifier signal target_not_reached."
failure_class: "not_verified"
verifier_signal: "target_not_reached"
candidate_family: "analysis_only"
input_format: "sip uri or sip message"
harness_convention: "libfuzzer"
vuln_class: "algorithmic-complexity-or-redundant-parse"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["not-verified", "target-not-reached", "sip-uri-or-sip-message", "libfuzzer", "negative-memory", "round-18"]
match_keys: ["not-verified", "target-not-reached", "sip-uri-or-sip-message", "libfuzzer", "algorithmic-complexity-or-redundant-parse", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 18
---
# Not Verified Target Not Reached SIP Uri Or SIP Message Negative Memory

- key: `not_verified x target_not_reached`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[sip-uri-or-sip-message]]
- related harness facts: [[libfuzzer]]

## Failure Shape
- The source-level issue is redundant IPv6-address detection inside URI AOR construction, but the extracted tree did not expose a clear single raw-input harness route to Uri::getAorInternal.
- I did not produce a SIP URI/message carrier that proves target reachability.

## Policy
Treat `not_verified x target_not_reached` on `sip uri or sip message` as a basin to avoid unless a new candidate changes the parser gate, state relation, or target-sink relation described above. Preserve any proven reachability, but discard variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to this same basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `target_not_reached`.
- Do not count parser reachability, local wrapper crashes, both-image crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[sip-uri-or-sip-message]] for descriptive format gates and invariants.

## Harness Contract
Use [[libfuzzer]] for the input-carving contract.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 18.
- Scope: generator repair and basin avoidance only.

## Round 18 Failure Evidence
- Verifier key: `not_verified x target_not_reached`.
- Candidate family: `analysis_only`.
- Basin summary: The source-level issue is redundant IPv6-address detection inside URI AOR construction, but the extracted tree did not expose a clear single raw-input harness route to Uri::getAorInternal.
