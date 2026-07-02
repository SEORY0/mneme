---
type: negative-memory
title: "Open62541 Json Variant Construct Generic Crash Post Patch Crash Out Of Bounds Access Negative Memory"
description: "Round 33 negative memory for generic_crash with verifier signal post_patch_crash."
failure_class: "generic_crash"
verifier_signal: "post_patch_crash"
candidate_family: "construct"
input_format: "open62541-json-variant"
harness_convention: "libfuzzer"
vuln_class: "out-of-bounds-access"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["generic-crash", "post-patch-crash", "open62541-json-variant", "libfuzzer", "construct", "out-of-bounds-access", "negative-memory", "round-33"]
match_keys: ["generic_crash", "post_patch_crash", "open62541-json-variant", "libfuzzer", "construct", "out-of-bounds-access", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 33
---
# Open62541 Json Variant Construct Generic Crash Post Patch Crash Out Of Bounds Access Negative Memory

- key: `generic_crash x post_patch_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[open62541-json-variant]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Valid Variant envelopes reached the JSON decode/encode round trip, but each crashing family was over-broad: deeply nested Variant arrays corrupted encoder depth state in both images, malformed ByteString text crashed the shared base64 decoder in both images, and unknown ExtensionObject structure encoding dereferenced an absent body type in both images. Scalar, string, dimension, special floating-point, short-null, and canonicalization families either decoded cleanly or were rejected before the target crash.

## Policy
Treat `generic_crash x post_patch_crash` on `open62541-json-variant` as a basin to avoid unless a new candidate changes the parser gate, state relation, sink relation, or official differential behavior described below. Do not repeat variants that only preserve the same clean-exit, off-target, post-patch-crash, both-image-crash, or target-handoff-missing signal.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing relation from the verifier signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one causal relation at a time and discard candidates that return to `post_patch_crash`.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed vulnerable-only target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `post_patch_crash`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, clean exits, timeouts, or fixed-image crashes as success.
- Never store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[open62541-json-variant]]. The input is raw JSON decoded as an OPC UA Variant. A Variant is an object with a numeric type selector and Body value; array-valued bodies make the Variant an array, and an optional Dimension array describes multidimensional values. Builtin bodies are decoded directly. ExtensionObject bodies carry a type identifier, optional encoding marker, and nested Body; unknown structure-encoded bodies can be stored or skipped by recursive token walking. ByteString bodies are base64 text before being stored as bytes.

## Harness Contract
Use [[libfuzzer]]. The libFuzzer target passes the complete input buffer directly as the JSON byte string, with no file wrapper, mode byte, or FuzzedDataProvider layout. The active target decodes a top-level Variant, calculates the reversible JSON size, encodes it, decodes that generated JSON again, re-encodes it, and then compares the generated encodings. Malformed JSON or values that fail the first decode exit before the encode stage.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 33 after 48 attempts.
- Scope: generator repair and basin avoidance only.
