---
type: causal-policy
title: "No Crash Sip Sdp Clean Exit Sip Message Sdp Body Negative Memory"
description: "Round 10 negative memory for no_crash with verifier signal sip_sdp_clean_exit."
failure_class: "no_crash"
verifier_signal: "sip_sdp_clean_exit"
candidate_family: "construct_sip_sdp"
input_format: "sip-message-with-sdp-body"
harness_convention: "libfuzzer"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "sip-sdp-clean-exit", "negative-memory", "round-10"]
match_keys: ["no_crash", "sip_sdp_clean_exit", "sip-message-with-sdp-body", "libfuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 10
---
# No Crash Sip Sdp Clean Exit Sip Message Sdp Body Negative Memory

## Policy
For `no_crash x sip_sdp_clean_exit`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
1. A syntactically valid SIP INVITE with an SDP body parsed cleanly.
2. When `no_crash x sip_sdp_clean_exit` appears for `sip-message-with-sdp-body`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
3. Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- The carrier is a complete SIP message with headers, Content-Type selecting SDP, Content-Length matching the body, and an SDP body with session lines and media/attribute lines. SDP parsing is line-oriented and depends on valid v/o/s/t/m lines before attributes are useful.
- Harness: The fuzzer passes the entire raw byte string as a SIP message buffer, calls parse_msg, parse_headers, parse_sdp, and several SIP header parsers. There is no front selector or FuzzedDataProvider layout; SIP and Content-Length syntax are the main gates.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed round-10 persistent failure.
- Scope: generator avoidance for the same failure-keyed basin.
