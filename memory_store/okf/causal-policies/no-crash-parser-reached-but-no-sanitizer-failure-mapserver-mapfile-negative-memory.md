---
type: causal-policy
title: "No Crash Parser Reached But No Sanitizer Failure Mapserver Mapfile Negative Memory"
description: "Round 24 negative memory for no_crash with verifier signal parser_reached_but_no_sanitizer_failure."
failure_class: "no_crash"
verifier_signal: "parser_reached_but_no_sanitizer_failure"
candidate_family: "construct"
input_format: "mapserver-mapfile"
harness_convention: "libfuzzer"
vuln_class: "memory-leak"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-reached-but-no-sanitizer-failure", "mapserver-mapfile", "libfuzzer", "construct", "negative-memory", "round-24"]
match_keys: ["no-crash", "parser-reached-but-no-sanitizer-failure", "mapserver-mapfile", "libfuzzer", "memory-leak"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 24
---
# No Crash Parser Reached But No Sanitizer Failure Mapserver Mapfile Negative Memory

- key: `no_crash x parser_reached_but_no_sanitizer_failure`
- outcome: negative memory
- success_count: 0
- failure_count: 1
- formats: [[mapserver-mapfile]]
- harnesses: [[libfuzzer]]

## Dead-End Shape
Repeated valid CLUSTER blocks were accepted by the mapfile parser, including variants that allocated region and expression members before reinitialization, but neither local verification nor official submit reported a leak or crash. The path likely needs a different allocation member, parser lifetime, or leak-detection configuration than the attempted mapfiles exposed.

## Policy
For `no_crash x parser_reached_but_no_sanitizer_failure` on `mapserver-mapfile`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission. Prefer `construct` only while this format and harness contract are present.

## Procedure
1. When `no_crash x parser_reached_but_no_sanitizer_failure` appears for `mapserver-mapfile`, treat this candidate family as a basin-to-avoid rather than evidence of proximity.
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
