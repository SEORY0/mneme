---
type: causal-policy
title: "TLS Clienthello Seed Mutate Parser Reached Sink Match Out Of Bounds Read Verified Recovery"
description: "Round 29 verified recovery for generic_crash with verifier signal parser_reached_sink_match."
failure_class: "generic_crash"
verifier_signal: "parser_reached_sink_match"
candidate_family: "seed_mutate"
input_format: "tls-clienthello"
harness_convention: "afl/libfuzzer wolfssl-server"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-sink-match", "tls-clienthello", "afl-libfuzzer-wolfssl-server", "seed-mutate", "out-of-bounds-read", "verified-recovery", "round-29"]
match_keys: ["generic_crash", "parser_reached_sink_match", "tls-clienthello", "afl/libfuzzer wolfssl-server", "out-of-bounds-read", "generic-crash", "parser-reached-sink-match", "tls-clienthello", "afl-libfuzzer-wolfssl-server", "out-of-bounds-read", "verified_recovery", "seed_mutate", "seed-mutate"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 29
---
# TLS Clienthello Seed Mutate Parser Reached Sink Match Out Of Bounds Read Verified Recovery

- key: `generic_crash x parser_reached_sink_match`
- outcome: verified target match / recovery policy
- success_count: 1
- related format facts: [[tls-clienthello]]
- related harness facts: [[afl-libfuzzer-wolfssl-server]]

## Policy
For `generic_crash x parser_reached_sink_match` on `tls-clienthello`, keep the parser and harness gates that produced the verifier signal, then vary only the causal relation described below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Use a structurally valid TLS ClientHello for the wolfSSL server harness that already reaches extension parsing. Preserve the TLS record, ClientHello, extension block, and status-request extension envelope, but make the OCSP status-request responder-id vector declare a size that extends beyond the extension body. The vulnerable parser advances by that unchecked vector size and then reads the next vector length outside the extension data; the fixed build rejects the inconsistent vector before the read.
2. Preserve format recognition and the harness input contract while mutating the narrow sink invariant; do not broaden into an off-target crash or a both-image crash.
3. If later verifier output changes the failure key, re-rank against that new key before mutating unrelated fields.

## Format Contract
- Format [[tls-clienthello]]: The input is a TLS handshake record containing a ClientHello. The ClientHello body includes version/random fields, session-id, cipher-suite and compression vectors, then a two-byte total extensions length followed by extension records. A status-request extension contains a one-byte status type, a two-byte responder-id-list vector length and bytes, then a two-byte request-extensions vector length and bytes.
- Harness [[afl-libfuzzer-wolfssl-server]]: The /bin/arvo wrapper runs the wolfSSL server fuzz target on the PoC file as raw network input. The harness installs custom recv/send callbacks and feeds the raw file bytes sequentially to wolfSSL_accept, resetting the same bytes for several server protocol methods. There is no FuzzedDataProvider splitting and no leading mode byte.

## Negative Memory
- Do not corrupt the outer `tls-clienthello` recognition gate while retargeting this signal.
- Do not count parser reachability, clean exits, fixed-image crashes, both-image crashes, or local wrong-sink labels as success without official target match.
- Never store payload bytes, exact positions, checksums, submit metadata, or task-local identifiers.

## Evidence Shape
- Support: one round-29 worker trace with official target match.
- Scope: generator repair and retargeting only; pair with [[tls-clienthello]] and [[afl-libfuzzer-wolfssl-server]].
