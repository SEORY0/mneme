---
type: causal-policy
title: "No Crash Parser Not Reached Fluent Bit Http Fuzzer Envelope Negative Memory"
description: "Round 16 negative memory for no_crash with verifier signal parser_not_reached."
failure_class: "no_crash"
verifier_signal: "parser_not_reached"
candidate_family: "construct"
input_format: "fluent-bit-http-fuzzer-envelope"
harness_convention: "libfuzzer"
vuln_class: "integer-overflow"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-not-reached", "fluent-bit-http-fuzzer-envelope", "negative-memory", "round-16"]
match_keys: ["no_crash", "parser_not_reached", "fluent-bit-http-fuzzer-envelope", "libfuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 16
---
# No Crash Parser Not Reached Fluent Bit Http Fuzzer Envelope Negative Memory

## Policy
For `no_crash x parser_not_reached`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
- The vulnerable chunk-size arithmetic requires chunked response parsing, but the OSS-Fuzz harness copies only a small fixed-size final response slice after consuming earlier fields. Compact chunked headers, content-length alternatives, and malformed response slices did not reach the chunk parser or overflow path.
- When `no_crash x parser_not_reached` appears for `fluent-bit-http-fuzzer-envelope`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
- Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- The HTTP client parser expects response headers terminated by a blank line. Chunked decoding requires a transfer-encoding header, then hexadecimal chunk sizes followed by chunk data and line endings. The vulnerable value is the parsed chunk size before it is used for buffer adjustment.
- Harness: The fuzzer consumes fields front-to-back: optional proxy text, URI text, method byte, authentication text, buffer-size controls, a large custom-header key view, and finally a fixed-size null-terminated response slice assigned to the client response before calling the parser helper.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed persistent failure from round 16.
- Scope: generator avoidance for the same failure-keyed basin.
