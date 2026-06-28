---
type: causal-policy
title: "No Crash Packet Injected Clean Exit Sctp Packet Negative Memory"
description: "Round 10 negative memory for no_crash with verifier signal packet_injected_clean_exit."
failure_class: "no_crash"
verifier_signal: "packet_injected_clean_exit"
candidate_family: "construct"
input_format: "sctp-packet"
harness_convention: "afl/libfuzzer-compatible"
vuln_class: "uninitialized-stack"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "packet-injected-clean-exit", "negative-memory", "round-10"]
match_keys: ["no_crash", "packet_injected_clean_exit", "sctp-packet", "afl/libfuzzer-compatible", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 10
---
# No Crash Packet Injected Clean Exit Sctp Packet Negative Memory

## Policy
For `no_crash x packet_injected_clean_exit`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
1. The selected binary was the client connect fuzzer, not the listener.
2. When `no_crash x packet_injected_clean_exit` appears for `sctp-packet`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
3. Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- SCTP packets have a common header followed by typed chunks with chunk-local lengths and padding. In this client harness the common header is synthesized by the target for the fuzzed packet, so the file bytes after the selector represent chunk payloads rather than a full wire packet.
- Harness: The first input byte selects a handshake stage when the build does not force one. The harness internally opens an SCTP client, injects canned peer handshake packets, prepends a common header with the captured verification tag to the remaining fuzz bytes, and then feeds that packet to usrsctp.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed round-10 persistent failure.
- Scope: generator avoidance for the same failure-keyed basin.
