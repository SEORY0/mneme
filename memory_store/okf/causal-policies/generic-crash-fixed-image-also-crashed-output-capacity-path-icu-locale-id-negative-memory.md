---
type: causal-policy
title: "Generic Crash Fixed Image Also Crashed Output Capacity Path ICU Locale Id Negative Memory"
description: "Round 18 negative memory for generic_crash with verifier signal fixed_image_also_crashed_output_capacity_path."
failure_class: "generic_crash"
verifier_signal: "fixed_image_also_crashed_output_capacity_path"
candidate_family: "construct"
input_format: "icu-locale-id"
harness_convention: "libfuzzer"
vuln_class: "buffer-overflow-read"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["generic-crash", "fixed-image-also-crashed-output-capacity-path", "icu-locale-id", "libfuzzer", "negative-memory", "round-18"]
match_keys: ["generic-crash", "fixed-image-also-crashed-output-capacity-path", "icu-locale-id", "libfuzzer", "buffer-overflow-read", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 18
---
# Generic Crash Fixed Image Also Crashed Output Capacity Path ICU Locale Id Negative Memory

- key: `generic_crash x fixed_image_also_crashed_output_capacity_path`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[icu-locale-id]]
- related harness facts: [[libfuzzer]]

## Failure Shape
- Locale IDs with long private-use, variant, keyword, and Unicode-extension material exercised the language-tag conversion selector.
- Long Unicode-extension keyword values produced a local stack-buffer-overflow write through the output sink, but the fixed image crashed the same way on submission.
- The described read-side boundary condition was not isolated from the harness-controlled sink-capacity failure.

## Policy
Treat `generic_crash x fixed_image_also_crashed_output_capacity_path` on `icu-locale-id` as a basin to avoid unless a new candidate changes the parser gate, state relation, or target-sink relation described above. Preserve any proven reachability, but discard variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to this same basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `fixed_image_also_crashed_output_capacity_path`.
- Do not count parser reachability, local wrapper crashes, both-image crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[icu-locale-id]] for descriptive format gates and invariants.

## Harness Contract
Use [[libfuzzer]] for the input-carving contract.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 18.
- Scope: generator repair and basin avoidance only.

## Round 18 Failure Evidence
- Verifier key: `generic_crash x fixed_image_also_crashed_output_capacity_path`.
- Candidate family: `construct`.
- Basin summary: Locale IDs with long private-use, variant, keyword, and Unicode-extension material exercised the language-tag conversion selector.
