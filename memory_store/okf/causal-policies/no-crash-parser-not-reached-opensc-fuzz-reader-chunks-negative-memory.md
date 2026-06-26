---
type: causal-policy
title: "No Crash Parser Not Reached Opensc Fuzz Reader Chunks Negative Memory"
description: "Round 7 negative memory for no_crash with verifier signal parser_not_reached."
failure_class: "no_crash"
verifier_signal: "parser_not_reached"
candidate_family: "construct"
input_format: "opensc-fuzz-reader-chunks"
harness_convention: "libfuzzer"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-not-reached", "opensc-fuzz-reader-chunks", "negative-memory", "round-7"]
match_keys: ["no_crash", "parser_not_reached", "opensc-fuzz-reader-chunks", "libfuzzer", "out-of-bounds-read", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 7
---
# No Crash Parser Not Reached Opensc Fuzz Reader Chunks Negative Memory

- key: `no_crash x parser_not_reached`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[opensc-fuzz-reader-chunks]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Constructed chunked reader streams with ATR-like data and CPLC-like APDU responses did not bind a
PKCS15 card object or reach the GlobalPlatform CPLC decode path.

## Policy
Treat `no_crash x parser_not_reached` on `opensc-fuzz-reader-chunks` as a basin to avoid unless a new candidate changes the specific parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_not_reached`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Format Contract
The OpenSC reader harness is a sequence of little-endian length-prefixed chunks. The first chunk is
used as ATR data; later chunks are consumed as card transmit responses where the last two bytes are
status words and the preceding bytes are copied as APDU response data.

## Harness Contract
The target is fuzz_pkcs15_reader. It installs a synthetic reader, connects a card, binds PKCS15,
then consumes more chunks as operation inputs and parameters only if a card was successfully bound.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 7.
- Scope: generator repair and basin avoidance only.
