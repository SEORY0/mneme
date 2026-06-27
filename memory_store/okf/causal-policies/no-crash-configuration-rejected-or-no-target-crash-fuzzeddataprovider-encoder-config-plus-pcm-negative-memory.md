---
type: causal-policy
title: "No Crash Configuration Rejected Or No Target Crash Fuzzeddataprovider Encoder Config Plus Pcm Negative Memory"
description: "Round 16 negative memory for no_crash with verifier signal configuration_rejected_or_no_target_crash."
failure_class: "no_crash"
verifier_signal: "configuration_rejected_or_no_target_crash"
candidate_family: "construct"
input_format: "FuzzedDataProvider encoder config plus PCM"
harness_convention: "libfuzzer"
vuln_class: "AAC encoder quantizer table out-of-bounds read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "configuration-rejected-or-no-target-crash", "fuzzeddataprovider-encoder-config-plus-pcm", "negative-memory", "round-16"]
match_keys: ["no_crash", "configuration_rejected_or_no_target_crash", "FuzzedDataProvider encoder config plus PCM", "libfuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 16
---
# No Crash Configuration Rejected Or No Target Crash Fuzzeddataprovider Encoder Config Plus Pcm Negative Memory

## Policy
For `no_crash x configuration_rejected_or_no_target_crash`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
- All-zero, all-ones, patterned, and compact AAC-LC-like FuzzedDataProvider layouts ran cleanly. The missing condition is likely a configuration that successfully creates and processes an encoder instance with zero spectrum, low available dynamic bits, and repeated rate-control iterations until global gain exceeds the quantizer table range.
- When `no_crash x configuration_rejected_or_no_target_crash` appears for `FuzzedDataProvider encoder config plus PCM`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
- Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- The input is not an AAC file. It is a FuzzedDataProvider byte stream consumed into encoder bitrate, channel count, sample-rate selection, frame length, audio object type, many feature flags, optional DRC configuration, and then repeated input-buffer fill commands. The vulnerable quantizer indexes a table with gain plus a fixed bias during AAC/USAC quantization.
- Harness: The libxaac encoder fuzzer consumes configuration fields before any PCM bytes. If creation succeeds, it obtains the encoder input buffer, initializes it, then loops over remaining provider bytes choosing either copied bytes or a repeated fill value before each process call.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed persistent failure from round 16.
- Scope: generator avoidance for the same failure-keyed basin.
