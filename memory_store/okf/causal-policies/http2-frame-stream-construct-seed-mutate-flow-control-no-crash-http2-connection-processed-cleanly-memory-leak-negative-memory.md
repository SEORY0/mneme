---
type: causal-policy
title: "HTTP2 Frame Stream Construct Seed Mutate Flow Control No Crash HTTP2 Connection Processed Cleanly Memory Leak Negative Memory"
description: "Negative memory for http2-frame-stream candidates that ended in no_crash with verifier signal http2_connection_processed_cleanly."
failure_class: "no_crash"
verifier_signal: "http2_connection_processed_cleanly"
candidate_family: "construct_seed_mutate_flow_control"
input_format: "http2-frame-stream"
harness_convention: "afl-libfuzzer-http2-socket"
vuln_class: "memory-leak"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "http2-connection-processed-cleanly", "http2-frame-stream", "afl-libfuzzer-http2-socket", "construct-seed-mutate-flow-control", "memory-leak", "negative-memory", "round-32"]
match_keys: ["no-crash", "http2-connection-processed-cleanly", "http2-frame-stream", "afl-libfuzzer-http2-socket", "construct-seed-mutate-flow-control", "memory-leak", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 32
---
# HTTP2 Frame Stream Construct Seed Mutate Flow Control No Crash HTTP2 Connection Processed Cleanly Memory Leak Negative Memory

- key: `no_crash x http2_connection_processed_cleanly`
- outcome: persistent diagnosed failure
- success_count: 0
- related format facts: [[http2-frame-stream]]
- related harness facts: [[afl-libfuzzer-http2-socket]]

## Policy
Treat `no_crash x http2_connection_processed_cleanly` for `[[http2-frame-stream]]` under `[[afl-libfuzzer-http2-socket]]` as a dead-end basin until new evidence changes the verifier signal. Preserve only parser-recognition facts, then change the missing relation named by the diagnosis.

## Procedure
1. Keep any envelope property that reached the parser or clean execution, but stop repeating the same carrier shape.
2. Avoid the observed dead end: Constructed and seed-mutated HTTP/2 streams were accepted by the harness but did not produce the target leak. Attempts covered valid preface and SETTINGS envelopes, parent streams left in request-body state, dependent child requests, child resets before parent close, SETTINGS ACK and window updates, corpus HPACK blocks, multiple children, streaming proxy parents, active recently-closed dependencies, priority-only parent resets, and a flow-control variant intended to make child scheduler activation explicit. The likely missing relation is the exact timing that leaves a scheduler queue allocated on a source stream whose child-ref list is empty at relocation.
3. Rebuild around `[[http2-frame-stream]]` and `[[afl-libfuzzer-http2-socket]]`, targeting the missing gate or state relation rather than padding, broad corruption, or unrelated seed churn.
4. Submit only after local verification produces a vulnerable-build crash or a plausible parser-branch wrong-sink crash; clean exits under this signal are not submit candidates.

## Format Contract
- The input is a raw HTTP/2 client byte stream: connection preface, binary frame headers, SETTINGS, PRIORITY, HEADERS, RST_STREAM, DATA, optional WINDOW_UPDATE frames, HPACK request header blocks, stream identifiers, END_HEADERS, END_STREAM, and PRIORITY flags. Stream dependency and close ordering, not a file header, determine whether the scheduler relocation path is exercised.

## Harness Contract
- The AFL/libFuzzer-compatible H2O harness reads the submitted file and writes it to a socket in chunks split by a textual marker. Bytes before each marker are sent as one client write, empty marker turns let the event loop drain without adding protocol bytes, and the server runs H2O HTTP/2 with fixed, reverse-proxy, and file-root handlers.

## Negative Memory
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.
- Do not treat parser reachability alone as success without the official target-match signal.
- Do not repeat a clean-exit or both-image-crash basin once the verifier has characterized it.

## Evidence Shape
- Support: one diagnosed Round 32 failed solve attempt.
- Attempts observed: 13.
