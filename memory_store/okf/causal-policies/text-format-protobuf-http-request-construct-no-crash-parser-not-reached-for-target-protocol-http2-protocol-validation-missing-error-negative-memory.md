---
type: negative-memory
title: "Text Format Protobuf Http Request Construct No Crash Parser Not Reached For Target Protocol Http2 Protocol Validation Missing Error Negative Memory"
description: "Round 36 negative memory for no_crash with verifier signal parser_not_reached_for_target_protocol."
failure_class: "no_crash"
verifier_signal: "parser_not_reached_for_target_protocol"
candidate_family: "construct"
input_format: "text-format-protobuf-http-request"
harness_convention: "libprotobuf-mutator-nginx-http-request-fuzzer"
vuln_class: "http2-protocol-validation-missing-error"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["no-crash", "parser-not-reached-for-target-protocol", "text-format-protobuf-http-request", "libprotobuf-mutator-nginx-http-request-fuzzer", "construct", "http2-protocol-validation-missing-error", "negative-memory", "round-36"]
match_keys: ["no_crash", "parser_not_reached_for_target_protocol", "text-format-protobuf-http-request", "libprotobuf-mutator-nginx-http-request-fuzzer", "http2-protocol-validation-missing-error", "no-crash", "parser-not-reached-for-target-protocol", "negative_memory", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 36
---
# Text Format Protobuf Http Request Construct No Crash Parser Not Reached For Target Protocol Http2 Protocol Validation Missing Error Negative Memory

- key: `no_crash x parser_not_reached_for_target_protocol`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[text-format-protobuf-http-request]]
- related harness facts: [[libprotobuf-mutator-nginx-http-request-fuzzer]]

## Failure Shape
The target protocol state did not appear reachable through this harness. The input is a text-format protobuf with request and reply strings, and the fuzzer feeds those strings as C strings, so embedded NULs truncate binary HTTP/2 frame carriers. Direct preface-style inputs, h2c-style upgrade carriers, HTTP/2-settings noise, and upstream-reply variations all stayed in the HTTP/1.x socket path without triggering the invalid-stream-id state.

## Observed Basin
- Failure trajectory classes: bad_format, no_crash.
- Official confirmation: no server target match for this basin.

## Policy
Treat `no_crash x parser_not_reached_for_target_protocol` on `text-format-protobuf-http-request` under `libprotobuf-mutator-nginx-http-request-fuzzer` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described above. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrapper-mismatch, usage-only, or fixed-image-crash behavior.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `parser_not_reached_for_target_protocol` basin.
4. Promote a recovery from this basin only after a later official target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_not_reached_for_target_protocol`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 36 after 8 attempts.
- Scope: generator repair and basin avoidance only.
