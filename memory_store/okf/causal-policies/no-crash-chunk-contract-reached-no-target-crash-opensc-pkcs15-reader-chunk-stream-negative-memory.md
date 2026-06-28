---
type: causal-policy
title: "No Crash Chunk Contract Reached No Target Crash Opensc Pkcs15 Reader Chunk Stream Negative Memory"
description: "Round 12 negative memory for no_crash with verifier signal chunk_contract_reached_no_target_crash."
failure_class: "no_crash"
verifier_signal: "chunk_contract_reached_no_target_crash"
candidate_family: "seed_mutate+construct"
input_format: "opensc pkcs15 reader chunk stream"
harness_convention: "honggfuzz/libfuzzer-wrapper"
vuln_class: "heap-buffer-overflow"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "chunk-contract-reached-no-target-crash", "opensc-pkcs15-reader-chunk-stream", "negative-memory", "round-12"]
match_keys: ["no_crash", "chunk_contract_reached_no_target_crash", "opensc-pkcs15-reader-chunk-stream", "honggfuzz-libfuzzer-wrapper", "heap-buffer-overflow", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 12
---
# No Crash Chunk Contract Reached No Target Crash Opensc Pkcs15 Reader Chunk Stream Negative Memory

- key: `no_crash x chunk_contract_reached_no_target_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[opensc-pkcs15-reader-chunk-stream]]
- related harness facts: [[honggfuzz-libfuzzer-wrapper]]

## Failure Shape
All in-repo pkcs15 reader corpus seeds stayed in no-crash. Hand-built chunk streams covering ATR-only, successful status responses, application FCI responses, compressed-certificate-like data, many status-word sequences, and larger compressed-looking certificate data also stayed in no-crash. The remaining gap is likely the exact APDU response sequence needed to bind the CAC/PKCS15 object and return a compressed certificate through the targeted cache/decompression path.

## Policy
Treat `no_crash x chunk_contract_reached_no_target_crash` on `opensc-pkcs15-reader-chunk-stream` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
The fuzz input is a sequence of length-prefixed chunks. The first chunk is used as ATR data and subsequent chunks are consumed as card/APDU responses. APDU response chunks end with status bytes and earlier response bytes are copied into the requested response buffer. The likely target path involves CAC compressed certificate handling and zlib-style decompression into a cached buffer.

## Harness Contract
The OpenSC pkcs15 reader harness installs a fuzz reader, connects using the first chunk as the card ATR, then services reader transmit calls from later chunks. It binds a PKCS15 card and drives reader operations from the chunk stream; it is not a raw ASN.1 file parser.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `chunk_contract_reached_no_target_crash`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 12.
- Scope: generator repair and basin avoidance only.
