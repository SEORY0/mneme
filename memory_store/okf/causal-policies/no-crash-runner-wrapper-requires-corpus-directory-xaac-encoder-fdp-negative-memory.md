---
type: causal-policy
title: "No Crash Runner Wrapper Requires Corpus Directory Xaac Encoder Fdp Negative Memory"
description: "Round 13 negative memory for no_crash with verifier signal runner_wrapper_requires_corpus_directory."
failure_class: "no_crash"
verifier_signal: "runner_wrapper_requires_corpus_directory"
candidate_family: "construct"
input_format: "xaac-encoder-fdp"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-write"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "runner-wrapper-requires-corpus-directory", "xaac-encoder-fdp", "negative-memory", "round-13"]
match_keys: ["no_crash", "runner_wrapper_requires_corpus_directory", "xaac-encoder-fdp", "libfuzzer", "heap-buffer-overflow-write", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 13
---
# No Crash Runner Wrapper Requires Corpus Directory Xaac Encoder Fdp Negative Memory

- key: `no_crash x runner_wrapper_requires_corpus_directory`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[xaac-encoder-fdp]]
- related harness facts: [[libfuzzer]]

## Failure Shape
The encoder source harness consumes FuzzedDataProvider configuration followed by synthetic audio payload, but the arvo wrapper invokes libFuzzer in corpus-directory mode. The runner copies a single file to the fixed input path, so the image reports that the required corpus directory is absent before executing candidate bytes.

## Policy
Treat `no_crash x runner_wrapper_requires_corpus_directory` on `xaac-encoder-fdp` as a basin to avoid unless a new candidate changes the specific parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `runner_wrapper_requires_corpus_directory`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
The logical input is not an AAC file. Front-loaded FuzzedDataProvider fields choose encoder parameters such as sample rate, channel mode, bit-rate, audio object type, SBR/USAC/DRC flags, and then supply synthetic PCM frame bytes or fill values.

## Harness Contract
The C++ harness uses FuzzedDataProvider from the front of the byte stream for configuration and per-frame booleans. In this generated arvo image, the shell wrapper calls the libFuzzer binary without single-input mode, creating a mismatch with the worker runner's file-copy contract.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 13.
- Scope: generator repair and basin avoidance only.
