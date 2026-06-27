---
type: causal-policy
title: "No Crash Parser Not Reached Opensc Fuzz Reader Chunks Negative Memory"
description: "Strengthened negative memory through round 12 for no_crash with verifier signal parser_not_reached."
failure_class: "no_crash"
verifier_signal: "parser_not_reached"
candidate_family: "construct"
input_format: "opensc-fuzz-reader-chunks"
harness_convention: "libfuzzer"
vuln_class: "missing-sentinel-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-not-reached", "opensc-fuzz-reader-chunks", "negative-memory", "round-7", "round-12"]
match_keys: ["no_crash", "parser_not_reached", "opensc-fuzz-reader-chunks", "libfuzzer", "missing-sentinel-read", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 12
---
# No Crash Parser Not Reached Opensc Fuzz Reader Chunks Negative Memory

- key: `no_crash x parser_not_reached`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[opensc-fuzz-reader-chunks]]
- related harness facts: [[libfuzzer]]

## Failure Shape
The tested chunk streams exercised the fuzz reader contract and several ATR/APDU shapes, but did not select the affected idprime ATR table. The likely missing gate is an ATR that dispatches to the exact card profile whose ATR list is unterminated, followed by enough successful APDU responses for PKCS#15 binding to walk that list.

## Policy
Treat `no_crash x parser_not_reached` on `opensc-fuzz-reader-chunks` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
The input is a concatenation of reader chunks. Each chunk starts with a little-endian length field followed by that many response bytes. The first chunk becomes the card ATR; later chunks are APDU response bodies whose final status bytes become the APDU status words.

## Harness Contract
The libFuzzer harness replaces OpenSC's reader with a fuzz reader, consumes the first chunk during card connection, then consumes additional chunks during PKCS#15 bind and object operations. After binding, it consumes two more chunks as operation input and parameters.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_not_reached`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: diagnosed persistent failures from rounds 7 and 12.
- Scope: generator repair and basin avoidance only.
