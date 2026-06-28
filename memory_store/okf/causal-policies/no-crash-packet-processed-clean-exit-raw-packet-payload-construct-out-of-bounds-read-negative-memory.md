---
type: negative-memory
title: "No Crash Packet Processed Clean Exit Raw Packet Payload Construct Out Of Bounds Read Negative Memory"
description: "Round 25 negative memory for no_crash with verifier signal packet_processed_clean_exit."
failure_class: "no_crash"
verifier_signal: "packet_processed_clean_exit"
candidate_family: "construct"
input_format: "raw-packet-payload"
harness_convention: "libfuzzer"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "packet-processed-clean-exit", "raw-packet-payload", "libfuzzer", "construct", "negative-memory", "round-25"]
match_keys: ["no_crash", "packet_processed_clean_exit", "raw-packet-payload", "libfuzzer", "out-of-bounds-read", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 25
---
# No Crash Packet Processed Clean Exit Raw Packet Payload Construct Out Of Bounds Read Negative Memory

- key: `no_crash x packet_processed_clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[raw-packet-payload]]
- related harness facts: [[libfuzzer]]

## Failure Shape
HTTP-like, NATS-like, and BitTorrent-like payloads reached the nDPI process-packet harness but did not fault in ndpi_strnstr. The missing relation is likely a protocol path where a bounded search length and an unterminated payload segment disagree, rather than a generic text packet.

## Policy
Treat `no_crash x packet_processed_clean_exit` on `raw-packet-payload` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, wrapper-mismatch, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `packet_processed_clean_exit` basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `packet_processed_clean_exit`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
The active nDPI process-packet target treats the entire input as one packet payload. Protocol detectors call bounded substring helpers over payload slices such as HTTP headers, NATS control lines, BitTorrent handshakes, and other application data.

## Harness Contract
The libFuzzer harness initializes nDPI once, allocates a flow, calls ndpi_detection_process_packet with the whole byte buffer and its size, then gives up detection and frees the flow. No outer pcap header or provider-carved fields are used by this target.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 25 after 3 attempts.
- Scope: generator repair and basin avoidance only.
