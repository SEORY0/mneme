---
type: causal-policy
title: "No Crash Quic Envelope Reached But No Target Crash Ip Packet Carrying Quic Negative Memory"
description: "Round 10 negative memory for no_crash with verifier signal quic_envelope_reached_but_no_target_crash."
failure_class: "no_crash"
verifier_signal: "quic_envelope_reached_but_no_target_crash"
candidate_family: "seed_mutate"
input_format: "raw IP packet carrying QUIC"
harness_convention: "libfuzzer raw packet processor"
vuln_class: "integer-overflow/wild-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "quic-envelope-reached-but-no-target-crash", "negative-memory", "round-10"]
match_keys: ["no_crash", "quic_envelope_reached_but_no_target_crash", "raw IP packet carrying QUIC", "libfuzzer raw packet processor", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 10
---
# No Crash Quic Envelope Reached But No Target Crash Ip Packet Carrying Quic Negative Memory

## Policy
For `no_crash x quic_envelope_reached_but_no_target_crash`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
1. Real QUIC packets extracted from repository pcaps and targeted mutations of Initial-packet variable-length fields did not crash.
2. When `no_crash x quic_envelope_reached_but_no_target_crash` appears for `raw IP packet carrying QUIC`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
3. Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- The target expects a complete raw IP packet, not a pcap file. QUIC must be inside UDP, use a long-header Initial form, have a supported version, CID lengths within limits, and a sufficiently large UDP payload before QUIC length parsing proceeds.
- Harness: The fuzz target passes the entire input buffer directly to nDPI packet processing as one packet. There is no pcap decoding and no leading mode selector.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed round-10 persistent failure.
- Scope: generator avoidance for the same failure-keyed basin.
