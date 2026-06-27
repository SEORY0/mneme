---
type: causal-policy
title: "No Crash Parser Not Reached Sctp Packet Negative Memory"
description: "Round 16 negative memory for no_crash with verifier signal parser_not_reached."
failure_class: "no_crash"
verifier_signal: "parser_not_reached"
candidate_family: "seed_mutate+construct"
input_format: "sctp-packet"
harness_convention: "afl-file"
vuln_class: "integer-overflow"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-not-reached", "sctp-packet", "negative-memory", "round-16"]
match_keys: ["no_crash", "parser_not_reached", "sctp-packet", "afl-file", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 16
---
# No Crash Parser Not Reached Sctp Packet Negative Memory

## Policy
For `no_crash x parser_not_reached`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
- Initial attempts assumed the connect-side fuzzer and targeted stale-cookie ERROR handling, but the built target was the listen-side AFL harness. Listen-side INIT packets with cookie-preserve parameters were accepted without crashing, and corpus packets did not reach a stale-cookie arithmetic fault.
- When `no_crash x parser_not_reached` appears for `sctp-packet`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
- Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- SCTP packets have a common header followed by typed chunks. INIT chunks carry an initiate tag, receive window, stream counts, initial sequence value, and optional parameters such as cookie-preserve. ERROR chunks carry nested causes such as stale-cookie with a staleness value.
- Harness: The built binary is an AFL-style listen fuzzer. It reads one raw SCTP packet including the common header and injects it into a passive endpoint; it does not use the connect-fuzzer first-byte handshake selector in this task image.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed persistent failure from round 16.
- Scope: generator avoidance for the same failure-keyed basin.
