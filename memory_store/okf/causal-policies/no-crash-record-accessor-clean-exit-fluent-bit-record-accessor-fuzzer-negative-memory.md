---
type: causal-policy
title: "No Crash Record Accessor Clean Exit Fluent Bit Record Accessor Fuzzer Negative Memory"
description: "Round 24 negative memory for no_crash with verifier signal record_accessor_clean_exit."
failure_class: "no_crash"
verifier_signal: "record_accessor_clean_exit"
candidate_family: "construct"
input_format: "fluent-bit-record-accessor-fuzzer"
harness_convention: "libfuzzer"
vuln_class: "unchecked-allocation-failure"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "record-accessor-clean-exit", "fluent-bit-record-accessor-fuzzer", "libfuzzer", "construct", "negative-memory", "round-24"]
match_keys: ["no-crash", "record-accessor-clean-exit", "fluent-bit-record-accessor-fuzzer", "libfuzzer", "unchecked-allocation-failure"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 24
---
# No Crash Record Accessor Clean Exit Fluent Bit Record Accessor Fuzzer Negative Memory

- key: `no_crash x record_accessor_clean_exit`
- outcome: negative memory
- success_count: 0
- failure_count: 1
- formats: [[fluent-bit-record-accessor-fuzzer]]
- harnesses: [[libfuzzer]]

## Dead-End Shape
Valid JSON-map prefixes and record-accessor expressions reached the fuzzer envelope but did not align the deterministic fuzz allocator failure with the ra_key string materialization call.

## Policy
For `no_crash x record_accessor_clean_exit` on `fluent-bit-record-accessor-fuzzer`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission. Prefer `construct` only while this format and harness contract are present.

## Procedure
1. When `no_crash x record_accessor_clean_exit` appears for `fluent-bit-record-accessor-fuzzer`, treat this candidate family as a basin-to-avoid rather than evidence of proximity.
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
