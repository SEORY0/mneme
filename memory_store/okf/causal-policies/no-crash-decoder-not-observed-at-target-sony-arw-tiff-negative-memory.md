---
type: causal-policy
title: "No Crash Decoder Not Observed At Target Sony Arw Tiff Negative Memory"
description: "Round 17 negative memory for no_crash with verifier signal decoder_not_observed_at_target."
failure_class: "no_crash"
verifier_signal: "decoder_not_observed_at_target"
candidate_family: "construct"
input_format: "sony-arw-tiff"
harness_convention: "libfuzzer"
vuln_class: "suppressed-io-exception"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "decoder-not-observed-at-target", "sony-arw-tiff", "libfuzzer", "negative-memory", "round-17"]
match_keys: ["no-crash", "decoder-not-observed-at-target", "sony-arw-tiff", "libfuzzer", "suppressed-io-exception", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 17
---
# No Crash Decoder Not Observed At Target Sony Arw Tiff Negative Memory

- key: `no_crash x decoder_not_observed_at_target`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[sony-arw-tiff]]
- related harness facts: [[libfuzzer]]

## Failure Shape
- A minimal TIFF-like Sony envelope did not trigger the target catch path.
- The missing piece is likely a fuller TIFF/ARW structure that RawSpeed accepts as Sony ARW while making the selected strip fail inside the uncompressed decoder after raw image allocation.

## Policy
Treat `no_crash x decoder_not_observed_at_target` on `sony-arw-tiff` as a basin to avoid unless a new candidate changes the parser gate, state relation, or target-sink relation described above. Preserve any proven reachability, but discard variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to this same basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `decoder_not_observed_at_target`.
- Do not count parser reachability, local wrapper crashes, both-image crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[sony-arw-tiff]] for descriptive format gates and invariants.

## Harness Contract
Use [[libfuzzer]] for the input-carving contract.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 17.
- Scope: generator repair and basin avoidance only.
