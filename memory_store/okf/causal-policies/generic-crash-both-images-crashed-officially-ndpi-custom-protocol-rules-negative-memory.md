---
type: causal-policy
title: "Generic Crash Both Images Crashed Officially Ndpi Custom Protocol Rules Negative Memory"
description: "Round 17 negative memory for generic_crash with verifier signal both_images_crashed_officially."
failure_class: "generic_crash"
verifier_signal: "both_images_crashed_officially"
candidate_family: "construct"
input_format: "ndpi-custom-protocol-rules"
harness_convention: "libfuzzer-raw-rules-file"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 0
confidence: medium
tags: ["generic-crash", "both-images-crashed-officially", "ndpi-custom-protocol-rules", "libfuzzer-raw-rules-file", "negative-memory", "round-17"]
match_keys: ["generic-crash", "both-images-crashed-officially", "ndpi-custom-protocol-rules", "libfuzzer-raw-rules-file", "use-of-uninitialized-value", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 17
---
# Generic Crash Both Images Crashed Officially Ndpi Custom Protocol Rules Negative Memory

- key: `generic_crash x both_images_crashed_officially`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[ndpi-custom-protocol-rules]]
- related harness facts: [[libfuzzer-raw-rules-file]]

## Failure Shape
- Risk-mask custom-rule lines reached IP/CIDR parsing, but malformed prefix lengths either exited cleanly or crashed both vulnerable and fixed builds.
- The target uninitialized patricia lookup likely needs a valid rule shape that preserves parser state while creating a narrower trie lookup edge case.

## Policy
Treat `generic_crash x both_images_crashed_officially` on `ndpi-custom-protocol-rules` as a basin to avoid unless a new candidate changes the parser gate, state relation, or target-sink relation described above. Preserve any proven reachability, but discard variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to this same basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `both_images_crashed_officially`.
- Do not count parser reachability, local wrapper crashes, both-image crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[ndpi-custom-protocol-rules]] for descriptive format gates and invariants.

## Harness Contract
Use [[libfuzzer-raw-rules-file]] for the input-carving contract.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 17.
- Scope: generator repair and basin avoidance only.
