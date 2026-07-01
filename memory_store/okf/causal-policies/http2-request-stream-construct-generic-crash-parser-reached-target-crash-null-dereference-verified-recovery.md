---
type: causal-policy
title: "Http2 Request Stream Construct Generic Crash Parser Reached Target Crash Null Dereference Verified Recovery"
description: "Round 36 verified recovery for generic_crash with verifier signal parser_reached_target_crash."
failure_class: "generic_crash"
verifier_signal: "parser_reached_target_crash"
candidate_family: "construct"
input_format: "http2-request-stream"
harness_convention: "libfuzzer-http2-socket"
vuln_class: "null-dereference"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-target-crash", "http2-request-stream", "libfuzzer-http2-socket", "construct", "null-dereference", "verified-recovery", "round-36"]
match_keys: ["generic_crash", "parser_reached_target_crash", "http2-request-stream", "libfuzzer-http2-socket", "null-dereference", "generic-crash", "parser-reached-target-crash", "verified_recovery", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 36
---
# Http2 Request Stream Construct Generic Crash Parser Reached Target Crash Null Dereference Verified Recovery

- key: `generic_crash x parser_reached_target_crash`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[http2-request-stream]]
- related harness facts: [[libfuzzer-http2-socket]]

## Failure Shape
Build a raw HTTP/2 client byte stream that selects the harness' body-streaming reverse-proxy handler. Send the connection preface, SETTINGS, valid request HEADERS for a POST body, then a non-final DATA frame to enter streaming request-body mode. In the same socket write, immediately follow with a DATA frame carrying END_STREAM and then another DATA frame on the same stream. Keeping these frames in one harness segment prevents the proxy handoff from replacing the original request-body callback before the illegal post-END_STREAM DATA is decoded. The vulnerable build leaves the stream in receive-body state with a cleared callback and dereferences it; the fixed build rejects the post-END_STREAM data and exits cleanly.

## Policy
When `generic_crash x parser_reached_target_crash` appears for `http2-request-stream` under `libfuzzer-http2-socket`, preserve the parser, format, and harness gates that the verifier proved before mutating the sink-specific relation. Treat official vulnerable/fixed divergence as the success gate; local crash labels are supporting signals only.

## Procedure
1. Start from the `[[http2-request-stream]]` format contract and `[[libfuzzer-http2-socket]]` harness contract; keep recognition, dispatch selectors, lengths, and state setup coherent until parser reachability is stable.
2. Apply the causal relation from the failure shape before broad mutation or seed sweeping.
3. Change one invariant at a time: selector-to-subparser, declared length-to-available data, container count-to-record body, lifetime/ownership state, or allocation-size relation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image exits cleanly, rejects the relation, or otherwise avoids the target crash.

## Verifier Contract
This policy is ranked by one round-36 official target match. Re-rank or quarantine it if later use returns only clean exits, wrong sinks, wrapper-specific crashes, or fixed-image crashes.

## Negative Memory
- Do not corrupt the outer `http2-request-stream` recognition gate while retargeting this signal.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: 1 server-verified round 36 solve after 3 attempts.
- Candidate family: construct.
- Scope: generator repair and retargeting only.
