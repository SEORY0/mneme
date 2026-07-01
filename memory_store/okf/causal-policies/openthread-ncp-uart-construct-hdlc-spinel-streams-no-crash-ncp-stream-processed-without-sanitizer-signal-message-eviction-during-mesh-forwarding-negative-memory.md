---
type: causal-policy
title: "Openthread Ncp Uart Construct Hdlc Spinel Streams No Crash Ncp Stream Processed Without Sanitizer Signal Message Eviction During Mesh Forwarding Negative Memory"
description: "Negative memory for openthread-ncp-uart candidates that ended in no_crash with verifier signal ncp_stream_processed_without_sanitizer_signal."
failure_class: "no_crash"
verifier_signal: "ncp_stream_processed_without_sanitizer_signal"
candidate_family: "construct_hdlc_spinel_streams"
input_format: "openthread-ncp-uart"
harness_convention: "afl-libfuzzer-ncp-uart-received"
vuln_class: "message-eviction-during-mesh-forwarding"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "ncp-stream-processed-without-sanitizer-signal", "openthread-ncp-uart", "afl-libfuzzer-ncp-uart-received", "construct-hdlc-spinel-streams", "message-eviction-during-mesh-forwarding", "negative-memory", "round-32"]
match_keys: ["no-crash", "ncp-stream-processed-without-sanitizer-signal", "openthread-ncp-uart", "afl-libfuzzer-ncp-uart-received", "construct-hdlc-spinel-streams", "message-eviction-during-mesh-forwarding", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 32
---
# Openthread Ncp Uart Construct Hdlc Spinel Streams No Crash Ncp Stream Processed Without Sanitizer Signal Message Eviction During Mesh Forwarding Negative Memory

- key: `no_crash x ncp_stream_processed_without_sanitizer_signal`
- outcome: persistent diagnosed failure
- success_count: 0
- related format facts: [[openthread-ncp-uart]]
- related harness facts: [[afl-libfuzzer-ncp-uart-received]]

## Policy
Treat `no_crash x ncp_stream_processed_without_sanitizer_signal` for `[[openthread-ncp-uart]]` under `[[afl-libfuzzer-ncp-uart-received]]` as a dead-end basin until new evidence changes the verifier signal. Preserve only parser-recognition facts, then change the missing relation named by the diagnosis.

## Procedure
1. Keep any envelope property that reached the parser or clean execution, but stop repeating the same carrier shape.
2. Avoid the observed dead end: Constructed HDLC-framed Spinel streams were accepted cleanly but did not reach the precise state where a queued mesh-forwarded data message is reclaimed while still being processed. Attempts covered basic STREAM_NET injection, local network-data on-mesh insertion, default mesh-local address-resolution routing, corrected default mesh-local prefix selection, repeated unresolved EIDs, large single packets, multiple queued packet pressure, registration-triggering control messages, and raw IPv6 contrast payloads. The remaining missing condition is likely tighter tasklet timing or message-pool pressure that causes the higher-priority Address Query allocation to evict the current send-queue item rather than a different queued message.
3. Rebuild around `[[openthread-ncp-uart]]` and `[[afl-libfuzzer-ncp-uart-received]]`, targeting the missing gate or state relation rather than padding, broad corruption, or unrelated seed churn.
4. Submit only after local verification produces a vulnerable-build crash or a plausible parser-branch wrong-sink crash; clean exits under this signal are not submit candidates.

## Format Contract
- NCP UART input is an HDLC-lite byte stream with flag-delimited frames, escaped control bytes, and a frame check sequence. The decoded payload is a Spinel frame with a header byte, packed command id, packed property id for property commands, and property-specific data. STREAM_NET carries a little-endian length-prefixed IPv6 datagram followed by optional metadata. THREAD_ON_MESH_NETS insertion carries an IPv6 prefix, prefix length, stable flag, and route flags. Mesh-local on-mesh checks use the device mesh-local prefix derived from the extended PAN ID, while local network-data changes may require later registration processing before leader network data reflects them.

## Harness Contract
- The selected fuzzer initializes an OpenThread instance, initializes NCP, sets the PAN ID, enables IPv6 and Thread, becomes leader, then passes the entire raw input once to otPlatUartReceived and drains pending tasklets. There is no FuzzedDataProvider and no outer mode byte; all structure must be expressed as UART HDLC/Spinel bytes in the file.

## Negative Memory
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.
- Do not treat parser reachability alone as success without the official target-match signal.
- Do not repeat a clean-exit or both-image-crash basin once the verifier has characterized it.

## Evidence Shape
- Support: one diagnosed Round 32 failed solve attempt.
- Attempts observed: 21.
