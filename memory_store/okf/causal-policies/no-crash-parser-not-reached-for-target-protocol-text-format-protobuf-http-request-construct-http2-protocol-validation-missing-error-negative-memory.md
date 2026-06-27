---
type: causal-policy
title: "No Crash Parser Not Reached For Target Protocol Text Format Protobuf Http Request Construct Http2 Protocol Validation Missing Error Negative Memory"
description: "Round 14 negative memory for no_crash with verifier signal parser_not_reached_for_target_protocol."
failure_class: "no_crash"
verifier_signal: "parser_not_reached_for_target_protocol"
candidate_family: "construct"
input_format: "text-format-protobuf-http-request"
harness_convention: "libfuzzer-protobuf-mutator"
vuln_class: "http2-protocol-validation-missing-error"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-not-reached-for-target-protocol", "text-format-protobuf-http-request", "negative-memory", "round-14"]
match_keys: ["no_crash", "parser_not_reached_for_target_protocol", "text-format-protobuf-http-request", "libfuzzer-protobuf-mutator", "http2-protocol-validation-missing-error", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 14
---
# No Crash Parser Not Reached For Target Protocol Text Format Protobuf Http Request Construct Http2 Protocol Validation Missing Error Negative Memory

- key: `no_crash x parser_not_reached_for_target_protocol`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[text-format-protobuf-http-request]]
- related harness facts: [[libfuzzer-protobuf-mutator]]

## Failure Shape
Raw HTTP/2 frame candidates were not the correct harness contract. The actual harness parses text-format protobuf with request and reply strings, then feeds C-string request bytes into nginx. That contract makes embedded-NUL HTTP/2 frame bytes difficult to represent directly, and the tested text-protobuf request routes did not reach the invalid-stream-id HTTP/2 state machine.

## Policy
Treat `no_crash x parser_not_reached_for_target_protocol` on `text-format-protobuf-http-request` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest carrier that the verifier proved reaches the parser, decoder, or harness path.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, parser-not-reached, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not count parser reachability, local crashes, clean exits, fixed-image crashes, usage banners, or sink mismatches as success.
- Do not repeat this candidate family unless the new attempt changes the causal gate named above.
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from Round 14.
- Scope: generator repair and basin avoidance only.
