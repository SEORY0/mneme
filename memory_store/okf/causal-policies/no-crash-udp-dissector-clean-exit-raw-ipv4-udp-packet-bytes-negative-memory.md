---
type: causal-policy
title: "No Crash UDP Dissector Clean Exit Raw Ipv4 UDP Packet Bytes Negative Memory"
description: "Round 16 negative memory for no_crash with verifier signal udp_dissector_clean_exit."
failure_class: "no_crash"
verifier_signal: "udp_dissector_clean_exit"
candidate_family: "construct"
input_format: "raw IPv4/UDP packet bytes"
harness_convention: "libfuzzer Wireshark udp dissector handoff"
vuln_class: "heap-use-after-free"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "udp-dissector-clean-exit", "raw-ipv4-udp-packet-bytes", "negative-memory", "round-16"]
match_keys: ["no_crash", "udp_dissector_clean_exit", "raw IPv4/UDP packet bytes", "libfuzzer Wireshark udp dissector handoff", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 16
---
# No Crash UDP Dissector Clean Exit Raw Ipv4 UDP Packet Bytes Negative Memory

## Policy
For `no_crash x udp_dissector_clean_exit`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
- Raw IPv4/UDP envelopes using H.225 RAS and call-signaling port hypotheses did not drive the UDP dissector handoff into the H.225 RasMessage path or next_tvb reuse condition.
- When `no_crash x udp_dissector_clean_exit` appears for `raw IPv4/UDP packet bytes`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
- Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- For this oss-fuzzshark target, the input is a raw packet buffer interpreted by the UDP dissector table through an IPv4 protocol handoff. A packet must include a coherent IPv4 header, UDP header, and payload whose ports and payload cause secondary protocol dispatch.
- Harness: The wrapper runs fuzzshark configured for the UDP dissector in the IP protocol table. It wraps the raw bytes in an in-memory Wireshark frame, dissects them, then resets the epan dissection state between iterations.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed persistent failure from round 16.
- Scope: generator avoidance for the same failure-keyed basin.
