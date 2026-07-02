---
type: causal-policy
title: "Opensc Pkcs15 Reader Chunk Stream Construct No Crash Chunk Contract Reached No Target Crash Cplc Length Validation Negative Memory"
description: "Round 34 negative memory for opensc-pkcs15-reader-chunk-stream when no_crash pairs with chunk_contract_reached_no_target_crash."
failure_class: "no_crash"
verifier_signal: "chunk_contract_reached_no_target_crash"
candidate_family: "construct"
input_format: "opensc-pkcs15-reader-chunk-stream"
harness_convention: "libfuzzer"
vuln_class: "cplc-length-validation"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "chunk-contract-reached-no-target-crash", "opensc-pkcs15-reader-chunk-stream", "libfuzzer", "construct", "negative-memory", "round-34"]
match_keys: ["no-crash", "chunk-contract-reached-no-target-crash", "opensc-pkcs15-reader-chunk-stream", "libfuzzer", "construct", "cplc-length-validation", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 34
---
# Opensc Pkcs15 Reader Chunk Stream Construct No Crash Chunk Contract Reached No Target Crash Cplc Length Validation Negative Memory

- key: `no_crash x chunk_contract_reached_no_target_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[opensc-pkcs15-reader-chunk-stream]]
- related harness facts: [[libfuzzer]]

## Round 34 Negative Support

- key: `no_crash x chunk_contract_reached_no_target_crash`
- outcome: persistent failure / basin to avoid
- candidate family: `construct`
- vulnerability class: `cplc-length-validation`
- related format facts: [[opensc-pkcs15-reader-chunk-stream]]
- related harness facts: [[libfuzzer]]

### Failure Shape
Valid AuthentIC ATR transcripts with short, exact-boundary, overlong, retry, and select-failure CPLC responses stayed clean. A separate CoolKey/GlobalPlatform transcript hypothesis with padded driver-probe responses, applet selection, object-list termination, card-manager selection, and short CPLC data also stayed clean. The likely missing relation is deeper successful card binding or a sanitizer-visible use of the trusted CPLC length after the card driver accepts the state.

### Policy
Treat `no_crash x chunk_contract_reached_no_target_crash` on `opensc-pkcs15-reader-chunk-stream` as a basin to avoid unless a new candidate changes the parser gate, state relation, harness contract, or target sink relation described below. Preserve any proven reachability, but reject variants that return to the same signal without changing the causal gate under test.

### Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. Promote a recovery from this basin only after a later verifier-confirmed target match.

### Format Contract
The OpenSC reader input is a sequence of native little-endian length-prefixed chunks. The first chunk becomes the ATR used for driver matching. Later chunks emulate APDU responses: response body bytes precede the final status words, and the harness only copies response data according to the APDU response buffer requested by the active driver.

### Harness Contract
The libFuzzer target installs the synthetic OpenSC reader, connects a card from the first chunk, calls PKCS#15 bind, and only consumes the later operation-input chunks if a PKCS#15 card is successfully bound. There is no raw ASN.1 or standalone smart-card file envelope.

### Evidence Shape
- Support: one diagnosed persistent round 34 failure.
- Candidate family: `construct`.
- Verifier key: `no_crash x chunk_contract_reached_no_target_crash`.
- Vulnerability class: `cplc-length-validation`.

## Negative Memory
- Do not count parser reachability, both-image crashes, fixed-image crashes, local wrapper crashes, clean exits, or off-target sanitizer crashes as success for this key.
- Do not store concrete payload bytes, exact positions, task identifiers, checksums, or submit metadata.
