---
type: causal-policy
title: "No Crash Decoder Clean Or Rejected Jpeg Xl Fuzzer Input Negative Memory"
description: "Round 12 negative memory for no_crash with verifier signal decoder_clean_or_rejected."
failure_class: "no_crash"
verifier_signal: "decoder_clean_or_rejected"
candidate_family: "seed_mutate"
input_format: "jpeg-xl-fuzzer-input"
harness_convention: "libfuzzer"
vuln_class: "state-desynchronization"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "decoder-clean-or-rejected", "jpeg-xl-fuzzer-input", "negative-memory", "round-12"]
match_keys: ["no_crash", "decoder_clean_or_rejected", "jpeg-xl-fuzzer-input", "libfuzzer", "state-desynchronization", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 12
---
# No Crash Decoder Clean Or Rejected Jpeg Xl Fuzzer Input Negative Memory

- key: `no_crash x decoder_clean_or_rejected`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[jpeg-xl-fuzzer-input]]
- related harness facts: [[libfuzzer]]

## Failure Shape
A real JPEG XL sample with several decoder option footer settings, plus truncated and magic-only carriers, decoded or failed cleanly. These attempts did not synthesize the specific meta-channel squeeze transform mismatch needed to desynchronize transform application.

## Policy
Treat `no_crash x decoder_clean_or_rejected` on `jpeg-xl-fuzzer-input` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
The main JPEG XL fuzzer input is a JPEG XL codestream or container followed by a small option footer. The footer controls decoder modes such as streaming, callback output, orientation handling, pixel format, and generated target selection. The target bug involves modular squeeze transforms and metadata channel counts.

## Harness Contract
The djxl fuzzer consumes the last few bytes as flags and decodes the preceding bytes as JPEG XL data. It may decode in one shot or streamed chunks and may request pixel, extra-channel, preview, or JPEG reconstruction output depending on flags.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `decoder_clean_or_rejected`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 12.
- Scope: generator repair and basin avoidance only.
