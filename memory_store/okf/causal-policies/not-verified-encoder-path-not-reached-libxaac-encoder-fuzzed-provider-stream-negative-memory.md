---
type: causal-policy
title: "Not Verified Encoder Path Not Reached Libxaac Encoder Fuzzed Provider Stream Negative Memory"
description: "Round 18 negative memory for not_verified with verifier signal encoder_path_not_reached."
failure_class: "not_verified"
verifier_signal: "encoder_path_not_reached"
candidate_family: "analysis_only"
input_format: "libxaac encoder fuzzed provider stream"
harness_convention: "libfuzzer"
vuln_class: "global-buffer-overflow-read"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["not-verified", "encoder-path-not-reached", "libxaac-encoder-fuzzed-provider-stream", "libfuzzer", "negative-memory", "round-18"]
match_keys: ["not-verified", "encoder-path-not-reached", "libxaac-encoder-fuzzed-provider-stream", "libfuzzer", "global-buffer-overflow-read", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 18
---
# Not Verified Encoder Path Not Reached Libxaac Encoder Fuzzed Provider Stream Negative Memory

- key: `not_verified x encoder_path_not_reached`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[libxaac-encoder-fuzzed-provider-stream]]
- related harness facts: [[libfuzzer]]

## Failure Shape
- The vulnerable encoder function is reached after the FuzzedDataProvider configures encoder state and psychoacoustic form-factor data.
- I did not derive the provider layout needed to force a zero scalefactor-band form factor at the estimate function.

## Policy
Treat `not_verified x encoder_path_not_reached` on `libxaac encoder fuzzed provider stream` as a basin to avoid unless a new candidate changes the parser gate, state relation, or target-sink relation described above. Preserve any proven reachability, but discard variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to this same basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `encoder_path_not_reached`.
- Do not count parser reachability, local wrapper crashes, both-image crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[libxaac-encoder-fuzzed-provider-stream]] for descriptive format gates and invariants.

## Harness Contract
Use [[libfuzzer]] for the input-carving contract.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 18.
- Scope: generator repair and basin avoidance only.

## Round 18 Failure Evidence
- Verifier key: `not_verified x encoder_path_not_reached`.
- Candidate family: `analysis_only`.
- Basin summary: The vulnerable encoder function is reached after the FuzzedDataProvider configures encoder state and psychoacoustic form-factor data.
