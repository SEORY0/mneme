---
type: causal-policy
title: "No Crash Card Driver Or Pkcs15 State Not Sufficient Opensc Virtual Card Transcript Negative Memory"
description: "Round 10 negative memory for no_crash with verifier signal card_driver_or_pkcs15_state_not_sufficient."
failure_class: "no_crash"
verifier_signal: "card_driver_or_pkcs15_state_not_sufficient"
candidate_family: "construct"
input_format: "OpenSC virtual-card transcript"
harness_convention: "libfuzzer raw transcript chunks"
vuln_class: "OID decoding/driver emulation edge case"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "card-driver-or-pkcs15-state-not-sufficient", "negative-memory", "round-10"]
match_keys: ["no_crash", "card_driver_or_pkcs15_state_not_sufficient", "OpenSC virtual-card transcript", "libfuzzer raw transcript chunks", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 10
---
# No Crash Card Driver Or Pkcs15 State Not Sufficient Opensc Virtual Card Transcript Negative Memory

## Policy
For `no_crash x card_driver_or_pkcs15_state_not_sufficient`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
1. Oberthur ATR selection and multiple APDU response transcript variants did not produce the target.
2. When `no_crash x card_driver_or_pkcs15_state_not_sufficient` appears for `OpenSC virtual-card transcript`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
3. Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- The input is a sequence of little-endian length-prefixed chunks. The first chunk becomes the virtual card ATR. Each later chunk is one APDU response where the final two bytes are status words and preceding bytes are response data.
- Harness: The harness installs a fuzz reader, connects a virtual card, binds PKCS#15, then consumes additional chunks as operation inputs only after a p15 card exists. Raw ASN.1 bytes at the start are interpreted as an ATR, not as file content.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed round-10 persistent failure.
- Scope: generator avoidance for the same failure-keyed basin.
