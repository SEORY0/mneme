---
type: causal-policy
title: "No Crash Parser Not Reached Ipv4 Cotp Negative Memory"
description: "Round 10 negative memory for no_crash with verifier signal parser_not_reached."
failure_class: "no_crash"
verifier_signal: "parser_not_reached"
candidate_family: "construct"
input_format: "ipv4-cotp"
harness_convention: "libfuzzer-fuzzshark-ip"
vuln_class: "logic-error-empty-payload-dispatch"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-not-reached", "negative-memory", "round-10"]
match_keys: ["no_crash", "parser_not_reached", "ipv4-cotp", "libfuzzer-fuzzshark-ip", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 10
---
# No Crash Parser Not Reached Ipv4 Cotp Negative Memory

## Policy
For `no_crash x parser_not_reached`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
1. Direct COTP, TPKT-wrapped COTP, and IPv4 carriers using ISO transport and ISO network protocol dispatch all executed cleanly.
2. When `no_crash x parser_not_reached` appears for `ipv4-cotp`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
3. Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- COTP data packets use a length indicator followed by a TPDU type and sequence/control byte; CR and CC packets include reference fields and may carry user data after the variable part. In the IP harness, OSI transport is reached through IPv4 protocol dispatch rather than raw COTP bytes.
- Harness: The fuzzshark target consumes raw IPv4 packet bytes and configures the IP dissector. Protocol-specific payloads must be wrapped in an IP header with the correct next-protocol value; direct protocol fragments are ignored as malformed IP.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed round-10 persistent failure.
- Scope: generator avoidance for the same failure-keyed basin.
