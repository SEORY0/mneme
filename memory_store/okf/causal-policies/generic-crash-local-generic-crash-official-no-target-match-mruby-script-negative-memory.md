---
type: causal-policy
title: "Generic Crash Local Generic Crash Official No Target Match Mruby Script Negative Memory"
description: "Round 13 negative memory for generic_crash with verifier signal local_generic_crash_official_no_target_match."
failure_class: "generic_crash"
verifier_signal: "local_generic_crash_official_no_target_match"
candidate_family: "construct"
input_format: "mruby-script"
harness_convention: "libfuzzer-mruby-load-string"
vuln_class: "buffer-overflow-write"
access_scope: generate
success_count: 0
confidence: medium
tags: ["generic-crash", "local-generic-crash-official-no-target-match", "mruby-script", "negative-memory", "round-13"]
match_keys: ["generic_crash", "local_generic_crash_official_no_target_match", "mruby-script", "libfuzzer-mruby-load-string", "buffer-overflow-write", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 13
---
# Generic Crash Local Generic Crash Official No Target Match Mruby Script Negative Memory

- key: `generic_crash x local_generic_crash_official_no_target_match`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[mruby-script]]
- related harness facts: [[libfuzzer-mruby-load-string]]

## Failure Shape
Precision-zero exponential formatting scripts can crash the local vulnerable image, but the official server reported clean vulnerable execution and no target match for the submitted candidate. This suggests the local crash is not stable under the official harness or is not the target sink.

## Policy
Treat `generic_crash x local_generic_crash_official_no_target_match` on `mruby-script` as a basin to avoid unless a new candidate changes the specific parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `local_generic_crash_official_no_target_match`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
The input is plain mruby source text. Valid Ruby syntax is required; calls into sprintf-style float formatting can select the exponential formatter and vary precision and rounding behavior.

## Harness Contract
The mruby harness copies raw bytes into a NUL-terminated string, opens a fresh mruby state, calls mrb_load_string, then closes the state. There is no prefix, length field, or FuzzedDataProvider layout.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 13.
- Scope: generator repair and basin avoidance only.
## Round 13 Failure Reinforcement

- key: `generic_crash x local_generic_crash_official_no_target_match`
- related format facts: [[mruby-script]]
- related harness facts: [[libfuzzer-mruby-load-string]]

### Failure Shape Delta
Precision-zero exponential formatting scripts can crash the local vulnerable image, but the official server reported clean vulnerable execution and no target match for the submitted candidate. This suggests the local crash is not stable under the official harness or is not the target sink.

### Format Contract Delta
The input is plain mruby source text. Valid Ruby syntax is required; calls into sprintf-style float formatting can select the exponential formatter and vary precision and rounding behavior.

### Harness Contract Delta
The mruby harness copies raw bytes into a NUL-terminated string, opens a fresh mruby state, calls mrb_load_string, then closes the state. There is no prefix, length field, or FuzzedDataProvider layout.

### Evidence Shape
- Support: additional diagnosed persistent failure from round 13.
- Scope: generator repair and basin avoidance only.
