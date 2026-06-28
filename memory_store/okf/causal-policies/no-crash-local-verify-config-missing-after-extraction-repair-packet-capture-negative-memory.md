---
type: causal-policy
title: "No Crash Local Verify Config Missing After Extraction Repair Packet Capture Negative Memory"
description: "Round 24 negative memory for no_crash with verifier signal local_verify_config_missing_after_extraction_repair."
failure_class: "no_crash"
verifier_signal: "local_verify_config_missing_after_extraction_repair"
candidate_family: "construct"
input_format: "packet-capture"
harness_convention: "libfuzzer"
vuln_class: "buffer-overread"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "local-verify-config-missing-after-extraction-repair", "packet-capture", "libfuzzer", "construct", "negative-memory", "round-24"]
match_keys: ["no-crash", "local-verify-config-missing-after-extraction-repair", "packet-capture", "libfuzzer", "buffer-overread"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 24
---
# No Crash Local Verify Config Missing After Extraction Repair Packet Capture Negative Memory

- key: `no_crash x local_verify_config_missing_after_extraction_repair`
- outcome: negative memory
- success_count: 0
- failure_count: 1
- formats: [[packet-capture]]
- harnesses: [[libfuzzer]]

## Dead-End Shape
A minimal capture with zlib-looking payload did not trigger the target. The missing piece is a specific dissector path that calls tvbuff_zlib with an empty buffer or negative length; simply placing deflate bytes in a generic capture is not enough to select that decompression path.

## Policy
For `no_crash x local_verify_config_missing_after_extraction_repair` on `packet-capture`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission. Prefer `construct` only while this format and harness contract are present.

## Procedure
1. When `no_crash x local_verify_config_missing_after_extraction_repair` appears for `packet-capture`, treat this candidate family as a basin-to-avoid rather than evidence of proximity.
2. Preserve any proven format or harness envelope, but change the missing gate, state relation, or sink path before another official submission.
3. Prefer a different construction family if the same verifier signal repeats without new parser-depth evidence.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for recovery policies; local crash class is supporting evidence only.

## Negative Memory
- Do not resubmit candidates that are clean, off-target, rejected before the target path, or crashing both fixed and vulnerable images in this same shape.
- Do not promote this trace as a recovery unless a later verifier run flips the target relation.
- Preserve only descriptive format and harness facts from this failed attempt.

## Evidence Shape
- Support: one diagnosed round 24 persistent failure.
- Scope: generator repair and retargeting only.
