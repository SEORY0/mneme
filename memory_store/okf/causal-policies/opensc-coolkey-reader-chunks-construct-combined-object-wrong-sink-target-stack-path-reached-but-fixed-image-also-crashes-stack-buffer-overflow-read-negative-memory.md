---
type: causal-policy
title: "Opensc Coolkey Reader Chunks Construct Combined Object Wrong Sink Target Stack Path Reached But Fixed Image Also Crashes Stack Buffer Overflow Read Negative Memory"
description: "Round 34 negative memory for opensc-coolkey-reader-chunks when wrong_sink pairs with target_stack_path_reached_but_fixed_image_also_crashes."
failure_class: "wrong_sink"
verifier_signal: "target_stack_path_reached_but_fixed_image_also_crashes"
candidate_family: "construct-combined-object"
input_format: "opensc-coolkey-reader-chunks"
harness_convention: "libfuzzer"
vuln_class: "stack-buffer-overflow-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["wrong-sink", "target-stack-path-reached-but-fixed-image-also-crashes", "opensc-coolkey-reader-chunks", "libfuzzer", "construct-combined-object", "negative-memory", "round-34"]
match_keys: ["wrong-sink", "target-stack-path-reached-but-fixed-image-also-crashes", "opensc-coolkey-reader-chunks", "libfuzzer", "construct-combined-object", "stack-buffer-overflow-read", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 34
---
# Opensc Coolkey Reader Chunks Construct Combined Object Wrong Sink Target Stack Path Reached But Fixed Image Also Crashes Stack Buffer Overflow Read Negative Memory

- key: `wrong_sink x target_stack_path_reached_but_fixed_image_also_crashes`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[opensc-coolkey-reader-chunks]]
- related harness facts: [[libfuzzer]]

## Round 34 Negative Support

- key: `wrong_sink x target_stack_path_reached_but_fixed_image_also_crashes`
- outcome: persistent failure / basin to avoid
- candidate family: `construct-combined-object`
- vulnerability class: `stack-buffer-overflow-read`
- related format facts: [[opensc-coolkey-reader-chunks]]
- related harness facts: [[libfuzzer]]

### Failure Shape
The reachable crash is the known both-image RSA response-length basin. Earlier variants either did not bind a supported key or were rejected before the operation sink. Tightening the key size reached the intended stack copy path, but the official differential rejected it because the fixed build also exits nonzero.

### Policy
Treat `wrong_sink x target_stack_path_reached_but_fixed_image_also_crashes` on `opensc-coolkey-reader-chunks` as a basin to avoid unless a new candidate changes the parser gate, state relation, harness contract, or target sink relation described below. Preserve any proven reachability, but reject variants that return to the same signal without changing the causal gate under test.

### Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. Promote a recovery from this basin only after a later verifier-confirmed target match.

### Format Contract
The fuzz input is a stream of native little-endian length-prefixed chunks. The first chunk is ATR data. Later chunks emulate APDU responses, with optional response body bytes followed by status bytes. A CoolKey combined object has an outer header with compression metadata, then an uncompressed area with a token-name header and embedded V1 object records. Private key records need class, key type, identifier, usage bits, and RSA public parameters to pass PKCS#15 operation selection.

### Harness Contract
The target installs a virtual reader, connects a card, binds PKCS#15, then consumes two more chunks as operation input and parameter data before iterating PKCS#15 objects through crypto and PIN operations. CoolKey is reached through APDU-speaking driver matching; APDU chunks are consumed statefully, so operation-response chunks must appear after card initialization and object binding.

### Evidence Shape
- Support: one diagnosed persistent round 34 failure.
- Candidate family: `construct-combined-object`.
- Verifier key: `wrong_sink x target_stack_path_reached_but_fixed_image_also_crashes`.
- Vulnerability class: `stack-buffer-overflow-read`.

## Negative Memory
- Do not count parser reachability, both-image crashes, fixed-image crashes, local wrapper crashes, clean exits, or off-target sanitizer crashes as success for this key.
- Do not store concrete payload bytes, exact positions, task identifiers, checksums, or submit metadata.
