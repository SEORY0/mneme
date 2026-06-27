---
type: causal-policy
title: "No Crash Pkcs15init Starcos Gen Key Not Reached Opensc Pkcs15init Profile Plus Virtual Reader Stream Negative Memory"
description: "Round 13 negative memory for no_crash with verifier signal pkcs15init_starcos_gen_key_not_reached."
failure_class: "no_crash"
verifier_signal: "pkcs15init_starcos_gen_key_not_reached"
candidate_family: "construct"
input_format: "opensc-pkcs15init-profile-plus-virtual-reader-stream"
harness_convention: "libfuzzer"
vuln_class: "missing-status-word-check"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "pkcs15init-starcos-gen-key-not-reached", "opensc-pkcs15init-profile-plus-virtual-reader-stream", "negative-memory", "round-13"]
match_keys: ["no_crash", "pkcs15init_starcos_gen_key_not_reached", "opensc-pkcs15init-profile-plus-virtual-reader-stream", "libfuzzer", "missing-status-word-check", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 13
---
# No Crash Pkcs15init Starcos Gen Key Not Reached Opensc Pkcs15init Profile Plus Virtual Reader Stream Negative Memory

- key: `no_crash x pkcs15init_starcos_gen_key_not_reached`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[opensc-pkcs15init-profile-plus-virtual-reader-stream]]
- related harness facts: [[libfuzzer]]

## Failure Shape
A simple virtual-card chunk stream with a Starcos-like ATR and APDU status responses did not reach the vulnerable key-generation path. The missing state is likely the pkcs15init profile and operation parameters that select Starcos key generation before the reader transcript returns SW1 success with a non-success SW2.

## Policy
Treat `no_crash x pkcs15init_starcos_gen_key_not_reached` on `opensc-pkcs15init-profile-plus-virtual-reader-stream` as a basin to avoid unless a new candidate changes the specific parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `pkcs15init_starcos_gen_key_not_reached`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
OpenSC virtual-reader fuzz inputs are synthetic smart-card transcripts. Reader chunks are length-prefixed; the first chunk is used as ATR/card identity data and later chunks are returned as APDU response data with trailing status words. For this bug, the semantic invariant is that SW1 indicating success must be paired with the correct SW2 before key material is consumed.

## Harness Contract
The selected target is the pkcs15init fuzzer. It installs a fake reader, consumes virtual-card APDU chunks, and must be driven into a card-control key-generation operation. Raw APDU responses alone are insufficient unless the profile and operation input select the Starcos gen-key path.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 13.
- Scope: generator repair and basin avoidance only.
