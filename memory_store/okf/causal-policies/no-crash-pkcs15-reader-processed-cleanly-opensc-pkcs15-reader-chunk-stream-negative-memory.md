---
type: causal-policy
title: "No Crash Pkcs15 Reader Processed Cleanly Opensc Pkcs15 Reader Chunk Stream Negative Memory"
description: "Round 12 negative memory for no_crash with verifier signal pkcs15_reader_processed_cleanly."
failure_class: "no_crash"
verifier_signal: "pkcs15_reader_processed_cleanly"
candidate_family: "seed_mutate"
input_format: "opensc-pkcs15-reader-chunk-stream"
harness_convention: "libfuzzer"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "pkcs15-reader-processed-cleanly", "opensc-pkcs15-reader-chunk-stream", "negative-memory", "round-12"]
match_keys: ["no_crash", "pkcs15_reader_processed_cleanly", "opensc-pkcs15-reader-chunk-stream", "libfuzzer", "out-of-bounds-read", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 12
---
# No Crash Pkcs15 Reader Processed Cleanly Opensc Pkcs15 Reader Chunk Stream Negative Memory

- key: `no_crash x pkcs15_reader_processed_cleanly`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[opensc-pkcs15-reader-chunk-stream]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Multiple in-repo fuzz_pkcs15_reader corpus seeds bound the synthetic reader path cleanly but did not drive TCOS file construction or TCOS card operations into the described out-of-bounds read.

## Policy
Treat `no_crash x pkcs15_reader_processed_cleanly` on `opensc-pkcs15-reader-chunk-stream` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
The input is a synthetic smart-card reader transcript rather than a conventional file. The transcript is consumed as a sequence of length-prefixed chunks that emulate connect, transmit, operation input, operation parameter, and key-material responses.

## Harness Contract
The libFuzzer target installs a fuzz reader, connects a card through OpenSC, attempts PKCS#15 binding, then consumes additional chunks for decipher, derive, wrap, unwrap, and signature operations only when binding succeeds. Chunk lengths are consumed from the front of the raw byte stream.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `pkcs15_reader_processed_cleanly`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 12.
- Scope: generator repair and basin avoidance only.
