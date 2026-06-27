---
type: causal-policy
title: "No Crash Mruby Runtime Executed No Crash Mruby Script Negative Memory"
description: "Round 10 negative memory for no_crash with verifier signal mruby_runtime_executed_no_crash."
failure_class: "no_crash"
verifier_signal: "mruby_runtime_executed_no_crash"
candidate_family: "construct"
input_format: "mruby-script"
harness_convention: "libfuzzer"
vuln_class: "type-confusion-or-api-contract-violation"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "mruby-runtime-executed-no-crash", "negative-memory", "round-10"]
match_keys: ["no_crash", "mruby_runtime_executed_no_crash", "mruby-script", "libfuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 10
---
# No Crash Mruby Runtime Executed No Crash Mruby Script Negative Memory

## Policy
For `no_crash x mruby_runtime_executed_no_crash`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
1. Scripts that instantiate, subclass, include, extend, and evaluate through FileTest exercised the Ruby-level class/module mismatch without producing a native sanitizer failure.
2. When `no_crash x mruby_runtime_executed_no_crash` appears for `mruby-script`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
3. Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- The input is plain mruby source code. FileTest is exposed in the runtime as a class in the vulnerable build, so scripts can interact with it through class operations that would normally be invalid for a module.
- Harness: The harness copies raw bytes into a NUL-terminated buffer and executes them with the mruby string loader. There is no length trailer or multi-field provider contract; reachability depends on valid mruby syntax and runtime operations.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed round-10 persistent failure.
- Scope: generator avoidance for the same failure-keyed basin.
