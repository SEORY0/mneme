---
type: causal-policy
title: "No Crash Http2 Connection Processed Cleanly Http2 Request Stream Negative Memory"
description: "Round 12 negative memory for no_crash with verifier signal http2_connection_processed_cleanly."
failure_class: "no_crash"
verifier_signal: "http2_connection_processed_cleanly"
candidate_family: "seed_mutate_and_construct"
input_format: "http2-request-stream"
harness_convention: "afl/libfuzzer-compatible stdin harness"
vuln_class: "memory-leak"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "http2-connection-processed-cleanly", "http2-request-stream", "negative-memory", "round-12"]
match_keys: ["no_crash", "http2_connection_processed_cleanly", "http2-request-stream", "afl-libfuzzer-compatible-stdin-harness", "memory-leak", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 12
---
# No Crash Http2 Connection Processed Cleanly Http2 Request Stream Negative Memory

- key: `no_crash x http2_connection_processed_cleanly`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[http2-request-stream]]
- related harness facts: [[afl-libfuzzer-compatible-stdin-harness]]

## Failure Shape
Valid HTTP/2 corpus inputs and synthetic priority/reset sequences were accepted by the server harness but did not create the specific recently-closed stream relocation state that leaks when the source scheduler has no descendants.

## Policy
Treat `no_crash x http2_connection_processed_cleanly` on `http2-request-stream` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
The input is a raw HTTP/2 byte stream delivered as a client connection. A useful carrier begins with the HTTP/2 client preface, then binary HTTP/2 frames such as SETTINGS, PRIORITY, HEADERS, and stream-closing frames. Stream dependency and priority state, not a file header, control reachability.

## Harness Contract
The harness writes the raw input to one side of a socket pair, accepts the other side as an H2O HTTP/2 connection, then runs the event loop until the connection closes. There is no mode byte or FuzzedDataProvider carving; the whole input is interpreted as network bytes.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `http2_connection_processed_cleanly`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 12.
- Scope: generator repair and basin avoidance only.
