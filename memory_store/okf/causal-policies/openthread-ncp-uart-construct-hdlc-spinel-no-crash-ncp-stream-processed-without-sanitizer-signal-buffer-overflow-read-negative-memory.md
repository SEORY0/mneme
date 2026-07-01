---
type: negative-memory
title: "Openthread Ncp Uart Construct Hdlc Spinel No Crash Ncp Stream Processed Without Sanitizer Signal Buffer Overflow Read Negative Memory"
description: "Round 33 negative memory for no_crash with verifier signal ncp_stream_processed_without_sanitizer_signal."
failure_class: "no_crash"
verifier_signal: "ncp_stream_processed_without_sanitizer_signal"
candidate_family: "construct-hdlc-spinel"
input_format: "openthread-ncp-uart"
harness_convention: "libfuzzer"
vuln_class: "buffer-overflow-read"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["no-crash", "ncp-stream-processed-without-sanitizer-signal", "openthread-ncp-uart", "libfuzzer", "construct-hdlc-spinel", "buffer-overflow-read", "negative-memory", "round-33"]
match_keys: ["no_crash", "ncp_stream_processed_without_sanitizer_signal", "openthread-ncp-uart", "libfuzzer", "construct-hdlc-spinel", "buffer-overflow-read", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 33
---
# Openthread Ncp Uart Construct Hdlc Spinel No Crash Ncp Stream Processed Without Sanitizer Signal Buffer Overflow Read Negative Memory

- key: `no_crash x ncp_stream_processed_without_sanitizer_signal`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[openthread-ncp-uart]]
- related harness facts: [[libfuzzer]]

## Failure Shape
The selected harness is NCP UART, not CLI text. HDLC-framed Spinel streams were accepted cleanly, but the attempted state transitions did not produce a vulnerable-only sanitizer signal. Attempts covered normal local on-mesh route registration, off-mesh route registration, stable service registration, near-limit service data, raw IPv6/UDP/CoAP server-data registration through the stream property, a high-margin valid-TLV service update, and a normal NCP sequence that registered non-stable padding routes before updating the same service with a maximum server-data field. The likely missing condition is a precise leader network-data comparison state that creates an addressable-looking but sanitizer-visible TLV overread; the public NCP property APIs tend to rebuild valid local TLVs or keep the overread within addressable object storage.

## Policy
Treat `no_crash x ncp_stream_processed_without_sanitizer_signal` on `openthread-ncp-uart` as a basin to avoid unless a new candidate changes the parser gate, state relation, sink relation, or official differential behavior described below. Do not repeat variants that only preserve the same clean-exit, off-target, post-patch-crash, both-image-crash, or target-handoff-missing signal.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing relation from the verifier signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one causal relation at a time and discard candidates that return to `ncp_stream_processed_without_sanitizer_signal`.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed vulnerable-only target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `ncp_stream_processed_without_sanitizer_signal`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, clean exits, timeouts, or fixed-image crashes as success.
- Never store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[openthread-ncp-uart]]. OpenThread NCP UART input is an HDLC-lite stream of flag-delimited Spinel frames. Decoded Spinel property frames contain a header byte, a packed command id, a packed property id, and property-specific values. THREAD_ON_MESH_NETS and THREAD_OFF_MESH_ROUTES insertions carry an IPv6 prefix, prefix length, stable flag, and route flags after local network-data changes are enabled. SERVER_SERVICES insertion carries an enterprise number, length-prefixed service data, stable flag, and length-prefixed server data. Thread Network Data TLVs use a one-byte type/stable discriminator and a one-byte length, with nested Prefix, HasRoute, Service, and Server TLVs governed by their advertised lengths.

## Harness Contract
Use [[libfuzzer]]. The libFuzzer target feeds raw bytes to the NCP UART receive path after initializing a single OpenThread instance, enabling IPv6 and Thread, and becoming leader. There is no FuzzedDataProvider or mode byte. The UART stream must be HDLC-framed Spinel; local network-data and server-data changes register with the leader on true-to-false allow-property transitions. STREAM_NET and STREAM_NET_INSECURE carry little-endian length-prefixed IPv6 datagrams followed by optional metadata.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 33 after 8 attempts.
- Scope: generator repair and basin avoidance only.
