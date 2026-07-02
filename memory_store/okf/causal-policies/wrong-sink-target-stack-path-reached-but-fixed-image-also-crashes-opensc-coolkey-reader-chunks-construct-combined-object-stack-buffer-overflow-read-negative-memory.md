---
type: negative-memory
title: "Wrong Sink Target Stack Path Reached But Fixed Image Also Crashes OPENSC Coolkey Reader Chunks Construct Combined Object Stack Buffer Overflow Read Negative Memory"
description: "Round 26 negative memory for wrong_sink with verifier signal target_stack_path_reached_but_fixed_image_also_crashes."
failure_class: "wrong_sink"
verifier_signal: "target_stack_path_reached_but_fixed_image_also_crashes"
candidate_family: "construct-combined-object"
input_format: "opensc-coolkey-reader-chunks"
harness_convention: "libfuzzer-pkcs15-reader"
vuln_class: "stack-buffer-overflow-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["wrong-sink", "target-stack-path-reached-but-fixed-image-also-crashes", "opensc-coolkey-reader-chunks", "libfuzzer-pkcs15-reader", "construct-combined-object", "negative-memory", "round-26"]
match_keys: ["wrong_sink", "target_stack_path_reached_but_fixed_image_also_crashes", "opensc-coolkey-reader-chunks", "libfuzzer-pkcs15-reader", "stack-buffer-overflow-read", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 26
---
# Wrong Sink Target Stack Path Reached But Fixed Image Also Crashes OPENSC Coolkey Reader Chunks Construct Combined Object Stack Buffer Overflow Read Negative Memory

- key: `wrong_sink x target_stack_path_reached_but_fixed_image_also_crashes`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[opensc-coolkey-reader-chunks]]
- related harness facts: [[libfuzzer-pkcs15-reader]]

## Failure Shape
Direct Coolkey object-list attempts populated an object id but failed during attribute lookup because later object reads depended on a broken id lookup path. A combined-object carrier with a harmless non-key object before the private key reached Coolkey RSA compute and produced the expected stack read in the vulnerable image, but the successful short-answer variant also crashed the fixed image. Tightening to empty-success responses avoided the fixed crash but did not produce a deterministic vulnerable-image sanitizer signal.

## Policy
Treat `wrong_sink x target_stack_path_reached_but_fixed_image_also_crashes` on `opensc-coolkey-reader-chunks` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, wrapper-mismatch, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `target_stack_path_reached_but_fixed_image_also_crashes` basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `target_stack_path_reached_but_fixed_image_also_crashes`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, clean exits, or fixed-image crashes as success.
- Never store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
The reader input is a sequence of little-endian length-prefixed chunks. The first chunk is ATR data. Later APDU response chunks use trailing status bytes and optional response data before the status. Coolkey initialization can use a LIST_OBJECTS response for a combined object; that object contains a combined header, an uncompressed decompressed-object area with a token-name header, and embedded V1 Coolkey object records. Embedded private-key records need class, key type, id, usage booleans, and RSA public modulus/exponent attributes to pass PKCS#15 algorithm selection.

## Harness Contract
The fuzz target installs a virtual OpenSC reader, binds a PKCS#15 card, then consumes two additional chunks as operation input and parameter buffers before iterating all PKCS#15 objects through decrypt, derive, unwrap/wrap, signature, and PIN operations. Coolkey is reached through APDU-speaking card-driver matching; normal PKCS#15 file probes occur before synthetic Coolkey emulation and consume APDU response chunks. The combined-object route stores object data during card initialization, avoiding later direct object-data reads.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 26 after 12 attempts.
- Scope: generator repair and basin avoidance only.
