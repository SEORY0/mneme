---
type: causal-policy
title: "Raw Ipv4 Packet Construct Raw IP Packet Target Sink Ndpi Check Amazon Video Heap Buffer Overflow Read Verified Recovery"
description: "Round 20 verified recovery for generic_crash with verifier signal target_sink_ndpi_check_amazon_video."
failure_class: "generic_crash"
verifier_signal: "target_sink_ndpi_check_amazon_video"
candidate_family: "construct_raw_ip_packet"
input_format: "raw IPv4 packet"
harness_convention: "AFL/libFuzzer raw nDPI process-packet"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: medium
tags: ["generic-crash", "target-sink-ndpi-check-amazon-video", "raw-ipv4-packet", "afl-libfuzzer-raw-ndpi-process-packet", "construct-raw-ip-packet", "verified-recovery", "round-20"]
match_keys: ["generic-crash", "target-sink-ndpi-check-amazon-video", "raw-ipv4-packet", "afl-libfuzzer-raw-ndpi-process-packet", "heap-buffer-overflow-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 20
---
# Raw Ipv4 Packet Construct Raw IP Packet Target Sink Ndpi Check Amazon Video Heap Buffer Overflow Read Verified Recovery

- key: `generic_crash x target_sink_ndpi_check_amazon_video`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[raw-ipv4-packet]]
- harnesses: [[afl-libfuzzer-raw-ndpi-process-packet]]

## Failure Shape
Build a valid IPv4/TCP carrier with a payload-bearing TCP header so nDPI dispatches protocol dissectors. Select the Amazon Video TCP magic prefix but make the application payload shorter than the four-byte magic comparison, causing the dissector to read beyond the packet buffer while all IP/TCP length fields remain coherent.

## Policy
For `generic_crash x target_sink_ndpi_check_amazon_video` on `raw IPv4 packet`, preserve the parser and harness gates first, then mutate only the causal invariant described by the verified trace. Prefer `construct_raw_ip_packet` while this format and harness contract are present.

## Procedure
1. Preserve the `raw IPv4 packet` carrier enough for the `AFL/libFuzzer raw nDPI process-packet` harness to reach the parser path.
2. Keep unrelated envelope fields minimal and stable so verifier feedback stays tied to the target sink.
3. Apply the verified invariant from the failure shape rather than random broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The local class may remain coarse. Treat the official vulnerable-versus-fixed target match as the confirmation gate for this policy.

## Negative Memory
- Do not corrupt the outer `raw IPv4 packet` recognition gate while retargeting this signal.
- Do not treat off-target crashes or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified round 20 solve.
- Scope: generator repair only.
