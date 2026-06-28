---
type: causal-policy
title: "No Crash Openssl Server Handshake Executed Clean Tls Clienthello Stream Negative Memory"
description: "Round 9 negative memory for no_crash with verifier signal openssl_server_handshake_executed_clean."
failure_class: "no_crash"
verifier_signal: "openssl_server_handshake_executed_clean"
candidate_family: "seed_mutate-and-construct"
input_format: "tls-clienthello-stream"
harness_convention: "afl-file-fuzzer"
vuln_class: "heap-use-after-free"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "openssl-server-handshake-executed-clean", "tls-clienthello-stream", "negative-memory", "round-9"]
match_keys: ["no_crash", "openssl_server_handshake_executed_clean", "tls-clienthello-stream", "afl-file-fuzzer", "heap-use-after-free", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 9
---
# No Crash Openssl Server Handshake Executed Clean Tls Clienthello Stream Negative Memory

- key: `no_crash x openssl_server_handshake_executed_clean`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[tls-clienthello-stream]]
- related harness facts: [[afl-file-fuzzer]]

## Failure Shape
- Large and small server corpus seeds plus a minimal ClientHello executed cleanly.
- The missing invariant is a TLS handshake/session-ticket or PSK extension path that frees a session
  object and then continues to use the stale sess variable before it is nulled.

## Policy
Treat `no_crash x openssl_server_handshake_executed_clean` on `tls-clienthello-stream` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
- The server fuzzer consumes TLS record bytes representing the client side of an OpenSSL server
  handshake.
- Useful inputs are ClientHello-oriented byte streams with coherent TLS record headers, handshake
  lengths, protocol version, random/session fields, cipher suites, and extensions such as session
  tickets or PSK-related data.

## Harness Contract
- The AFL wrapper feeds the raw file bytes to the OpenSSL server fuzzer.
- There is no extra prefix; the fuzzer initializes a server context with built-in credentials and
  drives the first part of the server handshake from the supplied TLS records.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `openssl_server_handshake_executed_clean`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 9.
- Scope: generator repair and basin avoidance only.
