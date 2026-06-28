---
type: causal-policy
title: "No Crash Pkcs15Init Usage Or Setup Path Opensc Pkcs15Init Profile Plus Virtual Reader Chunks Negative Memory"
description: "Round 17 negative memory for no_crash with verifier signal pkcs15init_usage_or_setup_path."
failure_class: "no_crash"
verifier_signal: "pkcs15init_usage_or_setup_path"
candidate_family: "construct"
input_format: "opensc-pkcs15init-profile-plus-virtual-reader-chunks"
harness_convention: "honggfuzz-style-pkcs15init-wrapper"
vuln_class: "invalid-key-type-handling"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "pkcs15init-usage-or-setup-path", "opensc-pkcs15init-profile-plus-virtual-reader-chunks", "honggfuzz-style-pkcs15init-wrapper", "negative-memory", "round-17"]
match_keys: ["no-crash", "pkcs15init-usage-or-setup-path", "opensc-pkcs15init-profile-plus-virtual-reader-chunks", "honggfuzz-style-pkcs15init-wrapper", "invalid-key-type-handling", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 17
---
# No Crash Pkcs15Init Usage Or Setup Path Opensc Pkcs15Init Profile Plus Virtual Reader Chunks Negative Memory

- key: `no_crash x pkcs15init_usage_or_setup_path`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[opensc-pkcs15init-profile-plus-virtual-reader-chunks]]
- related harness facts: [[honggfuzz-style-pkcs15init-wrapper]]

## Failure Shape
- OpenPGP profile plus virtual-reader chunks with OpenPGP-like ATR and success/error APDU responses stayed in the harness usage or setup path.
- The missing gate is a card-driver state transcript that binds an OpenPGP card, reaches RSA key generation, and returns ECC-shaped key data at the precise command sequence.

## Policy
Treat `no_crash x pkcs15init_usage_or_setup_path` on `opensc-pkcs15init-profile-plus-virtual-reader-chunks` as a basin to avoid unless a new candidate changes the parser gate, state relation, or target-sink relation described above. Preserve any proven reachability, but discard variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to this same basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `pkcs15init_usage_or_setup_path`.
- Do not count parser reachability, local wrapper crashes, both-image crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[opensc-pkcs15init-profile-plus-virtual-reader-chunks]] for descriptive format gates and invariants.

## Harness Contract
Use [[honggfuzz-style-pkcs15init-wrapper]] for the input-carving contract.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 17.
- Scope: generator repair and basin avoidance only.
