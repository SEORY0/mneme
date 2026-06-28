---
type: causal-policy
title: "No Crash Transport Reached No Target Error Http2 Frame Stream Negative Memory"
description: "Round 24 negative memory for no_crash with verifier signal transport_reached_no_target_error."
failure_class: "no_crash"
verifier_signal: "transport_reached_no_target_error"
candidate_family: "construct"
input_format: "http2-frame-stream"
harness_convention: "libfuzzer-h2o-http2"
vuln_class: "http2-state-machine-error"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "transport-reached-no-target-error", "http2-frame-stream", "libfuzzer-h2o-http2", "construct", "negative-memory", "round-24"]
match_keys: ["no-crash", "transport-reached-no-target-error", "http2-frame-stream", "libfuzzer-h2o-http2", "http2-state-machine-error"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 24
---
# No Crash Transport Reached No Target Error Http2 Frame Stream Negative Memory

- key: `no_crash x transport_reached_no_target_error`
- outcome: negative memory
- success_count: 0
- failure_count: 1
- formats: [[http2-frame-stream]]
- harnesses: [[libfuzzer-h2o-http2]]

## Dead-End Shape
Valid-looking HTTP/2 client preface, SETTINGS, HEADERS, and DATA-after-END_STREAM sequences executed without crashing. Variants changed path, content-length, empty-body termination, and packet splitting but did not trigger the streaming-body error propagation bug.

## Policy
For `no_crash x transport_reached_no_target_error` on `http2-frame-stream`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission. Prefer `construct` only while this format and harness contract are present.

## Procedure
1. When `no_crash x transport_reached_no_target_error` appears for `http2-frame-stream`, treat this candidate family as a basin-to-avoid rather than evidence of proximity.
2. Preserve any proven format or harness envelope, but change the missing gate, state relation, or sink path before another official submission.
3. Prefer a different construction family if the same verifier signal repeats without new parser-depth evidence.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for recovery policies; local crash class is supporting evidence only.

## Negative Memory
- Do not resubmit candidates that are clean, off-target, rejected before the target path, or crashing both fixed and vulnerable images in this same shape.
- Do not promote this trace as a recovery unless a later verifier run flips the target relation.
- Preserve only descriptive format and harness facts from this failed attempt.

## Evidence Shape
- Support: one diagnosed round 24 persistent failure.
- Scope: generator repair and retargeting only.
