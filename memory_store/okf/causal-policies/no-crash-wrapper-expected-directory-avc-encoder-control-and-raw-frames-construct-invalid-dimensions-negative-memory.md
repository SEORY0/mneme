---
type: negative-memory
title: "No Crash Wrapper Expected Directory Avc Encoder Control And Raw Frames Construct Invalid Dimensions Negative Memory"
description: "Round 25 negative memory for no_crash with verifier signal wrapper_expected_directory."
failure_class: "no_crash"
verifier_signal: "wrapper_expected_directory"
candidate_family: "construct"
input_format: "avc-encoder-control-and-raw-frames"
harness_convention: "libfuzzer-corpus-wrapper"
vuln_class: "invalid-dimensions"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "wrapper-expected-directory", "avc-encoder-control-and-raw-frames", "libfuzzer-corpus-wrapper", "construct", "negative-memory", "round-25"]
match_keys: ["no_crash", "wrapper_expected_directory", "avc-encoder-control-and-raw-frames", "libfuzzer-corpus-wrapper", "invalid-dimensions", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 25
---
# No Crash Wrapper Expected Directory Avc Encoder Control And Raw Frames Construct Invalid Dimensions Negative Memory

- key: `no_crash x wrapper_expected_directory`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[avc-encoder-control-and-raw-frames]]
- related harness facts: [[libfuzzer-corpus-wrapper]]

## Failure Shape
Boundary width and height candidates were rejected by the wrapper before the encoder fuzzer entrypoint because the runner supplied a file where the wrapper expected a corpus directory.

## Policy
Treat `no_crash x wrapper_expected_directory` on `avc-encoder-control-and-raw-frames` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, wrapper-mismatch, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `wrapper_expected_directory` basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `wrapper_expected_directory`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
The encoder fuzzer format starts with a fixed control header containing width, height, color format, architecture, rate-control, and other encoder knobs, followed by raw frame bytes. The vulnerable invariant is that dimensions outside the supported encoder range can still be used if the set-dimensions error is ignored.

## Harness Contract
The observed wrapper did not pass raw bytes to LLVMFuzzerTestOneInput. It emitted a required-directory error for both file and directory-path attempts under the local verify surface.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 25 after 4 attempts.
- Scope: generator repair and basin avoidance only.
