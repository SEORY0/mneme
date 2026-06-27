---
type: causal-policy
title: "No Crash Idprime State Not Sufficient Opensc Pkcs15 Crypt Cli Virtual Negative Memory"
description: "Round 10 negative memory for no_crash with verifier signal idprime_state_not_sufficient."
failure_class: "no_crash"
verifier_signal: "idprime_state_not_sufficient"
candidate_family: "construct"
input_format: "OpenSC pkcs15-crypt CLI bytes plus virtual-card transcript"
harness_convention: "libfuzzer CLI option and card-response fuzzer"
vuln_class: "string handling/type confusion in card metadata"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "idprime-state-not-sufficient", "negative-memory", "round-10"]
match_keys: ["no_crash", "idprime_state_not_sufficient", "OpenSC pkcs15-crypt CLI bytes plus virtual-card transcript", "libfuzzer CLI option and card-response fuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 10
---
# No Crash Idprime State Not Sufficient Opensc Pkcs15 Crypt Cli Virtual Negative Memory

## Policy
For `no_crash x idprime_state_not_sufficient`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
1. IDPrime ATR matching plus plausible file-select, container-map, and index-map responses did not create the target crash.
2. When `no_crash x idprime_state_not_sufficient` appears for `OpenSC pkcs15-crypt CLI bytes plus virtual-card transcript`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
3. Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- The card transcript portion uses little-endian length-prefixed chunks: first ATR, then APDU responses with trailing status words. IDPrime initialization reads card OS data, selects internal files, and consumes container and index records before crypt operations can reference keys.
- Harness: Before the reader transcript, the fuzz bytes select the pkcs15-crypt operation, PIN string, option flags, optional AID/key strings, and an input-file slice. Only the remaining bytes are passed to the virtual card reader.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed round-10 persistent failure.
- Scope: generator avoidance for the same failure-keyed basin.
