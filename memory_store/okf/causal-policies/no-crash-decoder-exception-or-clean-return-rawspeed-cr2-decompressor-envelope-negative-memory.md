---
type: causal-policy
title: "No Crash Decoder Exception Or Clean Return Rawspeed Cr2 Decompressor Envelope Negative Memory"
description: "Strengthened negative memory through round 12 for no_crash with verifier signal decoder_exception_or_clean_return."
failure_class: "no_crash"
verifier_signal: "decoder_exception_or_clean_return"
candidate_family: "construct"
input_format: "rawspeed-cr2-decompressor-envelope"
harness_convention: "libfuzzer"
vuln_class: "slice-width-miscalculation"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "decoder-exception-or-clean-return", "rawspeed-cr2-decompressor-envelope", "negative-memory", "round-8", "round-12"]
match_keys: ["no_crash", "decoder_exception_or_clean_return", "rawspeed-cr2-decompressor-envelope", "libfuzzer", "slice-width-miscalculation", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 12
---
# No Crash Decoder Exception Or Clean Return Rawspeed Cr2 Decompressor Envelope Negative Memory

- key: `no_crash x decoder_exception_or_clean_return`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[rawspeed-cr2-decompressor-envelope]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Several fuzzer-envelope variants with different slice-width relations reached only clean return or swallowed RawSpeed exceptions. The synthetic LJpeg-like payload was not valid enough to drive Cr2Decompressor::decodeN_X_Y into the slice-copy invariant.

## Policy
Treat `no_crash x decoder_exception_or_clean_return` on `rawspeed-cr2-decompressor-envelope` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
The fuzzer-specific RawSpeed carrier begins with a RawImage construction envelope, then a slice count and signed slice-width table, followed by compressed LJpeg-style image data consumed by Cr2Decompressor. The slice widths must both pass image-size sanity checks and remain inconsistent enough to expose the c-p-p relation.

## Harness Contract
The libFuzzer target consumes fields front-to-back from a little-endian ByteStream, creates a RawImage, reads slice metadata, constructs Cr2Decompressor on the remaining stream, allocates image storage, calls decode, and swallows RawSpeed exceptions.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `decoder_exception_or_clean_return`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: diagnosed persistent failures from rounds 8 and 12.
- Scope: generator repair and basin avoidance only.
